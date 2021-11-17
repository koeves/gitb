from simple_term_menu import TerminalMenu

class MenuCreator:
    def __init__(self, options) -> None:
        self.options = options

    def show(self) -> int:
        self.menu = TerminalMenu(self.options)
        menu_entry_index = self.menu.show()
        return self.options[menu_entry_index]

