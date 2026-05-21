None selected

Skip to content
Using Gmail with screen readers
Enable desktop notifications for Gmail.
   OK  No thanks
2 of 94
(no subject)
Inbox

shasrutha s
Attachments
9:52 AM (22 minutes ago)
to me


 28 Attachments
  •  Scanned by Gmail
from pynput import keyboard

def press(key):
    try:
        print("You pressed:", key.char)
    except:
        print("Special key pressed:", key)

    if key == keyboard.Key.esc:
        print("Program Closed")
        return False

print("KEYBOARD CHECKER")
print("Press keys...")
print("Press ESC to exit")

with keyboard.Listener(on_press=press) as listener:
    listener.join()
KEYBOARD.py
Displaying KEYBOARD.py.
