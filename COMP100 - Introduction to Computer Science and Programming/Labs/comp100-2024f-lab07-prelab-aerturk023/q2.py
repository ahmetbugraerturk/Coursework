stock = {
    "ram": 6,
    "ssd": 0,
    "monitor": 32,
    "power_supply": 15,
    "keyboard": 20
} # Do not modify this dictionary

prices = {
    "ram": 55,
    "ssd": 90,
    "monitor": 220,
    "power_supply": 35,
    "keyboard": 25
} # Do not modify this dictionary

def compute_bill(order):
    """Calculates the total price for the given hardware list,
    only billing items that are in stock, and updates the stock accordingly."""
    
    price = 0
    
    for i in order:
        if stock[i] != 0:
            price += prices[i]
            stock[i] -= 1
    return price