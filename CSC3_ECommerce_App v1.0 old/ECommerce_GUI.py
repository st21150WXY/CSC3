from tkinter import *
import customtkinter
import random
# from CTkListbox import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import CSC3_ECommerce_App.AccountSystem
from AccountSystem import page
from CSC3_ECommerce_App.Product_Information import product_info

# from CSC3_ECommerce_App.Product_Information import product_widget_global

Category_Names = ["Accessories", "Games", "Electronics", "Food",
                              "Beauty", "Home", "Fashion"]
Cart_Items = []   #Stores values of items that have been added to cart
current_page = 0  #The current page the user is on
Credit = 500   #How much money left is in the users account


class FirstPage:
    def __init__(self, main_window):
        self.main_window = main_window

        # global product_widget_global

        # Window Size and Placement
        main_window.rowconfigure(0, weight=1)
        main_window.columnconfigure(0, weight=1)
        screen_width = main_window.winfo_screenwidth()
        screen_height = main_window.winfo_screenheight()
        screen_height_position = main_window.winfo_height()
        app_width = screen_width
        app_height = screen_height - 72
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height_position / 160) - (app_height / 160)
        main_window.geometry(f"{app_width}x{app_height}+{int(x) - 8}+{int(y)}")

        # window Icon
        icon = PhotoImage(file='images/Amazing-Logo-Brand.png')
        main_window.iconphoto(True, icon)
        main_window.title('Amazing')

        # Navigating through windows
        homepage = Frame(main_window)
        dashboard_page = Frame(main_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        Main_Frame_HP = customtkinter.CTkFrame(homepage, fg_color="#c5c5c5", corner_radius=0)
        Main_Frame_HP.place(relx=0.5, rely=0.55, relwidth=1, relheight=0.9, anchor=CENTER)

        ### ===== Nested Class, Filter GUI (Animated widget) ===== ###

        class SlidePanel(customtkinter.CTkFrame):
            def __init__(self, parent, start_pos, end_pos):
                super().__init__(master=parent)

                # general attributes
                self.start_pos = start_pos
                self.end_pos = end_pos
                self.width = abs(start_pos - end_pos)

                # animation logic
                self.pos = self.start_pos
                self.in_start_pos = True

                # layout
                self._fg_color = "#acacac"
                self.place(relx=self.start_pos - 0.3, rely=0.115, relwidth=self.width, relheight=0.885)

            def animate(self):
                if self.in_start_pos:
                    self.animate_forward()
                else:
                    self.animate_backwards()

            def animate_forward(self):
                if self.pos < self.end_pos:
                    self.pos += 0.008
                    self.place(relx=self.pos, rely=0.115, relwidth=self.width, relheight=0.885)
                    self.after(10, self.animate_forward)
                    Filter_Btn.configure(fg_color="#a8cce8")
                else:
                    self.in_start_pos = False

            def animate_backwards(self):
                if self.pos > self.start_pos:
                    self.pos -= 0.008
                    self.place(relx=self.pos, rely=0.115, relwidth=self.width, relheight=0.885)
                    self.after(10, self.animate_backwards)
                    Filter_Btn.configure(fg_color="#dedede")
                else:
                    self.in_start_pos = True

        class SlidePanel2(customtkinter.CTkFrame):
            def __init__(self, parent, start_pos, end_pos):
                super().__init__(master=parent)

                # general attributes
                self.start_pos = start_pos
                self.end_pos = end_pos
                self.width = abs(start_pos - end_pos)

                # animation logic
                self.pos = self.start_pos
                self.in_start_pos = True

                # layout
                self._fg_color = "#acacac"
                self.place(relx=0, rely=self.start_pos - 0.5, relwidth=self.width, relheight=1)

            def animate(self):
                if self.in_start_pos:
                    self.animate_forward()
                else:
                    self.animate_backwards()

            def animate_forward(self):
                if self.pos < self.end_pos:
                    self.pos += 0.008
                    self.place(relx=0, rely=self.pos, relwidth=self.width, relheight=1)
                    self.after(5, self.animate_forward)
                    Account_Btn.configure(fg_color="#a8cce8")
                else:
                    self.in_start_pos = False

            def animate_backwards(self):
                if self.pos > self.start_pos:
                    self.pos -= 0.008
                    self.place(relx=0, rely=self.pos, relwidth=self.width, relheight=1)
                    self.after(5, self.animate_backwards)
                    Account_Btn.configure(fg_color="#c5c5c5")
                else:
                    self.in_start_pos = True

        def move_btn():
            global button_x
            button_x += 0.001
            Filter_Btn.place(relx=button_x, rely=0.5, anchor='center')

            if button_x < 0.9:
                homepage.after(10, move_btn)

            # configure
            # colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
            # color = choice(colors)
            # button.configure(fg_color = color)

        def infinite_print():
            global button_x
            button_x += 0.5
            if button_x < 10:
                print('infinite')
                print(button_x)
                homepage.after(100, infinite_print)


        def filter(letter):
            product_info_name = list(product_info.keys())
            word = []
            lm = 0
            for each_word in range(len(product_info_name)):
                word.append(product_info_name[each_word])
                for check_letter in list(word)[each_word]:
                    print(check_letter)
                    if check_letter[0] == list(product_info_name[each_word])[0]:
                        lm += 1
                    else:
                        break
                #break
            print(f"{lm} are matching '{letter}'")

        animated_panel = SlidePanel(homepage, -0.3, 0)
        animated_panel.configure(bg_color="#acacac", corner_radius=0, border_width=2, border_color="#000")
        customtkinter.CTkLabel(animated_panel, text='Filter by A - Z', font=("Century Gothic", 20, "bold"),
                               text_color="#4a4a4a").place(relx=0.33, rely=0.0125)
        filter_panel_cb = customtkinter.CTkComboBox(animated_panel, font=("Century Gothic", 20, "bold"),
                                                    text_color="#a3a3a3", state="readonly",
                                                    values=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                                                            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                                                            "W", "X", "Y", "Z"])
        filter_panel_cb.place(relx=0.325, rely=0.09)
        (customtkinter.CTkButton(animated_panel, text='Apply', font=("Century Gothic", 18, "bold"), width=80, cursor="hand2",
                                 command=lambda: filter(filter_panel_cb.get()))
         .place(relx=0.4, rely=0.16))
        (customtkinter.CTkCanvas(animated_panel, width=430, height=1.5, bg="#181818", highlightthickness=0)
         .place(relx=0, rely=0.225))
        customtkinter.CTkLabel(animated_panel, text='Filter by Category', font=("Century Gothic", 20, "bold"),
                               text_color="#4a4a4a").place(relx=0.3, rely=0.23)

        filter_panel_checkbox = customtkinter.CTkCheckBox(animated_panel, text='Category', font=("Century Gothic", 18, "bold"),
                                                          cursor="hand2", command=lambda: print(filter_panel_checkbox.get()))
        filter_panel_checkbox.place(relx=0.36, rely=0.3)
        # customtkinter.CTkLabel(animated_panel, text='Label 2').pack(expand=True, fill='both', padx=2, pady=10)
        # customtkinter.CTkButton(animated_panel, text='Button', corner_radius=0).pack(expand=True, fill='both', pady=10)
        # customtkinter.CTkTextbox(animated_panel, fg_color=('#dbdbdb', '#2b2b2b')).pack(expand=True, fill='both', pady=10)

        # testing button
        button_x = 0.5
        # button = customtkinter.CTkButton(homepage, text='toggle sidebar', command=animated_panel.animate)
        # button.place(relx=button_x, rely=0.5, anchor='center')

        animated_panel2 = SlidePanel2(homepage, -1, 0)
        animated_panel2.configure(bg_color="#acacac", corner_radius=0, border_width=1, border_color="#c5c5c5")
        def logout():
            win = Toplevel()
            CSC3_ECommerce_App.AccountSystem.AccountPage(win)
            main_window.withdraw()
            win.deiconify()
        # ========== LOG OUT ========== #
        logout_button = customtkinter.CTkButton(animated_panel2, text='Logout', font=("Century Gothic", 18, "bold"),
                                                cursor='hand2', command=logout)
        logout_button.place(relx=0.45, rely=0.8)

        # --- Display Credit --- #
        display_credit = customtkinter.CTkLabel(animated_panel2, text=f"Credit: ${Credit:,}", font=("Century Gothic", 25, "bold"),
                                                text_color="#313131")
        display_credit.place(relx=0.125, rely=0.15)


        # ======================================================================================#

        show_frame(homepage)

        ## TESTING FRAMES ##
        # f = customtkinter.CTkFrame(homepage, width=100, height=50)
        # f.grid(row=0, column=0, padx=500, pady=500)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#ffffff')

        def clear_frame(selected_frame):
            for widgets in selected_frame.winfo_children():
                widgets.destroy()

        var_name = ["indicator_c1", "indicator_c2", "indicator_c3", "indicator_c4",
                    "indicator_c5", "indicator_c6", "indicator_c7"]

        ### ===== PRODUCT DETAILS PAGE ===== ###
        def product_details_page(product_title, product_price, product_image, product_description, product_uuid, qty, cframe):
            hide_indicate()
            try:
                clear_frame(home_frame)
            except:
                clear_frame(cframe)
            pd_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)
            #print(f"{product_title}, {product_price}, {product_image}, {product_description}")

            def separators(relative_x, relative_y):
                pd_separator = customtkinter.CTkCanvas(pd_frame, height=3, bg="#a5a5a5", highlightthickness=0)
                pd_separator.place(relx=relative_x, rely=relative_y, relwidth=0.33, anchor=CENTER)

            #####___SECTION 1___#####
            pd_front_frame = customtkinter.CTkFrame(pd_frame, width=1435, height=725, fg_color="#c5c5c5")
            pd_front_frame.grid(row=0, column=0)

            pd_image_frame = customtkinter.CTkFrame(pd_frame, width=500, height=500, fg_color="#a3a3a3")
            pd_image_frame.place(relx=0.08, rely=0.125)

            pd_image = Image.open(f'{product_image}')
            pd_image_widget = customtkinter.CTkImage(pd_image, size=(500, 500))
            pd_image_display = customtkinter.CTkLabel(pd_image_frame, image=pd_image_widget, text="",
                                                      width=500, height=500, corner_radius=1)
            pd_image_display.image = pd_image_widget
            pd_image_display.place(relx=0.5, rely=0.5, anchor=CENTER)

            pd_title = customtkinter.CTkLabel(pd_frame, text=product_title, font=("Century Gothic", 25, "bold"),
                                              text_color="#313131")
            pd_title.place(relx=0.615, rely=0.125, anchor=CENTER)

            separators(0.615, 0.15)

            #####___SECTION 2___#####
            pd_price = customtkinter.CTkLabel(pd_frame, text=f"${product_price}", font=("Century Gothic", 22, "bold"),
                                              text_color="#313131")
            pd_price.place(relx=0.525, rely=0.2, anchor=CENTER)

            pd_stocks = customtkinter.CTkLabel(pd_frame, text=f"Stock: {qty}", font=("Century Gothic", 22, "bold"),
                                              text_color="#313131")
            pd_stocks.place(relx=0.615, rely=0.275, anchor=CENTER)

            def qty_check():
                check_amount = pd_qty_amount.get()
                if not check_amount:
                    add_to_cart(product_title, product_price,
                                product_uuid, 1)
                elif check_amount > qty:
                    pd_qty_amount.delete(0, "end")
                elif check_amount <= qty:
                    add_to_cart(product_title, product_price,
                                product_uuid, check_amount)
                else:
                    pd_qty_amount.delete(0, "end")

            pd_qty_amount = customtkinter.CTkEntry(pd_frame, placeholder_text="Qty.",
                                                   font=("Century Gothic", 17, "bold"), width=50)
            pd_qty_amount.place(relx=0.75, rely=0.275, anchor=CENTER)

            separators(0.615, 0.3)

            #####___SECTION 3___#####
            pd_description = customtkinter.CTkLabel(pd_frame, text="------------[ Description ]------------",
                                                    font=("Century Gothic", 21, "bold"),
                                                    text_color="#313131")
            pd_description.place(relx=0.615, rely=0.325, anchor=CENTER)

            pd_description = customtkinter.CTkLabel(pd_frame, text=f"{product_description}", font=("Century Gothic", 16, "bold"),
                                               text_color="#313131")
            pd_description.place(relx=0.615, rely=0.55, anchor=CENTER)

            separators(0.615, 0.79)

            ## --- Product Add to Cart Button --- ##
            ATC_btn = customtkinter.CTkButton(pd_frame, width=50, height=25,
                                                      font=("Century Gothic", 20, "bold"), fg_color="#949494",
                                                      bg_color="#c5c5c5", border_color="#7b7b7b", border_width=2,
                                                      hover_color="#949494", text_color="#4a4a4a", text="Add to Cart",
                                                      command=lambda: qty_check())
            ATC_btn.place(relx=0.615, rely=0.83, anchor=CENTER)

            def OnHoverBtn(button, fgcolorOnHover, fgcolorNotHover, bdcolorOnHover, bdcolorNotHover):
                button.bind("<Enter>", command=lambda e: button.configure(fg_color=fgcolorOnHover))
                button.bind("<Enter>", command=lambda e: button.configure(border_color=bdcolorOnHover))

                button.bind("<Leave>", command=lambda e: button.configure(fg_color=fgcolorNotHover))
                button.bind("<Leave>", command=lambda e: button.configure(border_color=bdcolorNotHover))

            OnHoverBtn(ATC_btn, "#ffd3a4", "#949494",
                       "#ff931c", "#7b7b7b")

            #Back Button
            back_btn = customtkinter.CTkButton(pd_frame, width=40, height=20,
                                              font=("Century Gothic", 18, "bold"), fg_color="#949494",
                                              bg_color="#c5c5c5", border_color="#7b7b7b", border_width=2,
                                              hover_color="#949494", text_color="#4a4a4a", text="Back",
                                              command=lambda: home_page(0))
            back_btn.place(relx=0.102, rely=0.09, anchor=CENTER)
            OnHoverBtn(back_btn, "#a8cce8", "#949494",
                       "#158aff", "#7b7b7b")

            #Side frame for shipping details
            pd_frame2 = customtkinter.CTkFrame(pd_frame, width=225, height=625, fg_color="#a3a3a3")
            pd_frame2.place(relx=0.8, rely=0.09)

            text_event = random.randint(1, 4)
            extra_text = "Product is available and\nis ready to be shipped\ntomorrow." if text_event == 1 else \
                "Product is available and\nis ready to be shipped\ntoday." if text_event == 2 else \
                "Product is unavailable,\nout of stock currently." if text_event == 3 else \
                "Product is available\nfor pre-order."

            pd_f2_text = customtkinter.CTkLabel(pd_frame2, text=f"{extra_text}", font=("Century Gothic", 18, "bold"),
                                              text_color="#313131")
            pd_f2_text.place(relx=0.5, rely=0.2, anchor=CENTER)

            pd_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)


        ### ===== DEFINE FUNCTIONS FOR PAGES ===== ###
        def home_page(current_page):
            global product_frame_list, product_info_widgets, current_rows, current_columns, add_to_cart_btn, home_frame, \
                num_of_frame_column, current_value_row, page_, pi_information_

            hide_indicate()
            animated_panel2.animate_backwards()
            home_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            max_frame_per_page = 25
            max_num_of_column = 5  # Maximum number of frames in one row (This is a constant value)
            num_of_frame_column = 25  # Number of Lists in the main list (This value can be changed)

            ##---Main Variables---##
            current_rows = 0  # The current number of rows (set to 0 because it is suppose to start at no frames)

            # Note: the number of items in current_columns as an array counts as rows as well
            current_columns = []  # The current number of columns respective to the num_of_frame_column
            ##--------------------##

            current_value_row = 0
            page_ = 0  #The current page the programme is creating frames for


            def load_page(num_of_frame_column, current_rows, page_, current_value_row):
                global product_info_widgets
                # This is also a main variable as it is used to store columns and rows of the number of frames
                # The nested list is the rows and the values inside the nested list are columns
                product_frame_list = []
                pi_information_ = []  # Stores each individual product_info in a triple multiple-dimensional list


                #Foundation of creating pages
                for c in range(num_of_frame_column):  # Runs the value of 'num_of_frame_column' of times
                    if len(current_columns) == 0:
                        current_columns.append([])
                        pi_information_.append([])
                        #print("Created New Page")
                    # Checks if the current_columns is creating its first page

                    '''If |num_of_frame_column| is greater than |max_num_of_column| then append the value of 
                    |max_num_of_column| and minus the |num_of_frame_column| by the |max_num_of_column|'''
                    if num_of_frame_column > max_num_of_column:
                        current_columns[page_].append(max_num_of_column)
                        for add_frames in range(max_num_of_column):
                            pi_information_[page_].append([])
                        num_of_frame_column -= max_num_of_column
                        current_rows += 1  # Add 1 more row to current_rows

                    # If num_of_frame_column less than 5 then it will append the current value of num_of_frame_column
                    elif num_of_frame_column < max_num_of_column:
                        current_columns[page_].append(num_of_frame_column)
                        for add_frames in range(num_of_frame_column):
                            pi_information_[page_].append([])
                        current_rows += 1
                        break  # This breaks out of the loop
                    else:
                        current_columns[page_].append(max_num_of_column)
                        for add_frames in range(max_num_of_column):
                            pi_information_[page_].append([])
                        current_rows += 1
                        break

                    #Adds a new list(page) when
                    if sum(current_columns[page_]) >= max_frame_per_page:
                        current_columns.append([])  # New Page
                        pi_information_.append([])
                        page_ += 1
                        #print("Added a page")

                #print(current_rows)
                #print(current_columns)
                #print(pi_information_)
                row_n_column = []

                clear_frame(home_frame)

                #Calculates the total number of frames since the num_of_frame_column(var) has been used to calculate -
                #number of frames per page
                total_display_frames = 0
                for cal in range(len(current_columns)):
                    total_display_frames += sum(current_columns[cal])

                '''Since current_columns is counted as a row when obtaining the length of this list, 
                it is used to loop the for loop below'''
                for product_rows in range(len(current_columns[current_page])):
                    product_frame_list.append([])
                    # product_widget_global.append([])

                    for product_columns in range(current_columns[current_page][product_rows]):
                        product_frame = customtkinter.CTkFrame(home_frame, width=240, height=300, fg_color="#949494",
                                                               corner_radius=3)
                        product_frame.grid(row=0 + product_rows, column=0 + product_columns, sticky="W", padx=23, pady=23)
                        product_frame_list[current_value_row].append(product_frame)
                        # product_widget_global[current_value_row].append(product_frame)

                        row_of_frame = product_frame_list[product_rows][product_columns].grid_info()["row"]
                        column_of_frame = product_frame_list[product_rows][product_columns].grid_info()["column"]
                        row_n_column.append([row_of_frame, column_of_frame])

                    current_value_row += 1

                    # This if statement limits the number of frames per row. (5rows x 5columns = 25 frames total)
                    if (current_page >= 0 and (total_display_frames > max_frame_per_page)
                            and (sum(current_columns[current_page]) == max_frame_per_page)):
                        next_page_btn = customtkinter.CTkButton(home_frame, text='>', font=("Century Gothic", 22, "bold"),
                                                                cursor="hand2", width=35, height=15,
                                                                command=lambda: home_page(current_page+1),
                                                                fg_color="#c5c5c5", hover_color="#a8cce8",
                                                                text_color="#313131")
                        next_page_btn.grid(row=6, column=3, sticky="S", pady=40)

                    px = 0
                    if current_page > 0:
                        if len(current_columns[current_page]) < max_num_of_column:
                            px = 120
                        back_page_btn = customtkinter.CTkButton(home_frame, text='<',
                                                                font=("Century Gothic", 22, "bold"),
                                                                cursor="hand2", width=35, height=15,
                                                                command=lambda: home_page(current_page-1),
                                                                fg_color="#c5c5c5", hover_color="#a8cce8",
                                                                text_color="#313131")
                        back_page_btn.grid(row=6, column=1, sticky="S", pady=40, padx=px)

                    indicator_pages = customtkinter.CTkLabel(home_frame,
                                                             text=f'{current_page + 1}/{len(current_columns)}',
                                                             font=("Century Gothic", 22, "bold"),
                                                             text_color="#313131")
                    indicator_pages.grid(row=6, column=2, sticky="S", pady=40, padx=px)

                #print(current_page)
                #print(row_n_column)

                # Same as product_info accept similar to creating the frame, this list stores widgets
                product_info_widgets = {}

                product_info_name = list(product_info.keys())
                product_info_details = list(product_info.values())

                pg = 0

                """The True and False boolean values are used to check if the system has already appended the
                information to the list"""
                # Creating a multidimensional list to store other list that are represented as individual frames
                try:
                    for i in range(sum(current_columns[pg])):
                        if i < len(product_info_name):
                                pi_information_[pg][i].append(product_info_name[i])
                                pi_information_[pg][i].append(product_info_details[i])
                        elif len(pi_information_[pg]) >= max_frame_per_page:
                            pg += 1
                        else:
                            break
                except: pass

                increment_value = 1   #Keeps track of how many frames have been created for this instance
                change_config_row = 0   #Configures the index of 'rows' for display frames
                change_parent_frame = 0   #Configures the parent frame inside the list with corresponding parent frames
                #print(pi_information_)
                for create_lbl in range(len(pi_information_[current_page])):  #original: len(product_info_name)
                    ## --- Product Image --- ##
                    # Original list used for display: product_info_details[create_lbl][1][2]
                    try:
                        product_image = Image.open(f'{pi_information_[current_page][create_lbl][1][1][2]}')
                        product_image_widget = customtkinter.CTkImage(product_image, size=(240, 205))
                        product_image_display = customtkinter.CTkButton(product_frame_list[change_config_row][change_parent_frame],
                                                                        image=product_image_widget, text="",
                                                                        width=200, height=100, corner_radius=1,
                                                                        hover_color="#a8cce8", fg_color="#949494",
                                                                        cursor="hand2",
                                                                        command=lambda
                                                                            title=pi_information_[current_page][create_lbl][0],
                                                                            price=pi_information_[current_page][create_lbl][1][0][0],
                                                                            image=pi_information_[current_page][create_lbl][1][1][2],
                                                                            description=pi_information_[current_page][create_lbl][1][0][1],
                                                                            uuid=pi_information_[current_page][create_lbl][1][1][3],
                                                                            stocks=pi_information_[current_page][create_lbl][1][0][2]:
                                                                        product_details_page(title, price, image,
                                                                                             description, uuid, stocks, home_frame))
                        product_image_display.image = product_image_widget
                        product_image_display.place(relx=0.5, rely=0.31, anchor=CENTER)

                        ## --- Product Title/Name --- ##
                        # Original list used for display: product_info_name[create_lbl]
                        product_title = customtkinter.CTkLabel(product_frame_list[change_config_row][change_parent_frame],
                                                               text=pi_information_[current_page][create_lbl][0], font=("Bold", 17))
                        product_title.place(relx=0.5, rely=0.875, anchor=CENTER)

                        ## --- Product Price --- ##
                        # Original list used for display: product_info_details[create_lbl][0][0]
                        price_lbl = customtkinter.CTkLabel(product_frame_list[change_config_row][change_parent_frame],
                                                           text=f"${pi_information_[current_page][create_lbl][1][0][0]}",
                                                           font=("Bold", 17))
                        price_lbl.place(relx=0.25, rely=0.75, anchor=CENTER)

                        ## --- Product Add to Cart Button --- ##
                        add_to_cart_btn = customtkinter.CTkButton(product_frame_list[change_config_row][change_parent_frame], width=30, height=15,
                                                                  font=("Century Gothic", 14, "bold"), fg_color="#949494",
                                                                  bg_color="#949494", border_color="#7b7b7b", border_width=2,
                                                                  hover_color="#949494", text_color="#4a4a4a",
                                                                  text="Add to Cart",
                                                                  command=lambda name=product_title.cget('text'),
                                                                                 pi_index=create_lbl:
                                                                  add_to_cart(name, product_info_details[pi_index][0][0],
                                                                              product_info_details[pi_index][1][3], 1))
                        add_to_cart_btn.place(relx=0.775, rely=0.75, anchor=CENTER)

                        ## --- Store all 4 widgets to a dictionary --- ##
                        product_info_widgets[f"product_frame{create_lbl + 1}"] = [pi_information_[current_page][create_lbl][1][1][2],
                                                                                  product_title,
                                                                                  price_lbl,
                                                                                  add_to_cart_btn,
                                                                                  "",
                                                                                  product_info_details[create_lbl][0][1],
                                                                                  product_info_details[create_lbl][1][3],
                                                                                  pi_information_[current_page][create_lbl][1][0][2]]

                        change_parent_frame += 1
                        increment_value += 1

                        if increment_value > max_num_of_column:
                            change_config_row += 1
                            change_parent_frame = 0
                            increment_value = 1
                    except: pass

                # - Add to Cart Indicators -#
                def OnHoverATC(button, fgcolorOnHover, fgcolorNotHover, bdcolorOnHover, bdcolorNotHover):
                    button.bind("<Enter>", command=lambda e: button.configure(fg_color=fgcolorOnHover))
                    button.bind("<Enter>", command=lambda e: button.configure(border_color=bdcolorOnHover))

                    button.bind("<Leave>", command=lambda e: button.configure(fg_color=fgcolorNotHover))
                    button.bind("<Leave>", command=lambda e: button.configure(border_color=bdcolorNotHover))

                productw_atc = list(product_info_widgets.values())

                for pw_atc in range(len(productw_atc)):
                    OnHoverATC(productw_atc[pw_atc][3], "#ffd3a4", "#949494",
                               "#ff931c", "#7b7b7b")

                # lbl = customtkinter.CTkLabel(product_frame_list[3][1], text="This is Text", font=("Bold", 20))
                # lbl.place(relx=0.315, rely=0.33)

                home_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

            load_page(num_of_frame_column, current_rows, page_, current_value_row)

        def search_page():
            hide_indicate()
            clear_frame(home_frame)
            search_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            max_frame_per_page = 25
            max_num_of_column = 5  # Maximum number of frames in one row (This is a constant value)
            num_of_frame_column = len(product_info)  # Number of Lists in the main list (This value can be changed)

            ##---Main Variables---##
            current_rows = 0  # The current number of rows (set to 0 because it is suppose to start at no frames)

            # Note: the number of items in current_columns as an array counts as rows as well
            current_columns = []  # The current number of columns respective to the num_of_frame_column
            ##--------------------##

            current_value_row = 0

            # This is also a main variable as it is used to store columns and rows of the number of frames
            # The nested list is the rows and the values inside the nested list are columns
            product_frame_list = []

            for c in range(num_of_frame_column):  # Runs the value of 'num_of_frame_column' of times
                '''If |num_of_frame_column| is greater than |max_num_of_column| then append the value of 
                |max_num_of_column| and minus the |num_of_frame_column| by the |max_num_of_column|'''
                if num_of_frame_column > max_num_of_column:
                    current_columns.append(max_num_of_column)
                    num_of_frame_column -= max_num_of_column
                    current_rows += 1  # Add 1 more row to current_rows

                # If num_of_frame_column less than 5 then it will append the current value of num_of_frame_column
                elif num_of_frame_column < max_num_of_column:
                    current_columns.append(num_of_frame_column)
                    current_rows += 1
                    break  # This breaks out of the loop
                else:
                    current_columns.append(max_num_of_column)
                    current_rows += 1
                    break

            # print(current_rows)
            row_n_column = []

            clear_frame(search_frame)

            '''Since current_columns is counted as a row when obtaining the length of this list, 
            it is used to loop the for loop below'''
            for product_rows in range(len(current_columns)):
                product_frame_list.append([])
                # product_widget_global.append([])

                for product_columns in range(current_columns[product_rows]):
                    product_frame = customtkinter.CTkFrame(search_frame, width=240, height=300, fg_color="#949494",
                                                           corner_radius=3)
                    product_frame.grid(row=0 + product_rows, column=0 + product_columns, sticky="W", padx=23, pady=23)
                    product_frame_list[current_value_row].append(product_frame)

                    row_of_frame = product_frame_list[product_rows][product_columns].grid_info()["row"]
                    column_of_frame = product_frame_list[product_rows][product_columns].grid_info()["column"]
                    row_n_column.append([row_of_frame, column_of_frame])

                current_value_row += 1

            #product_info_name = list(converted_matching_dict.keys())
            product_info_details = list(converted_matching_dict.values())
            pi_details2 = list(product_info.values())

            ##--- Sorting matched values with UUID ---##
            before_sort_lst = list(matching_dict.values())
            after_sort_lst = []
            for arrange in range(len(before_sort_lst)):
                after_sort_lst.append([pi_details2[arrange][1][3], before_sort_lst[arrange]])

            sort_matching_uuid_dict = sorted(dict(after_sort_lst).items(), key=lambda m: m[1], reverse=True)
            converted_uuid_dict = list(dict(sort_matching_uuid_dict))

            increment_value = 1  # Keeps track of how many frames have been created for this instance
            change_config_row = 0  # Configures the index of 'rows' for display frames
            change_parent_frame = 0

            ###--- Creating Product Display Frames ---###
            # A new list is made to replace the var=productw_atc as the widget config stored within the list -
            # is no longer valid out its parent function
            new_product_widgets = []
            for create_lbl in range(len(pi_details2)):
                try:
                    separate_sign = product_info_details[create_lbl][2].cget('text').split('$')
                    price_ = separate_sign[1]

                    product_image = Image.open(f'{product_info_details[create_lbl][0]}')
                    product_image_widget = customtkinter.CTkImage(product_image, size=(240, 205))
                    product_image_display = customtkinter.CTkButton(
                        product_frame_list[change_config_row][change_parent_frame],
                        image=product_image_widget, text="",
                        width=200, height=100, corner_radius=1,
                        hover_color="#a8cce8", fg_color="#949494",
                        cursor="hand2",
                        command=lambda
                            title=product_info_details[create_lbl][1].cget('text'),
                            price=price_,
                            image=product_info_details[create_lbl][0],
                            description=product_info_details[create_lbl][5],
                            uuid=product_info_details[create_lbl][6],
                            stocks=product_info_details[create_lbl][7]:
                        product_details_page(title, price, image,
                                             description, uuid, stocks, search_frame))
                    product_image_display.image = product_image_widget
                    product_image_display.place(relx=0.5, rely=0.31, anchor=CENTER)

                    ## --- Product Title/Name --- ##
                    # Original list used for display: product_info_name[create_lbl]
                    product_title = customtkinter.CTkLabel(
                        product_frame_list[change_config_row][change_parent_frame],
                        text=product_info_details[create_lbl][1].cget('text'), font=("Bold", 17))
                    product_title.place(relx=0.5, rely=0.875, anchor=CENTER)

                    ## --- Product Price --- ##
                    # Original list used for display: product_info_details[create_lbl][0][0]
                    price_lbl = customtkinter.CTkLabel(product_frame_list[change_config_row][change_parent_frame],
                                                       text=f"${price_}",
                                                       font=("Bold", 17))
                    price_lbl.place(relx=0.25, rely=0.75, anchor=CENTER)

                    ## --- Product Add to Cart Button --- ##
                    add_to_cart_btn = customtkinter.CTkButton(
                        product_frame_list[change_config_row][change_parent_frame], width=30, height=15,
                        font=("Century Gothic", 14, "bold"), fg_color="#949494",
                        bg_color="#949494", border_color="#7b7b7b", border_width=2,
                        hover_color="#949494", text_color="#4a4a4a",
                        text="Add to Cart",
                        command=lambda name=product_title.cget('text'),
                                       pi_index=create_lbl:
                        add_to_cart(name, price_, converted_uuid_dict[pi_index], 1))
                    add_to_cart_btn.place(relx=0.775, rely=0.75, anchor=CENTER)

                    change_parent_frame += 1
                    increment_value += 1

                    if increment_value > max_num_of_column:
                        change_config_row += 1
                        change_parent_frame = 0
                        increment_value = 1
                except:
                    pass
                """try:
                    ## --- Product Image --- ##
                    product_image = Image.open(f'{pi_details2[create_lbl][1][2]}')
                    product_image_widget = customtkinter.CTkImage(product_image, size=(240, 205))
                    product_image_display = customtkinter.CTkLabel(product_frame_list[0][create_lbl],
                                                                   image=product_image_widget, text="",
                                                                   width=200, height=100, corner_radius=1)
                    product_image_display.place(relx=0.5, rely=0.31, anchor=CENTER)

                    ## --- Product Title/Name --- ##
                    product_title = customtkinter.CTkLabel(product_frame_list[0][create_lbl],
                                                           text=product_info_details[create_lbl][1].cget('text'), font=("Bold", 17))
                    product_title.place(relx=0.5, rely=0.875, anchor=CENTER)

                    separate_sign = product_info_details[create_lbl][2].cget('text').split('$')
                    price_ = separate_sign[1]
                    ## --- Product Price --- ##
                    price_lbl = customtkinter.CTkLabel(product_frame_list[0][create_lbl],
                                                       text=f"${price_}",
                                                       font=("Bold", 17))
                    price_lbl.place(relx=0.25, rely=0.75, anchor=CENTER)

                    ## --- Product Add to Cart Button --- ##
                    add_to_cart_btn = customtkinter.CTkButton(product_frame_list[0][create_lbl], width=30, height=15,
                                                              font=("Century Gothic", 14, "bold"), fg_color="#949494",
                                                              bg_color="#949494", border_color="#7b7b7b", border_width=2,
                                                              hover_color="#949494", text_color="#4a4a4a",
                                                              text="Add to Cart",
                                                              command=lambda name=product_title.cget('text'),
                                                                             pi_index=create_lbl:
                                                              add_to_cart(name, price_,
                                                                          converted_uuid_dict[pi_index], 1))
                    add_to_cart_btn.place(relx=0.775, rely=0.75, anchor=CENTER)

                    new_product_widgets.append([product_image_display, product_title, price_lbl, add_to_cart_btn])
                except: pass"""

            # - Add to Cart Indicators -#
            def OnHoverATC2(button, fgcolorOnHover, fgcolorNotHover, bdcolorOnHover, bdcolorNotHover):
                button.bind("<Enter>", command=lambda e: button.configure(fg_color=fgcolorOnHover))
                button.bind("<Enter>", command=lambda e: button.configure(border_color=bdcolorOnHover))

                button.bind("<Leave>", command=lambda e: button.configure(fg_color=fgcolorNotHover))
                button.bind("<Leave>", command=lambda e: button.configure(border_color=bdcolorNotHover))

            for pw_atc in range(len(new_product_widgets)):
                OnHoverATC2(new_product_widgets[pw_atc][3], "#ffd3a4", "#949494",
                           "#ff931c", "#7b7b7b")

            # lbl = customtkinter.CTkLabel(product_frame_list[3][1], text="This is Text", font=("Bold", 20))
            # lbl.place(relx=0.315, rely=0.33)

            search_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)
        #####===============================================================================######

        ################## Work on this Tomorrow #####################
        def category_df(category, cframe):
            max_frame_per_page = 25
            max_num_of_column = 5  # Maximum number of frames in one row (This is a constant value)

            product_info_details = list(product_info.values())
            how_many_frames = 0
            for check_c in range(len(product_info)):
                if product_info_details[check_c][0][3] == category:
                    how_many_frames += 1
            num_of_frame_column = how_many_frames  # Number of Lists in the main list (This value can be changed)

            ##---Main Variables---##
            current_rows = 0  # The current number of rows (set to 0 because it is suppose to start at no frames)

            # Note: the number of items in current_columns as an array counts as rows as well
            current_columns = []  # The current number of columns respective to the num_of_frame_column
            ##--------------------##

            current_value_row = 0
            page_ = 0  # The current page the programme is creating frames for

            def load_page(num_of_frame_column, current_rows, page_, current_value_row):
                global product_info_widgets
                # This is also a main variable as it is used to store columns and rows of the number of frames
                # The nested list is the rows and the values inside the nested list are columns
                product_frame_list = []
                pi_information_ = []  # Stores each individual product_info in a triple multiple-dimensional list

                # Foundation of creating pages
                for c in range(num_of_frame_column):  # Runs the value of 'num_of_frame_column' of times
                    if len(current_columns) == 0:
                        current_columns.append([])
                        pi_information_.append([])
                        # print("Created New Page")
                    # Checks if the current_columns is creating its first page

                    '''If |num_of_frame_column| is greater than |max_num_of_column| then append the value of 
                    |max_num_of_column| and minus the |num_of_frame_column| by the |max_num_of_column|'''
                    if num_of_frame_column > max_num_of_column:
                        current_columns[page_].append(max_num_of_column)
                        for add_frames in range(max_num_of_column):
                            pi_information_[page_].append([])
                        num_of_frame_column -= max_num_of_column
                        current_rows += 1  # Add 1 more row to current_rows

                    # If num_of_frame_column less than 5 then it will append the current value of num_of_frame_column
                    elif num_of_frame_column < max_num_of_column:
                        current_columns[page_].append(num_of_frame_column)
                        for add_frames in range(num_of_frame_column):
                            pi_information_[page_].append([])
                        current_rows += 1
                        break  # This breaks out of the loop
                    else:
                        current_columns[page_].append(max_num_of_column)
                        for add_frames in range(max_num_of_column):
                            pi_information_[page_].append([])
                        current_rows += 1
                        break

                    # Adds a new list(page) when
                    if sum(current_columns[page_]) >= max_frame_per_page:
                        current_columns.append([])  # New Page
                        pi_information_.append([])
                        page_ += 1

                row_n_column = []

                # Calculates the total number of frames since the num_of_frame_column(var) has been used to calculate -
                # number of frames per page
                total_display_frames = 0
                for cal in range(len(current_columns)):
                    total_display_frames += sum(current_columns[cal])

                '''Since current_columns is counted as a row when obtaining the length of this list, 
                it is used to loop the for loop below'''
                try:
                    for product_rows in range(len(current_columns[current_page])):
                        product_frame_list.append([])

                        for product_columns in range(current_columns[current_page][product_rows]):
                            product_frame2 = customtkinter.CTkFrame(cframe, width=240, height=300, fg_color="#949494",
                                                                   corner_radius=3)
                            product_frame2.grid(row=0 + product_rows, column=0 + product_columns, sticky="W", padx=23,
                                               pady=23)
                            product_frame_list[current_value_row].append(product_frame2)
                            # product_widget_global[current_value_row].append(product_frame)

                            row_of_frame = product_frame_list[product_rows][product_columns].grid_info()["row"]
                            column_of_frame = product_frame_list[product_rows][product_columns].grid_info()["column"]
                            row_n_column.append([row_of_frame, column_of_frame])

                        current_value_row += 1

                        #if product_info_details[product_rows][0][3] == category:
                            #product_frame_list[product_rows][product_rows].destroy()

                        # This if statement limits the number of frames per row. (5rows x 5columns = 25 frames total)
                        if (current_page >= 0 and (total_display_frames > max_frame_per_page)
                                and (sum(current_columns[current_page]) == max_frame_per_page)):
                            next_page_btn = customtkinter.CTkButton(cframe, text='>',
                                                                    font=("Century Gothic", 22, "bold"),
                                                                    cursor="hand2", width=35, height=15,
                                                                    command=lambda: home_page(current_page + 1),
                                                                    fg_color="#c5c5c5", hover_color="#a8cce8",
                                                                    text_color="#313131")
                            next_page_btn.grid(row=6, column=3, sticky="S", pady=40)

                        px = 0
                        if current_page > 0:
                            if len(current_columns[current_page]) < max_num_of_column:
                                px = 120
                            back_page_btn = customtkinter.CTkButton(cframe, text='<',
                                                                    font=("Century Gothic", 22, "bold"),
                                                                    cursor="hand2", width=35, height=15,
                                                                    command=lambda: home_page(current_page - 1),
                                                                    fg_color="#c5c5c5", hover_color="#a8cce8",
                                                                    text_color="#313131")
                            back_page_btn.grid(row=6, column=1, sticky="S", pady=40, padx=px)

                        indicator_pages = customtkinter.CTkLabel(cframe,
                                                                 text=f'{current_page + 1}/{len(current_columns)}',
                                                                 font=("Century Gothic", 22, "bold"),
                                                                 text_color="#313131")
                        indicator_pages.grid(row=6, column=2, sticky="S", pady=40, padx=px)
                except: pass

                # Same as product_info accept similar to creating the frame, this list stores widgets
                product_info_widgets = {}

                product_info_name = list(product_info.keys())
                #product_info_details = list(product_info.values())

                pg = 0

                new_pi = []
                for add_to_new in range(len(current_columns)):
                    new_pi.append([])
                    for check_c in range(len(product_info)):
                        if product_info_details[check_c][0][3] == category:
                            new_pi[add_to_new].append([product_info_name[check_c], product_info_details[check_c]])

                """The True and False boolean values are used to check if the system has already appended the
                information to the list"""
                # Creating a multidimensional list to store other list that are represented as individual frames
                try:
                    for i in range(sum(current_columns[pg])):
                        if i < len(product_info_name):
                            pi_information_[pg][i].append(product_info_name[i])
                            pi_information_[pg][i].append(product_info_details[i])
                        elif len(pi_information_[pg]) >= max_frame_per_page:
                            pg += 1
                        else:
                            break
                except:
                    pass

                increment_value = 1  # Keeps track of how many frames have been created for this instance
                change_config_row = 0  # Configures the index of 'rows' for display frames
                change_parent_frame = 0

                # print(pi_information_)
                try:
                    for create_lbl in range(len(pi_information_[current_page])):  # original: len(product_info_name)
                        ## --- Product Image --- ##
                        # Original list used for display: product_info_details[create_lbl][1][2]
                        try:
                            product_image = Image.open(f'{new_pi[current_page][create_lbl][1][1][2]}')
                            product_image_widget = customtkinter.CTkImage(product_image, size=(240, 205))
                            product_image_display = customtkinter.CTkButton(
                                product_frame_list[change_config_row][change_parent_frame],
                                image=product_image_widget, text="",
                                width=200, height=100, corner_radius=1,
                                hover_color="#a8cce8", fg_color="#949494",
                                cursor="hand2",
                                command=lambda
                                    title=new_pi[current_page][create_lbl][0],
                                    price=new_pi[current_page][create_lbl][1][0][0],
                                    image=new_pi[current_page][create_lbl][1][1][2],
                                    description=new_pi[current_page][create_lbl][1][0][1],
                                    uuid=new_pi[current_page][create_lbl][1][1][3],
                                    stocks=new_pi[current_page][create_lbl][1][0][2]:
                                product_details_page(title, price, image,
                                                     description, uuid, stocks, cframe))
                            product_image_display.image = product_image_widget
                            product_image_display.place(relx=0.5, rely=0.31, anchor=CENTER)

                            ## --- Product Title/Name --- ##
                            # Original list used for display: product_info_name[create_lbl]
                            product_title = customtkinter.CTkLabel(
                                product_frame_list[change_config_row][change_parent_frame],
                                text=new_pi[current_page][create_lbl][0], font=("Bold", 17))
                            product_title.place(relx=0.5, rely=0.875, anchor=CENTER)

                            ## --- Product Price --- ##
                            # Original list used for display: product_info_details[create_lbl][0][0]
                            price_lbl = customtkinter.CTkLabel(product_frame_list[change_config_row][change_parent_frame],
                                                               text=f"${new_pi[current_page][create_lbl][1][0][0]}",
                                                               font=("Bold", 17))
                            price_lbl.place(relx=0.25, rely=0.75, anchor=CENTER)

                            ## --- Product Add to Cart Button --- ##
                            add_to_cart_btn = customtkinter.CTkButton(
                                product_frame_list[change_config_row][change_parent_frame], width=30, height=15,
                                font=("Century Gothic", 14, "bold"), fg_color="#949494",
                                bg_color="#949494", border_color="#7b7b7b", border_width=2,
                                hover_color="#949494", text_color="#4a4a4a",
                                text="Add to Cart",
                                command=lambda name=product_title.cget('text'),
                                               pi_index=create_lbl:
                                add_to_cart(name, product_info_details[pi_index][0][0],
                                            product_info_details[pi_index][1][3], 1))
                            add_to_cart_btn.place(relx=0.775, rely=0.75, anchor=CENTER)

                            change_parent_frame += 1
                            increment_value += 1

                            if increment_value > max_num_of_column:
                                change_config_row += 1
                                change_parent_frame = 0
                                increment_value = 1
                        except: pass
                except: pass

                # - Add to Cart Indicators -#
                def OnHoverATC3(button, fgcolorOnHover, fgcolorNotHover, bdcolorOnHover, bdcolorNotHover):
                    button.bind("<Enter>", command=lambda e: button.configure(fg_color=fgcolorOnHover))
                    button.bind("<Enter>", command=lambda e: button.configure(border_color=bdcolorOnHover))

                    button.bind("<Leave>", command=lambda e: button.configure(fg_color=fgcolorNotHover))
                    button.bind("<Leave>", command=lambda e: button.configure(border_color=bdcolorNotHover))

                productw_atc = list(product_info_widgets.values())

                for pw_atc in range(len(productw_atc)):
                    OnHoverATC3(productw_atc[pw_atc][3], "#ffd3a4", "#949494",
                               "#ff931c", "#7b7b7b")

            load_page(num_of_frame_column, current_rows, page_, current_value_row)


        def category1_page():
            global category1_frame
            category1_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            category_df(Category_Names[0], category1_frame)
            '''lb = Label(category1_frame, text="Category 1 Page\n\nPage: 2", font=("Bold", 30), bg="#c5c5c5")
            lb.grid(sticky=NSEW, row=0, column=0)'''

            category1_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

        def category2_page():
            global category2_frame
            category2_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            category_df(Category_Names[1], category2_frame)

            category2_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

        def category3_page():
            global category3_frame
            category3_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            category_df(Category_Names[2], category3_frame)

            category3_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

        def category4_page():
            global category4_frame
            category4_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            category_df(Category_Names[3], category4_frame)

            category4_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

        def category5_page():
            global category5_frame
            category5_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            category_df(Category_Names[4], category5_frame)

            category5_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

        def category6_page():
            global category6_frame
            category6_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            category_df(Category_Names[5], category6_frame)

            category6_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

        def category7_page():
            global category7_frame
            category7_frame = customtkinter.CTkScrollableFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            category_df(Category_Names[6], category7_frame)

            category7_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

        def cart_items_page():
            hide_indicate()  # Hide all button indicators
            cart_items_frame = customtkinter.CTkFrame(Main_Frame_HP, fg_color="#c5c5c5", corner_radius=0)

            ci_title = customtkinter.CTkLabel(cart_items_frame, text="Your Cart", font=("Century Gothic", 18, "bold"),
                                              text_color="#4a4a4a")
            ci_title.place(relx=0.2, rely=0.03, anchor=CENTER)

            ci_scroll_frame = customtkinter.CTkScrollableFrame(cart_items_frame, fg_color="#a3a3a3", corner_radius=3)
            ci_scroll_frame.place(relx=0.5, rely=0.36, relwidth=0.675, relheight=0.63, anchor=CENTER)

            separator = customtkinter.CTkCanvas(cart_items_frame, height=3, bg="#7b7b7b", highlightthickness=0)
            separator.place(relx=0.5, rely=0.685, relwidth=0.71, anchor=CENTER)

            ci_info_frame = customtkinter.CTkFrame(Main_Frame_HP, fg_color="#a3a3a3", corner_radius=3)
            ci_info_frame.place(relx=0.5, rely=0.835, relwidth=0.675, relheight=0.28, anchor=CENTER)

            #Vertical separator
            separator2 = customtkinter.CTkCanvas(ci_info_frame, width=3, bg="#7b7b7b", highlightthickness=0)
            separator2.place(relx=0.525, rely=0.5, relheight=1, anchor=CENTER)
            #-----------------#

            ci_shipment_info = customtkinter.CTkLabel(ci_info_frame, text="Items ordered internationally will "
                                                                          "take around 3 - 10\nbusiness days to arrive.\n\n"
                                                                          "If items are ordered domestically,\n"
                                                                          "package arrival will be around\n"
                                                                          "2 - 5 business days.\n\n"
                                                                          "If you ordered more items than the\n"
                                                                          "maximum stock amount, arrival date\n"
                                                                          "will be delayed.",
                                                      font=("Century Gothic", 17, "bold"),
                                                      text_color="#4a4a4a")
            ci_shipment_info.place(relx=0.263, rely=0.5, anchor=CENTER)

            tc_lst = []
            for i in range(len(Cart_Items)):
                tc_lst.append(float(Cart_Items[i][1]))
            total_cost = round(sum(tc_lst), 2)

            # Checks if there are no more than two decimal places, if value has less than 2 then add a 0 as a str
            check_value_ = f"{total_cost}"
            if len(check_value_.rsplit('.')[-1]) != 2 and total_cost != 0:
                total_cost = f"{total_cost}0"
            elif total_cost == 0:
                total_cost = f"{total_cost}.00"

            ci_total_cost = customtkinter.CTkLabel(ci_info_frame, text=f"Total Cost: ${total_cost}",
                                                      font=("Century Gothic", 16, "bold"),
                                                      text_color="#4a4a4a")
            ci_total_cost.place(relx=0.775, rely=0.1, anchor=CENTER)

            text_of_dd = ""
            if total_cost == 0:
                text_of_dd = "Nothing"
            elif 1 <= float(total_cost) <= 50:
                text_of_dd = "Not Enough Money Spent"
            elif 51 <= float(total_cost) <= 99:
                text_of_dd = "Tiny"
            elif float(total_cost) >= 100:
                text_of_dd = "Amazing"

            ci_discount_display = customtkinter.CTkLabel(ci_info_frame, text=f"Discounted Amount: {text_of_dd}",
                                                   font=("Century Gothic", 16, "bold"),
                                                   text_color="#4a4a4a")
            ci_discount_display.place(relx=0.775, rely=0.25, anchor=CENTER)

            display_credit2 = customtkinter.CTkLabel(ci_info_frame, text=f"Credit: ${Credit:,}",
                                                    font=("Century Gothic", 16, "bold"),
                                                    text_color="#4a4a4a")
            display_credit2.place(relx=0.725, rely=0.4)

            #Checkout button validity
            def checkout():
                global Credit

                validity_text = customtkinter.CTkLabel(ci_info_frame, text="", text_color="#4a4a4a")
                validity_text.place(relx=0.585, rely=0.835)

                if len(Cart_Items) == 0:
                    validity_text.configure(text="Checkout invalid, there are no items in this cart!",
                                            font=("Century Gothic", 16, "bold"), text_color="#ff1919")
                    validity_text.after(5000, lambda: validity_text.configure(text=""))

                if float(total_cost) > float(Credit):
                    validity_text.configure(text="Checkout invalid, you are poor!",
                                            font=("Century Gothic", 16, "bold"), text_color="#ff1919")
                    validity_text.after(5000, lambda: validity_text.configure(text=""))
                if len(Cart_Items) > 0:
                    receipt_win = Toplevel()
                    receipt_win.geometry("350x500")
                    receipt_win.title(f"Amazing Receipt")

                    scrollable_receipt = customtkinter.CTkScrollableFrame(receipt_win, corner_radius=2, fg_color="#f1f1f1")
                    scrollable_receipt.place(relx=0.5, rely=0.575, anchor=CENTER, relheight=0.85, relwidth=1)

                    receipt_combine = []
                    for rn in range(5):
                        receipt_no_generate = random.randint(0, 50)
                        receipt_combine.append(receipt_no_generate)
                    receipt_join = [str(c) for c in receipt_combine]
                    receipt_no = "".join(receipt_join)

                    receipt_text = customtkinter.CTkLabel(receipt_win, text=f"Receipt No. #{receipt_no}",
                                                          text_color="#000000", font=("Century Gothic", 20, "bold"))
                    receipt_text.place(relx=0.5, rely=0.05, anchor=CENTER)

                    def separator2(rx, ry, rw):
                        separator = customtkinter.CTkCanvas(receipt_win, height=3, bg="#7b7b7b", highlightthickness=0)
                        separator.place(relx=rx, rely=ry, relwidth=rw, anchor=CENTER)

                    separator2(0.5, 0.075, 0.75)

                    receipt_tc = customtkinter.CTkLabel(receipt_win, text=f"Total Cost: ${total_cost}",
                                                          text_color="#000", font=("Arial", 20, "bold"))
                    receipt_tc.place(relx=0.5, rely=0.125, anchor=CENTER)

                    separator2(0.5, 0.15, 0.7)

                    for display_ci in range(len(Cart_Items)):
                        names_store_lbl = list(store_label.keys())
                        values_store_lbl = list(store_label.values())

                        clear_frame(ci_scroll_frame)

                        def store_and_create_frames():

                            for display_plbl in range(len(names_store_lbl)):
                                display_cart_items = customtkinter.CTkLabel(scrollable_receipt,
                                                                            text=f"{names_store_lbl[display_plbl]} "
                                                                                 f"x{values_store_lbl[display_plbl][0]}"
                                                                                 f" | ${values_store_lbl[display_plbl][1]}",
                                                                            font=("Century Gothic", 20, "bold"),
                                                                            text_color="#4a4a4a")
                                display_cart_items.grid(row=0 + display_plbl, column=0, padx=65, pady=5,
                                                        sticky="ew")

                        store_and_create_frames()

                    check_value_2 = f"{round(Credit - float(total_cost), 2)}"
                    if len(check_value_2.rsplit('.')[-1]) != 2:
                        check_value_2 = f"{check_value_2}0"
                    elif total_cost == 0:
                        check_value_2 = f"{check_value_2}.00"
                    Credit = float(check_value_2)

                    display_credit.configure(text=f"Credit: ${Credit:,}")

                    Cart_Items.clear()
                    configCartBtn()
                    home_page(0)

                    receipt_win.mainloop()

            #Indicator for checkout button
            def OnHoverCB(button, fgcolorOnHover, fgcolorNotHover, bdcolorOnHover, bdcolorNotHover):
                button.bind("<Enter>", command=lambda e: button.configure(fg_color=fgcolorOnHover))
                button.bind("<Enter>", command=lambda e: button.configure(border_color=bdcolorOnHover))

                button.bind("<Leave>", command=lambda e: button.configure(fg_color=fgcolorNotHover))
                button.bind("<Leave>", command=lambda e: button.configure(border_color=bdcolorNotHover))

            checkout_btn = customtkinter.CTkButton(ci_info_frame, text=f"Checkout", font=("Century Gothic", 18, "bold"),
                                                   fg_color="#949494", bg_color="#949494", border_color="#7b7b7b",
                                                   border_width=2, hover_color="#949494", text_color="#4a4a4a",
                                                   cursor="hand2", command=lambda: checkout())
            checkout_btn.place(relx=0.7, rely=0.685)

            OnHoverCB(checkout_btn, "#ddf0b2", "#949494",
                      "#80b900", "#7b7b7b")

            # - Display Cart Items on Page -#
            check_multiple = []
            check_multiple2 = []
            store_label = {}

            for display_ci in range(len(Cart_Items)):
                check_multiple.append(Cart_Items[display_ci][0])
                confirm_amount = check_multiple.count(Cart_Items[display_ci][0])

                check_multiple2.append(
                    Cart_Items[display_ci][1])  # This is a list with the actual prices of the products
                confirm_amount_price = check_multiple2.count(Cart_Items[display_ci][1])
                confirm_calc_price = round(float(confirm_amount_price) * float(Cart_Items[display_ci][1]), 2)
                check_value_notation = f"{confirm_calc_price}"

                # Checks if there are no more than two decimal places, if value has less than 2 then add a 0 as a str
                if len(check_value_notation.rsplit('.')[-1]) != 2:
                    confirm_calc_price = f"{confirm_calc_price}0"

                store_label[f"{Cart_Items[display_ci][0]}"] = [confirm_amount, confirm_calc_price,
                                                               Cart_Items[display_ci][2], check_multiple2[display_ci]]

                names_store_lbl = list(store_label.keys())
                values_store_lbl = list(store_label.values())

                clear_frame(ci_scroll_frame)

                def store_and_create_frames():

                    for display_plbl in range(len(names_store_lbl)):
                        display_cart_items = customtkinter.CTkLabel(ci_scroll_frame,
                                                                    text=f"{names_store_lbl[display_plbl]} "
                                                                         f"x{values_store_lbl[display_plbl][0]}"
                                                                         f" | ${values_store_lbl[display_plbl][1]}",
                                                                    font=("Century Gothic", 20, "bold"))
                        display_cart_items.grid(row=0 + display_plbl, column=0, padx=10, columnspan=2, sticky="ew")

                        remove_cart_item = customtkinter.CTkButton(ci_scroll_frame, text="X",
                                                                   font=("Century Gothic", 20, "bold"), width=10,
                                                                   command=lambda index=display_plbl,
                                                                                  ci=ci_scroll_frame:
                                                                   remove_item(names_store_lbl[index],
                                                                               values_store_lbl[index][3],
                                                                               values_store_lbl[index][2], ci))
                        remove_cart_item.grid(row=0 + display_plbl, column=1, padx=700, columnspan=2, sticky="ew")

                store_and_create_frames()

            """lb = Label(cart_items_frame, text="Cart Items Page\n\nPage: 9", font=("Bold", 30), bg="#c5c5c5")
            lb.grid(sticky="nsew", row=0, column=0)"""

            # - Positions the cart_items_frame -#
            cart_items_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)

        def configCartBtn():
            Cart_Btn.configure(text=f"{len(Cart_Items)}")

        ### ----- Add to Cart Function ----- ###
        def add_to_cart(specific_button, specific_price, uuid_of_product, amount):
            for multiply_items in range(int(amount)):
                Cart_Items.append([specific_button, specific_price, uuid_of_product])
            configCartBtn()

        def remove_item(name_of_item, price_of_item, uuid_of_item, ci):
            Cart_Items.remove([name_of_item, price_of_item, uuid_of_item])
            configCartBtn()
            cart_items_page()

        def hide_indicate():

            for hide_i in range(len(var_name)):
                ConvertVar[var_name[hide_i]].configure(bg_color="#dedede")
                ConvertVar[var_name[hide_i]].configure(fg_color="#dedede")

                ConvertVar[var_name[hide_i] + "b"].configure(bg_color="#dedede")
                ConvertVar[var_name[hide_i] + "b"].configure(fg_color="#dedede")

            """ConvertVar[var_name[0]].configure(bg_color="#dedede")
            ConvertVar[var_name[0]].configure(fg_color="#dedede")

            ConvertVar[var_name[0] + "b"].configure(bg_color="#dedede")
            ConvertVar[var_name[0] + "b"].configure(fg_color="#dedede")"""
            """home_indicator.config(bg="#a5a5a5")
            products_indicator.config(bg="#a5a5a5")
            menu_indicator.config(bg="#a5a5a5")
            contact_indicator.config(bg="#a5a5a5")
            account_indicator.config(bg="#a5a5a5")

            home_indicator2.config(bg="#a5a5a5")
            products_indicator2.config(bg="#a5a5a5")
            menu_indicator2.config(bg="#a5a5a5")
            contact_indicator2.config(bg="#a5a5a5")
            account_indicator2.config(bg="#a5a5a5")"""

        def delete_pages():
            for frame in Main_Frame_HP.winfo_children():
                frame.destroy()

        def indicate(lb, lb2, page):
            hide_indicate()
            lb.configure(bg_color="#158aff")
            lb.configure(fg_color="#158aff")
            lb2.configure(bg_color="#158aff")
            lb2.configure(fg_color="#158aff")
            delete_pages()
            page()

        ### ===== MAIN NAVIGATION BAR ===== ###
        ctkframe = customtkinter.CTkFrame

        NavBar = ctkframe(homepage, width=screen_width + 4, height=50, fg_color="#c5c5c5", bg_color="#c5c5c5")
        NavBar.place(x=-1, y=0)

        NavBar2 = ctkframe(homepage, width=screen_width + 4, height=35, fg_color="#dedede", bg_color="#dedede")
        NavBar2.place(x=-1, y=50)

        # ====== MENU BAR ==========
        logoIcon = Image.open('images/Amazing_Logo_Full.png')
        photo = customtkinter.CTkImage(logoIcon, size=(165, 42))
        logo = customtkinter.CTkButton(master=homepage, image=photo, fg_color="#c5c5c5", text="", bg_color="#c5c5c5",
                                       hover_color="#c5c5c5", width=49, height=49, corner_radius=1, cursor="hand2",
                                       command=lambda: home_page(0))
        logo.image = photo
        logo.place(x=0, y=0)

        class SearchBar(customtkinter.CTkFrame):
            def __init__(self, parent, allItems, widthInText=30, autoCompleteFunction=None, valuesToDisplay=5):
                """
                :param parent: The Parent Object
                :param allItems: this specifies the Items From Which the search happens
                :param widthInText: The width of search bar in text units but not pixels.
                :param autoCompleteFunction: if you want to specify your own function for autocomplete. Default function will be
                       used when set to None
                :param valuesToDisplay: The No Of Values to Display at a time
                """
                customtkinter.CTkFrame.__init__(self, parent, width=600, height=40, bg_color="#c5c5c5")
                self.width = widthInText
                self.height = 40
                self.hide_lb = []
                self.allItems = allItems
                self.autoCompleteFunction = autoCompleteFunction
                self.valuesToDisplay = valuesToDisplay
                if len(self.allItems) > self.valuesToDisplay:
                    self.displayValues = self.allItems[:self.valuesToDisplay]
                else:
                    self.displayValues = self.allItems
                self.searchBarOptionSelectedFunc = None
                self.searchVar = StringVar()
                self.searchBar = customtkinter.CTkEntry(self, textvariable=self.searchVar,
                                                        width=600, height=self.height,
                                                        font=("Arial", 20), bg_color="#c5c5c5",
                                                        placeholder_text='Search', corner_radius=2, border_width=2)
                self.listBox = Listbox(self, width=40, height=len(self.displayValues), font=("Arial", 20),
                                       activestyle='none', selectbackground="#e8e8e8", selectforeground="#000000",
                                       borderwidth=2, bg="#acacac", highlightbackground="#949494")

                self.searchBar.grid(row=0, column=0)
                self.updateListBox(self.displayValues)

                self.searchBar.bind("<KeyRelease>", self.keyPressOnSearchBar)
                self.listBox.bind("<Return>", self.returnPressedOnListBox)
                self.searchBar.bind("<Tab>", self.tabPressedOnEntry)
                self.listBox.bind("<Tab>", self.tabPressedOnListBox)
                self.listBox.bind("<<ListboxSelect>>", self.optionSelectedInListBox)

            def update_lb_frame(self):
                global saved_search, run_hide_lb  # Global variables
                saved_search = self.searchVar.get()  # Stores the search value(str)
                run_hide_lb = self.hide_lb

                new_search = [list(str(self.searchVar.get()))]

                if 0 <= len(self.searchBar.get()) <= 1:
                    customtkinter.CTkFrame.configure(self, height=40)
                    if len(self.searchVar.get()) == 1:
                        new_search.append("")
                        if len(new_search) == 2:
                            new_search.pop(0)
                if len(new_search) == 1 and new_search[0] == "":
                    customtkinter.CTkFrame.configure(self, height=40)
                elif len(self.searchBar.get()) != 0:
                    customtkinter.CTkFrame.configure(self, height=40 + (len(self.displayValues) * 33))

                self.searchBar.update_idletasks()
                customtkinter.CTkFrame.update_idletasks(self)

            def remove_lb(self):
                #####DOESN"T WORK, LOOK INTO THIS LATER#####
                self.listBox.grid_forget()

            def updateListBox(self, items):
                self.listBox.delete(0, END)
                self.update_lb_frame()
                for item in items:
                    self.listBox.insert(END, item)

            def matchString(self, text1):
                if self.autoCompleteFunction is None:
                    # s = time.time()
                    allStrings = self.allItems
                    text1 = [i for i in text1.lower()]
                    sameMatches = {}
                    for j in allStrings:
                        sameMatches[j] = 0
                    for idx, word in enumerate(allStrings):

                        letters = [i for i in word]
                        for letter in text1:
                            for letter2 in letters:
                                if letter == letter2.lower():
                                    sameMatches[allStrings[idx]] += 1

                    marklist = sorted(sameMatches.items(), key=lambda x: x[1], reverse=True)
                    allafgag = []
                    for sortedS in marklist:
                        allafgag.append(sortedS[0])
                    # e = time.time()
                    return allafgag
                else:
                    functionSorted = self.autoCompleteFunction

                    return functionSorted(text1, self.allItems)

            def returnPressedOnListBox(self, e=None):
                index = self.listBox.curselection()
                #self.listBox.place_forget()
                self.listBox.grid_forget()
                if len(index) > 0:
                    index = index[0]
                    self.searchVar.set(self.displayValues[index])
                    if self.searchBarOptionSelectedFunc is not None:
                        self.searchBarOptionSelectedFunc(self.displayValues[index])

            def tabPressedOnEntry(self, e=None):
                if self.listBox.winfo_ismapped():
                    self.listBox.select_set(0)

            def optionSelectedInListBox(self, e=None):
                index = self.listBox.curselection()
                if len(index) > 0:
                    index = index[0]
                    self.searchVar.set(self.displayValues[index])
                    if self.searchBarOptionSelectedFunc is not None:
                        self.searchBarOptionSelectedFunc(self.displayValues[index])

            def tabPressedOnListBox(self, e=None):
                if self.listBox.winfo_ismapped():
                    index = self.listBox.curselection()
                    if len(index) > 0:
                        index = index[0]
                        self.searchVar.set(self.displayValues[index])
                        if self.searchBarOptionSelectedFunc is not None:
                            self.searchBarOptionSelectedFunc(self.displayValues[index])
                    else:
                        self.searchVar.set(self.displayValues[0])
                        if self.searchBarOptionSelectedFunc is not None:
                            self.searchBarOptionSelectedFunc(self.displayValues[0])
                    #self.listBox.place_forget()
                    self.listBox.grid_forget()

            def keyPressOnSearchBar(self, e=None):
                if e.keycode == 40:  # Down Arrow presses on search Bar
                    self.listBox.focus_set()
                    self.listBox.select_set(0)
                    self.searchVar.set(self.displayValues[0])
                    if self.searchBarOptionSelectedFunc is not None:
                        self.searchBarOptionSelectedFunc(self.displayValues[0])
                elif e.keycode == 13:  # Enter Pressed on search Bar
                    #self.listBox.place_forget()
                    self.listBox.grid_forget()
                    self.searchVar.set(self.displayValues[0])
                    if self.searchBarOptionSelectedFunc is not None:
                        self.searchBarOptionSelectedFunc(self.displayValues[0])
                else:
                    searchBarText = self.searchVar.get()
                    if searchBarText == "":
                        #self.listBox.place_forget()
                        self.listBox.grid_forget()
                    else:
                        dataInOrder = self.matchString(searchBarText)
                        dataInOrder = dataInOrder[:self.valuesToDisplay]
                        self.displayValues = dataInOrder
                        self.updateListBox(dataInOrder)
                        if not self.listBox.winfo_ismapped():
                            self.listBox.grid(row=1, column=0)

            def bind_Function_To_SearchBar_Option_Selected(self, func):
                self.searchBarOptionSelectedFunc = func

            def configureListBox(self, **options):
                self.listBox.configure(options)

            def configureSearchBar(self, **options):
                self.searchBar.configure(options)

            def getValue(self):
                return self.searchVar.get()

        def remove_lb_outside():
            SearchBar(homepage, name_of_product).remove_lb()


        name_of_product = list(product_info.keys())
        random.shuffle(name_of_product)

        Searchbar = SearchBar(homepage, name_of_product)
        Searchbar.place(relx=0.229, rely=0.0065)

        def run_event():
            global converted_matching_dict
            #product_name = list(product_info_widgets.values())

            #Sorts the dictionary value in descending order
            sort_matching_dict = sorted(product_info_widgets.items(), key=lambda m: m[1][4], reverse=True)
            converted_matching_dict = dict(sort_matching_dict)

            remove_lb_outside()

        def onSearch():
            global matching_dict

            check_length = list(saved_search)  # From search bar
            pi_name = list(product_info.keys())  # From product info

            matching_dict = {}  #A dictionary, to store matching values

            ##- Matching Search of Item Function -##
            for cl_ in range(len(pi_name)):
                check_length2 = list(pi_name[cl_])
                matching = 0  # Assign a value of 0 to 'matching'. Start from 0
                for search in check_length:
                    # print(search)
                    # print(check_length)
                    # print(check_length2)
                    if search in check_length2:
                        matching += 1  # Increases matching value by 1 if a matching number is found
                        # print(f"{matching} has been found matched")
                    '''else:
                        print("No match has been found")'''
                product_info_widgets[f"product_frame{cl_ + 1}"].insert(4, matching)
                matching_dict[f"{pi_name[cl_]}"] = matching
                try:
                    product_info_widgets[f"product_frame{cl_ + 1}"].pop(5)
                except: pass

                # print("_________")
            # print("#---------------#")

            ##- Search for Item Function -##
            run_event()
            search_page()

        SearchbarBtn = customtkinter.CTkButton(NavBar, text="Search", width=100, height=40,
                                               font=("Century Gothic", 20, "bold"), command=lambda: onSearch())
        SearchbarBtn.place(relx=0.6475, rely=0.1)

        shopping_cart_icon = Image.open('images/Shopping_Cart_Icon.png')
        icon_sci = customtkinter.CTkImage(shopping_cart_icon, size=(30, 30))

        Cart_Btn = customtkinter.CTkButton(NavBar, text="0", width=80, height=40,
                                           font=("Century Gothic", 20, "bold"),
                                           image=icon_sci, compound=LEFT, command=cart_items_page)
        Cart_Btn.place(relx=0.8135, rely=0.1)

        Account_Btn = customtkinter.CTkButton(NavBar, text="Account", width=120, height=40, fg_color="#c5c5c5",
                                              bg_color="#c5c5c5", border_color="#c5c5c5", border_width=2,
                                              hover_color="#c5c5c5", text_color="#313131", cursor="hand2",
                                              font=("Century Gothic", 20, "bold"), command=animated_panel2.animate)
        Account_Btn.place(relx=0.9, rely=0.1)



        def OnHover(button, colorOnHover, colorNotHover):
            button.bind("<Enter>", command=lambda e: button.configure(border_color=colorOnHover))

            button.bind("<Leave>", command=lambda e: button.configure(border_color=colorNotHover))

        ### ===== SECOND NAVIGATION BAR ===== ###
        Filter_Btn = customtkinter.CTkButton(NavBar2, text="Filter", width=80, height=25,
                                             font=("Century Gothic", 20, "bold"), fg_color="#dedede",
                                             bg_color="#dedede", border_color="#dedede", border_width=2,
                                             hover_color="#dedede", text_color="#7b7b7b",
                                             command=animated_panel.animate)
        Filter_Btn.place(x=50, y=3)  # og: x=50, y=3

        OnHover(Filter_Btn, "#158aff", "#dedede")  # Hover Event
        OnHover(Account_Btn, "#158aff", "#c5c5c5")

        navbar2_line = customtkinter.CTkCanvas(NavBar2, width=1.5, height=35, bg="#c5c5c5", highlightthickness=0)
        navbar2_line.place(x=180, y=0)

        category_btn = [Category_Names[0], Category_Names[1], Category_Names[2], Category_Names[3], Category_Names[4],
                        Category_Names[5], Category_Names[6]]
        category_cmd_btn = [category1_page, category2_page, category3_page, category4_page, category5_page,
                            category6_page, category7_page, home_page]
        ConvertVar = vars()

        x_coordinates = [0.175, 0.305, 0.41, 0.54, 0.65, 0.75, 0.85]
        width_of_i = [132, 84, 118, 80, 82, 80, 88]
        #start_xpos = 0.175  # og: 240

        awp = 0

        for cbtn in range(len(category_btn)):
            (customtkinter.CTkButton(NavBar2, text=category_btn[cbtn], width=80, height=25,
                                     font=("Century Gothic", 20, "bold"), text_color="#7b7b7b",
                                     fg_color="#dedede", hover_color="#a8cce8",
                                     command=lambda new_var=0 + cbtn: indicate(ConvertVar[var_name[new_var]],
                                                                               ConvertVar[var_name[new_var] + "b"],
                                                                               category_cmd_btn[new_var]))
             .place(relx=x_coordinates[cbtn], rely=0.08))

            # def l_calculus(new_var2=0 + cbtn): ConvertVar[var_name[new_var2]]
            # lambda_calculus = lambda new_var2=0 + cbtn: cbtn

            ConvertVar[var_name[awp]] = customtkinter.CTkFrame(NavBar2, width=width_of_i[cbtn], height=3, bg_color="#dedede",
                                                               fg_color="#dedede", corner_radius=1)
            ConvertVar[var_name[awp]].place(relx=x_coordinates[cbtn], rely=0.099)

            ConvertVar[var_name[awp] + "b"] = customtkinter.CTkFrame(NavBar2, width=width_of_i[cbtn], height=3, bg_color="#dedede",
                                                                     fg_color="#dedede", corner_radius=1)
            ConvertVar[var_name[awp] + "b"].place(relx=x_coordinates[cbtn], rely=0.85)

            awp += 1

            #start_xpos += 0.1  # og: 140

        home_page(0)  # Default Page

        '''def obtain_ginfo(pframe):
            global animated_panel2

            pframe_r = pframe.grid_info()["row"]
            pframe_c = pframe.grid_info()["column"]
            animated_panel2 = SlidePanel_PDF(product_frame_list[pframe_r][pframe_c], 0.2, 0.5)
            return pframe_r, pframe_c'''

        '''def OnHoverInfo(frame_i):
            frame_i.bind("<Enter>", command=lambda e: obtain_ginfo(frame_i))

        def OnHoverFrame(frame):
            frame.bind("<Enter>", command=lambda e: animated_panel2.animate())

            frame.bind("<Leave>", command=lambda e: animated_panel2.animate())

        for pframe_rows in range(len(current_columns)):
            for pframe_columns in range(current_columns[pframe_rows]):
                OnHoverInfo(product_frame_list[pframe_rows][pframe_columns])

                pframe_r, pframe_c = obtain_ginfo(product_frame_list[pframe_rows][pframe_columns])
                #print(pframe_r, pframe_c)
                #new = customtkinter.CTkFrame(product_frame_list[pframe_rows][pframe_columns])
                #new.place(relx=0.085, rely=0.05)
        OnHoverFrame(product_frame_list[pframe_r][pframe_c])
        #print(pframe_r, pframe_c)

        #OnHoverFrame()'''

        # print(product_widget_global)

        """options_fm = Frame(homepage, width=500, height=45, bg="#a5a5a5")

        home_btn = Button(options_fm, text="Home", width=8, font=("Bold", 15), fg="#158aff", bd=0, bg='#a5a5a5',
                             command=lambda: indicate(home_indicator, home_indicator2, home_page))
        home_btn.place(x=0, y=4)

        home_indicator = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        home_indicator.place(x=2, y=39)
        home_indicator2 = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        home_indicator2.place(x=2, y=2)

        products_btn = Button(options_fm, text="Products", width=8, font=("Bold", 15), fg="#158aff", bd=0,
                                 bg='#a5a5a5',
                                 command=lambda: indicate(products_indicator, products_indicator2, products_page))
        products_btn.place(x=100, y=4)

        products_indicator = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        products_indicator.place(x=102, y=39)
        products_indicator2 = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        products_indicator2.place(x=102, y=2)

        menu_btn = Button(options_fm, text="Menu", width=8, font=("Bold", 15), fg="#158aff", bd=0, bg='#a5a5a5',
                             command=lambda: indicate(menu_indicator, menu_indicator2, menu_page))
        menu_btn.place(x=200, y=4)

        menu_indicator = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        menu_indicator.place(x=202, y=39)
        menu_indicator2 = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        menu_indicator2.place(x=202, y=2)

        contact_btn = Button(options_fm, text="Contact", width=8, font=("Bold", 15), fg="#158aff", bd=0,
                                bg='#a5a5a5',
                                command=lambda: indicate(contact_indicator, contact_indicator2, contact_page))
        contact_btn.place(x=300, y=4)

        contact_indicator = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        contact_indicator.place(x=302, y=39)
        contact_indicator2 = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        contact_indicator2.place(x=302, y=2)

        account_btn = Button(options_fm, text="Account", width=8, font=("Bold", 15), fg="#158aff", bd=0,
                                bg='#a5a5a5',
                                command=lambda: indicate(account_indicator, account_indicator2, account_page))
        account_btn.place(x=400, y=4)

        account_indicator = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        account_indicator.place(x=402, y=39)
        account_indicator2 = Frame(options_fm, width=90, height=3, bg="#a5a5a5")
        account_indicator2.place(x=402, y=2)

        options_fm.place(x=0, y=0)"""

        # main_frame = tk.Frame(root, width=500, height=455, bg="#c5c5c5")
        # main_frame.place(x=0, y=45)

        # menuBar_line = Canvas(homepage, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
        # menuBar_line.place(x=0, y=60)

        """admIcon = Image.open('images/Amazing-Logo-Brand.png')
        photo = ImageTk.PhotoImage(admIcon)
        adm = Label(homepage, image=photo, bg='#ffffff')
        adm.image = photo
        adm.place(x=1280, y=5)

        admLabel = Label(homepage, text='ADMIN', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#ffffff')
        admLabel.place(x=1180, y=11)

        home_bgImg = Image.open('images/Amazing-Logo-Brand.png')
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(x=0, y=60)

        brandIcon = Image.open('images/Amazing-Logo-Brand.png')
        photo = ImageTk.PhotoImage(brandIcon)
        brandlogo = Label(homepage, image=photo, bg='black')
        brandlogo.image = photo
        brandlogo.place(x=1085, y=83)

        heading = Label(homepage, text='© GIDE0NS C0FFEE SH0P', bg='black', fg='#ff6c38', font=("yu gothic ui", 19, "bold"))
        heading.place(x=770, y=90)

        heading2 = Label(homepage, text='Trending', bg='black', fg='#ff6c38', font=("", 19, "bold"))
        heading2.place(x=150, y=95)

        # Coffee Image
        coffeeImage = Image.open('images/Amazing-Logo-Brand.png')
        photo = ImageTk.PhotoImage(coffeeImage)
        coffeeImg = Label(homepage, image=photo, bg='black')
        coffeeImg.image = photo
        coffeeImg.place(x=50, y=150)"""

        """# ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        home_button.place(x=70, y=15)

        def manage():
            main_window.withdraw()
            os.system("python admin.py")
            main_window.destroy()

        # ========== MANAGE BUTTON =======
        manage_button = Button(homepage, text='Manage', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                               command= manage)
        manage_button.place(x=150, y=15)

        # ========== PRODUCTS BUTTON =======
        product_button = Button(homepage, text='Products', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                command=manage)
        product_button.place(x=250, y=15)"""

        # ========== HELP BUTTON =======

        def help():
            win = Toplevel()
            window_width = 1366
            window_height = 768
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            win.title('Forgot Password')
            # win.configure(background=('images/hel'))
            win.resizable(0, 0)

            # Coffee Image
            bgImage = Image.open('images/help.png')
            photo = ImageTk.PhotoImage(bgImage)
            Img = Label(win, image=photo)
            Img.image = photo
            Img.place(x=0, y=0)

        """help_button = Button(homepage, text='Help', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=help)
        help_button.place(x=360, y=15)"""

        def logout():
            win = Toplevel()
            CSC3_ECommerce_App.AccountSystem.AccountPage(win)
            main_window.withdraw()
            win.deiconify()

        """# ========== LOG OUT =======
        logout_button = Button(homepage, text='Logout', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=logout)
        logout_button.place(x=420, y=15)"""


def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
