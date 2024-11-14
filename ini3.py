#!/usr/bin/env python3

# Note: This script requires Python 3.12.7

# Given:  string s of length at most 200 letters and four integers a, b, c and d.
s = "b82RQeef71uXW7jlAeZe4A9IGekkoRPSIzAGrqmOdJFH2B2JHuiDHTHGRrLzx18XdbQ7A1SbHGZBQSu1ljbdagpBbFrI9jvLSecOdhFIjB7zQdhwtyVnnuptaDn5clNpsrPf3jcAWemngBZq12cHNSU6e2JiqfYkX8zALkquBN0N7KQO40fITYb."
a = 24
b = 28
c = 116
d = 120

# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
print(s[a:b+1], s[c:d+1])
