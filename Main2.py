
def  divide(a, b):
  if((a < 0) ^ (b < 0)):
    sign = -1
  else:
      sign = 1
  a= abs(a)
  b= abs(b)
  quo = 0
  temp=0
  for i in range(31, -1, -1):
    if (temp + (b << i) <= a):
      temp = temp + b << i
      quo = quo | 1 << i

  if sign == -1:
    quo = -quo
  return quo

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("The result after division is: ",divide(a, b))