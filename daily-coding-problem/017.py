#!/usr/bin/env python

"""
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1
contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing
a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to
a file within our file system. For example, in the second example above,
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length
is 32 (not including the double quotes).
Given a string representing the file system in the above format, return
the length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""

MAX_LEVEL = 20

path = [0] * MAX_LEVEL
dot = False
cnt = 0
m = 0  # longest absolute path
lvl = 0  # indent level

fs = [
    "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",  # longest: 20
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",  # longest: 32
][1]

fs = list(fs)

fs.append("\n")

for c in fs:
    if c == "\n":
        path[lvl] = cnt

        if dot:
            m = max(m, lvl + sum(path[: lvl + 1]))

        # reset
        dot = False
        cnt = 0
        lvl = 0

    elif c == "\t":
        lvl += 1

    else:
        cnt += 1

        if c == ".":
            dot = True

print(m)
