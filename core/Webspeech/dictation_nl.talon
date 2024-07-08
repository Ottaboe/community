mode: dictation
language: nl
-
command mode:
    mode.disable("dictation")
    mode.disable("user.dutch")
    mode.enable("command")

<phrase>: insert("{phrase} ")

#this is for letters in dutch
#{user.letter}:key(letter)

ga links: print("text")
ga rechts: print("text")

#nieuwe lijn 
(nieuwe| nieuw) lijn:
    edit.line_insert_down()
    user.dictation_format_reset()
    
(nieuwelijn| nieuwlijn):
    edit.line_insert_down()
    user.dictation_format_reset()

#nieuwe paragraaf 
(nieuwe| nieuw) (paragraaf | graaf | graf):
    edit.line_insert_down()
    edit.line_insert_down()
    user.dictation_format_reset()

(Nieuwegraaf | nieuwgraaf):
    edit.line_insert_down()
    edit.line_insert_down()
    user.dictation_format_reset()











^commando [<phrase>]$:
    mode.disable("user.dutch")
    mode.disable("dictation")
    mode.enable("command")

^over [<phrase>]$:
    mode.disable("user.dutch")
    mode.disable("dictation")
    mode.enable("command")
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()



(schip | uppercase) <user.letters> [(lowercase | sunk)]:
    user.insert_formatted(letters, "ALL_CAPS")