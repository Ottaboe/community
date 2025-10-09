mode: user.face_tracking
-




# Optional: clear state when the face drops out
face(presence:stop):
    user.stretch_clear()

# Feed live values (0..1) into our gate
face(mouth_stretch_right:change):
    user.stretch_update("left", value)

face(mouth_stretch_left:change):
    user.stretch_update("right", value)

# Scroll only when LEFT stretch is exclusive (left ON, right OFF)
face(mouth_stretch_right:repeat):
    user.stretch_scroll_left_exclusive(-50)

# (keep your existing)
face(brow_inner_up:repeat):
    mouse_scroll(-50, 0)