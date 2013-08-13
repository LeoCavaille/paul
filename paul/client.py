import xmlrpclib
from clint import args
from clint.textui import puts, colored
import getpass
import sys
import os
import gnupg
import shlex
import importlib
from subprocess import list2cmdline

from paul.modules import Modules

def load_command_file(filename):
    try:
        with open(filename, 'r') as command_file:
            commands = command_file.readlines()
            for c in commands:
                print c
                args = shlex.split(c)
                try:
                    module_name = "paul.%s" % args[0]
                    mod = importlib.import_module(module_name)
                except Exception as e:
                    print "Command not found : " +args[0]
                    sys.exit(1)
                if len(args) < 2:
                    print "No command given in module " +args[0]
                    sys.exit(1)
                class_name = args[0].title()
                command_name = "do_%s" % args[1]
                if len(args)==2:
                    cls = getattr(mod, class_name)
                    instance = cls()
                    getattr(instance, command_name)("")
                else:
                    args.pop(0)
                    args.pop(0)
                    getattr(instance, command_name)(list2cmdline(args))
    except IOError:
        puts(colored.red("File given with -f option does not exist : "+filename))
    sys.exit(0)

def main():
    puts("debuildme paul's client\n")

    # Parse the args
    all_args = args.grouped
    
    host = None
    port = None
    user = None
    password = None

    if '--host' in all_args:
        host = all_args['--host'].all[0]
    if '--port' in all_args:
        port = all_args['--port'].all[0]
    if '--user' in all_args:
        user = all_args['--user'].all[0]
    if '--password' in all_args:
        password = all_args['--password'].all[0]

    if not host:
        print "--host not given"
        sys.exit(1)
    if not port:
        print "--port not given"
        sys.exit(1)
    if not user:
        print "--user not given"
        sys.exit(1)

    if not password:
        # Prompt for password
        password = getpass.getpass("Password for user %s on %s:%s : " % (user, host, port))

    # Now we all have the info we need to connect to lucy
    proxy_url = "http://{user}:{password}@{host}:{port}/".format(
            user = user,
            password = password,
            host = host,
            port = port)
    global proxy
    proxy = xmlrpclib.ServerProxy(proxy_url)
    try:
        success_string = proxy.get_server_info()
        puts(colored.green(success_string))
    except:
        puts(colored.red("Connection failed, check the connection parameters or the server"))
        sys.exit(1)

    # Some modules need this resource
    gnupg_default_home = os.path.join(os.environ['HOME'], '.gnupg')
    global gpg
    gpg = gnupg.GPG(gnupghome=gnupg_default_home, verbose=False)

    if '-f' in all_args:
        load_command_file(all_args['-f'].all[0])

    m = Modules()
    m.cmdloop()
