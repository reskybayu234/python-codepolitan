customer = {"name" : "bayu",
            "age" : 27,
            "address" : "Mataram"}

name = customer["name"]
age = customer["age"]
address = customer["address"]

print(name)
print(age)
print(address)

print("="*100)

for key in customer:
    value = customer[key]
    print(f"{key} : {value}")

print("="*100)

print(customer.items())

print("="*100)

customer["Company"] = "X"

for key, value in customer.items():
    print(f"{key} : {value}")

print("="*100)

del customer["Company"]

for key, value in customer.items():
    print(f"{key} : {value}")