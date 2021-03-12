import re
pattern = re.compile(r'(\w){2}(\d){3}')
st = 'ab122'
# match 从开头匹配，只匹配一次
# search 全文搜索匹配，只匹配一次
ma = re.match(pattern,st)
print(ma)
print(ma.group())
st1 = 'ab44 d ajb aaab ar112'
ma = re.search(pattern,st1)
# print(ma)
# print(ma.group())
# print(ma.groups())
# print(ma.start())
# print(ma.end())
pattern = re.compile(r'\d+')
ma1 = re.split(pattern,'sj1jj234,hel333,fi444h,woloe')
print(ma1)
print('o'.join(ma1))
print(re.findall(pattern,'sj1jj234,hel333,fi444h,woloe'))
pattern = re.compile(r'\d+')
for m in re.finditer(pattern,'sj1jj234,hel333,fi444h,woloe'):
    print(m.group(),)

print(re.sub(pattern,'i','sj1jj234,hel333,fi444h,woloe',count=1))