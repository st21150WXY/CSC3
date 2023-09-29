import uuid
from random import randint

"""
product_info = {"Product Name": [["Product Price", "Product Details", "Quantity", "Product Category/Section"]
                                  , ["Product Discount", "Price Scale (1 to 5)", "Product Image"]]}

"""

###----- CATEGORIES QUANTITY -----###
food_qty_min, food_qty_max = 1, 50

product_info = {"Apple": [["4.50", "500g of apples", f"{randint(food_qty_min, food_qty_max)}", "Fruit"],
                          ["0", "1", "images/Product_Images/apple.png"]],
                "Pear": [["5.65", "500g of pears", f"{randint(food_qty_min, food_qty_max)}", "Fruit"],
                         ["0", "1", "images/Product_Images/pear.png"]],
                "Banana": [["5.25", "3 bananas", f"{randint(food_qty_min, food_qty_max)}", "Fruit"],
                           ["0", "1", "images/Product_Images/banana.png"]],
                "Strawberry": [["6.39", "Raw Berry", f"{randint(food_qty_min, food_qty_max)}", "Fruit"],
                               ["0", "1", "images/Product_Images/strawberry.png"]],
                "Orange": [["5.89", "Did you know that it is orange in color?", f"{randint(food_qty_min, food_qty_max)}", "Fruit"],
                           ["0", "1", "images/Product_Images/orange.png"]],
                "Peach": [["6.50", "It came from the beach.", f"{randint(food_qty_min, food_qty_max)}", "Food"],
                          ["0", "1", "images/Product_Images/peach.png"]],
                "Nectarine": [["7.00", "Very nice fruit indeed", f"{randint(food_qty_min, food_qty_max)}", "Fruit"],
                              ["0", "1", "images/Product_Images/nectarine.png"]]
                }
#print(product_info)
name_list = list(product_info.keys())
details_list = list(product_info.values())

for UUID in range(len(name_list)):
    random_uuid = uuid.uuid4()
    details_list[UUID][1].append(f"{random_uuid}")

"""a = list(product_info.values())
for i in range(len(a)):
    print(a[i][1][3])"""

#product_widget_global = []
