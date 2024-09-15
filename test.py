import math


def divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def best_divisor(x, y, th):
  if x < y:
      big = y
  else: 
      big = x

  # 両方収まってたらそのまま返す
  if big <= th:
      return(x, y)

  # 収まらないときはいい感じのやつを探す
  arr = divisors(math.gcd(x,y))
  for i in arr:
      print(i,x//i,y//i)
      if big // i <= th:
          return(x//i,y//i)
  
  return(x//arr[-1],y//arr[-1])
    

a = 1502
b = 772
th = 500

print(best_divisor(a,b,th))