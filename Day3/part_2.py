import re

with open("Day3\input.txt") as inp:
    content = inp.read()

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
patterns = re.finditer(mul_pattern,content)
ans = 0
do_mul = True
for pattern in patterns:
    if pattern.group() == "don't()":
        do_mul = False
    elif pattern.group() == "do()":
        do_mul = True
    elif do_mul:
        n1,n2 = map(int,pattern.groups())
        ans += n1*n2
print(ans)