not mode: sleep
-

# mouse click left
parrot(pop):
    user.parrot_click()

parrot(palate_click):
    user.parrot_click()

parrot(kik):
    user.parrot_click()

# control mouse click left
parrot(tut_low):
    user.parrot_middle_click()


# scrolling 
parrot(whistle_high):
    app.notify("Whistle high detected")
    user.scroll_up(f0)  
    # This should scroll up

parrot(whistle_low):
    app.notify("Whistle low detected")
    user.scroll_down(f0)  
    # This should scroll down


# browser control

parrot(tut):
    user.go_back()




