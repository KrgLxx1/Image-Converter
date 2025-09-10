from customtkinter import *
from tkinter import messagebox, filedialog
from PIL import Image

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def clear_entry():
    log = login_entry
    pas = password_entry

    log.delete(0, END)
    pas.delete(0, END)

def log_in():
    users = [('Hatred', "6683"), ('kirobotse', '2010'), ('pidor', 'я')]

    log = login_entry.get()
    pas = password_entry.get()

    if log != "" and pas != "":
        info = (log, pas)
        if info in users:
            messagebox.showinfo("Успешно!", f"Добро пожаловать, {log}")
            clear_entry()
            root.destroy()
            main_window()
        else:
            messagebox.showerror("Ошибка", "Не правильно имя или пароль")
            clear_entry()
    else:
        messagebox.showerror("Ошибка", "Введите имя или пароль!")

current_file = None

def choose_file():
    global current_file
    file_types = [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]

    file_name = filedialog.askopenfilename(
        title="Choose an Image",
        initialdir='/',
        filetypes=file_types
    )

    if file_name != "":
        current_file = file_name
        ChooseFile.configure(text=f'{file_name}')
        ConvertComboBox.configure(state='normal')
        ConvertBut.configure(state='normal')
        return file_name
    
    return None
    

def convert_into():
    global current_file
    if not current_file:
        messagebox.showerror("Ошибка", "Сначала выберите файл!")
        return
    
    nameOfFile = GiveName.get().strip()
    if not nameOfFile:
        messagebox.showwarning("Не удалось", "Вам надо дать название конвертированного файла.")
        return

    get_option = ConvertComboBox.get().replace(".", "").upper()
    if get_option == "JPG":
        get_option = "JPEG"

    try:
        ConvertBut.configure(state="disabled")
        image = Image.open(current_file)
        dir_path = os.path.dirname(current_file)
        save_name = os.path.join(dir_path, f"{nameOfFile}.{get_option.lower()}")
        image.save(save_name, get_option)

        messagebox.showinfo("Успех", f"Файл успешно конвертирован в {get_option}!\n{save_name}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось конвертировать:\n{e}")
    finally:
        ConvertBut.configure(state="normal")



def main_window():
    global ChooseFile, ConvertComboBox, ConvertBut, GiveName
    root = CTk()
    root.geometry("800x450")
    root.title("Панель Управления")
    root.config(background="#165985")
    root.resizable(False, False)
    root.iconbitmap('icon2.ico')
    center_window(root)
    root.grid_columnconfigure(0, weight=1)


    Title = CTkLabel(root, text="Панель Управления", bg_color="#165985", fg_color="transparent", text_color="white", font=("Arial", 32, "bold"))
    Title.grid(row=0, column=0, padx=8, pady=8, sticky='n')

    ChosFileLabel = CTkLabel(root, text="Выберите файл", bg_color="#165985", fg_color="transparent", text_color="#0C456B", font=("Arial", 24, "bold"))
    ChosFileLabel.grid(row=1, column=0, padx=8, pady=8, sticky='n')

    ChooseFile = CTkButton(root, text="...", text_color="#0C456B", bg_color='#165985', corner_radius=30, font=("Arial", 24, "bold"), command=choose_file)
    ChooseFile.grid(row=2, column=0, padx=8, pady=8, sticky='ew')

    ChosFileLabel = CTkLabel(root, text="Выберите во что конвертировать", bg_color="#165985", fg_color="transparent", text_color="#0C456B", font=("Arial", 24, "bold"))
    ChosFileLabel.grid(row=3, column=0, padx=8, pady=8, sticky='n')

    ConvertComboBox = CTkComboBox(root, text_color="white", bg_color='#165985', fg_color='#165985', border_color="#145179", corner_radius=30, font=('Arial', 16), state=DISABLED, justify='center', values=(".ico", ".jpg", ".png", ".webp", ".bmp", ".svg"))
    ConvertComboBox.grid(row=4, column=0, padx=8, pady=8, sticky='ew')

    GiveName = CTkEntry(root, placeholder_text="Придумайте название конвертированного файла",text_color="white", bg_color='#165985', fg_color='#165985', border_color="#145179", corner_radius=30, font=('Arial', 16), state=NORMAL, justify='center')
    GiveName.grid(row=5, column=0, padx=8, pady=8, sticky='ew')

    ConvertBut = CTkButton(root, text="Конвертировать", text_color="#0C456B", bg_color='#165985', corner_radius=30, font=("Arial", 24, "bold"), command=convert_into)
    ConvertBut.grid(row=6, column=0, padx=8, pady=8, sticky='n')
    ConvertBut.configure(state='disabled')
    root.mainloop()

def login_window():
    global root, login_entry, password_entry
    root = CTk()
    root.geometry("400x250")
    root.title("Авторизация")
    root.config(background="#0D171C")
    root.resizable(False, False)
    root.iconbitmap('icon.ico')
    center_window(root)

    root.grid_columnconfigure(0, weight=1)

    # Логин
    login_label = CTkLabel(
        root,
        text="Логин",
        fg_color="#0D171C",
        font=("Arial", 20, "bold"),
        text_color="white"
    )
    login_label.grid(row=0, column=0, pady=(40, 6), sticky="n")

    login_entry = CTkEntry(
        root,
        placeholder_text="Введите логин",
        width=250,
        font=("Arial", 16),
        border_color="#16262E",
        bg_color='#0D171C',
        fg_color="#0D171C",
        corner_radius=30,
        justify='center'
    )
    login_entry.grid(row=1, column=0, pady=(0, 20), sticky="n")

    # Пароль
    password_label = CTkLabel(
        root,
        text="Пароль",
        fg_color="transparent",
        font=("Arial", 20, "bold"),
        bg_color="#0D171C",
        text_color="white",
        corner_radius=30
    )
    password_label.grid(row=2, column=0, pady=(0, 6), sticky="n")

    password_entry = CTkEntry(
        root,
        placeholder_text="Введите пароль",
        width=250,
        font=("Arial", 16),
        show="*",
        corner_radius=30,
        border_color="#16262E",
        fg_color="#0D171C",
        justify='center',
        bg_color='#0D171C'
    )
    password_entry.grid(row=3, column=0, pady=(0, 20), sticky="n")

    enter_button = CTkButton(root, text="Войти", text_color="white", fg_color="#0D171C", font=("Arial", 24, "bold"), hover_color="#16242B", bg_color='#0D171C', command=log_in)
    enter_button.grid(row=4, column=0, pady=(0, 20), sticky='n')

    root.mainloop()



if __name__ == "__main__":
    login_window()