import re
mystring = 'ald'
result = re.search(r'[a]ld\b',mystring)
print(result.string)