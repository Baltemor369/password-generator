import tkinter as tk
import random as rd
import re

LOWERCASE = "azertyuiopqsdfghjklmwxcvbn"
CAPITALIZE = LOWERCASE.upper()
NUMBER = "0123456879"
SPECHAR = "&é\"'(-è_çà)=~#{[|`\\^@]}¨$£¤ù%*µ,?;.:/!+§"


class UI(tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)

        self.display_generator()

    def display_history(self):
        pass

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

        self.label = tk.Label(self, text="Wording : ")
        self.wording_E = tk.Entry(self)

    def display_save(self):
        self.label.pack()
        self.wording_E.pack()

    def save_password(self):
        if self.wording_E.winfo_ismapped():
            password = self.pw_text.get("1.0", tk.END)
            password = password.replace("\n", "")
            wording = self.wording_E.get()
            regex = r"^[^ \n]{5,100}$"
            if re.search(r"^[a-zA-Z\d]+$", wording) is not None:
                if re.search(regex, password) is not None:
                    with open("data/data.txt", "a") as file:
                        file.write(f"{wording}: {password}\n")
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

    def clear(self):
        for widget in self.winfo_children():
            widget.pack_forget()
