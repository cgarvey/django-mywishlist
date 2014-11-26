Intro
=====
To get this running on a local/development server,
use a 'virtualenv' environment (to get around
any potential library/module conflicts).

System-level prerequisites
==========================
VirtualEnv takes care of most modules required, but there
are some system-level modules that need to be installed
before any development on this app can happen:

+ **gcc / general build tools** We assume the presence of gcc and build tools required to build python modules.
+ **Python & SetupTools/pip** Obviously! Tested on v2.7 only. Pip is assumed to be present too.
+ **Node.js & NPM** Used to install various dependencies (primarily [Bootstrap](http://getbootstrap.com/)).

Creating Initial Environment
============================
VirtualEnv
----------
To get started (this done once at the start, only), you need to create a
virtual environment (in which to install dependent modules). Do this by
running, from the Django project directory (where `manage.py` resides):

	virtualenv --no-site-packages venv
or if you need to specify a Python ``virtualenv --python python2.5 --no-site-packages venv``.

Once initialised, switch to that virtualenv by calling its script:

	source venv/bin/activate

Which should now give you a `(venv)` prefix to your prompt.

PIP
---
Whilst within the `(venv)` prompt, we can update `distribute` if needs
be, and we an install any dependencies with PIP.

First, we may need to update `distribute` (and PIP can not update it
from within itself). This is especially true for older Ubunutu LTS
installs. You will know if this step needs to be complete if you skip
it, and go straight to the next PIP install/upgrade from reuqirements.txt.
You will get an error about easy_install, telling you to

	easy_install -U distribute

This is just a one-off step.

Next, from the same `(venv)` prompt, and Django project folder, install
the required Python modules using pip and the requirements
file that is included in the source:

	pip install --upgrade --timeout=120 --use-mirrors -r requirements.txt

If you get any errors in that process, your system likely needs to have
some development libraries installed (on a system level, not in the
virtual env). If that is the case, Google the error and see what is
needed. Once installed (system-level), recreate the `venv` as per above.

Node / Bower
------------
This project uses Bower to install dependencies (Bootstrap). Once you have installed Node.js and its package manager NPM, you should be able to install all dependencies by running the following from the project root level directory:

	npm install

Running the App
===============
Firstly, switch to the `venv`:

	source venv/bin/activate

Then run the standard Django `manage.py` as you normally do for a Django
project. E.g.

	python manage.py runserver
