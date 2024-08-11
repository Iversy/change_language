#Persistent
#NoEnv

^!v::
    SendWithDelay(Clipboard)

SendWithDelay(text) {
    Loop, Parse, text
    {
        Send, % A_LoopField
        Sleep, 20 
    }
}
