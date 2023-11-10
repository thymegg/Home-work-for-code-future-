list1=input()
n=int(input())

numb=list(map(int, list1 .split()))
power_num = [num ** n for num in numb]
print(power_num)