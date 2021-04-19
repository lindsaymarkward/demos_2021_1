"""
The following code came from a book but has some problems.
It prints the Python keywords in rows of 5 columns...
except the first row has 6.
There's also an if statement (i == 0) that's only ever true the first time
and we (the code) know it!
What can you do to solve this (efficiently, preferably) so it prints rows
each with 5 columns?
(Don't worry if the total number is not divisible by 5; the last row can have < 5.)
When you have that working, get it to line up neatly correctly. \t doesn't really work.
"""
import sys
import keyword

print("Python version:", sys.version)
print("Number of reserved keywords:", len(keyword.kwlist))
print("Reserved keywords:")
for i in range(len(keyword.kwlist)):
    print(keyword.kwlist[i], end="\t")
    if i != 0 and i % 5 == 0:
        print()


# Similar to the above question, the following is a simple version of handling the first/last elements in a list
# differently from the rest of them (using slicing).
# Your job is to rewrite this so that it handles the edge cases properly.
# It should not crash for an empty list
# A one-value list should only print one value

words = ["assert", "async", "await", "break", "class"]
# Edge cases:
# words = []
# words = ["assert"]

print(words[0].upper())
for word in words[1:-1]:
    print(word)
print(words[-1].upper())
