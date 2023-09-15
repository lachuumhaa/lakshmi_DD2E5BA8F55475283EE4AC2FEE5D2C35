# factorials using recursion
def fact_rec(n):
  if n==0 or n==1:
     return 1    
  else:
     return (n * fact_rec(n-1))
number=int (input("enter the value:"))
result=fact_rec(number)
print("the factorial of",number,"is",result)
  
