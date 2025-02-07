from talon import Context, Module, actions, clip, settings

ctx = Context()
mod = Module()

mod.setting(
    "selected_text_timeout",
    type=float,
    default=0.25,
    desc="Time in seconds to wait for the clipboard to change when trying to get selected text",
)

END_OF_WORD_SYMBOLS = ".!?;:—_/\\|@#$%^&*()[]{}<>=+-~`"


@ctx.action_class("edit")
class EditActions:
    def selected_text() -> str:
        timeout = settings.get("user.selected_text_timeout")
        with clip.capture(timeout) as s:
            actions.edit.copy()
        try:
            return s.text()
        except clip.NoChange:
            return ""

    def line_insert_down():
        actions.edit.line_end()
        actions.key("enter")

    def selection_clone():
        actions.edit.copy()
        actions.edit.select_none()
        actions.edit.paste()

    def line_clone():
        # This may not work if editor auto-indents. Is there a better way?
        actions.edit.line_start()
        actions.edit.extend_line_end()
        actions.edit.copy()
        actions.edit.right()
        actions.key("enter")
        actions.edit.paste()

    # # This simpler implementation of select_word mostly works, but in some apps it doesn't.
    # # See https://github.com/talonhub/community/issues/1084.
    # def select_word():
    #     actions.edit.right()
    #     actions.edit.word_left()
    #     actions.edit.extend_word_right()

    def select_word():
        actions.edit.extend_right()
        character_to_right_of_initial_caret_position = actions.edit.selected_text()

        # Occasionally apps won't let you edit.extend_right()
        # and therefore won't select text if your caret is on the rightmost character
        # such as in the Chrome URL bar
        did_select_text = character_to_right_of_initial_caret_position != ""

        if did_select_text:
            # .strip() turns newline & space characters into empty string; the empty
            # string is in any other string, so this works.
            if (
                character_to_right_of_initial_caret_position.strip()
                in END_OF_WORD_SYMBOLS
            ):
                # Come out of the highlight in the initial position.
                actions.edit.left()
            else:
                # Come out of the highlight one character
                # to the right of the initial position.
                actions.edit.right()

        actions.edit.word_left()
        actions.edit.extend_word_right()


@mod.action_class
class Actions:
    def paste(text: str):
        """Pastes text and preserves clipboard"""

        with clip.revert():
            clip.set_text(text)
            actions.edit.paste()
            # sleep here so that clip.revert doesn't revert the clipboard too soon
            actions.sleep("150ms")

    def delete_right():
        """Delete character to the right"""
        actions.key("delete")

    def delete_all():
        """Delete all text in the current document"""
        actions.edit.select_all()
        actions.edit.delete()

    def words_left(n: int):
        """Moves left by n words."""
        for _ in range(n):
            actions.edit.word_left()

    def words_right(n: int):
        """Moves right by n words."""
        for _ in range(n):
            actions.edit.word_right()

    def cut_word_left():
        """Cuts the word to the left."""
        actions.edit.extend_word_left()
        actions.edit.cut()

    def cut_word_right():
        """Cuts the word to the right."""
        actions.edit.extend_word_right()
        actions.edit.cut()

    def copy_word_left():
        """Copies the word to the left."""
        actions.edit.extend_word_left()
        actions.edit.copy()

    def copy_word_right():
        """Copies the word to the right."""
        actions.edit.extend_word_right()
        actions.edit.copy()

    # ----- Start / End of line -----
    def select_line_start():
        """Select to start of current line"""
        if actions.edit.selected_text():
            actions.edit.left()
        actions.edit.extend_line_start()

    def select_line_end():
        """Select to end of current line"""
        if actions.edit.selected_text():
            actions.edit.right()
        actions.edit.extend_line_end()

    def delete_word_smart():
        """Delete the entire word or the word to the left, depending on cursor position"""
        # Extend the selection to the left first
        actions.edit.extend_word_left()

        # Check if the entire word is selected
        # Move the cursor to the right and try to delete the remaining part if needed
        actions.key("ctrl-shift-right")

        # Delete the entire word
        actions.edit.delete()

    def wipe_word():
        """Delete the word to the right of the cursor, including any leading spaces"""
        
        # Step 1: Extend the selection to the right
        actions.edit.extend_word_right()

        # Step 2: Check if the selection is empty or only contains a space
        if actions.user.selection_is_space_or_empty():
            # If so, extend the selection to the right again to capture the next word
            actions.edit.extend_word_right()

        # Step 3: Delete the selected text
        actions.edit.delete()

    @mod.action_class
    class Actions:
        def selection_is_space_or_empty() -> bool:
            """Returns True if the current selection is empty or only contains whitespace"""
            # This is a stub; you'll need to implement this according to your environment.
            # You could check the length of the selected text or inspect the selected text itself.
            # Here we just return False as a placeholder.
            return False


    def line_middle():
        """Go to the middle of the line"""
        actions.edit.select_line()
        half_line_length = int(len(actions.edit.selected_text()) / 2)
        actions.edit.left()
        for i in range(0, half_line_length):
            actions.edit.right()

    def cut_line():
        """Cut current line"""
        actions.edit.select_line()
        actions.edit.cut()
