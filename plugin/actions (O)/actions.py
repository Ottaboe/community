# actions.py

from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def scroll_up(frequency: float):
        """Scroll up based on the frequency of the whistle"""
        base_frequency = 1200
        sensitivity = 5  # Lowering the sensitivity increases scroll speed
        amplification_factor = 3  # Increase this factor to make scrolling faster

        # Calculate the scroll amount based on the deviation from base frequency
        scroll_factor = (frequency - base_frequency) / sensitivity

        # Ensure the scroll amount is positive for upward scrolling
        scroll_amount = -scroll_factor * amplification_factor

        # Perform the scroll and notify for debugging
        actions.app.notify(f"Scrolling up: {scroll_amount}, Frequency: {frequency}")
        print(f"Scrolling up: {scroll_amount}, Frequency: {frequency}")
        actions.mouse_scroll(y=scroll_amount)

    def scroll_down(frequency: float):
        """Scroll down based on the frequency of the whistle"""
        base_frequency = 1200
        sensitivity = 5  # Lowering the sensitivity increases scroll speed
        amplification_factor = 3  # Increase this factor to make scrolling faster

        # Calculate the scroll amount based on the deviation from base frequency
        scroll_factor = (base_frequency - frequency) / sensitivity

        # Ensure the scroll amount is positive for downward scrolling
        scroll_amount = scroll_factor * amplification_factor

        # Perform the scroll and notify for debugging
        actions.app.notify(f"Scrolling down: {scroll_amount}, Frequency: {frequency}")
        print(f"Scrolling down: {scroll_amount}, Frequency: {frequency}")
        actions.mouse_scroll(y=scroll_amount)

    def go_back():
        """Go back to the previous page"""
        actions.key("alt-left")  # This simulates the Alt+Left arrow key combination
        print("Executing go_back action")
