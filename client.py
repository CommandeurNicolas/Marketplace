from soap_client import print_shipping, get_shipping
from graphql_client import print_products, get_price, get_weight, get_product

total = 0

def print_total_price(price, shipping):
    global total
    total = total + price + shipping
    print("Total price is : %i€" % total)

def main():
    while(1):
        print_products()
        choice = int(input("What do you want to buy ? ")) - 1
        times = int(input("How many ? "))
        distance = int(input("Distance from our center ? "))
        weight = int(get_weight(choice)*times)
        shipping = get_shipping(distance, weight)
        price = get_price(choice)*times
        print_total_price(price, shipping)

        buy = str(input("Go to payment ? y/n\t"))
        if(buy == "y"):
            print("payment processing ...")
            print("Payment succeeded !")
            break
        else:
            print("You continue your shopping ...")

    
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
