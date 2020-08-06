"""
Compute the number of sequences of n numbers from 1 to n that do not
have a subsequence that adds up to n. (OEIS sequence A336433)

More precise: Compute the number of sequences k1, k2, ..., kn, ki an
integer with 1 <= ki <= n and no indices 1 <= j1 < j2 < ... < js <= n
with sum(k{ji] i in 1 .. s) == n.

General description of approach:

(1) Any permutation of such a sequence is also such a sequence.

(2) An integer k > n//2 can be a member of the sequence if and
only if there is no subsequence that sums to n-k.

(3) Given a qualifying sequence assume by (1) that it is in
non-decreasing order. The sequence must consist of a prefix of
members <= n//2 followed by a suffix of elements > n//2 that meet
criteria (2).

(4) The possible prefixes for (3) are sequences k1, ..., ks such
that 1 <= ki <= n//2 and there is no subsequence that sums to n.
(See extendprefix for computation of all prefixes.)

(5) The number of possible suffixes for a given prefix is
(possible values)**(suffix length) where possible values is the
number of values satisfying (2).

(6) To compute the number of sequences for a given prefix, multiply
the number of permutations of that prefix into n positions times the
number of possible suffixes. (See countperms for this.)

(7) To compute the total number of sequences, sum the number of
permutations for each prefix over all prefixes. (See countsequences.)

Example:

>>> for n in range(19):
...     print(n, countsequences(n))
0 0
1 0
2 0
3 1
4 5
5 68
6 403
7 7257
8 61686
9 1174434
10 13810620
11 335547727
12 3783688286
13 124486381056
14 1935430229612
15 55798127869680
16 1058567311736669
17 39819079382937334
18 717447490866241055

Reference: https://oeis.org/A336433"""


## Precompute factorials to save a little time
fact = []

def makefact(n):
    """Initialize global list fact with all k! for k <= n."""
    newfact = [None] * (n + 1)
    newfact[0] = 1
    for i in range(1, n + 1):
        newfact[i] = i * newfact[i - 1]
    global fact
    fact = newfact


## Computation starts here
    
def extendprefix(n, prior, minimum, sums, found):
    """Call the function found for each extension of the prefix prior.

    Parameters are:
        n given maximum value for elements in the sequence--same as the
            total desired length of the sequence.  
        prior is the prefix up to this point.
        minimum is the minimum value for the next value extending the
            prefix.
        sums is a set of all sums < n of non-empty subsequences of prior.
        found is a function to be called for each prefix that is found.
            found should take two parameters, the prefix and the sums
            for that prefix.

    When called prior must be a sequence of length less than n of integers
    in the range 1 .. n//2 such that no subsequence sums to n. minimum
    must be greater than or equal to one if prior is empty or the largest
    element of prior if prior is non-empty.
    
    The function attempts to extend prior by appending minimum to create
    a new prefix. The procedure found is called if n is not a sum of some
    subsequence of the new sequence.

    If the length of the new sequence is less than n and all integers in
    the range 1 .. (n+1)//2 (inclusive) are in sums, the prefix cannot
    be the prefix of any qualifying sequence. (Some values > n/2 are
    required and all such values create a sum of n.) This is not tested
    for because it's covered in countperms.

    If the length of the prefix is less than n, extendprefix is called
    again to attempt to attempt to further extend the sequence."""

    for k in range(minimum, n//2 + 1):
        maxx = n - k
        ## Check to make sure k doesn't create n as a sum
        if maxx not in sums:
            newprefix = prior + [k]
            newsums = sums | {x + k for x in sums if x < maxx}
            newsums.add(k)
            found(newprefix, newsums)
            if len(newprefix) < n:
                extendprefix(n, newprefix, k, newsums, found)

def countperms(n, prefix, sums):
    """Return the number of sequences containing the given prefix.

    This computes the number of sequences which are permutations of a
    non-decreasing sequence with the given prefix and extended by
    values k, 1+n//2 <= k < n such that n-k is not in sums."""

    # Compute possible values for the suffix. This is done first
    # to short circuit this function if this is zero.
    if len(prefix) < n:
        possible = sum(1 for k in range(1, (n+1)//2) if k not in sums)
        if possible == 0:
            return 0 # Short circuit
    else:
        possible = 1 # So possible has a value

    # Compute the multinomial coefficient for the prefix
    denom = 1
    prior = 0
    count = 1
    for k in prefix:
        if k == prior:
            count += 1
            denom *= count
        else:
            count = 1
            prior = k
    coeff = fact[n] // (denom * fact[n - len(prefix)])

    return coeff * (possible ** (n - len(prefix)))

def countsequences(n):
    """Return number of sequences of integers in the range 1 .. n
    (inclusive) of length with no subsequence summing to n."""
    
    # Edge case
    if n == 0:
        ## This is correct from OEIS. Should the sequence of length zero
        ## count as solution or not? If it did, this should return 1.
        return 0

    # Housekeeping
    if len(fact) < n + 1:
        makefact(n)
    
    total = countperms(n, [], set())

    def handleprefix(prefix, sums):
        perms = countperms(n, prefix, sums)
        nonlocal total
        total += perms
        # print(prefix, perms)

    # Do work. Call handleprefix for each non-empty prefix.
    extendprefix(n, [], 1, set(), handleprefix)

    return total


if __name__ == '__main__':
    
    ## Check that computation matches OEIS (uncomment following)
    ## import doctest
    ## doctest.testmod()

    import sys

    usage = True # Print usage message
    try:
        if len(sys.argv) == 2:
            limit = int(sys.argv[1])
            if 3 <= limit <= 40:
                ## 40 wlll take a ridiculously large time to compute
                ## 30 can be done in a couple of minutes
                usage = False
                makefact(limit)
                for n in range(limit + 1):
                    print(n, countsequences(n))
    except ValueError:
        pass

    if usage:
        print(f"Usage: python3 {sys.argv[0]} N where 3 <= N <= 40")


