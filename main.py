from databse import database

#the example to call the data
print(database["history transaction"]["amount"][0])

print(type(database))




#to call all the key in the dictionary
"""
for x in database:
    
    print(x)

"""

id=int(input("key in your id : "))



def key_in_no(x) :
    
    id_no=database["id no"]
    name=database["name"]
    
    
    index = id_no.index(x)
    
    
    if x in id_no:
        
        return print("welcome ",name[index])
    
    else :
        
        return print(" you id is not exist")
    
    
try:    
    key_in_no(id)

except :
    print("you id is not exist or your key in invalid id")
    

