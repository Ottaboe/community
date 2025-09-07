from talon import Module, ctrl

mod = Module()

@mod.action_class
class Actions:
    def parrot_click():
        """Clicks the mouse left button"""
        ctrl.mouse_click(button=0) 

    def parrot_middle_click():
        """Clicks the mouse middle button"""
        ctrl.mouse_click(button=2)


