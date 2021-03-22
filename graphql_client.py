# GraphQL imports
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# GraphQL
request_transport=RequestsHTTPTransport(
    url='https://info802-commandeur-graphql.herokuapp.com/graphql',
    use_json=True,
    headers={
        "Content-type": "application/json",
    },
    verify=True,
    retries=3,
)

client = Client(
    transport=request_transport,
    fetch_schema_from_transport=True,
)

query = gql('''
    query {
        products {
            name
            price
            quantity
            weight
        }
    }
''')

j = client.execute(query)

def print_products():
    print("\t_____PRODUCT LIST_____")
    for i in range(len(j["products"])):
        print("\t" + str(i+1) + ". " + j["products"][i]["name"] + " : " + j["products"][i]["price"] + "€")

def get_product(item):
    return j["products"][item]

def get_weight(item):
    return float(j["products"][item]["weight"])

def get_price(item):
    return float(j["products"][item]["price"])