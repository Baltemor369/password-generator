from UI import UI
import os

# menu : generateur || historique

if not os.path.exists("data"):
    os.mkdir("data")
    os.system("type nul > data/data.txt")

ui = UI()
ui.mainloop()
