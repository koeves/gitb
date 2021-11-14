import subprocess
from runner.runner import Runner

class GitBranchRunner(Runner):
    def __init__(self, branch_name) -> None:
        self.branch_name = branch_name

    def run(self) -> None:
        branch_change = subprocess.run(["git", "checkout", self.branch_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        print(branch_change.stdout.split('\n')[0])
