import random, tkinter as tk

class App(tk.Tk):
    def __init__(self,title):
        tk.Tk.__init__(self)
        self.title=title
        self.check_capital=False
        self.check_lowercase=False
        self.check_num=False
        self.check_spechar=False
        self.len_pw=0
        self.pw=""
        self.config(bg="black")
        self.run()
    
    def run(self):
        self.backup_pw_E=tk.Entry(self,bg="light grey")
        self.len_pw_E=tk.Entry(self,bg="light grey")

        self.label=tk.Label(self,text="enter the wished length :")

        self.capital_B=tk.Button(self,bg="red",text="Capital",command=self.switch_cap)
        self.lowercase_B=tk.Button(self,bg="red",text="lowercase",command=self.switch_low)
        self.number_B=tk.Button(self,bg="red",text="number",command=self.switch_num)
        self.spechar_B=tk.Button(self,bg="red",text="spechar",command=self.switch_spe)

        self.exit_B=tk.Button(self,text="Exit",command=self.destroy)

        self.generator_B=tk.Button(self,text="generate",command=self.generator)

        self.backup_pw_E.grid(columnspan=2,row=0,sticky="E"+"W")
        self.label.grid(columnspan=2,row=1)
        self.len_pw_E.grid(columnspan=2,row=2,sticky="E"+"W")
        self.generator_B.grid(columnspan=2,row=3,sticky="E"+"W")

        self.capital_B.grid(column=0,row=4,sticky="E"+"W")
        self.lowercase_B.grid(column=1,row=4,sticky="E"+"W")
        self.number_B.grid(column=0,row=5,sticky="E"+"W")
        self.spechar_B.grid(column=1,row=5,sticky="E"+"W")

        self.exit_B.grid(column=1,row=6,sticky="E"+"W")
        

    def switch_cap(self):
        self.check_capital= not self.check_capital
        if self.check_capital:
            self.capital_B.config(bg="green")
        else:
            self.capital_B.config(bg="red")
    
    def switch_low(self):
        self.check_lowercase= not self.check_lowercase
        if self.check_lowercase:
            self.lowercase_B.config(bg="green")
        else:
            self.lowercase_B.config(bg="red")
    
    def switch_num(self):
        self.check_num= not self.check_num
        if self.check_num:
            self.number_B.config(bg="green")
        else:
            self.number_B.config(bg="red")
    
    def switch_spe(self):
        self.check_spechar= not self.check_spechar
        if self.check_spechar:
            self.spechar_B.config(bg="green")
        else:
            self.spechar_B.config(bg="red")
    
    def generator(self):
        self.reset()
        self.len_pw=int(self.len_pw_E.get())
        i=0
        while i<self.len_pw:
            if self.check_capital+self.check_lowercase+self.check_num+self.check_spechar==0:
                break
            loto=random.randrange(0,4)
            if self.check_lowercase and loto==0:
                self.pw+=letter_min[random.randrange(0,len(letter_min))]
            elif self.check_capital and loto==1:
                self.pw+=letter_maj[random.randrange(0,len(letter_maj))]
            elif self.check_num and loto==2:
                self.pw+=nb[random.randrange(0,len(nb))]
            elif self.check_spechar and loto==3:
                self.pw+=spe_char[random.randrange(0,len(spe_char))]
            i=len(self.pw)
            self.backup_pw_E.delete(0,tk.END)
        self.backup_pw_E.insert(0,self.pw)
        file=open("pw_backup.txt","a")
        file.write(self.pw)
        file.write("\n")
        file.close()
        self.reset()
    
    def reset(self):
        self.len_pw=0
        self.pw=""

letter_min="azertyuiopmlkjhgfdsqwxcvbn"
letter_maj="AZERTYUIOPQSDFGHJKLMWXCVBN"
nb="12345678901234567890"
spe_char="&#{[|\"\@]}=+-*/§?<>'(-_)$£*%!.;:,'"

win=App("password generator")
win.mainloop()