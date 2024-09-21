import customtkinter as ctk
import qrcode
from PIL import ImageTk, Image
import random
import string

# Initializing customtkinter
ctk.set_appearance_mode("dark")          # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")      # Themes: "blue", "green", "dark-blue"




class MultiToolApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        

        self.title("Multi-Tool GUI Based Application")
        self.geometry("1366x768")
        
        
        
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(expand=True, fill="both")

        self.create_tabs()



    def create_tabs(self):
        self.qr_tab = self.tabview.add("QR Generator")
        self.password_tab = self.tabview.add("Password Generator")
        self.temp_tab = self.tabview.add("Temperature Converter")
        self.todo_tab = self.tabview.add("To-Do List")

        self.create_qr_tab()
        self.create_password_tab()
        self.create_temp_tab()
        self.create_todo_tab()

    def create_qr_tab(self):
        ctk.CTkLabel(self.qr_tab,
                     text="Enter the URL/TEXT",
                                             height=30,
                                             width=150,
                                             font=("algerian",44),
                                             text_color=("#000000"),
                                             fg_color=("#66FF99"),
                                             corner_radius=700).pack(pady=10)
        
        self.qr_entry = ctk.CTkEntry(self.qr_tab,
                                     fg_color=("#FFFF66"),
                                     height=50,
                                     text_color=("#000000"),
                                     font=("aptos",24),
                                     corner_radius=25,
                                     width=700,
                                     border_width=10,
                                     border_color="#FF0066")
        self.qr_entry.pack(pady=10)

        self.qr_button = ctk.CTkButton(self.qr_tab, 
                                       text="Generate QR Code",
                                       command=self.generate_qr,
                                       height=20,
                                       width=100,
                                       font=("Georgia",24,'bold'),
                                       text_color=("#000000"),
                                       fg_color=("#FFF176"),
                                       hover_color=("#FF0033"),
                                       border_spacing=30,
                                       corner_radius=100,
                                       border_width=10,
                                       border_color=("#FF0066")).pack(pady=50)
         
        self.qr_image_label = ctk.CTkLabel(self.qr_tab)
        self.qr_image_label.pack(pady=10)

    def generate_qr(self):
        qr_data = self.qr_entry.get()
        if qr_data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4)
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            qr_image = qr.make_image(fill_color='black', back_color='white')
            qr_image = qr_image.resize((400,400))  # Fixed size for QR code
            qr_image.save("qr_code.png")
            img = ImageTk.PhotoImage(qr_image)
            self.qr_image_label.configure(image=img)
            self.qr_image_label.image = img
    def create_password_tab(self):
        ctk.CTkLabel(self.password_tab,
                     text="Enter the Password Length:",
                                             height=30,
                                             width=150,
                                             font=("algerian",44),
                                             text_color=("#000000"),
                                             fg_color=("#66FF99"),
                                             corner_radius=700).pack(pady=50)
        self.password_length_entry = ctk.CTkEntry(self.password_tab,
                                                        fg_color=("#FFCCCC"),
                                                        height=50,
                                                        text_color=("#000000"),
                                                        font=("algerian",24,'bold'),
                                                        corner_radius=25,
                                                        width=200,
                                                        border_color=("#FF0066"))
        self.password_length_entry.pack(pady=10)

        self.password_button = ctk.CTkButton(self.password_tab,
                                             text="Generate Password",
                                             height=20,
                                             width=100,
                                             font=("Bahnschrift",24),
                                             text_color=("#000000"),
                                             fg_color=("#FFF176"),
                                             hover_color=("#66FFCC"),
                                             corner_radius=700,
                                             border_width=10,
                                             border_color=("#FF0066"),
                                             command=self.generate_password)
        self.password_button.pack(pady=10)

        self.password_label = ctk.CTkLabel(self.password_tab)
        self.password_label.pack(pady=10)

    def generate_password(self):
        length = int(self.password_length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.configure(text=f"Generated Password is =  {password}",
                                      font=("algerian",24,'bold','underline'),
                                      text_color="#33FFCC",
                                      fg=("#99FF33"))

    def create_temp_tab(self):
        ctk.CTkLabel(self.temp_tab, 
                                             text="Temperature Converter:",
                                             height=30,
                                             width=150,
                                             font=("algerian",44),
                                             text_color=("#000000"),
                                             fg_color=("#66FF99"),
                                             corner_radius=700).pack(pady=10)
        self.temp_entry = ctk.CTkEntry(self.temp_tab,fg_color=("#FF99CC"),
                                                        height=50,
                                                        text_color=("#000000"),
                                                        font=("algerian",24,'bold'),
                                                        corner_radius=25,
                                                        width=200)
        self.temp_entry.pack(pady=10)

        self.temp_unit_var = ctk.StringVar(value="Celsius")
        ctk.CTkRadioButton(self.temp_tab, text="Celsius to Fahrenheit",font=("Arial",27),text_color=("#00FFFF"),fg_color=("#FF6699"),border_color=("#CC0099"), variable=self.temp_unit_var, value="Celsius").pack(pady=5)
        ctk.CTkRadioButton(self.temp_tab, text="Fahrenheit to Celsius",font=("Arial",27),text_color=("#00FFFF"),fg_color=("#FF6699"),border_color=("#CC0099"),variable=self.temp_unit_var, value="Fahrenheit").pack(pady=5)

        self.temp_button = ctk.CTkButton(self.temp_tab, text="Convert",height=20,
                                             width=100,
                                             font=("Bahnschrift",24),
                                             text_color=("#000000"),
                                             fg_color=("#66FFCC"),
                                             hover_color=("#B71C1C"),
                                             corner_radius=700,
                                             border_width=10,
                                             border_color=("#0066CC"),command=self.convert_temperature)
        self.temp_button.pack(pady=10)

        self.temp_result_label = ctk.CTkLabel(self.temp_tab)
        self.temp_result_label.pack(pady=10)

    def convert_temperature(self):
        temp_value = float(self.temp_entry.get())
        if self.temp_unit_var.get() == "Celsius":
            converted_temp = (temp_value * 9/5) + 32
            result_text = f"{temp_value}°C is {converted_temp:.2f}°F"
        else:
            converted_temp = (temp_value - 32) * 5/9
            result_text = f"{temp_value}°F is {converted_temp:.2f}°C"
        
        self.temp_result_label.configure(text=result_text)

    def create_todo_tab(self):
        ctk.CTkLabel(self.todo_tab, text="To-Do Item:",
                                             height=30,
                                             width=150,
                                             font=("algerian",44),
                                             text_color=("#000000"),
                                             fg_color=("#66FF99"),
                                             corner_radius=700).pack(pady=10)
        self.todo_entry = ctk.CTkEntry(self.todo_tab,fg_color=("#FFCCCC"),
                                                        height=50,
                                                        text_color=("#000000"),
                                                        font=("algerian",24,'bold'),
                                                        corner_radius=25,
                                                        width=200,
                                                        border_color=("#FF0066"))
        self.todo_entry.pack(pady=10)

        self.todo_button = ctk.CTkButton(self.todo_tab, text="Add To-Do",
                                             width=100,
                                             font=("Bahnschrift",24),
                                             text_color=("#000000"),
                                             fg_color=("#66FFCC"),
                                             hover_color=("#B71C1C"),
                                             corner_radius=700,
                                             border_width=10,
                                             border_color=("#0066CC"),
                                             command=self.add_todo)
        self.todo_button.pack(pady=10)

        self.todo_listbox = ctk.CTkTextbox(self.todo_tab,fg_color=("#99FFFF"),text_color=("#000000"),font=("Algerain",15),border_color=("#00FFFF"),width=400, height=300)
        self.todo_listbox.pack(pady=10)

    def add_todo(self):
        todo_item = self.todo_entry.get()
        if todo_item:
            self.todo_listbox.insert("end", todo_item + "\n")
            self.todo_entry.delete(0, 'end')

if __name__ == "__main__":
    app = MultiToolApp()
    app.mainloop()



