import string
import random

LOWERCASE = string.ascii_lowercase
CAPITALIZE = string.ascii_uppercase
NUMBER = string.digits
SPECHAR = string.punctuation

class GenPw:
    def __init__(self) -> None:
        self.password_dict = {}
        self.with_lower = True
        self.with_upper = True
        self.with_nb = True
        self.with_punct = True
        self.data_path = "data.txt"
        try:
            # try to read the file at the given path
            with open(self.data_path, 'r') as file:
                pass
        except FileNotFoundError:
            # if not found create a data file
            with open("data.txt", 'w') as file:
                pass
        
        self.load_passwords()

    def generate_pw(self, length:int) -> str:
        if length <= 0:
            return ""
        characters = ""
        if self.with_lower:
            characters += LOWERCASE
        if self.with_upper:
            characters += CAPITALIZE
        if self.with_nb:
            characters += NUMBER
        if self.with_punct:
            characters += SPECHAR
        if characters == "":
            return ""
        char_list = list(characters)
        for i in range(5):
            random.shuffle(char_list)
        characters = ''.join(char_list)

        password = ''.join(random.choice(characters) for _ in range(length))
        
        return password
    
    def set_attr(self, lower:bool, upper:bool, numb:bool, punct:bool):
        self.with_lower = lower
        self.with_upper = upper
        self.with_nb = numb
        self.with_punct = punct

    def save_pw(self, password:str, key:str):
        with open(self.data_path, 'a') as file:
            file.write(f"§{key} {password}")
        
        self.load_passwords()
    
    def load_passwords(self):
        with open(self.data_path, 'r') as file:
            self.password_dict = self.read_DB(file.read()).copy()
    
    def read_DB(self, text:str) -> dict:
        password_dict = {}
        if text!="":
            buffer = text.split("§")
            buffer.pop(0)
            for e in buffer:
                tmp = e.split(" ")
                password_dict[tmp[0]] = tmp[1]
            
        return password_dict

    
    def clear_DB(self):
        with open(self.data_path, "w") as file:
            file.write("")
    
    def get(self) -> dict:
        return self.password_dict

    def get_str(self) -> str:
        buffer = ""
        for key,val in self.get().items():
            buffer += f" - {key} : {val} \n"
        return buffer
    
    def display_data(self):
        print("Data found :")
        for key,val in self.password_dict.items():
            print(f" - {key} : {val}")