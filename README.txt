This buildout relates the configuration of the ric site environment.

The main config file is buildout.cfg.

We assume the installation in the folder /srv/instances/ricsite
 (that can be changed) and on an ubuntu distribution.
Your real username must replace in our commands the string "username".
Each command, specified by the symbol ">", can be executed
 (without the symbol >).

First we become root
> sudo -s

We install the necessary libraries
> apt install build-essential
> apt install libreadline6-dev
> apt install zlib1g-dev (support zlib)
> apt install libbz2-dev
> apt install libjpeg62-dev
> apt install subversion
> apt install git
> apt install libpq-dev
> apt install libxml2-dev
> apt install libxslt1-dev
> apt install ssl-dev
> apt install graphviz graphviz-dev (if buildout error, also pkg-config)

We work in the folder /srv
> cd /srv

We change the owner of the folder to avoid continue working as root
> chown -R username:username .

We leave the user root.
> exit

We create some directories
> mkdir jinstall
> mkdir instances
> cd jinstall

We install python2.7 that will be used to run the buildout and zope instance
> wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
> tar xvzf Python-2.7.18.tgz
> cd Python-2.7.18
> ./configure --prefix=/srv/python2718
> make
> make install

We install the python utility virtualenv
> cd /srv/python2718
> bin/python -m ensurepip
> bin/pip install virtualenv
> sudo ln -s /srv/python2718/bin/virtualenv /usr/local/bin/virtualenv-2.7

We can define a cache for buildout
> vi ~/.buildout/default.cfg
[buildout]
eggs-directory = /srv/cache/eggs
download-cache = /srv/cache/downloads
extends-cache = /srv/cache/extends
> mkdir -p /srv/cache/{eggs,downloads,extends}

We download the buildout files in our folder
> cd /srv/instances
For readonly mode:
> git clone https://github.com/IMIO/buildout.ricsite.git ricsite
For write mode:
> git clone git@github.com:IMIO/buildout.ricsite.git ricsite
> cd ricsite

we initialize the buildout
> make setup

==> 1) Use in development (without ZEO, with debug products)

We execute the buildout after each modification in the buildout.cfg file
> make buildout
OR
> bin/buildout -v

We start the zope server.
> bin/instance1 fg
OR
> bin/instance1 start

We can connect the zope server in a browser on the following address http://localhost:8081/manage_main

We can add a mount point (separate database file, defined in the file zope_add.conf)
=> choose in the list (up right in the browser page) "ZODB Mount Point"
Select a mount point name ("xxx" and click on "Create selected mount points").

All objects added in the zope folder "xxx" will be stored in the db file "xxx.fs"
 in place of in "Data.fs".

==> 2) Usage in production (multiple Zope instances for the same database, ZEO mode)

We can replace in the file buildout.cfg the name dev.cfg by prod.cfg.

We execute the buildout after each modification in the buildout.cfg file
> make buildout
OR
> bin/buildout -v

We start the zeo server.
> bin/zeoserver start

We start each zope server (following instance name section).
> bin/instance1 fg
OR
> bin/instance1 start

We can connect the zope server in a browser on the following address http://localhost:8081/manage_main

We can add a mount point (separate database file, defined in the file zeo_add.conf and zope_add_zeo.conf)
=> choose in the list (up right in the browser page) "ZODB Mount Point"
Select a mount point name ("xxx" and click on "Create selected mount points").

All objects added in the zope folder "xxx" will be stored in the db file "xxx.fs"
 in place of in "Data.fs".

==> 3) Use of solr

Uncomment solr.cfg in buildout.cfg.
Run buildout.
Install collective.solr product in plone site.
Index in solr : call /@@solr-maintenance/reindex in plone site.
