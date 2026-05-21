cart = []
total_product_amount = 0

while True:
    print("\n----- PRODUCT MENU -----")
    print("1. Mobile       - Rs. 15000")
    print("2. Headphone    - Rs. 1500")
    print("3. Keyboard     - Rs. 800")
    print("4. Mouse        - Rs. 500")
    print("5. Power Bank   - Rs. 1200")

    choice = int(input("Choose your product number: "))

    if choice == 1:
        product = "Mobile"
        price = 15000
    elif choice == 2:
        product = "Headphone"
        price = 1500
    elif choice == 3:
        product = "Keyboard"
        price = 800
    elif choice == 4:
        product = "Mouse"
        price = 500
    elif choice == 5:
        product = "Power Bank"
        price = 1200
    else:
        print("Invalid product choice")
        continue

    cart.append((product, price))
    total_product_amount += price

    more = input("Do you want to add more products? (yes/no): ")

    if more.lower() != "yes":
        break



print("\n----- DELIVERY DISTANCE -----")
print("1. 10 KM - Rs. 50")
print("2. 20 KM - Rs. 100")
print("3. 30 KM - No Delivery")

distance = int(input("Choose delivery distance option: "))

if distance == 1:
    delivery_charge = 50
    delivery_status = "10 KM"
elif distance == 2:
    delivery_charge = 100
    delivery_status = "20 KM"
elif distance == 3:
    print("Sorry, delivery not available for 30 KM")
    exit()
else:
    print("Invalid distance choice")
    exit()



confirm = input("\nConfirm order? (yes/no): ")

if confirm.lower() == "yes":
    final_total = total_product_amount + delivery_charge

    print("\n========== INVOICE ==========")
    print("Ordered Products:")

    for item, price in cart:
        print(item, "- Rs.", price)

    print("-----------------------------------------")
    print("Total Product Amount : Rs.", total_product_amount)
    print("Delivery Distance    :", delivery_status)
    print("Delivery Charges     : Rs.", delivery_charge)
    print("-----------------------------------------")
    print("Final Total Amount   : Rs.", final_total)
    print("-----------------------------------------")
    print("Order Completed Successfully!")
    print("Thank you for shopping with us.")
else:
    print("Order Cancelled")
