adj = {}
updates = []
with open("Day5\input.txt","r") as inp:
    for line in inp:
        if len(line) == 6:
            u,v = map(int,(line[:2],line[3:5]))
            if u in adj:
                adj[u].append(v)
            else:
                adj[u] = [v]
        elif len(line) > 4:
            updates.append(list(map(int,line[:-1].split(','))))
ans = 0

def isValid(update):
    seen = set()
    for num in update:
        for nei in adj[num]:
            if nei in seen:
                return False
        seen.add(num)
    return True

for update in updates:
    if isValid(update):
        ans += update[len(update)//2]

print(ans)