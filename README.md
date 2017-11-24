#Problem Statement :-
Write a program in python that can parse an algebraic expression stored as a string along with the values of each of the variables and calculate it.

For example :-

A string contains a formula :-

x = 24
y = 32
z = 45

a = (x+y)*z

The Python code should be able to parse this string and calculate the value of a using the variable values of x, y and z. The code should then return the value of a

Result of the above expression will be 2520

The expressions will contains only +, -, * and /
The expressions may contain one level of brackets ()
The expression may not contain brackets inside brackets.
The expression can have n number of variables as long as each variable has been assigned a value in the same string.

Write the code that will be able to solve the following expression :-

A = 23
B = 200
C = 234
D = 1.34
E = 22.45

Z = A * (C / E) + B / (A + D)
