from tabulate import tabulate
# define the following strings to help with formatting throughout
l = "_"
s = " "

#======== THE BEGINNING OF THE CLASS ==========

# define class called shoe
class Shoe:

    # initialise the following attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # define a method which returns the cost of the shoes
    def get_cost(self):
        return self.cost
     
    # define a method which returns the quantity of the shoes
    def get_quantity(self):
        return int(self.quantity)

    # define a method which returns the code of the shoes
    def get_code(self):
        return self.code

    # define a method which returns the product of the shoes
    def get_product(self):
        return self.product

    # define a method which presents the shoe data as a string
    # this is easy-to-read when presented to the user
    def __str__(self):
        s = " "
        shoe_string = f"{8*s}Country{3*s}:  {self.country}\n{8*s}Code{6*s}:  {self.code}\n{8*s}Product{3*s}:  {self.product}\n{8*s}Cost{6*s}:  £{self.cost}\n{8*s}Quantity{2*s}:  {self.quantity}\n"
        return shoe_string

    # define another method which returns the shoe data as a string
    # this time in a way more easily accessible by code
    def __repr__(self):
        data_string = f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
        return data_string

    # define a method to change the quantity
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity




#============= SHOE LIST ===========

# create an empty list to store the shoe objects
shoe_list = []



#==========FUNCTIONS OUTSIDE THE CLASS==============


#============= READ SHOE DATA ================

# define a function to read the shoe data
# and add each shoe object to the shoe list
def read_shoes_data():

    # use try-except in case the file cannot be found
    try:
        with open("inventory.txt", "r", encoding="utf-8") as inventory1:

            # loop through each line in the text file
            for count, line in enumerate(inventory1, 0):

                # skip over the first line of the file
                if count == 0:
                    continue
                
                # find the relevant data in each line and assign each to a variable
                new_country = line.split(",")[0]
                new_code = line.split(",")[1]
                new_product = line.split(",")[2]

                # use try-except to skip over any line in which the data is of the incorrect form
                # i.e., not of a form which can be cast to int or float
                try:
                    new_cost = float(line.split(",")[3])
                    new_quantity = int(line.split(",")[4])
                # print an error message if an error of this form occurs
                # and skip over the line
                except ValueError:
                    print(f"\nERROR - some of the data in row {count+1} of inventory.txt is of the wrong format.\nThis line has been skipped over.", end ="")
                    continue

                # create a shoe object using the data
                # and append this object to the shoe list
                new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
                shoe_list.append(new_shoe)

    # if file cannot be found, print an error message
    except FileNotFoundError:
        print("\nERROR - cannot find the following file: inventory.txt")
        print("It is recommended that you exit the programme and check the relevant files are present and named correctly.")

    



#============= CAPTURE SHOES ================

# define a funtion which takes in new data from the user
# and use this to create a new shoe object
def capture_shoes():
    print(f"\n{l*140}")
    print("\nCAPTURE SHOES:\n")

    # the user enters the relevant data
    user_country = input(f"Enter country{3*s}: ")
    user_code = input(f"Enter code{6*s}: ")
    user_product = input(f"Enter product{3*s}: ")

    # check the user enters data of the correct form
    # if not repeat until they enter an appropriate input
    while True:
        try:
            user_cost = float(input(f"Enter cost{6*s}: "))
            break
        except:
            print("\nInvalid input - please enter a number.\n")
    
    while True:
        try:
            user_quantity = int(input(f"Enter quantity{2*s}: "))
            break
        except:
            print("\nInvalid input - please enter an integer.\n")
            
    # create a shoe object using the data
    user_shoe = Shoe(user_country, user_code, user_product, user_cost, user_quantity)
    # add this data to the shoe list
    shoe_list.append(user_shoe)
    
    # add this data to the inventory text file
    with open("inventory.txt", "a", encoding="utf-8") as inventory2:
            inventory2.write(f"\n{user_country},{user_code},{user_product},{user_cost},{user_quantity}")
    
    print("\nYou have successfully added a new shoe.")
    



#============= VIEW ALL ================

# define a function which displays all the shoe data
def view_all():
    print(f"\n{l*140}")
    print("\nVIEW ALL SHOES:\n")
    
    # the user inputs how they wish to view the data
    while True:
        option = input("Would you like to view the data as text, or in a table? ")
        
        # if they want to view it as text
        # use the __str__() method on each shoe in the shoe list
        if option == "text":
            print("\n")
            for count, shoe in enumerate(shoe_list, 1):
                print(f"SHOE {count})")
                print(shoe.__str__())
            break

        # if they want to view it as a table
        # loop through each shoe in shoe list, convert the data to a list
        # and add each list to be stored within another list called table
        # print this as a table using the tabulate library
        elif option == "table":
            table = []

            for shoe in shoe_list:
                string_shoe = shoe.__repr__()
                categories = string_shoe.split(",")
                row = []
                for item in categories:
                    row.append(item)
                table.append(row)

            print(tabulate(table, headers = ["Country", "Code", "Product", "Cost", "Quantity"], tablefmt= "fancy_outline"))
            break

        # if user enters an invalid input, ask them to try again
        else:
            print("\nInvalid input - please enter 'text' or 'table'.")

        


#============= RESTOCK ================

# define a function which finds the shoe with the lowest quantity
# and gives the user the option to restock
def re_stock():
    print(f"\n{l*140}")
    print("\nRESTOCK:\n")

    # create a variable to store the lowest quantity
    # and a variable to store the index of the corresponding shoe in the list
    # first set this as the first shoe in the list
    lowest = shoe_list[0].get_quantity()
    lowest_index = 0

    # loop through each shoe in the list
    for count, shoe in enumerate(shoe_list):
        # check if the quantity is less than the current lowest
        # if it is, then set the lowest variable to this value
        # and set the index to the index of this shoe in the list
        if shoe.get_quantity() <= lowest:
            lowest = shoe.get_quantity()
            lowest_index = count
    
    # display this information
    print(f"\nShoe with the lowest quantity:\n\n{shoe_list[lowest_index].__str__()}")
    
    # ask if the user wants to restock the item 
    # repeat until 'y' or 'n' is entered
    while True:
        answer = input("Would you like to restock this item? (y/n) ")

        # if yes, user inputs how much they would like to add
        # repeat until an integer is entered
        if answer == "y":
            while True:
                try:
                    num_to_add = int(input("\nHow many would you like to add to this quantity? "))
                    break
                except:
                    print("Invalid input - please enter an integer")
            

            # update the shoe object in the list
            shoe_list[lowest_index].change_quantity(str(int(shoe_list[lowest_index].get_quantity()) + num_to_add))

            # and update the data in the text file
            # use try/except to check if file is not found
            try:
                # first read the file using readlines
                with open("inventory.txt", "r") as inventory:
                    rows =inventory.readlines() 
                
                # find the required line to edit
                row_to_edit = -1
                for count, row in enumerate(rows,0):
                    if row.split(",")[1] == shoe_list[lowest_index].get_code():
                        row_to_edit = count

                # update the data
                # and replace the old line with the new line
                shoe_to_edit = rows[row_to_edit].split(",")
                shoe_to_edit[4] = str(int(shoe_to_edit[4]) + num_to_add)
                replacement_row = ",".join(shoe_to_edit)
                rows[row_to_edit] = replacement_row + "\n" 

                # write the updated text to the file
                with open("inventory.txt", "w") as inventory:
                    inventory.writelines(rows)
                    print("\nThis data has been successfully updated in the file.")
            
            # if file not found, print error message
            except:
                print("\nERROR - the file 'inventory.txt' was not found. The updated data cannot be written to the file.")
            break
        
        # if no, break
        elif answer == "n":
            break

        # if other input, print error message and loop back
        else:
            print("\nInvalid input - please enter 'y' or 'n'\n")




#============= SEARCH FOR SHOE ================

# define a function to seach for a specific shoe
def search_shoe():
    print(f"\n{l*140}")
    print("\nSEARCH FOR A SHOE:")

    # the user enters the code of the shoe they want to search for
    code_to_search = input("\nPlease enter the code of the shoe you want to search for : ")

    # create an empty variable to store the shoe if found
    shoe_search = None

    # loop through the shoe list
    # if shoe in list has the inputted code, set the variable to this shoe
    for shoe in shoe_list:
        if shoe.get_code().upper() == code_to_search.upper():
            shoe_search = shoe
            break

    # if no shoe was found, print an error message
    # otherwise, print the details of the shoe
    if shoe_search == None:
        print("\nNo shoe found with that code.")
    else:
        print(f"\n{shoe_search.__str__()}")




#============= VALUE PER ITEM ================

# define a function which calculates the value per item of each shoe
# display the results in a table
def value_per_item():
    print(f"\n{l*140}")
    print("\nTOTAL VALUE PER ITEM:\n")

    # create empty list to store embedded lists representing rows of the table
    table = []
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        row = [shoe.get_product(), shoe.get_code(), value]
        table.append(row)
    
    # use tabulate library to present the data in a table
    print(tabulate(table, headers = ["Product", "Code", "Total Value"], tablefmt= "fancy_outline"))




#============= HIGHEST QUANTITY ================

# define a function which finds the shoe with the highest quantity
def highest_qty():
    print(f"\n{l*140}")
    print("\nHIGHEST QUANTITY:\n")

    # create a variable to store the highest quantity
    # and a variable to store the index of the corresponding shoe in the list
    # first set this as the first shoe in the list
    highest = shoe_list[0].get_quantity()
    highest_index = 0

    # loop through each shoe in the list
    for count, shoe in enumerate(shoe_list):
        # check if the quantity is greater than the current highest
        # if it is, then set the highest variable to this value
        # and set the index to the index of this shoe in the list
        if shoe.get_quantity() >= highest:
            highest = shoe.get_quantity()
            highest_index = count
    
    # display this information
    print(f"\nShoe with the highest quantity:\n\n{shoe_list[highest_index].__str__()}")
    print("\nThis shoe is for sale.")






#============= MAIN MENU ================
print(f"\n{l*140}")
# first call the function read the shoe data from the text file
read_shoes_data()

# present the menu
menu = ""
while True:
    print(f"\n{l*140}")

    print('''\nMAIN MENU:\n
    What do you want to do?\n
        c - capture shoe data
        v - view all
        r - restock
        s - search for item
        t - total value per item
        h - highest quantity
        e - exit
    ''')
    menu = input(": ")

    # depending on which option the user inputs
    # call the corresponding function

    if menu == "v":
        view_all()

    elif menu == "r":
        re_stock()

    elif menu == "c":
        capture_shoes()
        
    elif menu == "s":
        search_shoe()

    elif menu == "t":
        value_per_item()

    elif menu == "h":
        highest_qty()
    
    elif menu == "e":
        exit()
    
    # if the input is invalid, print an error message and loop back
    else:
        print("\nInvalid input. Please try again.")

