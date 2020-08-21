# Sliced ruler

This is a solution to the [FiveThirthEight Riddler Classic](https://fivethirtyeight.com/features/are-you-hip-enough-to-be-square/)
problem of August 20, 2020. The problem asks for the expected length of the part
of a foot long ruler that contains the six inch mark. (See link for more
complete description.)

The answer depends on the algorithm used to determine the locations for the
cuts. Below is a table that summarizes six different solutions. Due to a bug in
ruler.py an earlier version of this table incorrectly listed the expected length
for choose longest as 4.47. The value shown, 4.67 is correct.

| Algorithm | Expected Length |
| --------- | --------------- |
| Choose Three Independent Points | 5.625 (analytic, exact) |
| Choose x, then y, then z | 7.265298 (analytic, appoximate) |
| Choose y, then x and z | 6.341117 (analytic, approximate) |
| Choose x, then z, then y | 7.08 (simulated) |
| Choose Longest for next Slice | 4.67 (simulated) |
| Choose Slice containing 6" for next Slice | 4:35 (simulated)|

The PDF [slicedruler.pdf](slicedruler.pdf) contains a description of the analysis.
The Python program [ruler.py](ruler.py) was used to generated simulated results.
