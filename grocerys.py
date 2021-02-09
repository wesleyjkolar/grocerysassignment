stores = []

class Store: 
  def __init__(self, name): 
    self.name = name 
    self.items = [] 

# def thelist():
    #for loop that displays saved stores/items??? but how

print("Enter 1 to add a store: ")
print("Enter 2 to add item to a store: ")
print("Enter 3 to view list: ")
print("Enter q to quit: ")

while True: 
    choice = input("Enter choice: ")
    if choice == "1":
        store_name = input("Enter store name: ")
        store = Store(store_name)
        stores.append(store)
      
    elif choice == "2":
        store = Store(input("Name of store: "))
        item = (input("Name and quantity of item?:"))
        store.items.append(item)

# elif choice == "3":
        #call function called "thelist()" and have it display everything nicely
        #IDKIDKIDK
    elif choice == "q":
        break