import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# get total number of item
num_items = len(names)


random_choice = random.randint(0, num_items - 1)
print(random_choice)