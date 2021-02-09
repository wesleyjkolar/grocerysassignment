stores = []

class Store: 
  def __init__(self, name): 
    self.name = name 
    self.items = [] 
  def add_item(self, item):
      pass 

class Item: 
    def __init__(self, name): 
        self.name = name 
        


while True: 
    print("*************************")
    print("Enter 1 to add a store: ")
    print("Enter 2 to add item to a store: ")
    print("Enter 3 to view lists: ")
    print("Enter q to quit: ")
    print("*************************")
    choice = input("Enter choice: ")
    
    if choice == "1":
        store_name = input("Enter store name: ")
        store = Store(store_name)
        stores.append(store)
      
    elif choice == "2":
        for index in range(0, len(stores)): 
            store = stores[index]
            print(f"{index + 1} {store.name}")
        store_index = int(input("Choose store to add items: "))
        store = stores[store_index - 1]
        item_name = (input("Name and quantity of item?:"))
        item = Item(item_name)
        store.items.append(item)

    elif choice == "3":
        for store in stores: 
            print(f"{store.name} - ")
            for item in store.items: 
                print(f"{item.name}")

    elif choice == "q":
        break 