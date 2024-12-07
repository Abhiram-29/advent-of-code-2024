with open("Day4\input.txt") as inp:
    data = inp.readlines()

rows,cols = len(data),len(data[0])
count = 0
for r in range(1,rows-1):
    for c in range(1,cols-1):
        if data[r][c] == 'A':
            word_found = True
            if not((data[r-1][c-1] == 'M' and data[r+1][c+1] == 'S') or (data[r-1][c-1] == 'S' and data[r+1][c+1] == 'M')):
                word_found = False
            if not((data[r+1][c-1] == 'M' and data[r-1][c+1] == 'S') or (data[r+1][c-1] == 'S' and data[r-1][c+1] == 'M')):
                word_found = False
            if word_found:
                count += 1
print(count)