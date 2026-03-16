#dictionery kkey = value
meaning = {
    "bat":"used to hit",
    "ball":"used to paly"
}
print(type(meaning))
print(meaning["bat"]) #accesing dict
print(meaning.get("wicket" , "not found")) #safe access method for remove error .use .get

meaning["wicket"]="ued to diclare out" #add dict to variable in run time
print(meaning)

meaning["bat"]="used to fight" # updating variable in run time
print(meaning)

meaning.pop("bat") #remove key
print(meaning)
# del meaning["ball"] another way to remove or delete 
print(meaning)

print(meaning.keys()) # only keys are print
print(meaning.values())# only values are print

print(meaning.items()) # it will give keys and values in list 

games={
    "cricket":"famous",
    "volly ball":"play",
    "kabbadi":"physical"
}
             
meaning.update(games) #updating one dict to another
print(meaning)


items1={
    "balll":3,
    "price":30
}

items2={
    "bat":1,
    "price":500
}

print(f"total price:{items1["price"] + items2["price"]}")