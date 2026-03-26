from pynput import keyboard
import vlc
import time
from pynput import mouse

isp = False
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new('/path/to/file.mp3')
player.set_media(Media)
events = player.event_manager()

def on_click(x, y, button, pressed):
    global isp
    if pressed:
        if 100 <= x <= 520 and 100 <= y <= 340:
            time.sleep(4)
            player.play()
            isp = True

def end(event):
    global isp
    isp = False
events.event_attach(vlc.EventType.MediaPlayerEndReached, end)

def on_press(key):
    global isp
    if key == keyboard.Key.space:
        if isp == True:
            player.stop()
            isp = False
        else:
            player.play()
            isp = True

keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()