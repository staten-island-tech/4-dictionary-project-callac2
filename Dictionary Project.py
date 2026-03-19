






item = [
{
    "name": "White T-shirt",
    "price": 12.99,
    "department": "women's shirts",
    "description": "100 percent cotton, color: white."
},
{
    "name": "Blue T-shirt",
    "price": 12.99,
    "department": "women's shirts",
    "description": "100 percent cotton, color: blue."
},
{
    "name": "Red T-shirt",
    "price": 12.99,
    "department": "women's shirts",
    "description": "100 percent cotton, color: red"
},
{
    "name": "Black T-shirt",
    "price": 12.99,
    "department": "women's shirts",
    "description": "100 percent cotton, color: black"
},
{
    "name": "Purple T-shirt",
    "price": 12.99,
    "department": "women's shirts",
    "description": "100 percent cotton, color: purple"
},
{
    "name": "High Rise Jean shorts",
    "price": 24.99,
    "department": "women's shorts",
    "description": "100 percent cotton denim, color: denim blue"
},
{
    "name": "black sweatpants, fold-over waistband",
    "price": 20.99,
    "department": "women's apparel",
    "description": "100 percent cotton, color: black"
}
    ]

""" for index, item in enumerate(item):
        print(index, ":", item["name"])
 """
print(item[1]["name"])



add_to_cart = (int(input("Add to cart?? If YES, put 1 if NO put 0")))
cart = []

while add_to_cart == 1:
    

    if add_to_cart == 0:
        print ("Item was not added to your cart.")