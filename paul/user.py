# coding=utf-8
from clint.textui import puts, colored
import cmd
import shlex

import client
import texttable as tt

def wrong_syntax(cmd):
    print "Wrong syntax, check syntax with \"help create\""

class User(cmd.Cmd):
    def do_list(self, s):
        "List all users registered in lucy"
        users = client.proxy.list_user()
        puts(colored.green( "Here is a list of lucy users :"))
        table = tt.Texttable()
        header = ['Login', 'Name', 'Email', 'GPG fingerprint', 'Admin rights']
        table.header(header)
        for u in users:
            table.add_row([u['login'], u['name'].encode('utf8'), u['email'], u['gpg_fingerprint'], u['admin']])
        output = table.draw()
        print output

    def do_create(self, s):
        """
        Create a new lucy user
        syntax : create [login] [password] [name] [email] [gpgkeyid]
        paul:user > create leo suchagoodpassword 'Léo Cavaillé' leo@cavaille.net 0x29948D7F1AC8586F
        The gpg key must be present in your home gpg keyring.
        """
        try:
            args = shlex.split(s)
        except:
            wrong_syntax('create')
        if len(args) != 5:
            wrong_syntax('create')

        login = args[0]
        password = args[1]
        name = args[2]
        email = args[3]
        gpgkeyid = args[4]
        
        # Try to fetch an armored ascii version of the key
        ascii_armored_key = client.gpg.export_keys(gpgkeyid)
        user, reply = client.proxy.create_user(login, password, name, email, ascii_armored_key)
        # TODO : could use user var to print some debug info on the created entity
        if user:
            puts(colored.green("Success : "+reply))
        else:
            puts(colored.red("Failed : "+reply))

    # Catch ^D
    def do_EOF(self, line):
        print ''
        return True
