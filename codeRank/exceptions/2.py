"""
Validate a regex:
2
.*\+
.*+
"""
import re

s = int(input())
for _ in range(s):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)