l_array = []
r_freq = {}

with open('Day1\input.txt','r') as file:
    for line in file:
        l_digit,r_digit = map(int,line.split())
        l_array.append(l_digit)
        r_freq[r_digit] = r_freq.get(r_digit,0)+1
ans = 0
for num in l_array:
    ans += num*r_freq.get(num,0)

print(ans)
