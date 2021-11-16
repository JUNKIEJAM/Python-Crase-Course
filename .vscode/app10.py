customer={
    "name":"Anmol",
    "age":30,
    "is_verified":True
}

print(customer.get("birthdate","1 Jan 2000"))  #as it was not specified earlier

print(customer.get("birthdate")) #o/p: none

nums={
    "1":"one", 
    "2":"two",    
    "3":"three", 
    "4":"four", 
    "5":"five", 
    "6":"six", 
    "7":"seven", 
    "8":"eight", 
    "9":"nine"
}

ans=""
num=input("number: ")

for ch in num:
    ans+=nums.get(ch)
    ans+=" "
    
print(ans)

