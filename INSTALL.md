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

    paul --host debuild.me.ecranbleu.org --port 20017 --user paul
