import pytest
from inventory import Inventory

def test_add_item():
    inv = Inventory()
    inv.add_item("Laptop", 3, 2000)
    assert inv.get_item("Laptop") == {"qty": 3, "price": 2000}

def test_add_item_invalid_values():
    inv = Inventory()
    with pytest.raises(ValueError):
        inv.add_item("Mouse", 0, 50)
    with pytest.raises(ValueError):
        inv.add_item("Keyboard", 5, -10)

def test_add_existing_item():
    inv = Inventory()
    inv.add_item("Monitor", 2, 900)
    with pytest.raises(ValueError):
        inv.add_item("Monitor", 1, 800)

def test_remove_item():
    inv = Inventory()
    inv.add_item("Chair", 5, 300)
    inv.remove_item("Chair")
    with pytest.raises(KeyError):
        inv.get_item("Chair")

def test_update_quantity():
    inv = Inventory()
    inv.add_item("Table", 1, 500)
    inv.update_quantity("Table", 10)
    assert inv.get_item("Table")["qty"] == 10

def test_update_quantity_invalid():
    inv = Inventory()
    inv.add_item("Lamp", 2, 150)
    with pytest.raises(ValueError):
        inv.update_quantity("Lamp", -5)

def test_total_value():
    inv = Inventory()
    inv.add_item("ItemA", 2, 100)
    inv.add_item("ItemB", 3, 50)
    assert inv.total_value() == 2 * 100 + 3 * 50

def test_list_items():
    inv = Inventory()
    inv.add_item("Pen", 10, 2)
    inv.add_item("Notebook", 5, 5)
    items = inv.list_items()
    assert "Pen" in items
    assert "Notebook" in items
    assert len(items) == 2
