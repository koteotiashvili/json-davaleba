import json
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
def costum_encoder(obj):
    if isinstance(obj,Product):
        return {
            'name': obj.name,
            'price': obj.price,
            'quantity': obj.quantity,
        }
    return obj
lst = []
Product1 = Product('Banana', '2$', '1kg' )
Product2 = Product('apple', '1.5$', '0.5kg')
Product3 = Product('orange', '5$', '3kg')

lst.append(Product1)
lst.append(Product2)
lst.append(Product3)

# json_data = json.dumps(lst, default=costum_encoder)
# print(json_data)
with open ('products.json', 'w') as json_file:
    json.dump(lst,json_file,default=costum_encoder, indent=4)