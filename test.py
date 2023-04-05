#Just testing...

#num = list(range(1, 11))
#num2 = list(range(11, 21))
#
#for n in num:
#    for n2 in num2:
#    #    x = n * n2
#        print(n2)
#print()

######### LIST #########

# requested_toppings = ['mushroom', 'french fries', 'extra cheese']
# available_toppings = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# for requested_topping in requested_toppings:

#     if requested_topping in available_toppings:
#         print(f'Adding {requested_topping}.')
        
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")

# print('\nFinished making your pizza')

########## FAVORITE LANGUAGES DICTIONARY  #############

# favorite_language= {
#     'sara': 'python',
#     'jamilu': 'python', 
#     'suraj': 'c++', 
#     'shade': 'Java', 
#     'Ngozi': 'JavaScript'
# }

# # 
# # person_lang = favorite_language.get('arjun', 'Sorry, The Person you are requesting does not belong to our list') 
# # print(person_lang)

# print('Peopel: Favorite Language')
# for person, language in favorite_language.items(): 
#     print(f'{person.title()} : {language}') 

######### LIST OF DICTIONARIES ##########

# alien_0 = {'color': 'green', 'points': 5} 
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15} 

# aliens = [alien_0, alien_1, alien_2] 

# print()
# for alien in aliens: 
#     print(alien)

# print()

######### NESTED LIST/DICTIONARY #########

# aliens = [] 
# print('##############################################')
# print('\n....\n')

# #this for loop will add 30 new_aliens to aliens list
# for alien_number in range(30): 
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
    
#Accessing first three elements and changing their properties
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'blue'
#         alien['speed'] = 'mediu'
#         alien['points'] = 10 

#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# #this for loop will loop throgh the aliens list and print first five
# for alien in aliens[:5]: 
#     print(alien)

# print('\n....\n')
# print(f'Total number of aliens is {len(aliens)}')
# print('##############################################')


################ LIST IN A DICTIONARY ###################### 

# pizzas = {
#     'crust': 'thick', 
#     'toppings': ['onions', 'red oil']
# }

# for topping in pizzas['toppings']:
#     print(topping)


## Looping through names of people and their favourite languages
# favourite_languages = {
#     'jamilu': ['java', 'python', 'c++'],
#     'anas': ['sql'],
#     'musab': ['prolog', 'javascript']

# }

# for name, languages in favourite_languages.items():
#     print(f'{name.title()}  favourite language is: ')

#     for language in languages: 
#         print(f'\t* {language}')
#     print()


################ NESTING A DICTIONARY INSIDE ANOTHER DICTIONARY ##################### 
# users = {
#     'ajamilu': {
#         'first': 'jamilu', 
#         'last': 'ahmad',
#         'location': 'gwagwalada'
#     },

#     'isahmuzam' : {
#         'first': 'muzammilu', 
#         'last': 'isah',
#         'location': 'malumfashi'
#     }, 

#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# } 

# for username, user_info in users.items():

#     print(f'\n{username}:')
    
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = f"{user_info['location']}" 

#     print(f'\t* {full_name}')
#     print(f'\t- {location}') 


##################################### Nested Dictionary 2 ################################################# 

# students = {
#     'stud1':{'fname':'jamilu', 'lname':'ahmad', 'age':30}, 
#     'stud2':{'fname':'muzammil', 'lname':'isah', 'age':27}, 
#     'stud3':{'fname':'abubakar', 'lname':'mikail', 'age':22}
#     }

# print()
# for stds, stds_infor in students.items():
#     first = students[stds]['fname']
#     last = students[stds]['lname']
#     years = students[stds]['age']
#     print(f'\n{last.upper()}, {first.title()}. You are {years} years old')
# print()

####################### USER INPUT ############################### 
# message = ''
# while message != 'quit':
#     message = input('enter a short messag: ')
#     if message != 'quit':
#         print(message)

# Using a Flag
# active = True
# while active:
#     message = input('Enter a Message: ')
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


current_number = 1
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number) 
