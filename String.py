# ____________________ String function _________________________________

city = "Jalandhar"

new_string1=city.upper()  # Python functions return new String 
new_string2=city.lower()  # Python functions return new String 
new_string3=city.capitalize()  # Python functions return new String 
print(new_string1)
print(new_string2)
print(new_string3)

name="Tony Stark"

print(name.find("ark")) # return the index value of first accurance index
print(name.replace("Tony Stark", "Ironman"))

 # ____________________ Practic set 2 __________________________________

product1=float(input("Enter the First Product Price : "))
product2=float(input("Enter the Second Product Price : "))
product3=float(input("Enter the Third Product Price : "))

print(f"First Product Price :{product1} ")
print(f"Second Product Price :{product2} ")
print(f"Third Product Price :{product3} ")
print("Total Price :",product1+product2+product3)

superHeroName=input("Enter the Super Hero Name :")

print("S" in superHeroName)
print("s" in superHeroName)