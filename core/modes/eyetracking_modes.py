from talon import Module, actions

mod = Module()

# so cluck always enables eye tracker

@mod.action_class
class Actions:
    def ensure_tracking_enabled():
        """Ensure the tracking control is disabled."""
        if not actions.tracking.control_enabled():
            actions.tracking.control_toggle()