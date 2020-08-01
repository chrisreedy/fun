# A336433

Compute elements of sequence [A336433 from OEIS (On-line Encyclopedia of
   Integer Sequences)](https://oeis.org/A336433). This program was
   inspired by a message on the [MAA](https://maa.org) mailing list asking
   if it was possible to find a faster method to compute the elements of this
   sequence.

From the OEIS page:

> Number of sequences of n numbers from 1 to n that do not have a
> subsequence that adds up to n.

Examples:

> For n=3, the only solution is 2,2,2.
>
> For n=4, the 5 solutions are 3,3,3,3 and the four permutations of 3,3,3,2.

## Program Details

Check the doc strings and comments in the source for more details about
how the program works.

I've developed and run the program using Python 3.8.

On my MacBook Pro (2017, 2.8 GHz Quad-Core Intel Core i7) it takes about
110 seconds to generate the file `table.txt` with the values from 0 to 30.
For comparison it takes about about 30 seconds to generate 0 to 28 and under a
second for 0 to 20.

## Running the program

You can run the program directly. For example, print out the values from
3 to 10:
```
> python3 -m sequence.py 10
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
```

Or, get the value for 18:
```
> python3
>>> from sequence import countsequences
>>> countsequences(18)
717447490866241055
>>>
```
