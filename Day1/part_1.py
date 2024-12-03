l_array,r_array = [],[]

with open('Day1\input.txt','r') as file:
    for line in file:
        l_digit,r_digit = map(int,line.split())
        l_array.append(l_digit)
        r_array.append(r_digit)
l_array.sort()
r_array.sort()
ans = 0
for ld,rd in zip(l_array,r_array):
    ans += abs(ld-rd)

print(ans)
