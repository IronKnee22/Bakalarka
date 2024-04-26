<<<<<<< HEAD
import sqlite3
import customtkinter
import hashlib

from AdminWindow import adminWindow
from UserWindow import GUI

import time
from PneumoCVUTFBMI.DeviceLoader import DeviceLoader

dl = DeviceLoader()

b1 = dl.getBoard1()
b2 = dl.getBoard2()
b3 = dl.getBoard3()
b4 = dl.getBoard4()
b5 = dl.getBoard5()

b1.on()
b2.on()
b3.on()
b4.on()
b5.on()

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

        self.reject_label = customtkinter.CTkLabel(self, text=" ")
        self.reject_label.pack(side="top")

    def login(self): # function for login
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        hashed_password = hashlib.sha256(self.login_entry.get().encode()).hexdigest()
        cur.execute("SELECT id FROM authorization WHERE password=?", (hashed_password,))
        position = cur.fetchone()
        self.reject_label.configure(text=" ")

        

        if position:
            if position[0] == 1:
                self.toplevel = adminWindow(self,self)
                self.withdraw()
            elif position[0] == 2:
                self.toplevel = GUI(self,self)
                self.withdraw()
        else:
            # Show error message
            self.reject_label.configure(text="Přístup neudělen")
            
            
        


app = App()
app.mainloop()

svaly = {
    0: b1,
    1: b2,
    2: b3,
    3: b4,
    4: b5
}

brokenMuscle = 1

while True:  
    results = [sval.readA0() for sval in svaly.values()]

    all_in_range = all(600 <= result <= 620 for i, result in enumerate(results) if i != brokenMuscle)

    if all_in_range:
        break  

    for i in range(5):
        if i==brokenMuscle:
            continue

        if results[i] >= 620:
            svaly[i].go_backward(20, 10)
        elif results[i] <= 600:
            svaly[i].go_forward(20,10)


=======
import sqlite3
import customtkinter
import hashlib

from AdminWindow import adminWindow
from UserWindow import GUI

import time
from PneumoCVUTFBMI.DeviceLoader import DeviceLoader

dl = DeviceLoader()

b1 = dl.getBoard1()
b2 = dl.getBoard2()
b3 = dl.getBoard3()
b4 = dl.getBoard4()
b5 = dl.getBoard5()

b1.on()
b2.on()
b3.on()
b4.on()
b5.on()

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
        self.bind("<Return>", lambda event: self.login()) 
        
        self.reject_label = customtkinter.CTkLabel(self, text=" ")
        self.reject_label.pack(side="top")

    def login(self): # function for login
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        hashed_password = hashlib.sha256(self.login_entry.get().encode()).hexdigest()
        cur.execute("SELECT id FROM authorization WHERE password=?", (hashed_password,))
        position = cur.fetchone()
        self.reject_label.configure(text=" ")

        

        if position:
            if position[0] == 1:
                self.toplevel = adminWindow(self,self)
                self.withdraw()
            elif position[0] == 2:
                self.toplevel = GUI(self,self)
                self.withdraw()
        else:
            # Show error message
            self.reject_label.configure(text="Přístup neudělen")
            
            
        


app = App()
app.mainloop()

svaly = {
    0: b1,
    1: b2,
    2: b3,
    3: b4,
    4: b5
}

brokenMuscle = 1

while True:  
    results = [sval.readA0() for sval in svaly.values()]

    all_in_range = all(600 <= result <= 620 for i, result in enumerate(results) if i != brokenMuscle)

    if all_in_range:
        break  

    for i in range(5):
        if i==brokenMuscle:
            continue

        if results[i] >= 620:
            svaly[i].go_backward(20, 10)
        elif results[i] <= 600:
            svaly[i].go_forward(20,10)


>>>>>>> bc6dd23de6e6646deb02d6e696f44365a14f1e48
    time.sleep(3)