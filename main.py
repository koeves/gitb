#!/usr/bin/env python3

from menu.menu import MenuCreator
from runner.gitbranchrunner import GitBranchRunner
from parser.gitbranchparser import GitBranchParser
from parser.parser import Parser

if __name__ == "__main__":
    try:
        parser = GitBranchParser()
        options = parser.get()

        menu = MenuCreator(options)
        selected_branch_name = menu.show()

        runner = GitBranchRunner(selected_branch_name)
        runner.run()

    except Parser.ParserError:
        pass