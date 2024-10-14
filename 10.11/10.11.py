product = {
    "name" : "Sunglasses",
    "unit_price" : 99.99,
    "taxable" : True,
    "in_stock" : 10,
    "models" : ["Black", "Green"]
}

print("Name: ", product["name"])
print("Price: ", f"${product["unit_price"]:.2f}")
print("Taxable: ", product["taxable"])
print("In stock: ", product["in_stock"])
print("Models: ")
for model in product["models"]:
    print("\t-" + model)