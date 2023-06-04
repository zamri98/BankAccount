from databse import database

#the example to call the data
#print(database["history transaction"]["amount"][0])

#print(type(database))




#to call all the key in the dictionary
"""
for x in database:
    
    print(x)

"""

id=int(input("key in your id : "))
id_no=database["id no"]
index = id_no.index(id)
current_balance=database["balance"][index]




def key_in_no(x) :
    
    
    name=database["name"]
    
    

    
    
    if x in id_no:
        
        return print("welcome ",name[index])
    
    else :
        
        return print(" you id is not exist")
    
    
    
def transaction(operation):
    
    
    
    if operation == "cashout":
       current_balance_after= current_balance-amount
    elif operation == "cashin":
        current_balance_after=current_balance+amount

    
    
    return current_balance_after
        
        
    
    
    
    


    
try:    
    key_in_no(id)
    

except :
    print("you id is not exist or your key in invalid id")


print(current_balance)
operation=input("cashout,cashin or check balance ")
amount =int(input("amount : "))

current_balance_after=transaction(operation)
print(current_balance_after)







