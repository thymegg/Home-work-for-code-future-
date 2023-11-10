strin = str(input())

x = strin.find("(")
y=strin.find(")")

print(strin[x+1 :y])