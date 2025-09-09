mode: user.eye
-

settings():
    speech._subtitles = false

    user.mode_indicator_show = true
    user.mode_indicator_color_other = "ff0000"

    <phrase>: skip()



#^command mode$:
#    mode.disable("user.eye")
#    mode.enable("command")

#^drowsy [<phrase>]$:
#    user.switcher_hide_running()
#    user.history_disable()
#    user.homophones_hide()
#    user.mouse_sleep()
#    speech.disable()
#    user.dragon_engine_sleep()
#    mode.disable("user.eye")


# mouse click left
parrot(pop):
    user.parrot_click()

#parrot(palate_click):
    #user.parrot_click()

#parrot(kik):
    #user.parrot_click()ff

# scrolling 
#parrot(whistle_high):
#    app.notify("Whistle high detected")
#    user.scroll_up(f0)  
    # This should scroll up

#parrot(whistle_low):
#    app.notify("Whistle low detected")
#   user.scroll_down(f0)  
    # This should scroll down
