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
    "description": "100 percent cotton, color: blue"
},

{
    "name": "Black T-shirt",
    "price": 12.99,
    "department": "women's shirts"
    "description": "100 percent cotton, color: black"
}
    ]

for index, item in enumerate(item):
        print(index, ":", item["name"])

        item[0]["name"]