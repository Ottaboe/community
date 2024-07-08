import subprocess
from talon import Module, app

mod = Module()

@mod.action_class
class Actions:
    def open_website():
        """Open a specific website in Chrome."""
        subprocess.run(["start", "chrome", "http://localhost:7419/"], shell=True)

    def close_browser():
        """Close Chrome."""
        subprocess.run("taskkill /IM chrome.exe /F", shell=True)

#making sure Chrome closes when Talon does
@mod.scope
def talon_quit():
    actions.user.close_browser()
