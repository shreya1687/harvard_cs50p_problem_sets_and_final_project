from menu.menu import Menu
from generator.IDGenerator import IDGenerator
from datetime import datetime
import inflect
import csv

# Item Class : Represents item related information avaialble in online grocery store
class Item:
    def __init__(self):
        self._item_list = {}
    
    # Getter method using @property decorator
    @property
    def item_list(self):
        return self._item_list
    
    # Display the items available in online grocery store
    def display_items(self):
        print("Below are the list of items available for purchase in this store... ")
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row['Item_Id']} ---> {row['Item'].capitalize()} | {row['Quantity']} | Rs.{row['Price']}")
                self.item_list[row['Item_Id']] = [row['Item'], 1, row['Quantity'], row['Category']]
    
    
    # Return the cost of the item selected
    def calculate_total_bill(self, item):
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            item_cost = [int(row['Price']) for row in reader if row['Item'] == item]
            return item_cost.pop()
    
    # Return the selcted item related information to generate the invoice of items available in shopping cart 
    def generate_invoice(self, item):
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            item_info = [(int(row['Price']),row['Item_Id'],row['Quantity']) for row in reader if row['Item'] == item]
            for item_cost, item_id, qty in item_info:
               return item_id, int(item_cost), qty
                                                                                                                                        
# ShoppingCart Class: Represents list of items in shopping cart
class ShoppingCart:    
    def __init__(self):
        self.shopping_list = {}
        self.remove_items= {}
        self.item = Item()
        self.id = IDGenerator()
        
    def start(self):
        self.display_items()
    
    # Call to show the list of items to the customer
    def display_items(self):
        items = self.item.display_items()
        self.display_menu()
        
    # Call to show menu option
    def display_menu(self):
        while True:      
            print("Select from below...")
            menu = Menu()
            menu_list = menu.display_menu()
            
            for index, option in enumerate(menu_list, start=1):
                print(f"{index} | {option}")
            
            # Call to select the menu
            self.select_menu_option(menu_list)
        
    # Call to ask customer to select the menu item
    def select_menu_option(self, menu_list):
        option = 0
        while True:
            try:
                option = int(input("Select Menu option: "))
                if option <= 0 or option > len(menu_list):
                    print("Reselect the valid menu option...")
                    continue 
                break                    
            except ValueError:
                print("Invalid option!")
        
        match option: 
            case 1: 
                self.add_item_to_cart()
            case 2: 
                self.remove_item_from_cart()
            case 3: 
                sum = self.calculate_total_bill()
                print(f"Total amount: {sum}")
            case 4:
                self.generate_invoice()
                exit()
            case 5: 
                exit()

    # Call to add an item in shopping cart
    def add_item_to_cart(self):
        select_item = 0
        while True:            
            for index, value in enumerate(self.shopping_list.values(), start=1):
                print(f"{index} | {value[0]}| {value[1]}")
            try:
                select_item = int(input("Select the item to be added...\n"))
                if select_item <= 0 or select_item > len(self.item.item_list.keys()):
                    print("Reselect the valid item...")
                    continue
                # Add the item into shopping list
                item_info = self.item.item_list.get(str(select_item))
                if select_item in self.shopping_list.keys():
                    item_info[1] += 1
                else:                          
                    self.shopping_list[select_item] = item_info
                    print(self.shopping_list)
                break                    
            except ValueError:
                print("Invalid option!")
          
    # Call to remove an item from shopping cart
    def remove_item_from_cart(self):
        remove_item = 0
        response = None
        
        if not self.shopping_list.keys():
            print("No items added in the shopping cart!")
            self.display_menu()
        
        # Display items in the cart
        print("Items available in the cart....")
        
        while True:
            try:
                for index, value in enumerate(self.shopping_list.values(), start=1):
                    print(f"{index} | {value[0]} | {value[1]}")
                    self.remove_items[index] = value[0]
                    
                remove_item = int(input("Which item you wish to remove...\n"))
                if remove_item <= 0 or remove_item > len(self.shopping_list.keys()):
                    print("Reselect the valid item...")
                    continue
                # Remove item from the shopping list
                item_info = self.remove_items.get(remove_item)
                for index, value in self.shopping_list.items():
                    if value[0] == item_info:
                        remove_item = index
                        if int(value[1]) > 1:
                            response = input("Do you wish to remove entire item from the bucket? (Yes/No)..").capitalize()
                        if response == "No":
                            value[1] = int(value[1]) - 1
                            self.shopping_list[index]=value

                if response == "No":
                    break
                self.shopping_list.pop(remove_item)
                self.remove_items.clear()        
                break                    
            except ValueError:
                print("Invalid option!")
    
    # Call to calculate the total amount of the items available in the cart
    def calculate_total_bill(self): 
        # Display items in the cart
        print("Items available in the cart....")

        if not self.shopping_list.keys():
            print("No items added in the shopping cart!")
            self.display_menu()
        for index, value in enumerate(self.shopping_list.values(), start=1):
            print(f"{index} | {value[0]} | {value[1]}")
                   
        sum = 0
        for item in self.shopping_list.values():
            cost_per_item = self.item.calculate_total_bill(item[0])
            sum += cost_per_item * item[1]
        return sum
        
    # Call to generate the invoice of the items purchased by the customer
    def generate_invoice(self):
        total_bill = 0
        current_time = datetime.now()
        invoice_no = self.id.generate_invoice_id(current_time)
        order_id = self.id.generate_order_id()
                
        print("                       TAX INVOICE                        ")
        print("----------------------------------------------------------")
        print("Invoice No                      Date and Time")
        print(f"{invoice_no}              {current_time.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("----------------------------------------------------------")
        print("ITEM DESCRIPTION")
        print(f"Item ID                Qty                Rate")
        print("----------------------------------------------------------")
        for item in self.shopping_list.values():
            item_id, cost, qty = self.item.generate_invoice(item[0])
            print(f"{item[0].capitalize()} - {item[2]}")
            print(f"{int(item_id):02d}                     {item[1]:02d}                 {cost*item[1]}")
            total_bill += cost*item[1]
        print("----------------------------------------------------------")
        print(f"Total                               {total_bill}")
        print("----------------------------------------------------------")   
        print(f"Total Invoice Value (In Figure): Rs.{total_bill}")
        words = inflect.engine().number_to_words(total_bill).capitalize()
        print(f"Total Invoice Value (In Words): {words} rupees")
        print()
        print(f"                Order Id: {order_id:09d}")


def main():
    print("Welcome to Online Grocery Store... Enjoy your time shopping !")
    cart = ShoppingCart()    
    
    # Call to start the grocery shopping
    cart.start()
    
    print("Have a Nice day ! Visit again...")
    
if __name__ == "__main__":
    main()