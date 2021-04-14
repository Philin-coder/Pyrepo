N = int(input())
length = N*N
mx = [[None for z in range(N)]for z in range(N)]
y = 0
x = N // 2
mx[y][x]=1
for i in range(2,length+1):
  old_x,old_y=x,y
  x = (x+1) % N
  y = (y-1) % N
  if not mx[y][x] is None:
    x = old_x
    y = (old_y+1) % N
  mx[y][x] = i
a = []
for y in mx:
  a+=y
print(' '.join(map(str, a)))