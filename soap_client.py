# SOAP imports
import zeep

# SOAP
wsdl = 'https://info802-commandeur-soap.herokuapp.com/shipping?wsdl'
client = zeep.Client(wsdl=wsdl)

def get_shipping(distance, weight_t):
    return int(client.service.shipping(distance, weight_t)[0])

def print_shipping(distance, weight_t):
    print("Shipping price is %i€" % get_shipping(distance, weight_t))