import tkinter as tk
import module.useful_fct as use
from module.pwGen import GenPw
import re

BG = "#333333"
FG = "#FFFFFF"
FONT10 = ("Helvetica",10)
FONT20 = ("Helvetica",20)

L10PARAM = {
    "bg" : BG,
    "fg" : FG,
    "font" : ("Helvetica",10)
}
L20PARAM = {
    "bg" : BG,
    "fg" : FG,
    "font" : ("Helvetica",20)
}
BPARAM = {
    "bg" : "#555555",
    "fg" : FG,
    "font" : ("Helvetica",10),
    "relief" : "raised",
}
EPARAM = {
    "bg" : "#555555",
    "fg" : FG,
    "font" : ("Helvetica",10),
}
PACK = {
    "padx" : 8,
    "pady" : 8
}

class UI():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.config(bg=BG)
        self.root.iconbitmap("assets/cadenas.ico")
        self.root.bind("<Escape>", self.exit)
        self.generator = GenPw()
        self.generated_pw = "Generate a password"

        self.display_menu()

    def display_menu(self):
        use.clear(self.root)
        
        title = tk.Label(self.root, text="Password Generator", **L20PARAM)
        title.pack()

        buttonFrame = tk.Frame(self.root, bg=BG)
        buttonFrame.pack()

        sub1Frame = tk.Frame(buttonFrame, bg=BG)
        sub1Frame.pack(side="left")

        self.lower_B = tk.Label(sub1Frame, text="Lowercase", bg="#00DD00", fg="#000000", width=10)
        self.lower_B.bind("<Button-1>", self.toggle_label_color)
        self.lower_B.pack(**PACK)
        self.upper_B = tk.Label(sub1Frame, text="Uppercase", bg="#00DD00", fg="#000000", width=10)
        self.upper_B.bind("<Button-1>", self.toggle_label_color)
        self.upper_B.pack(**PACK)

        sub2Frame = tk.Frame(buttonFrame, bg=BG)
        sub2Frame.pack(side="right")

        self.digit_B = tk.Label(sub2Frame, text="Digit", bg="#00DD00", fg="#000000", width=10)
        self.digit_B.bind("<Button-1>", self.toggle_label_color)
        self.digit_B.pack(**PACK)
        self.punct_B = tk.Label(sub2Frame, text="Special char", bg="#00DD00", fg="#000000", width=10)
        self.punct_B.bind("<Button-1>", self.toggle_label_color)
        self.punct_B.pack(**PACK)

        lengthFrame = tk.Frame(self.root, bg=BG)
        lengthFrame.pack()

        subLeftFrame = tk.Frame(lengthFrame, bg=BG)
        subLeftFrame.pack(side="left")

        length_L = tk.Label(subLeftFrame, text="Length :", **L10PARAM)
        length_L.pack(side="right")

        subRightFrame = tk.Frame(lengthFrame, bg=BG)
        subRightFrame.pack(side="right")

        self.legnth_E = tk.Entry(subRightFrame, **EPARAM)
        self.legnth_E.insert(0, "10")
        self.legnth_E.pack(side="left", **PACK)

        genFrame = tk.Frame(self.root, bg=BG)
        genFrame.pack(fill="x", expand=True)

        generate_B = tk.Button(genFrame, text="Generate", **BPARAM, width=10, command=self.generation)
        generate_B.pack(**PACK)

        self.result_L = tk.Entry(genFrame, **EPARAM, width=30)
        self.result_L.insert(0, self.generated_pw)
        self.result_L.pack(fill="x", expand=True, **PACK)

        saveFrame = tk.Frame(self.root, bg=BG)
        saveFrame.pack()

        sub10Frame = tk.Frame(saveFrame, bg=BG)
        sub10Frame.pack(fill="x",expand=True, side="left")

        save_L = tk.Label(sub10Frame, text="Label : ", **L10PARAM)
        save_L.pack()

        sub11Frame = tk.Frame(saveFrame, bg=BG)
        sub11Frame.pack(fill="x",expand=True, side="left")

        self.save_E = tk.Entry(sub11Frame, **EPARAM)
        self.save_E.insert(0, "ID tag")
        self.save_E.bind("<Return>", self.save)
        self.save_E.pack()

        sub12Frame = tk.Frame(saveFrame, bg=BG)
        sub12Frame.pack(fill="x",expand=True, side="left")

        save_B = tk.Button(sub12Frame, text="Save", **BPARAM, command=self.save)
        save_B.pack(padx=10)

        botFrame = tk.Frame(self.root, bg=BG)
        botFrame.pack(fill="x", expand=True)

        sub20Frame = tk.Frame(botFrame, bg=BG)
        sub20Frame.pack(fill="x", expand=True)

        history_B = tk.Button(sub20Frame, text="History", **BPARAM, command=self.history_display)
        history_B.pack()

        sub21Frame = tk.Frame(botFrame, bg=BG)
        sub21Frame.pack(fill="x", expand=True)

        exit_B = tk.Button(sub21Frame, text="Exit", **BPARAM, command=self.exit)
        exit_B.pack(side="right")

        use.set_geometry(self.root, 100, 50)

    def history_display(self):
        use.popup(self.root, self.generator.get(),"History",font=FONT10)

    def generation(self):
        self.generator.set_attr((self.lower_B.cget("bg")=="#00DD00"),(self.upper_B.cget("bg")=="#00DD00"),(self.digit_B.cget("bg")=="#00DD00"),(self.punct_B.cget("bg")=="#00DD00"))
        try:
            length = int(self.legnth_E.get())
        except:
            length = 10
        self.generated_pw = self.generator.generate_pw(length)
        self.result_L.delete(0,"end")
        self.result_L.insert(0,self.generated_pw)

    def save(self, e=None):
        pw = self.result_L.get()
        tag = re.match("^[a-zA-Z0-9]+$",self.save_E.get())
        if tag is not None:
            self.generator.save_pw(pw,tag[0])
            use.popup(self.root,"Password Saved Successful", "Save Message", BG, FG, FONT10)
        else:
            use.popup(self.root,"Password Saved Failed", "Save Message", BG, FG, FONT10)

    def toggle_label_color(self, evt) -> None:
        label = evt.widget
        current_color = label.cget("background")

        if current_color == "#00DD00":
            label.config(bg="#DD0000")
        else:
            label.config(bg="#00DD00")

    def run(self):
        self.root.mainloop()

    def exit(self, e=None):
        self.root.destroy()