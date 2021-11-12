#!/usr/bin/env python3
from simple_term_menu import TerminalMenu
import subprocess

if __name__ == "__main__":
    useless_cat_call = subprocess.run(["git", "branch"], text=True, capture_output=True)
    # print(useless_cat_call.stdout)
    print(useless_cat_call.stderr)

    options = ["entry 1", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

