""" Write a Python class Restaurant with attributes like menu_items,
 book_table, and customer_orders, and methods like add_item_to_menu, 
 book_tables, and customer_order.
Perform the following tasks now:

Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders."""

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders =[]

    def add_item_to_menu(self,item_name, price):
        if item_name in self.menu_items:
            return f"{item_name} is on the list"
        else:
            self.menu_items[item_name]= price
            return f"{item_name} as been added to the menu"
        
    def book_tables(self, customer_name, table_number):
        for reservation in self.book_table:
            if reservation ['table_number'] == table_number:
                return f"table {table_number} already booked."
            self.book_table.append({"customer name": customer_name, "Table": table_number})
            return f"table {table_number} has been booked for {customer_name}"
        
    def customer_order(self,customer_name, customer_order):
        self.customer_orders.append({"customer name": customer_name, "customer order": customer_order})
        return f"order has been placed for {customer_name}"
    
    