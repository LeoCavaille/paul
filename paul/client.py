import xmlrpclib
from clint import args
from clint.textui import puts, colored
import getpass
import sys
import os
import gnupg

from paul.modules import Modules

def main():
    puts("debuildme paul's client\n")

    # Parse the args
    all_args = args.grouped
    
    host = None
    port = None
    user = None

    if '--host' in all_args:
        host = all_args['--host'].all[0]
    if '--port' in all_args:
        port = all_args['--port'].all[0]
    if '--user' in all_args:
        user = all_args['--user'].all[0]

    if not host:
        print "--host not given"
        sys.exit(1)
    if not port:
        print "--port not given"
        sys.exit(1)
    if not user:
        print "--user not given"
        sys.exit(1)

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


    m = Modules()
    m.cmdloop()
