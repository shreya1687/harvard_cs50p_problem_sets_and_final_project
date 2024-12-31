# Online Grocery Store
*This project implements a simple Online Grocery System that allows users to select the shopping items from a provided list, add or remove the items from their shopping cart, calculate the total bill, and generates an invoice.
*
Features:
Command Line Interface: Command line interface for all available features  
Menu Options: - 'Add to Cart', 'Remove from Cart','Total Bill', 'Generate Invoice','Exit'
Inovice: View detailed invoice of the customer displaying Item ID for each Item, Invoice ID and Order ID.

Prerequisites:
Python 3.x
Dependencies from requirements.txt

Setup:
Clone this repository: git clone https://github.com/shreya1687/harvard_cs50p_problem_sets_and_final_project.git
Install the required dependencies: pip install -r requirements.txt

Usage:
Start the application: python project.py

Testing:
To run the tests: pytest test_project.py

Tutorial:
Welcome to Online Grocery Store... Enjoy your time shopping ! 
1 ---> Tea_leaves | 1 kg | Rs.100
2 ---> Coffee | 1 kg | Rs.200
3 ---> Aluminium_foil | 1 l | Rs.100
4 ---> Sugar | 1 kg | Rs.60
5 ---> Toothpaste | 1 l | Rs.110
6 ---> Shampoo | 1 l | Rs.300
7 ---> Detergent_powder | 1 kg | Rs.250
8 ---> Phenyl | 1 l | Rs.299
9 ---> Wiper | 1 pc | Rs.105
10 ---> Incense_sticks | 1 pc | Rs.90
11 ---> Macroni | 1 kg | Rs.100
12 ---> Toor_dal | 1 kg | Rs.200
13 ---> Urad_dal | 1 kg | Rs.100
14 ---> Moong_dal | 1 kg | Rs.120
15 ---> Basmati_rice | 1 kg | Rs.120
16 ---> Cumin_spice | 1 kg | Rs.99
17 ---> Garam_masala | 1 kg | Rs.70
18 ---> Almonds | 1 kg | Rs.250
19 ---> Cashew_nuts | 1 kg | Rs.300

User is asked to select the menu option.

Select from below...
1 | Add to Cart
2 | Remove from Cart
3 | Total Bill
4 | Generate Invoice
5 | Exit

Select Menu Option: <enter the option from (1,2,3,4,5)>

If option 1 is selected:
User is asked to select the item to be added in the shopping cart. Any item from the items list can be selected. User need to provide the relevant number corresponding to each item. If incorrect number is selected, user is asked to select the item again. If incorrect input is added like "toor dal" etc , invalid option is displayed and user is asked to enter the number again.Once the user has added correct number to add the item in the cart, user is prompted with menu again. Same item can be added again and Quantity of the item will be increased.

If option 2 is selected:
User is asked to select the item to be removed from the shopping cart. Any item from the items list can be selected. User need to provide the relevant number corresponding to each item. If incorrect number is selected, user is asked to select the item again. If incorrect input is added like "toor dal" etc , invalid option is displayed and user is asked to enter the number again.Once the user has added correct number to remove the item in the cart, user is prompted with menu again. If the same item is available more than once i.e. quantity is more than 1, user is prompted if all the items need to be removed (Yes/No). If user selects No, quantity is decreased by one for that specific item. If user selects Yes, the whole item is removed from the shopping cart. 

If option 3 is selected:
User is displayed with the total cost of the items selected in shopping cart.

If option 4 is selected:
User is displayed with tdetailed invoce listing the Item ID, Date and time when the invoice is generated, Detail of each item purchased - Item ID, Quantity and Rate. Total bill amount (in figure and words) and Order ID.

If option 5 is selected, user is exited from the system.


Dependencies for test_project.py:
pytest: A framework used for testing Python code.
The test_project.py script is designed to test the functionality of the Online Grocery system. Here's a brief summary:
Creates an instance for Shopping Cart and verify the functionality.

Tests:
test_calculate_total_bill(): checks the total bill for an item.
test_add_item_to_cart(): Test to add a new item in the shopping cart.
test_remove_item_from_cart(): Tests the remove functionality when the shopping cart is empty .


Classes & Methods:
1. Item:
Represents item related information avaialble in online grocery store:
item_list()- Getter method using @property decorator. Returns the shopping list as a dictionary.
display_items() - Display the items available in online grocery store
calculate_total_bill(item) - Return the cost of the item selected
generate_invoice(item) - Return the selcted item related information to generate the invoice of items available in shopping cart

2. Shopping Cart:
Represents list of items in shopping cart
display_items() - Call to show the list of items to the customer
display_menu() - Call to show menu option
select_menu_option(menu_list) - Call to ask customer to select the menu option
add_item_to_cart() - Call to add an item in shopping cart
remove_item_from_cart() - Call to remove an item from shopping cart
calculate_total_bill() - Call to calculate the total amount of the items available in the cart
generate_invoice() - Call to generate the invoice of the items purchased by the customer

3. Menu:
Represents the menu options that can be added/removed 
display_menu(): Return the list of availble menu options

4. IDGenerator:
Generate the Invoice ID and Order ID for the Customer bill
generate_invoice_id(current_time) - Return Invoice ID with fixed sequence - IVFKA<last two digit of year>DAC<5 digits in order starting from 1>
generate_order_id() - Return Order ID with 9 digits starting from 1
