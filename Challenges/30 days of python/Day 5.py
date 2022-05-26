"""
Notes
Create a list
    liste = list() # builtin function
    liste = [] # using square brackets
    liste = ['banana', 'orange'] # with initial values

Informations about lists
    Index goes from 0 to the end when positive indexing and from -1
    to -NbItems when negative indexing

Functions of list()
    len(list) --> longueur de la liste, nombre ditems a linterieur
    append(item) --> ajoute un item a la fin de la liste.
    insert(index, item) --> insert item at a given index, other are shifted right
    remove(item) --> retire litem specifier
    pop() or pop(index) --> retire le dernier item ou litem a lindex specifier
    clear() --> empties the list
    copy() --> creer une nouvelle liste contenant une copie des valeurs, pas un lien vers la premiere liste
        important pour ne pas modifier la liste originale.
    extend(list) --> same as append but using a whole list as the thing to add
    count(item) --> number of item in list
    index(item) --> returns the index of the first occurence of item in list
    reverse() --> reverses a list
    sort() or sort(reverse=True) --> modifies the list to arrange it in ascending or descending order
    sorted() --> return the list sorted without changing the original

Tricks
    You can unpack a list using the *
        liste = ['banana', 'orange', 'mango', 'lemon','lime','apple']
        first_fruit, second_fruit, third_fruit, *rest = liste
        first_fruit = banana, second_fruit=orange, third_fruit=mango
        *rest = ['lemon','lime','apple']
        Can place de *rest anywhere.

    Slicing a list
        Defaults values of slicing [start = 0, end = len(liste)-1
        step =1]
        Positive indexing
            fruits = ['banana', 'orange', 'mango', 'lemon']
            all_fruits = fruits[0:4] # it returns all the fruits
            # this will also give the same result as the one above
            all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
            orange_and_mango = fruits[1:3] # it does not include the first index
            orange_mango_lemon = fruits[1:]
            orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item -
            ['banana', 'mango']
            liste[::-1] renvoit le mot en commencant par la fin
        Negative indexing
            fruits = ['banana', 'orange', 'mango', 'lemon']
            all_fruits = fruits[-4:] # it returns all the fruits
            orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
            orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
            reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
    Modify a list
        List are mutable and ordered. You can change any value of a given
        index for something else.
        list[0] = 'chevre'
        list[0] = 'dragon'
    Checking for items in a list
        fruits = ['banana', 'orange', 'mango', 'lemon']
        does_exist = 'banana' in fruits
        assert does_exist = True # yep
    Deleting
        del liste --> delete the whole list
        del liste[index] --> removes item of specified index
        del liste[slicing ranges like 1:3] --> removes items in range
    Joining lists
        Using the operator + we can join lists
"""

"""
Exercises: Level 1
"""

# Declare an empty list
liste = list()

# Declare a list with more than 5 items
liste = ['item1', 'item2', 'item3', 'item4', 'item5']

# Find the length of your list
lenght = len(liste)

# Get the first item, the middle item and the last item of the list
middle_of_index = int(lenght/2)
first_item = liste[0]
middle_item = liste[middle_of_index]
last_item = liste[-1]
print(liste)
print(first_item, middle_item, last_item)

"""
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#;  '

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list

Join the following lists:
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']

After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

Exercises: Level 2

The following is a list of 10 students ages:
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age

Add the min age and the max age again to the list

Find the median age (one middle item or two middle items divided by two)

Find the average age (sum of all items divided by their number )

Find the range of the ages (max minus min)

Compare the value of (min - average) and (max - average), use abs() method

Find the middle country(ies) in the countries list

Divide the countries list into two equal lists if it is even if not one more country for the first half.

['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
"""