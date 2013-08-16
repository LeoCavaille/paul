# coding=utf-8
from clint.textui import puts, colored
import cmd
import shlex

import paul.client

import texttable as tt

def wrong_syntax(cmd):
    print "Wrong syntax, check syntax with \"help create\""

def pretty_print_pause(b):
    if b:
        puts(colored.red("Lucy is PAUSED"))
    else:
        puts(colored.green("Lucy is working"))

class Job(cmd.Cmd):
    def do_paused(self, s):
        """
        Usage :
            paused - returns the status of lucy instance
            paused 0|1 - set the pause or resume
        """
        if s:
            paul.client.proxy.set_paused_status(s)
            pretty_print_pause(paul.client.proxy.get_paused_status())
        else:
            pretty_print_pause(paul.client.proxy.get_paused_status())

    # Catch ^D
    def do_EOF(self, line):
        print ''
        return True
