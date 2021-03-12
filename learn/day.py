parse1, parse2 = input().split(" ")
parse = parse1 + parse2

jishu = parse[::2]
jishu.sort(reverse=True)

oushu = parse[1::2]

oushu.sort(reverse=True)
print(oushu)
temp = []
for i in len(parse):
    if i %2 == 0:
        num = jishu.pop()
        temp.append(num)
    else:
        num = oushu.pop()
        temp.append(num)
print(temp)
str_union = "".join(temp)
# for word in str_union:
#     her_16 = hex(word)
#     print(her_16)


