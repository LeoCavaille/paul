paul
====

I thought after ricky, ethel, lucy and fred, there was only paul missing so there he is !
This thing is a CLI to interact with lucy server via XML-RPC.

# Installation

As root on your machine :

    git clone https://github.com/LeoCavaille/paul.git
    apt-get install python-clint python-gnupg python-pip
    pip install -U git+http://github.com/bufordtaylor/python-texttable
    cd paul
    python setup.py install

# Usage

Now have fun, for instance :

    paul --host debuild.me --port 20017 --user paul

To use with a list of commands :

    echo "user list" >> /tmp/commands.tag
    echo "machine list" >> /tmp/commands.tag
    paul --host debuild.me --port 20017 --user paul -f /tmp/commands.tag

A password can be supplied in the CLI with --password option.
