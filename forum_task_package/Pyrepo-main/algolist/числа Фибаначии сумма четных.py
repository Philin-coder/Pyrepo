previous = 0
next_ = 1
result = 0
while result < 4000000:
    previous, next_ = next_, previous + next_
    if not next_ % 2:
        result += next_
print(result)
