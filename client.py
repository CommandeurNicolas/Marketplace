from soap_client import print_shipping, get_shipping
from graphql_client import print_products, get_price, get_weight, get_product


def main():
    total = 0

    while(1):
        print_products()
        choice = int(input("What do you want to buy ?\t")) - 1
        times = int(input("How many ?\t"))
        distance = int(input("Distance from our center ? (km)\t"))
        weight = int(get_weight(choice)*times)
        shipping = get_shipping(distance, weight)
        price = get_price(choice)*times

        print("____________ CART ____________")
        total = total + price
        print(" Items price :\t\t%i€" % total)
        total = total + shipping
        print(" shipping price :\t%i€" % shipping)
        print(" Total price is :\t%i€" % total)

        buy = str(input("Go to payment ? y/n\t"))
        if(buy == "y"):
            print("\tPayment processing ...")
            print("\tPayment succeeded !")
            break
        else:
            print("You continue your shopping ...")

    
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
