lower = int("100")
upper = int("1000")

for num in range(lower,upper + 1):
      sum = 0

      temp = num
      while temp > 0:
              digit = temp % 10
              sum += digit ** 3
              temp //= 10

      if num == sum:
              print(num)