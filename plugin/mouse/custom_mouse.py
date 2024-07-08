from talon import Module, ctrl

mod = Module()

@mod.action_class
class Actions:
    def parrot_click():
        """Clicks the mouse left button and prints debug statement."""
        print("Executing parrot_click action")  # Debug print
        ctrl.mouse_click(button=0)  # This performs a simple left click.

    def parrot_middle_click():
        """Clicks the mouse middle button (scroll button) and prints debug statement."""
        print("Executing parrot_middle_click action")  # Debug print
        ctrl.mouse_click(button=2)  # This performs a middle mouse button click


