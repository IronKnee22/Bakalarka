import sqlite3
import customtkinter
import hashlib

from AdminWindow import adminWindow
from UserWindow import GUI

class App(customtkinter.CTk):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)

        # Set window size
        width = 300
        height = 150
        
        # Automatic calculation position of window based on monitor size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        screen_x = (screen_width - width) // 2
        screen_y = (screen_height - height) // 2

        # Set size a place parametrs
        self.geometry(f"{width}x{height}+{screen_x}+{screen_y}")

        
        self.toplevel = None

        self.login_entry = customtkinter.CTkEntry(self,placeholder_text="Heslo", show= "*") # entry for login
        self.login_entry.pack(side="top", pady = 20)

        self.login_button = customtkinter.CTkButton(self, text="Přihlášení", command= self.login) # button for login
        self.login_button.pack(side="top", pady = 10)
        self.bind("<Return>", lambda event: self.login()) # it works on enter FUCK YES

    def login(self): # function for login
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        hashed_password = hashlib.sha256(self.login_entry.get().encode()).hexdigest()
        cur.execute("SELECT id FROM authorization WHERE password=?", (hashed_password,))
        position = cur.fetchone()

        if position:
            if position[0] == 1:
                self.toplevel = adminWindow(self,self)
                self.withdraw()
            elif position[0] == 2:
                self.toplevel = GUI(self,self)
                self.withdraw()
        else:
            # Show error message
            self.reject_label = customtkinter.CTkLabel(self, text="Přístup neudělen")
            self.reject_label.pack(side="top")
        


app = App()
app.mainloop()