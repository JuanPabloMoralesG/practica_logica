"""It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores a-z A-Z -0-9 _-.
The website name can only have letters and digits a-z A-Z 0-9.
The extension can only contain letters a-z A-Z.
The maximum length of the extension is 3

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.commm

 """
import re

def fun(s:str):
    v = False
    if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s):
        v = True
    return v
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)