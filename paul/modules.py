import cmd
from paul.user import User
from paul.machine import Machine
from paul.job import Job

class Modules(cmd.Cmd):
    prompt = 'paul > '
    def do_user(self, s):
        "Load user module to manage lucy users"
        u = User()
        u.prompt = 'paul:user > '
        u.cmdloop()

    def do_machine(self, s):
        "Load machine module to manage lucy machines"
        m = Machine()
        m.prompt = 'paul:machine > '
        m.cmdloop()

    def do_job(self, s):
        "Load jobs module to interact with the jobs on lucy instance"
        j = Job()
        j.prompt = 'paul:job > '
        j.cmdloop()

    # Catch ^D
    def do_EOF(self, line):
        "Exit paul"
        return True
