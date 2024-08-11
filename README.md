# About
Small script that will turn all your *ghbdtn* to *привет*. Basically like you would change keyboard layout and retype all the text.
## Warnings
Python version sucks and only works from time to time but works
### Rewrites ALL TEXT THAT CAN BE SELECTED IN current scope/field
## Hotkey:
```<insert>```

### Also there is a smooth_ctrl_v file
that just writes text 1 symbol every 20 ms 
## Hotkey:
```<ctrl><alt><v>```

# Python
## For python version:
```console
pip install pyautogui keyboard
```
and then run it like(if you want it to run in background) 
```console
pythonw.exe \path\to\change_language.py
```
Haven't tested on linux though. Maybe works.
# AutoHotKey
## BUT! If you want more comfortable expirience, then use autohotkey!
1. Download autohotkey https://www.autohotkey.com/
2. run any .ahk script
3. or you can add to startup by copying .ahk file you prefer to %AppData%\Microsoft\Windows\Start Menu\Programs\Startup
## Difference between normal and smooth version
basicaly normal version just pastes the text while smooth version inputs every symbol every 20ms

