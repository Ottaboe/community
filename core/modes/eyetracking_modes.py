from talon import Module, actions

mod = Module()
# Assuming the default state of the tracking control is disabled

@mod.action_class
class Actions:
    def ensure_tracking_enabled():
        """Ensure the tracking control is enabled."""
        if not actions.tracking.control_enabled():
            actions.tracking.control_toggle()