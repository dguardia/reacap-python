totalSum = 0

for i in range(10000000):
  if(i%3 == 0 or i%5 == 0):
    print(i%3, i%5)
    totalSum = totalSum + i
    print(totalSum)

print(totalSum)
print("below using one liner")

# def divisible_by_under(limit, divs):
#     return (i for i in  range(limit) if any(i % div == 0 for div in divs))


# print(sum(divisible_by_under(1000, (3, 5))))

# print sum(n for n in range(1000) if (n%3==0 or n%5==0))