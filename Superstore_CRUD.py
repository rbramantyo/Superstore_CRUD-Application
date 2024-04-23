
from pyfiglet import figlet_format
from tabulate import tabulate

inventory = [ # Category, Name, Brand, Stock, Price
    {'Category': 'Food', 'Name': 'Steaks', 'Brand': 'Aria', 'Stock': 20, 'Price': 75000},
    {'Category': 'Food', 'Name': 'Eggs', 'Brand': 'Aria', 'Stock': 42, 'Price': 30500},
    {'Category': 'Food', 'Name': 'Eggs', 'Brand': 'Indofarm', 'Stock': 30, 'Price': 32000},
    {'Category': 'Food', 'Name': 'Bread', 'Brand': 'Sari Roti', 'Stock': 20, 'Price': 15000},
    {'Category': 'Food', 'Name': 'Lettuce', 'Brand': 'Aria', 'Stock': 21, 'Price': 12000},
    {'Category': 'Homegoods', 'Name': 'Saucepans', 'Brand': 'Maxim', 'Stock': 10, 'Price': 180000},
    {'Category': 'Homegoods', 'Name': 'Pans', 'Brand': 'Maxim', 'Stock': 8, 'Price': 150000},
    {'Category': 'Homegoods', 'Name': 'Kitchen Knives', 'Brand': 'Krischef', 'Stock': 45, 'Price': 20000},
    {'Category': 'Homegoods', 'Name': 'Cutting Boards', 'Brand': 'Krischef', 'Stock': 20, 'Price': 25000},
    {'Category': 'Homegoods', 'Name': 'Vacuum Cleaner', 'Brand': 'Philips', 'Stock': 50, 'Price': 699000},
    {'Category': 'Appliances', 'Name': 'Toaster', 'Brand': 'Philips', 'Stock': 70, 'Price': 210000},
    {'Category': 'Appliances', 'Name': 'Microwave', 'Brand': 'Modena', 'Stock': 128, 'Price': 1150000},
    {'Category': 'Appliances', 'Name': 'Refrigerator', 'Brand': 'Modena', 'Stock': 20, 'Price': 4599000}, 
    {'Category': 'Appliances', 'Name': 'Oven', 'Brand': 'Modena', 'Stock': 15, 'Price': 599000},
    {'Category': 'Furniture', 'Name': 'Armchair', 'Brand': 'Informa', 'Stock': 10, 'Price': 699000},
    {'Category': 'Furniture', 'Name': 'Bed', 'Brand': 'King Koil', 'Stock': 20, 'Price': 2499000},
    {'Category': 'Furniture', 'Name': 'Couch', 'Brand': 'Informa', 'Stock': 10, 'Price': 1350000},
    {'Category': 'Furniture', 'Name': 'Dining Set', 'Brand': 'Informa', 'Stock': 0, 'Price': 3550000}
]

adminList = [
    {'Username': 'admin', 'Password': 'admin123', 'Name':'Admin Bram'}
]

cart = []
favorites = []
exitFlag = False
backFlag = False

def login():
    login_logo = (figlet_format("     Aria's", font = "standard"))
    return f'''
_________________________________________

Welcome to 
\n{login_logo}
\t\t\t       Superstore
_________________________________________
'''

def below_menu(hint):
    return f'''
    _________________________________________
    
    Option

    a. Search items
    b. Filter items (by Category)
    c. Order items (by Price)
    d. Back
    _________________________________________

    {hint}
    ''' 

def cust_main_menu():
    return f'''
    _________________________________________

    Hello, {user_name}

                GET 10% DISCOUNT  
             (Min. Purchase Rp500k)

    1. Buy items
    2. Cart
    3. Exit
    _________________________________________
    '''

def display_items():
    header = ['Index', 'Name', 'Brand', 'Stock', 'Price']
    formatted_data = [(i+1, values['Name'], values['Brand'], values['Stock'], values['Price']) for i, values in enumerate(inventory)]
    return tabulate(formatted_data, headers = header, tablefmt="simple_grid")

def display_cart():
    totalCart_header = ['Number', 'Name', 'Qty', 'Price', 'Total Price']
    totalCart = [(i+1, values['Name'], values['Qty'], values['Price'], values['Qty'] * values['Price']) for i, values in enumerate(cart)]
    totalCart_table = tabulate(totalCart, headers=totalCart_header, tablefmt="simple_grid")
    return totalCart_table

def display_category():
    categories_str = '''
    _________________________________________

    Category
    '''
    global categories
    categories = sorted(set(item['Category'] for item in inventory))

    for index, category in enumerate(categories, start=1):
        categories_str += f"\n    {index}. {category}"

    categories_str += '''
    _________________________________________
    '''
    return categories_str

def filter_items():  
    global backFlag
    print(display_category())
    while not backFlag:
        category_choice = input("Select category number: ")
        try:
            category_choice = int(category_choice)
            if 0 < category_choice <= len(categories):
                selected_category = categories[category_choice - 1]

                filtered_items = [item for item in inventory if item['Category'].lower() == selected_category.lower()]
                
                if filtered_items:
                    header = ["Index", "Name", "Brand", "Stock", "Price"]
                    table = [(i+1, item['Name'], item['Brand'], item['Stock'], item['Price']) for i, item in enumerate(filtered_items)]
                    print(f'\n{selected_category.capitalize()}:')
                    print(tabulate(table, headers=header, tablefmt="simple_grid"))
                    add_to_cart(filtered_items, cart) 
                    backFlag = True # Set backFlag to True after adding item to cart
                else:
                    print('No items found in the selected category.')
            else:
                print('Invalid category number. Please select a valid number.')
        except ValueError:
            print('Invalid input. Please select the category number.')

def search_items():
    term = input("Search items: ").lower()
    result_list = []

    for item in inventory:
        if term in item['Name'].lower() or term in item['Brand'].lower():
            result_list.append(item)

    if result_list:
        print("Search Results:")
        header_result_list_table = ["Index", "Name", "Brand", "Stock", "Price"]
        result_list_table = [(i+1, item["Name"], item["Brand"], item["Stock"], item["Price"]) for i, item in enumerate(result_list)]
        print(tabulate(result_list_table, headers=header_result_list_table, tablefmt="simple_grid"))
        add_to_cart(result_list, cart)
    else:
        print("No matching items found.")

def order_by_price_asc():
    header = ['Index', 'Name', 'Brand', 'Stock', 'Price']
    global sorted_inventory_asc
    sorted_inventory_asc = sorted(inventory, key=lambda x: x['Price']) # Sort inventory by 'Price' key
    
    formatted_data = [(i+1, values['Name'], values['Brand'], values['Stock'], values['Price']) for i, values in enumerate(sorted_inventory_asc)]
    print(tabulate(formatted_data, headers=header, tablefmt="simple_grid"))

def order_by_price_desc():
    header = ['Index', 'Name', 'Brand', 'Stock', 'Price']
    global sorted_inventory_desc
    sorted_inventory_desc = sorted(inventory, key=lambda x: x['Price'], reverse=True) # Sort inventory by 'Price' key, but reversen  
    
    formatted_data = [(i+1, values['Name'], values['Brand'], values['Stock'], values['Price']) for i, values in enumerate(sorted_inventory_desc)]
    print(tabulate(formatted_data, headers=header, tablefmt="simple_grid"))

def order_items():
    while (True):
        order = input("Order by (asc/desc): ").lower()
        if order == "asc":
            order_by_price_asc()
            add_to_cart(sorted_inventory_asc, cart)
            break
        elif order == "desc":
            order_by_price_desc()
            add_to_cart(sorted_inventory_desc, cart)
            break
        else:
            print("Invalid input. Please enter 'asc' for ascending order or 'desc' for descending order.")
 
def add_to_cart(items_list, cart):
    while True:
        input_choice = input('\nSelect index you want to buy (enter "cancel" to go back): ')
        if input_choice.lower() == 'cancel':
            break
        try:
            input_int = int(input_choice)
            if 0 < input_int <= len(items_list):
                selected_item = items_list[input_int - 1]
                available_stock = selected_item['Stock']
                total_qty_in_cart = sum(item['Qty'] for item in cart if item['Name'] == selected_item['Name'] and item['Brand'] == selected_item['Brand'])
                
                buy_amount = int(input('Enter the amount: '))
                if 0 < buy_amount <= available_stock - total_qty_in_cart:  # Check if buy amount doesn't exceed available stock
                    cart.append({'Name': selected_item['Name'], 'Brand': selected_item['Brand'], 
                                  'Qty': buy_amount, 'Price': selected_item['Price']})
                    print('Item has been added to cart')
                    break
                elif buy_amount <= 0:
                    print("\nInvalid input. Please enter a valid amount.")
                else:
                    print(f"\nStock is not enough for your demand. \nYou already have {total_qty_in_cart} in your cart.")
            else:
                print('Invalid index. Please select a valid index.')
        except ValueError:
            print('Invalid input. Please enter a valid index.')

def checkout():
    global exitFlag
    user_reply = input("\nContinue Shopping? (yes/no): ").lower()
    while user_reply not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        user_reply = input("\nContinue Shopping? (yes/no): ").lower()

    if user_reply == 'no':
        if cart:  # If the cart is not empty
            payment()
        else: # If the cart is empty
            print(f'Thank you, {user_name}. Come back later')
            exitFlag = True
    elif user_reply == 'yes':
        pass

def payment():
    global exitFlag
    user_reply_payment = input("\nContinue to Payment? (yes/no): ").lower()
    while user_reply_payment not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        user_reply_payment = input("\nContinue to Payment? (yes/no): ").lower()

    if user_reply_payment == 'yes':
        sum_prices = sum(item['Qty'] * item['Price'] for item in cart)
        print('\nCart list: ')
        print(display_cart())
        print(f'The amount to be paid is: Rp{sum_prices}')
        if sum_prices >= 500000:
            discount = int(sum_prices * 0.10)
            sum_prices -= discount
            print(f'A 10% discount has been applied. \n\nNew amount to be paid is: Rp{sum_prices}\n')
        else:
            print("No discount applied.")

        while not exitFlag:
            try:
                user_money = int(input('\nEnter your money: '))
                if user_money < sum_prices:
                    print('Sorry, your money is not enough. Please try again.')
                else:
                    for item in cart:
                        for inventory_item in inventory:
                            if item['Name'] == inventory_item['Name'] and item['Brand'] == inventory_item['Brand']:
                                inventory_item['Stock'] -= item['Qty']  # Reduce the stock
                    print(f'\nThank you for shopping, {user_name}.')
                    change = user_money - sum_prices
                    print(f'Your change is Rp{change}.')
                    cart.clear() # Clear the cart
                    exitFlag = True
            except ValueError:
                print("Invalid input. Please enter a valid number for the money.")
    elif user_reply_payment == 'no':
        exitFlag = True

def authenticate(username, password, userList):
    for user in userList:
        if username == user['Username'] and password == user['Password']:
            return user
    return None

def emp_main_menu():
    return f'''
                   CMS Admin 
    _________________________________________
    
    Welcome, {authenticated_user['Name']}!

    1. Show items
    2. Exit
    _________________________________________
    '''

def emp_below_menu():
    return '''
    _________________________________________
    
    Option

    a. Add items
    b. Update items
    c. delete items
    d. Back
    _________________________________________
    ''' 

def emp_display_items():
    header = ['Index','Category', 'Name', 'Brand', 'Stock', 'Price']
    formatted_data = [(i+1, values['Category'],  values['Name'], values['Brand'], values['Stock'], values['Price']) for i, values in enumerate(inventory)]
    return tabulate(formatted_data, headers = header, tablefmt="simple_grid")
 
def add_items():
    while (True):
        addCategory = input('\nInput new item\'s Category: ').capitalize()
        if not addCategory.isalpha():
            print('Invalid input. Please enter a valid input.')
            continue
        else:
            break
    while (True):
        addName = input('Input new item\'s Name: ').capitalize()
        if not addName.isalpha():
            print('Invalid input. Please enter a valid input.')
            continue
        else:
            break
    while (True):
        addBrand = input('Input new item\'s Brand: ').capitalize()
        if not addBrand.isalpha():
            print('Invalid input. Please enter a valid input.')
            continue
        else:
            break
    while (True):
        addStock = input('Input new item\'s Stock: ')
        if addStock.isdigit():
            addStock = int(addStock)
            if addStock > 0:
                break
            else:
                print('Invalid input. Please enter a positive input.')
        else:
            print('Invalid input. Please enter a valid input.')
    while (True):
        addPrice = input('Input new item\'s Price: ')
        if addPrice.isdigit():
            addPrice = int(addPrice)
            if addPrice >= 0:
                break
            else:
                print('Invalid input. Please enter a positive input.')
        else:
            print('Invalid input. Please enter a valid input.')
        
    # Check if an item with the same name and brand already exists
    if any(item['Name'].capitalize() == addName and item['Brand'].capitalize() == addBrand for item in inventory):
        print("\nAn item with the same name and brand already exists in the inventory.\n")
    else:
        inventory.append({'Category': addCategory, 'Name': addName, 'Brand': addBrand, 'Stock': addStock, 'Price': addPrice})
        print("\nItem added successfully!\n")

def update_items():
    while (True):
        editItemIndex = input('\nSelect index to edit (enter "cancel" to go back): ')
        if editItemIndex.lower() == 'cancel':
            break 
        try:
            editItemIndex = int(editItemIndex)
            if 0 < editItemIndex <= len(inventory):
                item = inventory[editItemIndex - 1]
                print("\nEditing item:")
                print("1. Category:", item['Category'])
                print("2. Name:", item['Name'])
                print("3. Brand:", item['Brand'])
                print("4. Stock:", item['Stock'])
                print("5. Price:", item['Price'])
                editChoice = int(input("\nSelect number you want to edit: "))
                if editChoice == 1:
                    newCategory = input('Input new category: ').capitalize()
                    item['Category'] = newCategory
        
                elif editChoice == 2:
                    newName = input('Input new name: ').capitalize()
                    item['Name'] = newName
                    
                elif editChoice == 3:
                    newBrand = input('Input new brand: ').capitalize()
                    item['Brand'] = newBrand
                    
                elif editChoice == 4:
                    newStock = int(input('Input new stock (must be greater than or equal to 0): '))
                    if newStock >= 0:
                        item['Stock'] = newStock
                        
                    else:
                        print('Invalid stock value! Please input a positive number.')
                elif editChoice == 5:
                    newPrice = int(input('Input new price: '))
                    if newPrice > 0:
                        item['Price'] = newPrice
                            
                    else:
                        print('Invalid price! Please input a positive number.')
                else:
                    print('Invalid choice!')

                print('\nItem updated successfully!')
                print(tabulate([[item['Category'], item['Name'], item['Brand'], item['Stock'], item['Price']]], 
                                headers=['Category', 'Name', 'Brand', 'Stock', 'Price'], tablefmt="simple_grid"))
                break
            else:
                print('Invalid index. Please select a valid index.')
        except ValueError:
            print('Invalid input. Please enter a valid index.')

def delete_items():
    while True:
        deleteIndex = input('\nSelect index to delete (enter "cancel" to go back): ')
        if deleteIndex.lower() == 'cancel':
            print("Deletion canceled.")
            break  # Exit the delete loop and go back to the previous menu
        try:
            deleteIndex = int(deleteIndex)
            if 0 < deleteIndex <= len(inventory):
                # Confirm deletion
                confirm_delete = input(f"Are you sure you want to delete item {inventory[deleteIndex - 1]['Name']}? (yes/no): ").lower()
                if confirm_delete == 'yes':
                    del inventory[deleteIndex - 1]
                    print("\nItem deleted successfully!\n")
                    break
                else:
                    print("Deletion canceled.")
            else:
                print('Invalid index. Please select a valid index.')
        except ValueError:
            print('Invalid input. Please enter a valid index.')
    
while (True):

    print(login())
    login_choice = str(input('''Role: \nA. Customer \nB. Employee \n\nSelect your role: ''').lower())

    if login_choice == 'customer' or login_choice == 'a':
        user_name = input("Enter your name: ")

        while (True):
            print("\n")
            print(cust_main_menu())
            cust_main_choice = input('Select menu number: ')
            exitFlag = False
            try: 
                cust_main_choice = int(cust_main_choice)
                if cust_main_choice == 1: # Buy items

                    while not exitFlag:
                        print("\n")
                        print(display_items())
                        print(below_menu("\nHint: Select an index from the table to purchase \nitems directly or choose an option from the menu.\n"))
                        backFlag = False

                        while (True):
                            cust_display_choice = input('\nSelect index or option: ')
                            try:
                                cust_display_choice_int = int(cust_display_choice)
                                if 0 < cust_display_choice_int <= len(inventory):
                                    try:
                                        selected_item = inventory[cust_display_choice_int - 1]
                                        available_stock = selected_item['Stock']
                                        total_qty_in_cart = sum(item['Qty'] for item in cart if item['Name'] == selected_item['Name'] and item['Brand'] == selected_item['Brand'])

                                        buy_amount = int(input('Enter the amount: '))
                                        if 0 < buy_amount <= available_stock - total_qty_in_cart:
                                            cart.append({'Name' : selected_item['Name'], 'Brand' : selected_item['Brand'], 
                                                        'Qty' : buy_amount, 'Price' : selected_item['Price']})
                                            print('Item has been added to cart') 
                                            break
                                        elif buy_amount <= 0:
                                            print("Invalid input. Please enter a valid amount.")
                                        else:
                                            print(f"\nStock is not enough for your demand. \nYou already have {total_qty_in_cart} in your cart.")
                                    except ValueError:
                                        print("Invalid amount. Please input a valid amount.")
                                else:
                                    print("Invalid index. Please select a valid index.")

                            except ValueError:
                                if cust_display_choice == 'a': # Search items by Name or Brand
                                    search_items()
                                    break

                                elif cust_display_choice == 'b': # Filter items by Category
                                    filter_items()
                                    break
                                    
                                elif cust_display_choice == 'c': # Order items by Price
                                    order_items()
                                    break

                                elif cust_display_choice == 'd': # Back
                                    break

                                else:
                                    print('Invalid option. Please input a valid option.')

                        checkout()

                elif cust_main_choice == 2: # Cart 
                    if cart:
                        print(display_cart())
                        payment()
                    else:
                        print("Your cart is empty")

                elif cust_main_choice == 3: # Exit
                    break

                else:
                    print("Invalid menu number. Please select a valid menu.")

            except:
                print('Invalid input. Please enter a valid menu number.')
                
    elif login_choice == 'employee' or login_choice == 'b':
        attempt = 0
        while attempt < 3:
            login_username = input('Enter Username: ')
            login_password = input('Enter Password: ')
            
            authenticated_user = authenticate(login_username, login_password, adminList)
            
            if authenticated_user:
                break
            else:
                attempt += 1 
                print('Invalid username or password.')
        else:
            print('Maximum login attempts reached. Exiting...')
            continue

        while (True):
            print(emp_main_menu())
            try:
                emp_main_choice = int(input('\nSelect menu number: '))
            except ValueError:
                print('Invalid input. Please enter a valid menu number.')
                continue

            if emp_main_choice == 1: # Show items

                while (True):
                    print(emp_display_items()) 
                    print(emp_below_menu())
                    emp_show_choice = input('\nSelect option: ').lower()

                    if emp_show_choice == 'a': # Add
                        add_items()
                    elif emp_show_choice == 'b': # Update
                        update_items()
                    elif emp_show_choice == 'c': # Delete
                        delete_items()
                    elif emp_show_choice == 'd': # Back
                        break
                    else:
                        print('Invalid option. Please input a valid option.')
        
            elif emp_main_choice == 2: # Exit
                break

    else:
        print("\nInvalid input. Please select either 'Customer' or 'Employee'.")

