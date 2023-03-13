import tkinter as tk
import random as rd
import re

LOWERCASE = "azertyuiopqsdfghjklmwxcvbn"
CAPITALIZE = LOWERCASE.upper()
NUMBER = "0123456879"
SPECHAR = "é\"'(-è_çà)=~<>#{[|`\\^@]}¨$£¤ù%*µ,?;.:/!+§"


class UI(tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)

        self.display_menu()

    def set_geometry(self):
        self.update_idletasks()
        width = self.winfo_reqwidth() + 100  # margin E-W
        height = self.winfo_reqheight() + 20  # margin N-S

        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def display_menu(self):
        self.clear()
        frame_menu = tk.Frame(self)
        frame_menu.pack()
        generator_b = tk.Button(frame_menu, text="Generator",
                                command=self.display_generator,
                                width=15
                                )
        history_b = tk.Button(frame_menu, text="Password history",
                              command=self.display_history,
                              width=15
                              )
        generator_b.pack(pady=10)
        history_b.pack(pady=10)

        self.set_geometry()

    def display_history(self):
        self.clear()
        frame_history = tk.Frame(self)
        frame_history.pack()

        data = self.recover_history()

        for line in data:
            frame_line = tk.Frame(frame_history)
            frame_line.pack()
            wording = re.search(r"([a-zA-Z\d]+)(-&:)", line).group(1)
            password = re.search(r"(?:&-)([^ \n]+)", line).group(1)

            label = tk.Label(frame_line, text=f"{wording} : ")
            label.pack(side="left")

            text = tk.Text(frame_line,
                           width=int(len(password)/(((len(password)) > 50)+1)),
                           height=1+(len(password) > 50)
                           )
            text.insert("1.0", password)
            text.pack(side="left")

        back_B = tk.Button(self, text="Return", command=self.display_menu)
        back_B.pack(side="bottom")

        self.set_geometry()

    def display_generator(self):
        self.clear()

        frame_body = tk.Frame(self)
        frame_body.pack()

        self.pw_text = tk.Text(frame_body, width=34, height=3)
        self.pw_text.grid(row=0, column=0, columnspan=2, sticky="nsew")

        label_length = tk.Label(frame_body, text="length :", width=10)
        label_length.grid(row=1, column=0)

        pw_length = tk.StringVar(frame_body)
        self.spinbox = tk.Spinbox(frame_body, textvariable=pw_length, from_=5,
                                  to=100, width=10)
        self.spinbox.grid(row=1, column=1)

        self.lowercase_L = tk.Label(frame_body,
                                    text="Lower case",
                                    relief="raised",
                                    bg="green",
                                    width=10)
        self.capitalize_L = tk.Label(frame_body,
                                     text="Capitalize",
                                     relief="raised",
                                     bg="green",
                                     width=10)
        self.Number_L = tk.Label(frame_body,
                                 text="Number",
                                 relief="raised",
                                 bg="green",
                                 width=10)
        self.spechar_L = tk.Label(frame_body,
                                  text="Special Char",
                                  relief="raised",
                                  bg="green",
                                  width=10)

        self.lowercase_L.grid(row=2, column=0, sticky="nsew")
        self.capitalize_L.grid(row=2, column=1, sticky="nsew")
        self.Number_L.grid(row=3, column=0, sticky="nsew")
        self.spechar_L.grid(row=3, column=1, sticky="nsew")

        self.lowercase_L.bind("<Button-1>", self.toggle_label_color)
        self.capitalize_L.bind("<Button-1>", self.toggle_label_color)
        self.Number_L.bind("<Button-1>", self.toggle_label_color)
        self.spechar_L.bind("<Button-1>", self.toggle_label_color)

        generate_B = tk.Button(frame_body, text="Generate",
                               command=self.validate_password_input)
        generate_B.grid(row=4, column=0, sticky="nesw")

        save_B = tk.Button(frame_body, text="Save", command=self.save_password)
        save_B.grid(row=4, column=1, sticky="nesw")

        frame_footer = tk.Frame(self)
        frame_footer.pack()

        self.label = tk.Label(frame_footer, text="Wording : ")
        self.wording_E = tk.Entry(frame_footer)

        back_B = tk.Button(self, text="Return", command=self.display_menu)
        back_B.pack(side="bottom")

        self.set_geometry()

    def display_save(self):
        self.label.pack()
        self.wording_E.pack()

        self.set_geometry()

    def save_password(self):
        if self.wording_E.winfo_ismapped():
            password = self.pw_text.get("1.0", tk.END)
            password = password.replace("\n", "")
            wording = self.wording_E.get()
            regex = r"^[^ \n&]{5,100}$"
            if re.search(r"^[a-zA-Z\d]+$", wording) is not None:
                if re.search(regex, password) is not None:
                    with open("data/data.txt", "a") as file:
                        file.write(f"{wording}-&: &-{password}\n")
                    self.display_generator()
        else:
            self.display_save()

    def toggle_label_color(self, evt) -> None:
        label = evt.widget
        current_color = label.cget("background")

        if current_color == "green":
            label.config(background="red")
        else:
            label.config(background="green")

    def validate_password_input(self):
        try:
            length = int(self.spinbox.get())
        except Exception:
            pass
        lowercase_bool = (self.lowercase_L.cget("background") == "green")
        capitalize_bool = (self.capitalize_L.cget("background") == "green")
        number_bool = (self.Number_L.cget("background") == "green")
        spechar_bool = (self.spechar_L.cget("background") == "green")

        if 5 <= length <= 100:
            self.pw_text.delete("1.0", "end")
            password = self.generate_password(length,
                                              lowercase_bool,
                                              capitalize_bool, number_bool,
                                              spechar_bool
                                              )
            self.pw_text.insert("end", password)

    def generate_password(self, length, lower_case, capitalize, number,
                          spe_char) -> str:
        password = ""

        while len(password) < length:

            percent = rd.randrange(0, 100) % 4

            match percent:
                case 0:
                    if lower_case:
                        password += rd.choice(LOWERCASE)
                case 1:
                    if capitalize:
                        password += rd.choice(CAPITALIZE)
                case 2:
                    if number:
                        password += rd.choice(NUMBER)
                case 3:
                    if spe_char:
                        password += rd.choice(SPECHAR)

        return password

    def recover_history(self):
        with open("data/data.txt", "r") as file:
            data = file.readlines()
            return data

    def clear(self):
        for widget in self.winfo_children():
            widget.pack_forget()
