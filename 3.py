def power(base,exponent):
    if exponent==0:
        return 1
    elif exponent>0:
        return base*power(base,exponent-1)
    else:
        return 1/power(base,-exponent)
    
base=int(input("enter base:"))
exponent=int(input("enter exponent:"))
print("result is ",power(base,exponent))    
