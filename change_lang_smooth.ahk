; AutoHotkey script to switch text between English and Russian keyboard layouts
#Persistent
#NoEnv

; Set the hotkey for the Insert key
Insert::
    ; Send Ctrl+A to select all text
    Send, ^a
    ; Send Ctrl+C to copy the selected text
    Send, ^c
    ; Wait for the clipboard to contain the copied text
    ClipWait, 1
    ; Get the copied text
    originalText := Clipboard
    ; Convert the text from English to Russian or vice versa
    convertedText := ConvertText(originalText)
    ; Clear the clipboard and set the converted text
    Clipboard := convertedText
    ; Send the converted text with a delay
    SendWithDelay(convertedText)
return

; Function to convert text between English and Russian layouts
ConvertText(text) {
    ; Define the English and Russian keyboard layouts
    english := "qwertyuiop[]asdfghjkl;'zxcvbnm,QWERTYUIOP{}ASDFGHJKL:""ZXCVBNM<>~"
    russian := "йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"
    
    ; Create a variable to hold the converted text
    converted := ""
    
    ; Loop through each character in the original text
    Loop, Parse, text
    {
        char := A_LoopField
        ; Find the index of the character in the English layout
        index := InStr(english, char, false)
        if (index) {
            ; If found, replace it with the corresponding Russian character
            converted .= SubStr(russian, index, 1)
        } else {
            ; If not found, check the Russian layout
            index := InStr(russian, char, false)
            if (index) {
                ; If found, replace it with the corresponding English character
                converted .= SubStr(english, index, 1)
            } else {
                ; If the character is not found in either layout, keep it unchanged
                converted .= char
            }
        }
    }
    
    return converted
}

; Function to send text with a delay between each character
SendWithDelay(text) {
    Loop, Parse, text
    {
        Send, % A_LoopField
        Sleep, 20 ; Delay of 20 milliseconds (0.02 seconds)
    }
}
