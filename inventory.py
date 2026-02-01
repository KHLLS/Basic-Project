import pandas as pd

class AppInventory:
    def __init__(self):
        self.inventory = {}

    def run(self):
        while True:
            print("Welcome To Inventory App")
            print("Menu List")
            print("1. Add Item")
            print("2. Update Item")
            print("3. Show All Item")
            print("4. Find Item")
            print("5. Save File")
            print("6. Exit")
            try:
                option = int(input("Input Your Option: "))
                if option == 1:
                    self.run_add_item()
                elif option == 2:
                    self.run_update_item()
                elif option == 3:
                    self.run_show_item()
                elif option == 4:
                    self.run_find_item()
                elif option == 5:
                    self.save_file()
                elif option == 6:
                    break
                else:
                    print("Option Not Valid")
                    input("Enter To Main Menu")

            except ValueError:
                print("Input Not Valid")
                input("Enter To Main Menu")

    def run_add_item(self):
        name = input("Input Name Item: ").lower().strip()

        if name in self.inventory:
            print("Item Already Exist")
        else:
            price = float(input("Input The Price: "))
            stock = int(input("Input Stock: "))
            self.inventory[name] = {"price": price, "stock": stock}
            print(f"{name} added successfully")
        input("Enter To Main Menu")
    
    def run_update_item(self):
        name = input("Input Name Item: ").lower().strip()

        if name in self.inventory:
            new_price = float(input("Input New Price: "))
            new_stock = int(input("Input New Stock: "))
            self.inventory[name]["price"] = new_price
            self.inventory[name]["stock"] = new_stock
            print(f"{name} updated successfully")
        else:
            print(f"{name} Not Found")
        input("Enter To Main Menu")

    def run_show_item(self):
        inventory = pd.DataFrame(self.inventory).T
        print("Inventory Item: ")
        print(inventory)
        input("Enter To Main Menu")

    def run_find_item(self):
        name = input("Search Item: ")

        if name in self.inventory:
            inventory = pd.DataFrame(self.inventory[name]).T
            print(f"{inventory}")
        else:
            print(f"{name} Not Found")
        input("Enter To Main Menu")
        
    def save_file(self):
        if not self.inventory:
            print("Inventory is empty")
        else:
            data_list = []
            for item_name, item_data in self.inventory.items():
                data_list.append({
                    'name': item_name,
                    'price': item_data['price'],
                    'stock': item_data['stock']
                })
            df = pd.DataFrame(data_list)
            name_file = input("Input Name File: ")
            df.to_csv(f'{name_file}.csv', index=False)
            print(f"File saved to {name_file}.csv")
        input("Enter To Main Menu")


if __name__ == "__main__":
    app = AppInventory()
    app.run()
    print("Done")


        