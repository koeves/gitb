from parser.parser import Parser
from typing import List
import subprocess

class GitBranchParser(Parser):

    class GitBranchParser(Parser.ParserError):
        pass

    def __init__(self) -> None:
        self._list = self._parse()

    def _parse(self) -> List:
        branch_call = subprocess.run(["git", "branch"], text=True, capture_output=True)

        if "".join(branch_call.stderr.split()) != "":
            print(f"stderr: {branch_call.stderr}")
            raise GitBranchParser.GitBranchParser

        branch_list = branch_call.stdout.split('\n')
        branch_list_nonempty = [x for x in branch_list if len(x) > 0]
        branch_list_stripped = [x.replace(' ', '') for x in branch_list_nonempty]
        return [x.replace('*', '') for x in branch_list_stripped]


