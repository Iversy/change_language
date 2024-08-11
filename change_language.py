import pyautogui as pykey
import pyperclip
import time
import keyboard as k
en_ru_en = {'q': 'й', 'й': 'q', 'w': 'ц', 'ц': 'w', 'e': 'у', 'у': 'e', 'r': 'к', 'к': 'r', 't': 'е', 'е': 't', 'y': 'н', 'н': 'y', 'u': 'г', 'г': 'u', 'i': 'ш', 'ш': 'i', 'o': 'щ', 'щ': 'o', 'p': 'з', 'з': 'p', '[': 'х', 'х': '[', ']': 'ъ', 'ъ': ']', 'a': 'ф', 'ф': 'a', 's': 'ы', 'ы': 's', 'd': 'в', 'в': 'd', 'f': 'а', 'а': 'f', 'g': 'п', 'п': 'g', 'h': 'р', 'р': 'h', 'j': 'о', 'о': 'j', 'k': 'л', 'л': 'k', 'l': 'д', 'д': 'l', ';': 'ж', 'ж': 
';', "'": 'э', 'э': "'", 'z': 'я', 'я': 'z', 'x': 'ч', 'ч': 'x', 'c': 'с', 'с': 'c', 'v': 'м', 'м': 'v', 'b': 'и', 'и': 'b', 'n': 'т', 'т': 'n', 'm': 'ь', 'ь': 'm', ',': 'б', 'б': ',', '.': 'ю', 'ю': '.', '`': 'ё', 'ё': '`', 'Q': 'Й', 'Й': 'Q', 'W': 'Ц', 'Ц': 'W', 'E': 'У', 'У': 'E', 'R': 'К', 'К': 'R', 'T': 'Е', 'Е': 'T', 'Y': 'Н', 'Н': 'Y', 'U': 'Г', 'Г': 'U', 'I': 'Ш', 'Ш': 'I', 'O': 'Щ', 'Щ': 'O', 'P': 'З', 'З': 'P', '{': 'Х', 'Х': '{', '}': 'Ъ', 'Ъ': '}', 'A': 'Ф', 'Ф': 'A', 'S': 'Ы', 'Ы': 'S', 'D': 'В', 'В': 'D', 'F': 'А', 'А': 'F', 'G': 'П', 'П': 'G', 'H': 'Р', 'Р': 'H', 'J': 'О', 'О': 'J', 'K': 'Л', 'Л': 'K', 'L': 'Д', 'Д': 'L', ':': 'Ж', 'Ж': ':', '"': 'Э', 'Э': '"', 'Z': 'Я', 'Я': 'Z', 'X': 'Ч', 'Ч': 'X', 'C': 'С', 'С': 'C', 'V': 'М', 'М': 'V', 'B': 'И', 'И': 'B', 'N': 'Т', 'Т': 'N', 'M': 'Ь', 'Ь': 'M', '<': 'Б', 'Б': '<', '>': 'Ю', 'Ю': '>', '~': 'Ё', 'Ё': '~'}


def change_letter(letter):
    global en_ru_en
    return en_ru_en[letter] if en_ru_en.get(letter) else letter
    

# ru-en only
def change_text():
    pyperclip.copy("")
    time.sleep(0.1)
    pykey.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pykey.hotkey('ctrl', 'c')
    time.sleep(0.1)
    
    text = pyperclip.paste()
    time.sleep(0.1)
    
    changed_text = "".join(map(change_letter, text))
    k.write(changed_text, delay=0.02)
    
k.add_hotkey("insert", change_text)
k.add_hotkey("ctrl+shift+\\", exit)
k.wait()

