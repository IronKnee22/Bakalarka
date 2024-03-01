import customtkinter

class userWindow(customtkinter.CTkToplevel):
    def __init__(self, mainwindow, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

        self.admin_label = customtkinter.CTkLabel(self, text="user")
        self.admin_label.pack(side="top", pady = 10)

        self.home_button = customtkinter.CTkButton(self, text="Hlavní stránka", command= self.back2Main) # button for login
        self.home_button.pack(side="bottom", pady = 10)

        self.mainwindow = mainwindow

    def back2Main(self):
        self.withdraw()
        self.mainwindow.deiconify()