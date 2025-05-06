# AI-EBPL-Supply-chain-management-
# supply_chain.py

class Product:
    def __init__(self, pid, name, quantity):
        self.pid = pid
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.pid}, Name: {self.name}, Quantity: {self.quantity}"


class Supplier:
    def __init__(self, sid, name, contact):
        self.sid = sid
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"ID: {self.sid}, Name: {self.name}, Contact: {self.contact}"


class SupplyChainManager:
    def __init__(self):
        self.products = {}
        self.suppliers = {}

    def add_product(self, pid, name, quantity):
        self.products[pid] = Product(pid, name, quantity)
        print("Product added.")

    def update_inventory(self, pid, quantity):
        if pid in self.products:
            self.products[pid].quantity += quantity
            print("Inventory updated.")
        else:
            print("Product not found.")

    def add_supplier(self, sid, name, contact):
        self.suppliers[sid] = Supplier(sid, name, contact)
        print("Supplier added.")

    def list_inventory(self):
        print("Inventory:")
        for product in self.products.values():
            print(product)

    def list_suppliers(self):
        print("Suppliers:")
        for supplier in self.suppliers.values():
            print(supplier)


def main():
    scm = SupplyChainManager()
    while True:
        print("\n1. Add Product\n2. Update Inventory\n3. Add Supplier\n4. List Inventory\n5. List Suppliers\n6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            pid = input("Product ID: ")
            name = input("Product Name: ")
            quantity = int(input("Quantity: "))
            scm.add_product(pid, name, quantity)

        elif choice == "2":
            pid = input("Product ID: ")
            quantity = int(input("Quantity to Add/Subtract: "))
            scm.update_inventory(pid, quantity)

        elif choice == "3":
            sid = input("Supplier ID: ")
            name = input("Supplier Name: ")
            contact = input("Contact Info: ")
            scm.add_supplier(sid, name, contact)

        elif choice == "4":
            scm.list_inventory()

        elif choice == "5":
            scm.list_suppliers()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
