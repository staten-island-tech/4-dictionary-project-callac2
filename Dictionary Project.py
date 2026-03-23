






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
    "department": "women's pants",
    "description": "100 percent cotton, color: black"
}
    ]




""" print(item[2]["name"]) """


cart = []
prices = []
cost = 0
shop = True
for index, item in enumerate(item):
        print(index, ":", item["name"],item["price"])

while shop:
    add_to_cart = int(input("Add item to your cart? Type the number"))
    cart.append(item[add_to_cart]["name"])
    prices.append(item[add_to_cart]["price"])
    shop_continiue = input("continue shopping or check out? Enter Yes or No")

    if shop_continiue == "No":
         shop = False

for item in cart:
    print(f"{cart}")
for price in prices:
    cost += prices

print (f"{cart, cost}")