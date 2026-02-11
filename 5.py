# values=[True,False]
# print("p \t q\t p v q")
# for p in values:
#     for q in values:
#         print(f"{p} \t {q} \t {p or q}")



# def disjunction(p,q):
#     return p or q
# print("p \t q \t pvq")
# for p in [True,False]:
#     for q in [True,False]:
#         a=disjunction(p,q)
#         print(f"{p} \t {q} \t {a}")  


# values=[True,False]
# print("p \t ~p \t")
# for p in values:
#     print(f"{p} \t {not p}")     

# def negation(a):
#     return not a
# values=[True,False]
# print("p \t ~p \t")

# for p in values:
#     a=negation(p)
#     print(f"{p} \t {a}") 


# def conjection(p,q):
#     return p and q
# values=[True,False]
# print("p \t q \t p ^ q")
# for p in values:
#     for q in values:
#         a=conjection(p,q)
#         print(f"{p} \t {q} \t {a}")
         

def implication(p,q):
    return not p or q
values=[True,False]
print("p \t q \t p=>q")
for p in values:
    for q in values:
        a=implication(p,q)
        print(f"{p} \t {q} \t {a}")
