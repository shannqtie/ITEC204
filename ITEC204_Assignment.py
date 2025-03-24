# Importing required modules
import random  # Example of `import` for random number generation

# Define classes for User and Product
class User:
    def __init__(self, username, password, role, email=None):
        self.username = username
        self.password = password
        self.role = role
        self.email = email
        self.cart = []
        self.is_active = True

    def __str__(self):
        return f"User {self.username}, Role: {self.role}"


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}, Price: {self.price}, Stock: {self.stock}"


# Global variables
users = []
products = []
current_user = None

# Sample Users
seller = User("seller", "seller123", "seller", "seller123.com")
buyer = User("shann", "1234", "buyer", "shannmaganda.com")
users.append(seller)
users.append(buyer)

# Sample Products
products.append(Product(1, "Laptop", 1000, 10))
products.append(Product(2, "Smartphone", 500, 15))

# Function for Seller Role
def seller_dashboard():
    global current_user
    while True:
        print("\nSeller Dashboard:")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. View Products")
        print("4. Logout")
        choice = input("Select an option or type 'back' to return: ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            delete_product()
        elif choice == "3":
            view_products()
        elif choice == "4":
            print(f"Logged out {current_user.username}")
            break
        elif choice.lower() == 'back':
            break  # Go back to the previous menu
        else:
            print("Invalid choice, please try again.")

# Function for Buyer Role
def buyer_dashboard():
    global current_user
    while True:
        print("\nBuyer Dashboard:")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Make Purchase")
        print("5. Change Email")
        print("6. Logout")
        choice = input("Select an option or type 'back' to return: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            make_purchase()
        elif choice == "5":
            change_email()
        elif choice == "6":
            print(f"Logged out {current_user.username}")
            break
        elif choice.lower() == 'back':
            break  # Go back to the previous menu
        else:
            print("Invalid choice, please try again.")

# Function for viewing products (for both Seller and Buyer)
def view_products():
    print("\nAvailable Products:")
    for product in products:
        print(f"{product.product_id}. {product.name} - {product.price} - {product.stock} in stock")
    print("")

# Function for adding a new product (Seller only)
def add_product():
    if current_user.role != "seller":
        print("You must be an seller to add products.")
        return
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    product_id = len(products) + 1
    new_product = Product(product_id, name, price, stock)
    products.append(new_product)
    print(f"Product '{name}' added successfully.")

# Function for deleting a product (Seller only)
def delete_product():
    if current_user.role != "seller":
        print("You must be an seller to delete products.")
        return
    product_id = int(input("Enter the product ID to delete: "))
    product = next((p for p in products if p.product_id == product_id), None)
    if product:
        products.remove(product)
        print(f"Product '{product.name}' deleted successfully.")
    else:
        print("Product not found.")

# Function for adding product to cart (Buyer only)
def add_to_cart():
    if current_user.role != "buyer":
        print("You must be a buyer to add products to your cart.")
        return
    
    print("\nSelect a product to add to your cart:")
    view_products()  # Show products before asking for input
    product_id = int(input("Enter product ID to add to cart: "))
    product = next((p for p in products if p.product_id == product_id), None)
    
    if product and product.stock > 0:
        current_user.cart.append(product)
        product.stock -= 1  # Decrease stock when added to cart
        print(f"{product.name} added to your cart.")
    else:
        print("Product not found or out of stock.")

# Function for viewing cart (Buyer only)
def view_cart():
    if current_user.role != "buyer":
        print("You must be a buyer to view your cart.")
        return
    if not current_user.cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        for item in current_user.cart:
            print(f"{item.name} - {item.price}")
    print("")

# Function for making a purchase (Buyer only)
def make_purchase():
    if current_user.role != "buyer":
        print("You must be a buyer to make a purchase.")
        return
    if not current_user.cart:
        print("Your cart is empty. Add products first.")
        return
    total_amount = sum(item.price for item in current_user.cart)
    print(f"Total amount: {total_amount}")
    confirm = input("Do you want to make the purchase? (yes/no): ")
    if confirm.lower() == "yes":
        print("Purchase successful!")
        current_user.cart.clear()  # Empty the cart after purchase
    else:
        print("Purchase cancelled.")

# Function for changing email (Buyer only)
def change_email():
    if current_user.role != "buyer":
        print("You must be a buyer to change your email.")
        return
    new_email = input("Enter your new email: ")
    current_user.email = new_email
    print(f"Email changed to {new_email}")

# Login system with exception handling
def login():
    global current_user
    print("Welcome to the E-Commerce Platform")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    try:
        current_user = next(user for user in users if user.username == username and user.password == password)
    except StopIteration:
        print("Invalid credentials. Please try again.")
        return
    
    print(f"Welcome {current_user.username}!")
    if current_user.role == "seller":
        seller_dashboard()
    else:
        buyer_dashboard()

# Main program flow
if __name__ == "__main__":
    login()
