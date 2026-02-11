# def factorial(n):
#   if n==0:
#     return 1
#   else:
#     return n*factorial(n-1)
# n=int(input('Enter number'))
# if n<0:
#   print("factorial does not exist")
# else:
  
#     print("Factorial of",n,"is",factorial(n))  


# def factorial(n):
#   if n==0:
#     return 1
#   else:
#     return n*factorial(n-1)
# n=int(input('Enter number'))
# if n<0:
#   print("factorial does not exist")
# else:
#     for n in range(0,n):
  
#      print("Factorial of",n,"is",factorial(n))  

# def power(base,exponent):
#     if exponent==0:
#         return 1
#     elif exponent>0:
#         return base*power(base,exponent-1)
#     else:
#         return 1/power(base,-exponent)
    
# base=int(input("enter base:"))
# exponent=int(input("enter exponent:"))
# print("result is ",power(base,exponent))    

#calculating gcd
def hcf(max,min):
    if min==0:
        return max
    else:
       return hcf(min,max%min)
a=int (input("enter first num"))
b=int(input("enter second num"))
if a<b:
    min=a
    max=b
else:
    min=b
    max=a
print("The gcd of",a,"and",b,"is :",end=" ")
print(hcf(max,min)) 


