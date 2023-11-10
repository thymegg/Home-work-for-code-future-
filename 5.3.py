s1 = input()
s2 = input()

s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")

if set(s1) == set(s2):
    print("Это анаграммы")
else:
    print("Это не анаграммы")