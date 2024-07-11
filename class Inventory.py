"""4. Write a Python class Inventory with attributes like item_id,
 item_name, stock_count, and price, and methods like add_item, update_item,
   and check_item_details.
Use a dictionary to store the item details, where the key is the item_id 
and the value is a dictionary containing the item_name, stock_count, and price.  (5 marks)"""


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id in self.items:
            return f"Item ID {item_id} already exists."
        self.items[item_id] = {
            "item_name": item_name,
            "stock_count": stock_count,
            "price": price
        }
        return f"Item {item_name} added successfully."

    