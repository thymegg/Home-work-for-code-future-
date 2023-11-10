n = int(input())
cities = []

for i in range(n):
    city = input()
    cities.append(city)

duplicates = 0
for city in set(cities):
    if cities.count(city) > 1:
        duplicates += 2

print(duplicates)