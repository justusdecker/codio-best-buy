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
    print(MENU)

if __name__ == '__main__':
    main()