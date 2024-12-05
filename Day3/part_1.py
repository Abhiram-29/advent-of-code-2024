import re

with open("Day3\input.txt") as inp:
    content = inp.read()

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
patterns = re.findall(mul_pattern,content)
ans = 0
for pattern in patterns:
    n1,n2 = map(int,pattern)
    ans += n1*n2
print(ans)