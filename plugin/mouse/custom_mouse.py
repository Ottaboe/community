from talon import Module, ctrl

mod = Module()

@mod.action_class
class Actions:
    def parrot_click():
        """Clicks the mouse left button and prints debug statement."""
        print("Executing parrot_click action")  # Debug print
        ctrl.mouse_click(button=0)  # This performs a simple left click.
