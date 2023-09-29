import uuid
from random import randint
import random

"""
product_info = {"Product Name": [["Product Price", "Product Details", "Quantity", "Product Category/Section"]
                                  , ["Product Discount", "Price Scale (1 to 5)", "Product Image"]]}

"""

###----- CATEGORIES QUANTITY -----###
accessories_qty_min, accessories_qty_max = 1, 40
games_qty_min, games_qty_max = 1, 25
electronics_qty_min, electronics_qty_max = 1, 15
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

    "Asus Vivobook Go": [["1078.75", 'E1504FA-NJ274W 15.6" FHD Laptop -\n'
                                     'AMD Ryzen5 7520U/16GB/512GB SSD/Win11Home \n'
                                     '- WiFiAC + BT4.1, Webcam, USB-C & HDMI',
                          f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                         ["0", "1", "images/Product_Images/Electronics/asus_vivobook_go.png"]],
    "Asus ROG Zephyrus G14": [["3210.03", 'GA402XV-N2032W RTX 4060 Gaming Laptop 14"\n'
                                          'QHD+ 165Hz AMD Ryzen9 7940HS 16GB 512GB SSD\n'
                                          'Win11Home 1yr warranty - WiFi6E + BT5.2, IR Cam,\n'
                                          'USB-C (with PD & DP), HDMI2.1, MicroSD Reader, Backlit Keyboard',
                               f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                              ["0", "1", "images/Product_Images/Electronics/asus_rog_zephyrus_g14.png"]],
    "Asus TUF F15": [["1872.10", 'TUF507ZC4-HN082W RTX 3050 Gaming Laptop 15.6"\n'
                                 'FHD 144Hz Intel i7-12700H 16GB 512GB SSD\n'
                                 'RTX3050 4GB Graphics Win11Home 1yr warranty -\n'
                                 'WiFi6 + BT5.2, Webcam, Thunderbolt4 (with DP),\n'
                                 'USB-C (with DP), HDMI2.1 TMDS',
                      f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                     ["0", "1", "images/Product_Images/Electronics/asus_tuf_f15.png"]],
    "Asus ROG Zephyrus Duo 16": [["6998.00", 'RTX 4090 Gaming Laptop --16"\n'
                                             'QHD+240Hz/AMD Ryzen9 7945HX/64GB/1TB SSD --\n'
                                             'RTX4090 16GB Graphics . Win11 Home -\n'
                                             'WiFi6E + BT5.2, Webcam, ScreenPad Plus, Per-Key RGB Keyboard',
                                  f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                                 ["0", "1", "images/Product_Images/Electronics/asus_rog_zephyrus_duo_16.png"]],
    "Asus Zenbook Pro 14 Duo": [["3955.00", 'UX8402ZE-M3026X 14" 2.8K Duo Touch OLED --\n'
                                            'Intel i7-12700H/16GB/1TB SSD/RTX3050Ti --\n'
                                            'Win11Pro - WiFi6E + BT5.2, Webcam,\n'
                                            'Type-C (with Power Delivery & DP), with Sleeve, Stand & Stylus',
                                 f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                                ["0", "1", "images/Product_Images/Electronics/asus_zenbook_pro_14_duo.png"]],
    "Apple MacBook Air": [["3178.99", '15" Laptop with M2 Chip - Midnight 16GB Unified Memory -\n'
                                      '512GB SSD - 8-Core CPU - 10-Core GPU - 16-Core Neural Engine -\n'
                                      '15.3 Inch Liquid Retina Display with TrueTone - 35W Dual USB-C Charger',
                           f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                          ["0", "1", "images/Product_Images/Electronics/macbook_air.png"]],
    "Apple MacBook Pro": [["2095.00", '13" Laptop with M2 Chip - Space Grey 8GB RAM -\n'
                                      '256GB SSD - 13" Retina Display - Touch Bar -\n'
                                      'Backlit Keyboard - FaceTime HD Camera - Works with iPhone & iPad',
                           f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                          ["0", "1", "images/Product_Images/Electronics/macbook_pro.png"]],
    "MSI MEG Trident X2 13NUI-\n"
    "008NZ RTX 4090 Gaming PC": [["12498.99", 'Intel Core i9 13900KF 24 Core - 64GB DDR5 - 2TB SSD -\n'
                                              'NVIDIA RTX 4090 24GB - AX WiFi 6 + Bluetooth -\n'
                                              'Windows 11 Home - Keyboard & Mouse Included\n',
                                  f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                                 ["0", "1", "images/Product_Images/Electronics/msi_meg_trident.png"]],
    "GGPC RTX 4070 Ti Gaming PC": [["3699.00", 'Intel Core i7 13700F 16 Core - 32GB RGB RAM -\n'
                                               '1TB NVMe SSD - NVIDIA GeForce RTX4070Ti 12GB Graphics -\n'
                                               'AX WiFi 6 + Bluetooth - Windows 11 Home\n',
                                    f"{randint(electronics_qty_min, electronics_qty_max)}", "Electronics"],
                                   ["0", "1", "images/Product_Images/Electronics/ggpc_rtx_4070ti_gaming_pc.png"]],

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
