mode: dictation
mode: command
mode: user.eye
mode: user.dutch
-
# Scroll down continuously while you frown.
face(mouth_stretch_right:repeat):
    mouse_scroll(50, 0)

# Optional: a small nudge when the frown begins
#face(frown:start):
#    mouse_scroll(240, 0)

# Optional: scroll up while you smile
face(mouth_stretch_left:repeat):
    mouse_scroll(-50, 0)

#face(smile:repeat):
#    mouse_scroll(-240, 0)