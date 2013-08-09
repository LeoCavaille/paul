# coding=utf-8
from clint.textui import puts, colored
import cmd
import shlex

import client
import texttable as tt

def wrong_syntax(cmd):
    print "Wrong syntax, check syntax with \"help %s\"" % cmd

class Machine(cmd.Cmd):
    def do_list(self, s):
        "List all machines registered in lucy"
        users = client.proxy.list_machine()
        puts(colored.green( "Here is a list of lucy users :"))
        table = tt.Texttable()
        header = ['Name', 'Last ping', 'GPG fingerprint']
        table.header(header)
        for u in users:
            table.add_row([u['name'], u['last_ping'], u['gpg_fingerprint']])
        output = table.draw()
        print output

    def do_create(self, s):
        """
        Create a new lucy machine (builder)
        syntax : create [name] [password] [gpgkeyid]
        paul:user > create builder1 ohmygodsosecure 0x896AE222CC16515C
        The gpg key must be present in your home gpg keyring.
        """
        try:
            args = shlex.split(s)
        except:
            wrong_syntax('create')
        if len(args) != 3:
            wrong_syntax('create')

        name = args[0]
        password = args[1]
        gpgkeyid = args[2]
        
        # Try to fetch an armored ascii version of the key
        ascii_armored_key = client.gpg.export_keys(gpgkeyid)
        user, reply = client.proxy.create_machine(name, password, ascii_armored_key)
        # TODO : could use user var to print some debug info on the created entity
        if user:
            puts(colored.green("Success : "+reply))
        else:
            puts(colored.red("Failed : "+reply))

    # Catch ^D
    def do_EOF(self, line):
        print ''
        return True
