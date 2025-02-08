import socket, os, requests, time
import win32gui
import win32con
import pyvolume

hostname = '192.168.0.10'
port = 3600

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((hostname, port))

s.listen()

conn, addr = s.accept()

conn.send("connectet".encode("utf-8"))

while True:
    command = conn.recv(5024).decode("utf-8")
    if command == "jumpscare":
        if not os.path.exists("jumpscare.mkv"):
            url = "https://github.com/wastedkoala/jumpscare/raw/refs/heads/main/jumpscare.mkv"
            r = requests.get(url)
            open("jumpscare.mkv", "wb").write(r.content)
        
        pyvolume.custom(percent=80)
        time.sleep(0.5)
        os.startfile("jumpscare.mkv")
        jump = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(jump, win32con.SW_MAXIMIZE)
        time.sleep(2.5)
        win32gui.PostMessage(jump,win32con.WM_CLOSE,0,0)
        conn.send("modtaget".encode("utf-8"))
    else:
        conn.send("forkert".encode("utf-8"))

    
        
