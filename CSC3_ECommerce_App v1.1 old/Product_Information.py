import random
import uuid
from random import randint

"""
product_info = {"Product Name": [["Product Price", "Product Details", "Quantity", "Product Category/Section"]
                                  , ["Product Discount", "Price Scale (1 to 5)", "Product Image"]]}

"""

###----- CATEGORIES QUANTITY -----###
accessories_qty_min, accessories_qty_max = 1, 40
games_qty_min, games_qty_max = 1, 25
food_qty_min, food_qty_max = 1, 50

product_info = {
    "Black Framed Glasses": [["9.30", "Small glasses, good lens.", f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                             ["0", "1", "images/Product_Images/Accessories/glasses1.png"]],
    "White Nike Cap": [["12.50", "High Quality, branded cap.", f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                       ["0", "1", "images/Product_Images/Accessories/white_nike_cap.png"]],
    "Black Cap": [["7.79", "Medium Quality, decent cap.", f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                             ["0", "1", "images/Product_Images/Accessories/black_cap.png"]],
    "Black Fedora": [["43.25", "Premium Quality, black in colour.",
                      f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                     ["0", "1", "images/Product_Images/Accessories/black_fedora.png"]],
    "Black Socks": [["3.00", "Normal pairs of socks.", f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                    ["0", "1", "images/Product_Images/Accessories/black_socks.png"]],
    "Socks Bundle": [["14.75", "Variation in colour, white, gray and black\npairs of socks.",
                      f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                     ["0", "1", "images/Product_Images/Accessories/socks_variety_bundle.png"]],
    "Blue Tie (Stripe Design)": [["19.20", "High quality tie, blue in colour, stripe design.",
                                  f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                                 ["0", "1", "images/Product_Images/Accessories/blue_tie_stripe_design.png"]],
    "Green Tie (Stripe Design)": [["19.20", "High quality tie, green in colour, stripe design.",
                                  f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                                  ["0", "1", "images/Product_Images/Accessories/green_tie_stripe_design.png"]],
    "Red Tie (Stripe Design)": [["19.20", "High quality tie, red in colour, stripe design.",
                                 f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                                ["0", "1", "images/Product_Images/Accessories/red_tie_stripe_design.png"]],
    "Black Purse": [["91.45", "High quality purse, black in colour, small size.",
                     f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                    ["0", "1", "images/Product_Images/Accessories/black_purse.png"]],
    "Gucci Purse (Heart Shaped)": [["825.49", "High quality branded purse, black and gold\nvariation in colour, heart shaped.",
                                    f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                                   ["0", "1", "images/Product_Images/Accessories/gucci_heart_shaped_purse.png"]],
    "G-Shock Watch (White)": [["125.49", "High quality branded watch, white variation.\nYou can look at the time.",
                               f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                              ["0", "1", "images/Product_Images/Accessories/white_G_shock_watch.png"]],
    "G-Shock Watch (Black)": [["125.49", "High quality branded watch, black variation.\nYou can look at the time.",
                               f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                              ["0", "1", "images/Product_Images/Accessories/black_G_shock_watch.png"]],
    "Full Gloves (Black)": [["15.99", "Good quality, black variation.\nYou can wear it on your hands.",
                             f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                            ["0", "1", "images/Product_Images/Accessories/black_full_gloves.png"]],
    "Full Hard Gloves (Black)": [["21.99", "Good quality, black variation.\nYou can wear it on your hands.\n"
                                           "It covers your entire hands.",
                                  f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                                 ["0", "1", "images/Product_Images/Accessories/black_hard_gloves.png"]],
    "Half Hard Gloves (Black)": [["18.19", "Good quality, black variation.\nYou can wear it on your hands.\n"
                                           "It doesn't cover your fingers.",
                                  f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                                 ["0", "1", "images/Product_Images/Accessories/black_hard_gloves.png"]],
    "Premium Gold Necklace": [["2749.99", "Premium quality, 13 carats.\nNice and premium hard gold.\n" 
                                          "Its a necklace, you can wear it on your neck.",
                               f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                              ["0", "1", "images/Product_Images/Accessories/ultra_premium_gold_necklace.png"]],
    "Cocoa Quartz White\n"
    "Mocha Diamond Necklace": [["7199.49", "Premium quality,\nshiny things on you.\n"
                                           "Its a necklace, you can wear it on your neck.",
                                f"{randint(accessories_qty_min, accessories_qty_max)}", "Accessories"],
                               ["0", "1", "images/Product_Images/Accessories/cocoa_quartz_white_mocha_diamond_necklace.png"]],

    "Battleship Board Game": [["29.99", "Strategical board game, 2 players.",
                               f"{randint(games_qty_min, games_qty_max)}", "Games"],
                              ["0", "1", "images/Product_Images/Games/battleship_board_game.png"]],
    "Play Balls": [["1.00", "soft juicy balls for playing, perfect for,\n2 players,\nperfectly smooth balls.",
                    f"{randint(games_qty_min, games_qty_max)}", "Games"],
                   ["0", "1", "images/Product_Images/Games/play_balls.png"]],

    "Apple": [["4.50", "500g of apples", f"{randint(food_qty_min, food_qty_max)}", "Food"],
              ["0", "1", "images/Product_Images/Food/apple.png"]],
    "Pear": [["5.65", "500g of pears", f"{randint(food_qty_min, food_qty_max)}", "Food"],
             ["0", "1", "images/Product_Images/Food/pear.png"]],
    "Banana": [["5.25", "3 bananas", f"{randint(food_qty_min, food_qty_max)}", "Food"],
               ["0", "1", "images/Product_Images/Food/banana.png"]],
    "Strawberry": [["6.39", "Raw Berry", f"{randint(food_qty_min, food_qty_max)}", "Food"],
                   ["0", "1", "images/Product_Images/Food/strawberry.png"]],
    "Orange": [["5.89", "Did you know that it is orange in color?", f"{randint(food_qty_min, food_qty_max)}", "Food"],
               ["0", "1", "images/Product_Images/Food/orange.png"]],
    "Peach": [["6.50", "It came from the beach.", f"{randint(food_qty_min, food_qty_max)}", "Food"],
              ["0", "1", "images/Product_Images/Food/peach.png"]],
    "Nectarine": [["7.00", "Very nice fruit indeed", f"{randint(food_qty_min, food_qty_max)}", "Food"],
                  ["0", "1", "images/Product_Images/Food/nectarine.png"]]
}

convert_dict = list(product_info.items())
random.shuffle(convert_dict)
product_info = dict(convert_dict)
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
