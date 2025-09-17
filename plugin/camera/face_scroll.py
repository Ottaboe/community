from talon import Module, actions

#makes sure smile face scroll only activates when smiling with left side. Checks for right side.
    
mod = Module()

# Hysteresis thresholds to prevent flicker
START_T = 0.45   # must exceed this to turn ON
STOP_T  = 0.35   # must drop below this to turn OFF

_state = {
    "left_val": 0.0,
    "right_val": 0.0,
    "left_on": False,
    "right_on": False,
}

def _latch(current_on: bool, v: float) -> bool:
    if not current_on and v >= START_T:
        return True
    if current_on and v <= STOP_T:
        return False
    return current_on

@mod.action_class
class Actions:
    def stretch_update(side: str, value: float):
        """Update mouth_stretch side and apply hysteresis."""
        v = float(value)
        if side == "left":
            _state["left_val"] = v
            _state["left_on"] = _latch(_state["left_on"], v)
        elif side == "right":
            _state["right_val"] = v
            _state["right_on"] = _latch(_state["right_on"], v)

    def stretch_clear():
        """Reset state (e.g., when face lost)."""
        _state.update({"left_val": 0.0, "right_val": 0.0, "left_on": False, "right_on": False})

    def stretch_scroll_left_exclusive(step_y: int = 50):
        """
        Scroll only if LEFT stretch is ON and RIGHT is OFF.
        Negative y scrolls up; positive y scrolls down.
        """
        if _state["left_on"] and not _state["right_on"]:
            actions.mouse_scroll(-int(step_y), 0)  # up; flip sign for down