pschecker
=========

`pschecker` stands for Personal Server Checker. It's a simple Python script
that will audit the state of the security of your personal server. That way you
will know if your setup has the minimum security to survive in the wild
Internet.

.. code::

    $ pip install pschecker
    $ pschecker

    Welcome to Personal Server Checker!
    Your personal server diagnostic is:
    Distribution: debian
    Root must not use password: OK
    No process listens on 0.0.0.0 host: OK
    You are all good!
