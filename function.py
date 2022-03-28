
def sayHello(name):
    nama = f"nama saya {name}"
    return nama

def total(*angkaList):
    total = 0
    for data in angkaList:
        total = total + data
    return total