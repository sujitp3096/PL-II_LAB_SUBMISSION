import os
from datetime import datetime

# ----------- MENU -----------
menu = {
    1: ("Coffee", 50),
    2: ("Tea", 30),
    3: ("Sandwich", 80),
    4: ("Burger", 120),
    5: ("Pizza", 200)
}

# ----------- UI FUNCTIONS -----------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(title):
    print("\n" + "="*40)
    print(title.center(40))
    print("="*40)

# ----------- BASE CLASS -----------
class Cafe:
    def display_menu(self):
        clear()
        header("☕ CAFE MENU ☕")
        print(f"{'No.':<5}{'Item':<15}{'Price':>10}")
        print("-"*40)

        for key, value in menu.items():
            print(f"{key:<5}{value[0]:<15}₹{value[1]:>8}")

        print("="*40)

# ----------- ORDER CLASS -----------
class Order(Cafe):
    def __init__(self):
        self.order_list = []

    def take_order(self):
        self.order_list = []

        while True:
            try:
                item = int(input("\nEnter item number: "))

                if item in menu:
                    qty = int(input("Enter quantity: "))
                    self.order_list.append((menu[item][0], menu[item][1], qty))

                    # PROFESSIONAL CHOICE MENU
                    while True:
                        print("\n1. Add more items")
                        print("2. Finish order")

                        choice = input("Enter choice (1/2): ")

                        if choice == "1":
                            break

                        elif choice == "2":
                            return

                        else:
                            print("❌ Invalid choice! Enter 1 or 2.")

                else:
                    print("❌ Invalid item!")

            except ValueError:
                print("❌ Enter valid number!")

    def generate_bill(self):
        if not self.order_list:
            print("No items ordered!")
            return 0

        clear()
        header("🧾 FINAL BILL 🧾")

        print(f"{'Item':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
        print("-"*40)

        total = 0

        for name, price, qty in self.order_list:
            cost = price * qty
            total += cost
            print(f"{name:<15}{qty:<5}₹{price:<10}₹{cost:<10}")

        print("-"*40)
        print(f"{'TOTAL AMOUNT':<25}₹{total}")
        print("="*40)

        return total

# ----------- FILE HANDLING -----------
class FileManager:
    def save_bill(self, orders, total):
        try:
            with open("bill.txt", "a", encoding="utf-8") as file:   # FIXED HERE
                file.write("\n===== NEW ORDER =====\n")
                file.write(f"Date: {datetime.now()}\n")

                for name, price, qty in orders:
                    file.write(f"{name} x {qty} = ₹{price*qty}\n")

                file.write(f"Total: ₹{total}\n")

            print("\n✅ Bill saved successfully!")

        except Exception as e:
            print("❌ Error saving file:", e)

# ----------- MAIN PROGRAM -----------
def main():
    cafe = Order()
    file_manager = FileManager()

    while True:
        clear()
        header("🍽️ CAFE MANAGEMENT SYSTEM 🍽️")

        print("1. Show Menu")
        print("2. Take Order")
        print("3. Exit")
        print("="*40)

        choice = input("Enter choice: ")

        if choice == "1":
            cafe.display_menu()
            input("\nPress Enter to continue...")

        elif choice == "2":
            cafe.display_menu()
            cafe.take_order()
            total = cafe.generate_bill()
            file_manager.save_bill(cafe.order_list, total)

            # RESET ORDER AFTER BILL
            cafe.order_list = []

            input("\nPress Enter to continue...")

        elif choice == "3":
            print("\n🙏 Thank you! Visit Again ☕")
            break

        else:
            print("❌ Invalid choice!")
            input("Press Enter to continue...")

# ----------- RUN PROGRAM -----------
main()