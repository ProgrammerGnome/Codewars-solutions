# Codewars
### CW1.c 
#### Replace With Alphabet Position (6 kyu)
Programming Language: C

Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it. "a" = 1, "b" = 2, etc. Example: alphabet_position("The sunset sets at twelve o' clock.") Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

### CW2.py
#### This time no story, no theory. The examples below show you how to write function accum:
Programming Language: Python

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"; accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"; accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

### CW3.py
Programming Language: Python

Task: Given an array of numbers and an index, return either the index of the smallest number that is larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

Notes

Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.

Example

least_larger({4, 1, 3, 5, 6}, 5, 0) ==  3;
least_larger({4, 1, 3, 5, 6}, 5, 4) == -1;
