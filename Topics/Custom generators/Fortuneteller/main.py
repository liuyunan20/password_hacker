num = list(input())
gen = (int(x) for x in num)
print(sum(x for x in gen))
