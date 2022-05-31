mary_fav_food = ['chicken','beef','vegetable',]
jane_fav_food = ['rice','ugali','potato',]
food = {
    'mary':'chicken ' 'beef ' 'vegetable',
    'jane': 'rice ' 'ugali ' 'potato',
}
fav_food={
    'mary':['beef','chicken','vegetable'],
    'jane':['rice','ugali','potato']
}
# print(fav_food)
#Combine lists above into one dictionary 
for key,value in fav_food.items():
    print(f"{key}:{value}")
#Person 1 and 2 which name, email and password