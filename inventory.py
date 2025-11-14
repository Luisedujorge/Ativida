class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        if qty <= 0 or price <= 0:
            raise ValueError("QUantidade deve ser maior que 0")
        if name in self.items:
            raise ValueError("Item já cadastrado")
        self.items[name] = {"qty": qty, "price": price}

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError("Item não encontrado")
        del self.items[name]

    def update_quantity(self, name, qty):
        if name not in self.items:
            raise KeyError("Item não encontrado")
        if qty < 0:
            raise ValueError("Quantidade não pode ser menor que 0")
        self.items[name]["qty"] = qty

    def get_item(self, name):
        if name not in self.items:
            raise KeyError("Item não encontrado")
        return self.items[name]

    def list_items(self):
        return list(self.items.keys())

    def total_value(self):
        return sum(info["qty"] * info["price"] for info in self.items.values())
