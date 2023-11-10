x = input()
x = list(x)

for i in range(len(x)):
    if i == 0:
        x[i] = x[i].upper()
    elif x[i] in ['.', '!', '?']:
        if i+1 < len(x):
            x[i+2] = x[i+2].upper()

result = ''.join(x)
print(result)