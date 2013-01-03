Django Metrics Dashboard Pypispy Users
======================================

A widget for the django-metrics-dashboard that displays the user count of
pypispy.com

Installation
------------

To get the latest stable release from PyPi::

    $ pip install md-pypispy-users

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/md-pypispy-users.git#egg=md_pypispy_users

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'md_pypispy_users',
    ]

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate md_pypispy_users


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 md-pypispy-users
    $ pip install -r requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch


Testing
-------

If you want to contribute to this project you can run the tests without setting
up a Django project. Just clone this repository and execute the
``runtests.py``::

    $ ./md_pypispy_users/tests/runtests.py

Sometimes a new feature needs new South migrations, in this case you should
do the following::

    $ rm db.sqlite
    $ ./manage.py syncdb --migrate
    $ ./manage.py schemamigration md_pypispy_users --auto


Discuss
-------

If you have questions or issues, please open an issue on GitHub.

If we don't react quickly, please don't hesitate to ping me on Twitter
(`@mbrochh <https://twitter.com/mbrochh>`_)
