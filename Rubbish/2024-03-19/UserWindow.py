import time
import customtkinter
import re
from tkinter import messagebox

import sqlite3

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

maxHodnotaSvalu = 700
minHodnotaSvalu = 550

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class LeftFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="left frame")
        self.label.grid(row=0, column=0, padx=10)

        self.button1 = customtkinter.CTkButton(
            self, text="Akce 1", command=self.button_event)
        self.button1.grid(row=1, column=0, padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(
            self, text="Akce 2", command=self.button_event)
        self.button2.grid(row=2, column=0, padx=10, pady=10)

        self.button3 = customtkinter.CTkButton(
            self, text="Akce 3", command=self.button_event)
        self.button3.grid(row=3, column=0, padx=10, pady=10)

        self.button4 = customtkinter.CTkButton(
            self, text="Akce 4", command=self.button_event)
        self.button4.grid(row=4, column=0, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(self, text=" ")
        self.label2.grid(row=5, column=0, padx=10)

        self.label1 = customtkinter.CTkLabel(self, text=" ")
        self.label1.grid(row=6, column=0, padx=10)

        self.label = customtkinter.CTkLabel(self, text=" ")
        self.label.grid(row=7, column=0, padx=10)

        self.label_switch = customtkinter.CTkLabel(
            self, text="Light/Dark Mode")
        self.label_switch.grid(row=8, column=0, padx=10)

        self.switch = customtkinter.CTkSwitch(self, text="Light Mode", command=self.switch_event,
                                              onvalue="on", offvalue="off")
        self.switch.grid(row=10, column=0, padx=10)



    def switch_event(self):
        if (self.switch.get() == "on"):
            customtkinter.set_appearance_mode("dark")
            self.switch.configure(text="Dark Mode")
        else:
            customtkinter.set_appearance_mode("light")
            self.switch.configure(text="Light Mode")

    def button_event(self):
        print("Akce")


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        global maxHodnotaSvalu
        global minHodnotaSvalu
        global sklon
        global posun
        global aktualni_poz
        aktualni_poz = [0,0,0,0,0]

        # ?první sloupec

        self.label_sval1 = customtkinter.CTkLabel(self, text="sval1")
        self.label_sval1.grid(row=1, column=0, padx=20)

        self.progressbar1 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar1.grid(row=2, column=0, padx=20)
        self.progressbar1.set((b1.readA0()-minHodnotaSvalu)/(maxHodnotaSvalu-minHodnotaSvalu))



        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="entry")
        self.entry1.configure(validate='focusout', validatecommand=(self.register(self.validate_1), '%P'))
        self.entry1.grid(row=3, column=0, padx=20, pady=10)

        self.label_sval3 = customtkinter.CTkLabel(self, text="sval3")
        self.label_sval3.grid(row=7, column=0, padx=20)

        self.progressbar3 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar3.grid(row=8, column=0, padx=20)
        self.progressbar3.set((b3.readA0()-minHodnotaSvalu)/(maxHodnotaSvalu-minHodnotaSvalu))

        self.entry3 = customtkinter.CTkEntry(self, placeholder_text="entry3")
        self.entry3.configure(validate='focusout', validatecommand=(self.register(self.validate_3), '%P'))
        self.entry3.grid(row=9, column=0, padx=20, pady=10)

        # ?druhý sloupec
        self.label = customtkinter.CTkLabel(self, text="main frame")
        self.label.grid(row=0, column=1, padx=20)

        self.label_sval5 = customtkinter.CTkLabel(self, text="sval5")
        self.label_sval5.grid(row=4, column=1, padx=20)

        self.progressbar5 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar5.grid(row=5, column=1, padx=20)
        self.progressbar5.set((b5.readA0()-minHodnotaSvalu)/(maxHodnotaSvalu-minHodnotaSvalu))

        self.entry5 = customtkinter.CTkEntry(self, placeholder_text="entry5")
        self.entry5.configure(validate='focusout', validatecommand=(self.register(self.validate_5), '%P'))
        self.entry5.grid(row=6, column=1, padx=20, pady=10)

        self.button = customtkinter.CTkButton(
            self, text="Spustit", command=self.button_event)
        self.button.grid(row=10, column=1, padx=20, pady=10)

        # ?třetí sloupec
        self.label_sval2 = customtkinter.CTkLabel(self, text="sval2")
        self.label_sval2.grid(row=1, column=2, padx=20)

        self.progressbar2 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar2.grid(row=2, column=2, padx=20)
        self.progressbar2.set((b2.readA0()-minHodnotaSvalu)/(maxHodnotaSvalu-minHodnotaSvalu))

        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="entry2")
        self.entry2.configure(validate='focusout', validatecommand=(self.register(self.validate_2), '%P'))
        self.entry2.grid(row=3, column=2, padx=20, pady=10)

        self.label_sval4 = customtkinter.CTkLabel(self, text="sval4")
        self.label_sval4.grid(row=7, column=2, padx=20)

        self.progressbar4 = customtkinter.CTkProgressBar(
            self, orientation="horizontal")
        self.progressbar4.grid(row=8, column=2, padx=20)
        self.progressbar4.set((b4.readA0()-minHodnotaSvalu)/(maxHodnotaSvalu-minHodnotaSvalu))

        self.entry4 = customtkinter.CTkEntry(self, placeholder_text="entry4")
        self.entry4.configure(validate='focusout', validatecommand=(self.register(self.validate_4), '%P'))
        self.entry4.grid(row=9, column=2, padx=20, pady=10)

    def validate_1(self, value):
        pattern = r'^\d+$'  # Regulární výraz přijímající pouze čísla
        if re.fullmatch(pattern, value) is None:
            messagebox.showerror("Chybný vstup", "Prosím, zadejte pouze čísla. \nVstup nesmí být prázdný.")
            self.entry1.delete(0, customtkinter.END)            
            return False
        else:
            return True
    
    def validate_2(self, value):
        pattern = r'^\d+$'  # Regulární výraz přijímající pouze čísla
        if re.fullmatch(pattern, value) is None:
            messagebox.showerror("Chybný vstup", "Prosím, zadejte pouze čísla. \nVstup nesmí být prázdný.")
            self.entry2.delete(0, customtkinter.END)            
            return False
        else:
            return True
    
    def validate_3(self, value):
        pattern = r'^\d+$'  # Regulární výraz přijímající pouze čísla
        if re.fullmatch(pattern, value) is None:
            messagebox.showerror("Chybný vstup", "Prosím, zadejte pouze čísla. \nVstup nesmí být prázdný.")
            self.entry3.delete(0, customtkinter.END)            
            return False
        else:
            return True
    
    def validate_4(self, value):
        pattern = r'^\d+$'  # Regulární výraz přijímající pouze čísla
        if re.fullmatch(pattern, value) is None:
            messagebox.showerror("Chybný vstup", "Prosím, zadejte pouze čísla. \nVstup nesmí být prázdný.")
            self.entry4.delete(0, customtkinter.END)            
            return False
        else:
            return True
    
    def validate_5(self, value):
        pattern = r'^\d+$'  # Regulární výraz přijímající pouze čísla
        if re.fullmatch(pattern, value) is None:
            messagebox.showerror("Chybný vstup", "Prosím, zadejte pouze čísla. \nVstup nesmí být prázdný.")
            self.entry5.delete(0, customtkinter.END)            
            return False
        else:
            return True

    def button_event(self):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        
        sval1= self.entry1.get()
        sval2= self.entry2.get()
        sval3= self.entry3.get()
        sval4= self.entry4.get()
        sval5= self.entry5.get()

        if radio_var.get() == 0:
            messagebox.showerror("Chybí sval", "Prosím vyber sval")
        
        if self.validate_1(sval1) and self.validate_2(sval2) and self.validate_3(sval3) and self.validate_4(sval4) and self.validate_5(sval5) and radio_var.get() !=0:

            radio_value = radio_var.get()
            entry_values = [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get()]
            entry_values = [0 if not value else value for value in entry_values]

            

            if radio_value == 1:
                #rovnice = hodnoty_mm
                jednotka = "mm"
            elif radio_value == 2:
                #rovnice = hodnoty_mbar
                prepocet_jednotka = "mV2bar"
                jednotka = "mbar"
            elif radio_value == 3:                
                jednotka = "mv"


            results = []

            svaly = {
                0: b1,
                1: b2,
                2: b3,
                3: b4,
                4: b5
            }

            for index, entry in enumerate(entry_values, start=1):

                cur.execute(f"SELECT sval{index}_{jednotka} FROM sval{index}")
                cislo_vzorce = cur.fetchone()
                cur.execute(f"SELECT * FROM sval{index}_{jednotka} WHERE id IN ({int(cislo_vzorce[0])})")
                rovnice = cur.fetchall()
            

                if radio_value == 4: #pokud dělám jenom kroky tak nemusím nic počítat
                    result = int(entry)

                else:

                    akt_hod_mV = svaly[index-1].readA0() #získání aktuální hodnoty v mV 

                    if entry !=0:

                        if radio_value == 3:
                            start_hodnta = akt_hod_mV 
                        elif radio_value == 1: #! z mV Na mm
                            start_hodnta = akt_hod_mV #převedení hodnoty na správné jednotky
                        elif radio_value == 2: #! z mV na mbar
                            cur.execute(f"SELECT * FROM sval{index}_{prepocet_jednotka} WHERE id IN ({int(cislo_vzorce[0])})")
                            prepocet = cur.fetchall()
                            sklon = prepocet[0][1]
                            posun = prepocet[0][2]
                            start_hodnta =sklon * akt_hod_mV + posun #převedení hodnoty na správné jednotky

                        konecna_hodnota = float(start_hodnta) + float(entry)  #získání hodnoty na kterou se chceme dostat pomocí startovní + posunu

                        sklon = rovnice[0][1]
                        posun = rovnice[0][2]

                        kon_kroky = (konecna_hodnota - posun) / sklon #přepočet na kroky
                        start_kroky = float((start_hodnta - posun) / sklon) #přepočet na kroky

                        result = kon_kroky - start_kroky #spočítání nutných kroků
                    else:
                        result = 0
                aktualni_poz[index-1] += result
                results.append(result)





            progressbars = [self.progressbar1, self.progressbar2, self.progressbar3, self.progressbar4, self.progressbar5]

            for i in range(5):
                if results[i] > 0:
                    svaly[i].go_forward(10, results[i])
                    #time.sleep(2)
                elif results[i] < 0:
                    svaly[i].go_backward(10, -results[i])
            time.sleep(3)
            for i in range(5):
                print(svaly[i].readA0())
                b = (svaly[i].readA0() - minHodnotaSvalu) / (maxHodnotaSvalu - minHodnotaSvalu)
                progressbars[i].set(b)
    


class RightFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global radio_var

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="right frame")
        self.label.grid(row=0, column=0, padx=20)

        radio_var = customtkinter.IntVar(value=0)
        self.radiobutton_1 = customtkinter.CTkRadioButton(self, text="mm",
                                                          command=self.radiobutton_event, variable=radio_var, value=1)
        self.radiobutton_1.grid(row=1, column=0, padx=20, pady=10)

        self.radiobutton_2 = customtkinter.CTkRadioButton(self, text="mbar",
                                                          command=self.radiobutton_event, variable=radio_var, value=2)
        self.radiobutton_2.grid(row=2, column=0, padx=20, pady=10)

        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="mV",
                                                          command=self.radiobutton_event, variable=radio_var, value=3)
        self.radiobutton_3.grid(row=3, column=0, padx=20, pady=10)

        self.radiobutton_3 = customtkinter.CTkRadioButton(self, text="kroky",
                                                          command=self.radiobutton_event, variable=radio_var, value=4)
        self.radiobutton_3.grid(row=4, column=0, padx=20, pady=10)

        self.back2Main_button = customtkinter.CTkButton(self, text="Main", command= master.back2Main) # button for login
        self.back2Main_button.grid(row=7, column=0, padx=20, pady=10)


    def radiobutton_event(self):
        print("radiobutton toggled, current value:", radio_var.get())


class GUI(customtkinter.CTkToplevel):
    def __init__(self, mainwindow, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set window size
        width = 1060
        height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        screen_x = (screen_width - width) // 2
        screen_y = (screen_height - height) // 2

        # Set size a place parametrs
        self.geometry(f"{width}x{height}+{screen_x}+{screen_y}")
        

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.left_frame = LeftFrame(master=self)
        self.left_frame.grid(row=0, column=0, pady=20, sticky="nsew")

        self.main_frame = MainFrame(master=self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.right_frame = RightFrame(master=self)
        self.right_frame.grid(row=0, column=2, pady=20, sticky="nsew")

        print(b1.readA0())
        print(b2.readA0())
        print(b3.readA0())
        print(b4.readA0())
        print(b5.readA0())

        self.mainwindow = mainwindow

    def back2Main(self):
        self.withdraw()
        self.mainwindow.deiconify()







