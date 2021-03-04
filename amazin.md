```
n = int(input())
print(str(1) + " times " + str(n) + " equals " + str(n))
for i in range(0, n):
   for j in range(0, n):
      v = i * j
      if v == n:
         print(str(i) + " times " + str(j) + " equals " + str(n))
print(str(n) + " times " + str(1) + " equals " + str(n))
```
