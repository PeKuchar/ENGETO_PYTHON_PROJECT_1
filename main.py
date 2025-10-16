import sys


texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


# registered users
users = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"
        }

# user login
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("-"*40)
    print(f"Welcome to the app, {username}.")
    print(f"We have {len(texts)} texts to be analyzed.")
    print("-"*40)

else:
    print("-"*40)
    print(f"username: {username}")
    print(f"password: {password}")
    print(f"unregistered user, terminating the program...")
    sys.exit()


# text selection
text_number = input(f"Enter a number btw. 1 and {len(texts)} to select: ")

if text_number.isdigit():
    text_number = int(text_number)
    if text_number >= 1 and text_number <= len(texts):
        print(f"Text number {text_number} was selected.")
    elif text_number < 1 or text_number > len(texts):
        print(f"The entered number {text_number} is outside the valid range.")
        sys.exit()
else:
    print(f"The entered input is not a number.")
    sys.exit()
    

# text cleaning and word division
index = text_number - 1
words = texts[index].replace(",", "").replace(".", "").split() 
word_count = len(words)
print("-"*40)
print(f"There are {word_count} words in the selected text.")


# titlecase words number
titlecase_words = 0
for word in words:
    if word[0].isupper():
        titlecase_words += 1
print(f"There are {titlecase_words} titlecase words.")


# uppercase words number
uppercase_words = 0
for word_u in words:
    if word_u.isupper():
        uppercase_words += 1
print(f"There are {uppercase_words} uppercase words.")


# lowercase words number
lowercase_words = 0
for word_l in words:
    if word_l.islower():
        lowercase_words += 1
print(f"There are {lowercase_words} lowercase words.")


# numeric strings number
numeric_strings = 0
for num_str in words:
    if num_str.isdigit():
        numeric_strings += 1
print(f"There are {numeric_strings} numeric strings.")


# sum of all the numbers
sum = 0
for number_str in words:
    if number_str.isdigit():
        number = int(number_str)
        sum = sum + number
print(f"The sum of all the numbers is {sum}.")


# frequency of different word lengths in the text
occurrences = {}
for word_occ in words:
    length_word = len(word_occ)
    occurrences[length_word] = occurrences.get(length_word, 0) + 1


# bar chart
print("-"*40)
print("LEN|OCCURRENCES                   |NR.")
print("-"*40)

for length, occurence in sorted(occurrences.items()):
    print(f"{length:>3}|{"*" * occurence:<30}|{occurence:<3}")
    






    
    



















