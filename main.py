from store import Store
STORE = Store()
MENU = """
Welcome to BestBuy!
-----------------------------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""

def main():
    is_running = True
    while is_running:
        print(MENU)
        user_input = input('Please choose a number: ')
        match user_input:
            case "1":
                print(f"{'Name':<30} {'Price':<6} {'Quantity':<15}")
                for prod in STORE.products:
                    print(prod.show())
                input('ENTER to continue!')
            case "2":
                print(STORE.get_total_quantity())
                input('ENTER to continue!')
            case "3":
                pass
            case "4":
                is_running = False

if __name__ == '__main__':
    main()