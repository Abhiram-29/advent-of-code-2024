from collections import deque

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

def isValid(update):
    seen = set()
    for num in update:
        for nei in adj[num]:
            if nei in seen:
                return False
        seen.add(num)
    return True

ans = 0

for update in updates:
    if not isValid(update):
        indegree = {num:0 for num in update}
        for num in update:
            for nei in adj.get(num,[]):
                if nei in indegree:
                    indegree[nei] += 1
        q = deque([num for num in update if indegree[num] == 0])
        dbg_ele = len(q)
        if dbg_ele > 1:
            print(q)
            print(indegree)
        valid_ordering = []
        while q:
            num = q.popleft()
            valid_ordering.append(num)
            for nei in adj.get(num,[]):
                if nei in indegree:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        if dbg_ele > 1:
            print(valid_ordering)
        ans += valid_ordering[len(valid_ordering)//2]

print(ans)