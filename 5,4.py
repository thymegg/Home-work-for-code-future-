algebra = input().split()
geometry = input().split()
trigonometry = input().split()

all_solved = list(set(algebra) & set(geometry) & set(trigonometry))
all_solved.sort()

if all_solved:
    print(' '.join(all_solved))
else:
    print("Все три задачи никто не решил")