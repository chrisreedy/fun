# Copyright 2020 Christopher L Reedy (<Christopher.Reedy@wwu.edu)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.import math

import math
import random

def average_length(process, trials):
    total = 0.0
    for t in range(trials):
        total += process()
    return total/trials

def processsort():
    """Return the length of the part of the ruler containing 6.

    The process is to choose 3 random cuts then sort them in order."""
    cuts = [random.uniform(0, 12) for i in range(3)]
    cuts.sort()
    x, y, z = cuts
    assert 0 <= x <= y <= z <= 12
    if x >= 6.0:
        return x
    elif y >= 6.0:
        return y - x
    elif z >= 6.0:
        return z - y
    else:
        return 12 - z

def processcut123():
    """Return the length of the part of the ruler containing 6.

    The process is to choose a random cut for the first, then second, then
    third cuts in that order."""
    x = random.uniform(0, 12)
    if x >= 6.0:
        return x
    else:
        y = random.uniform(x, 12)
        if y >= 6.0:
            return y - x
        else:
            z = random.uniform(y, 12)
            if z >= 6.0:
                return z - y
            else:
                return 12 - z

def cut123_ey_proc(y):
    def proc():
        z = random.uniform(y, 12)
        if z <= 6:
            return 12 - z
        else:
            return z - y
    return proc

def cut123_ey_poly(y):
    return (0.5*y**2 - 18*y + 108)/(12-y)

def cut123_ex_proc(x):
    def proc():
        y = random.uniform(x, 12)
        if y <= 6:
            return cut123_ey_poly(y)
        else:
            return y - x
    return proc

def cut123_ex_poly(x):
    return (1/4*x**2 - 18*x - 36*math.log((12 - x)/6) + 117)/(12-x)

def cut123_e_proc():
    x = random.uniform(0, 12)
    if x >= 6:
        return x
    else:
        return cut123_ex_poly(x)

def processcut132():
    """Return the length of the part of the ruler containing 6.

    The process is to choose a random cut for the first, then third, then
    second cuts in that order."""
    x = random.uniform(0, 12)
    if x >= 6.0:
        return x
    else:
        z = random.uniform(x, 12)
        if z < 6.0:
            return 12 - z
        else:
            y = random.uniform(x, z)
            if y >= 6.0:
                return y - x
            else:
                return z - y

def processcut213():
    """Return the length of the part of the ruler containing 6.

    The process is to choose a random cut for the second, then first or third
    cuts in that order."""
    y = random.uniform(0, 12)
    if y >= 6.0:
        x = random.uniform(0, y)
        if x >= 6.0:
            return x
        else:
            return y - x
    else:
        z = random.uniform(y, 12)
        if z >= 6.0:
            return z - y
        else:
            return 12 - z

def cut213_ey_poly(y):
    return 1/2*y + 6 - 36/y

def cut213_e_proc():
    return cut213_ey_poly(random.uniform(6, 12))

def processlongest():
    """Return the length of the part of the ruler containing 6.

    The process is to choose a random initial cut and then choose to cut
    the longest of the remaining segments."""
    x = random.uniform(0, 12)
    if x >= 6:
        x, y  = random.uniform(0, x), x
    else:
        y = random.uniform(x, 12)
    assert 0 <= x <= y <= 12
    if x >= y - x and x >= 12 - y:
        x, y, z = random.uniform(0, x), x, y
    elif y - x >= 12 - y:
        y, z = random.uniform(x, y), y
    else:
        z = random.uniform(y, 12)
    assert 0 <= x <= y <= z <= 12
    if x >= 6:
        return x
    elif y >= 6:
        return y - x
    elif z >= 6:
        return z - y
    else:
        return 12 - z

def processlongestV2():
    z = random.uniform(6, 12)
    if z >= 8:
        t = random.uniform(0, z)
        if t >= z/2:
            y = t
            if y <= 6:
                return z - y
            else:
                x = random.uniform(0, y)
                if x >= 6:
                    return x
                else:
                    return y - x
        else:
            x = t
            y = random.uniform(x, z)
            if y >= 6:
                return y - x
            else:
                return z - y
    else:
        t = random.uniform(0, z)
        if t < 2*z - 12:
            x = t
            y = random.uniform(x, z)
            if y <= 6:
                return z - y
            else:
                return y - x
        elif t <= 12 - z:
            x = t
            y = z
            return y - x
        else:
            y = t
            if y <= 6:
                return z - y
            else:
                x = random.uniform(0, y)
                if x >= 6:
                    return x
                else:
                    return y - x

def processlongest_ey(y):
    def proc():
        x = random.uniform(6, y)
        if x <= 6:
            return y - x
        else:
            return x
    return proc

def processlongest_ex(x, z):
    def proc():
        y = random.uniform(x, z)
        if y <= 6:
            return z - y
        else:
            return y - x
    return proc

def processslice6():
    """Return the length of the part of the ruler containing 6.

    The process is to choose a random initial cut and then choose to cut
    the remaining segment containing the 6 inch mark."""
    x = random.uniform(0, 12)
    if x >= 6:
        x, y  = random.uniform(0, x), x
    else:
        y = random.uniform(x, 12)
    if x >= 6:
        x, y, z = random.uniform(0, x), x, y
        if x >= 6:
            return x
        else:
            return y - x
    elif y >= 6:
        y, z = random.uniform(x, y), y
        if y >= 6:
            return y - x
        else:
            return z - y
    else:
        z = random.uniform(y, 12)
        if z >= 6:
            return z - y
        else:
            return 12 - z
