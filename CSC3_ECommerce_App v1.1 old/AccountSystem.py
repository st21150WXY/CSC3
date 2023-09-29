from tkinter import *
import customtkinter
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import sqlite3
import CSC3_ECommerce_App.ECommerce_GUI



class AccountPage:
    def __init__(self, AccountSystem_window):
        self.AccountSystem_window = AccountSystem_window

        # Window Size and Placement
        AccountSystem_window.rowconfigure(0, weight=1)
        AccountSystem_window.columnconfigure(0, weight=1)
        screen_width = AccountSystem_window.winfo_screenwidth()
        screen_height = AccountSystem_window.winfo_screenheight()
        window_width = screen_width
        window_height = screen_height - 72
        x = (screen_width//2)-(window_width//2)
        y = (screen_height//2)-(window_height//2)
        AccountSystem_window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x - 8, y - 39))
        AccountSystem_window.resizable(0, 0)

        # window Icon
        icon = PhotoImage(file='images/Amazing-Logo-Brand.png')
        AccountSystem_window.iconphoto(True, icon)

        AccountSystem_window.title('AMAZING')
        #AccountSystem_window.configure(bg="#c5c5c5")
        logo_login = customtkinter.CTkImage(Image.open('images/Large_Amazing-Logo-Brand.png'), size=(145, 145))

        # Navigating through windows
        sign_up = Frame(AccountSystem_window)
        sign_in = Frame(AccountSystem_window)
        landing_page = Frame(AccountSystem_window)

        for frame in (landing_page, sign_in, sign_up):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(landing_page)

        # ======================================================================================
        # =================== START PAGE =======================================================
        # ======================================================================================
        landing_page.config(background='#ffffff')


        # ========= START PAGE WIDGETS ===============
        frame = customtkinter.CTkFrame(master=AccountSystem_window, width=450, height=550, corner_radius=15)  # width: 320, height: 360
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Label
        heading_label = customtkinter.CTkLabel(frame, text="Log into your Account", font=('Century Gothic', 20, "bold"))
        heading_label.place(x=119, y=10)

        logo = customtkinter.CTkLabel(master=frame, image=logo_login, text="")
        logo.place(x=150, y=45)

        # Login Button
        login_button = customtkinter.CTkButton(frame, width=220, height=20, text='Login', font=("Century Gothic", 20, "bold"),
                              cursor='hand2', command=lambda: show_frame(sign_in), corner_radius=6)
        login_button.place(x=115, y=270)

        or_lbl = customtkinter.CTkLabel(master=frame, text="or", font=('Century Gothic', 13))
        or_lbl.place(x=219, y=300)

        # Sign Up Button
        signUp_button = customtkinter.CTkButton(frame, width=220, height=20, text='Register', font=("Century Gothic", 20, "bold"),
                               cursor='hand2', command=lambda: show_frame(sign_up), corner_radius=6)
        signUp_button.place(x=115, y=330)


        """def open_admin():
            win = Toplevel()
            C3C3_ECommerce_App.admin_start.FirstPage(win)
            AccountSystem_window.withdraw()
            win.deiconify()"""

        def open_customer(): #NEED TO MAKE FIRSTPAGE class for ECommerce_GUI
            win = Toplevel()
            CSC3_ECommerce_App.ECommerce_GUI.FirstPage(win)
            AccountSystem_window.withdraw()
            win.deiconify()

        # ==========================================================================================================
        # ================================ SIGN IN PAGE ============================================================
        # ==========================================================================================================
        sign_in.config(background='#ffffff')


        # ===== LOGIN FRAME ===== #
        frame2 = customtkinter.CTkFrame(master=sign_in, width=450, height=550, corner_radius=15)
        frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

        heading = customtkinter.CTkLabel(frame2, text="Sign In", font=('Century Gothic', 20, "bold"))
        heading.place(x=190, y=10)

        Username = StringVar()
        Password = StringVar()

        def login_all():
            # Amazing Customer
            conn1 = sqlite3.connect("Database/Amazing.db")

            table_create_query = '''CREATE TABLE IF NOT EXISTS Customer_Account 
                                            (customer_fullname TEXT, customer_username TEXT, customer_password TEXT)'''
            conn1.execute(table_create_query)

            cursor1 = conn1.cursor()
            find_user1 = 'SELECT * FROM Customer_Account WHERE customer_username = ? and customer_password = ?'
            cursor1.execute(find_user1, [(username_entry.get()), (password_entry.get())])

            result1 = cursor1.fetchall()

            if result1:
                messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
                open_customer()
            else:
                messagebox.showerror("Failed", "Wrong Login details, please try again.")

        # ----- USERNAME ----- #
        logo = customtkinter.CTkLabel(master=frame2, image=logo_login, text="")
        logo.place(x=150, y=45)

        username_label = customtkinter.CTkLabel(frame2, text='Username', font=("Century Gothic", 17, "bold"))
        username_label.place(x=180, y=195)
        username_entry = customtkinter.CTkEntry(frame2, width=300, height=27, font=("Arial", 22), textvariable=Username)
        username_entry.place(x=75, y=225)
        #username_entry.configure(highlightbackground="#6b6a69", highlightcolor="black")

        # ----- PASSWORD ----- #
        password_label = customtkinter.CTkLabel(frame2, text='Password', font=("Century Gothic", 17, "bold"))
        password_label.place(x=180, y=270)
        password_entry = customtkinter.CTkEntry(frame2, font=("Arial", 22), width=300, height=27, show="•", textvariable=Password)
        password_entry.place(x=75, y=300)
        #password_entry.configure(highlightbackground="#6b6a69", highlightcolor="black")

        loginButton = customtkinter.CTkButton(frame2, text='Login', width=220, height=20, font=("Century Gothic", 20, "bold"),
                             cursor='hand2', command=login_all)
        loginButton.place(x=115, y=375)

        line = customtkinter.CTkCanvas(frame2, width=300, height=1.5, bg="#e6e6e6", highlightthickness=0)
        line.place(x=75, y=418)
        label = customtkinter.CTkLabel(frame2, text='No Account Yet', font=("", 15,"bold"), text_color='#f9f9f9')
        label.place(x=170, y=405)

        createButton = customtkinter.CTkButton(frame2, text='Create New Account', width=220, height=20, font=("Century Gothic", 20, "bold"),
                              cursor='hand2', command=lambda: show_frame(sign_up))
        createButton.place(x=115, y=435)

        # function for show and hide password
        def password_command():
            if password_entry.cget('show') == "•":
                password_entry.configure(show="")
            else:
                password_entry.configure(show="•")

        # Check Button
        show_password = customtkinter.CTkCheckBox(frame2, text="Show password", command=password_command)
        show_password.deselect()
        show_password.place(x=83, y=340)


        def forgot_password():
            win = Toplevel()
            window_width = 350
            window_height = 350
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            win.title('Forgot Password')
            # win.iconbitmap('images\\aa.ico')
            win.configure(background='#f8f8f8')
            win.resizable(0, 0)

            # Variables
            username = StringVar()
            password = StringVar()
            confirmPassword = StringVar()

            # ====== Email ====================
            username_entry3 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                                    textvariable=username)
            username_entry3.place(x=40, y=30, width=256, height=34)
            username_entry3.config(highlightbackground="black", highlightcolor="black")
            username_label3 = Label(win, text='• Username', fg="#89898b", bg='#f8f8f8',
                                    font=("yu gothic ui", 11, 'bold'))
            username_label2.place(x=40, y=0)

            # ====  New Password ==================
            new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                                       textvariable=password)
            new_password_entry.place(x=40, y=110, width=256, height=34)
            new_password_entry.config(highlightbackground="black", highlightcolor="black")
            new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8',
                                       font=("yu gothic ui", 11, 'bold'))
            new_password_label.place(x=40, y=80)

            # ====  Confirm Password ==================
            confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2
                                           , textvariable=confirmPassword)
            confirm_password_entry.place(x=40, y=190, width=256, height=34)
            confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
            confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                           font=("yu gothic ui", 11, 'bold'))
            confirm_password_label.place(x=40, y=160)

            # ======= Update password Button ============
            update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#ff6c38', font=("", 12, "bold"),
                                 cursor='hand2', activebackground='#ff6c38', command=lambda: change_password())
            update_pass.place(x=40, y=240, width=256, height=50)



            # ========= DATABASE CONNECTION FOR FORGOT PASSWORD=====================
            def change_password():
                db = sqlite3.connect("Database/Amazing.db")
                cur = db.cursor()

                #insert = '''update Guest_Account set guest_password=? where guest_username=? '''
                #cur.execute(insert, [new_password_entry.get(), username_entry3.get(), ])
                #db.commit()
                #db.close()
                #messagebox.showinfo('Congrats', 'Password changed successfully')



        forgotPassword = customtkinter.CTkButton(frame2, text='Forgot password', font=("Century Gothic", 15, "bold"),
                                                 command=lambda: forgot_password(), cursor="hand2")
        forgotPassword.place(x=225, y=337)

        # =============================================================================================================
        # ================================ SIGN UP PAGE ===============================================================
        # =============================================================================================================
        sign_up.config(background='#ffffff')

        frame3 = customtkinter.CTkFrame(master=sign_up, width=450, height=550, corner_radius=15)
        frame3.place(relx=0.5, rely=0.5, anchor=CENTER)

        heading = customtkinter.CTkLabel(frame3, text="Create New Account", font=('Century Gothic', 20, "bold"))
        heading.place(x=125, y=10)

        FullName = StringVar()
        Username2 = StringVar()
        Password2 = StringVar()
        def signup_all():
            check_counter = 0
            warn = ""
            if fullname_entry.get() == "":
                warn = "Please enter your full name"
            else:
                check_counter += 1

            if username_entry2.get() == "":
                warn = "Please enter your username"
            else:
                check_counter += 1

            if password_entry2.get() == "":
                warn = "Please make sure your PASSWORD, USERNAME AND FULLNAME Fields are not empty"
            else:
                check_counter += 1

            if check_counter == 3:
                try:
                    connection = sqlite3.connect("Database/Amazing.db")
                    cur = connection.cursor()
                    cur.execute("INSERT INTO Customer_Account(customer_fullname, customer_username, customer_password) VALUES(?,?,?)",
                                (FullName.get(), Username2.get(), Password2.get()))

                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Success", 'New account created successfully\n\nClick "OK" to continue')
                    open_customer()

                except Exception as ep:
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)


        # ===== Registration Frame ===== #
        #CONTINUE TO REPOSITION GUI

        # ========================================================================
        # ============================Full name====================================
        # ========================================================================
        fullname_label = customtkinter.CTkLabel(frame3, text='Fullname', font=("Century Gothic", 20, "bold"))
        fullname_label.place(x=181, y=80)
        fullname_entry = customtkinter.CTkEntry(frame3, font=("Arial", 22),
                                                width=300, height=27, textvariable=FullName)
        fullname_entry.place(x=79, y=112)
        #fullname_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        # ========================================================================
        # ============================Username====================================
        # ========================================================================
        username_label2 = customtkinter.CTkLabel(frame3, text='Username', font=("Century Gothic", 20, "bold"))
        username_label2.place(x=181, y=165)
        username_entry2 = customtkinter.CTkEntry(frame3, font=("Arial", 22),
                                                 width=300, height=27, textvariable=Username2)
        username_entry2.place(x=79, y=197)
        #username_entry2.configure(highlightbackground="#6b6a69", highlightcolor="black")

        # ========================================================================
        # ============================Password====================================
        # ========================================================================
        password_label2 = customtkinter.CTkLabel(frame3, text='Password', font=("Century Gothic", 20, "bold"))
        password_label2.place(x=181, y=250)
        password_entry2 = customtkinter.CTkEntry(frame3, font=("Arial", 22), show='•',
                                                 width=300, height=27, textvariable=Password2)
        password_entry2.place(x=79, y=282)
        #password_entry2.config(highlightbackground="#6b6a69", highlightcolor="black")

        signupButton = customtkinter.CTkButton(frame3, text='Create Account', font=("Century Gothic", 20, "bold"),
                                               width=220, height=20, cursor='hand2', command=signup_all)
        signupButton.place(x=117, y=370)

        line = customtkinter.CTkCanvas(frame3, width=300, height=1.5, bg="#e6e6e6", highlightthickness=0)
        line.place(x=77, y=413)
        label = customtkinter.CTkLabel(frame3, text='Already have account', font=("", 15, "bold"), text_color='#f9f9f9')
        label.place(x=155, y=400)

        sign_inButton = customtkinter.CTkButton(frame3, text='Login', width=220, height=20,
                                                font=("Century Gothic", 20, "bold"), cursor='hand2',
                                                command=lambda: show_frame(sign_in))
        sign_inButton.place(x=115, y=430)

        # function for show and hide password

        def password_command2():
            if password_entry2.cget('show') == '•':
                password_entry2.configure(show='')
            else:
                password_entry2.configure(show='•')

        # Check Button
        show_password2 = customtkinter.CTkCheckBox(frame3, text="Show password", command=password_command2)
        show_password2.deselect()
        show_password2.place(x=115, y=332)


        #AccountSystem_window.mainloop()

def page():
    window = Tk()
    AccountPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
