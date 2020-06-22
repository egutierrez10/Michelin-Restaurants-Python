# main.py
#
#   Name: Everardo Gutierrez
#   Program to read in Michelin restuarant data files and lookup 
#   based on criteria the user would like to. 
import pandas as pd 

def displayCommands():
    """
        Function: printCommands
        Display all the commands available for the user to enter
        Parameters: 
            none
        Returns:
            none
    """
    print("Commands available to be entered:")
    print("   Search by city (ex. cChicago)")
    print("   Search by region (ex. rCalifornia)")
    print("   Search by cuisine (ex. fContemporary)")
    print("   Search by price (ex. $$$)")
    print("   Search by price unknown (ex. N/A)")
    print("   Search by name (ex. Alinea)")

# Prompt user to enter there choice of michelin restaurants to lookup
print("*** Michelin Restaurant Lookup ***")
print("Choose Michelin Restaurant filename.")
print("   1 = One Star Michelin Restaurants")
print("   2 = Two Star Michelin Restaurants")
print("   3 = Three Star Michelin Restaurants")
choice = input("Enter your choice: ")
pd.set_option('display.max_rows', None)

# determine what file to read in
if choice == "1":
    data = pd.read_csv('one-star-michelin.csv')
elif choice == "2":
    data = pd.read_csv('two-star-michelin.csv')
else: 
    data = pd.read_csv('three-star-michelin.csv')

displayCommands() # display commands available to user
print("Reading in file", choice, "star michelin....")
# prompt user for how they want to search the data
command = input("Enter a command, help to display commands, or # to quit>") 
while command != "#":
    if command == "help": #display commands
        displayCommands()
    elif command[0] == 'c': # search by city
        command = command.replace('c','',1)
        d = data.loc[data.city == command]
    elif command[0] == 'r': # search by region
        command = command.replace('r','',1)
        d = data.loc[data.region == command]
    elif command[0] == 'f': # search by cuisine
        command = command.replace('f','',1)
        d = data.loc[data.cuisine == command]
    elif command[0] == '$' or command == 'N/A': # search by price
        d = data.loc[data.price == command]
    else: # search by name
        d = data.loc[data.name.str.contains(command, na=False)]
    print('Restaurants found: ')
    #print information of all the restaurants found 
    for i, j, k, l, m, n, o in zip(d['name'], d['city'], d['region'],d['latitude'],d['longitude'],d['cuisine'],d['url']):
        print(' Name: ',i)
        print(' Location:',j,',',k,'(',l,',',m,')')
        print(' Cuisine:',n)
        print(' Visit website for more info:',o)
    command = input("Enter a command, help to display commands, or # to quit>")