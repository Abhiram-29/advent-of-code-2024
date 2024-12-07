with open("Day4\input.txt") as inp:
    data = inp.readlines()


word = "XMAS"
count = 0
rows,cols = len(data),len(data[0])

def isValid(x,y):
    if x < rows and y < cols and x >= 0 and y >=0:
        return True
    return False

for r in range(rows):
    for c in range(cols):
        for arow in range(-1,2):
            for acol in range(-1,2):
                word_found = True
                for i in range(4):
                    nr,nc = r+i*arow, c+i*acol
                    if isValid(nr,nc) and data[nr][nc] == word[i]:
                        pass
                    else:
                        word_found = False
                        break
                if word_found:
                    count += 1
print(count)
