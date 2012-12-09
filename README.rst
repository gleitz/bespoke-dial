Bespoke Dial: Old-Timey Speed Dial
==================================

Bespoke Dial allows you to enter a number a rotary phone and immediately connectes your party via Google Voice. On a deeper level you can use Bespoke Dial to automate most any process at the touch of a rotating button – unlocking a secret room, controlling the lights in your home, or surreptitiously ordering a pizza.

Installation
------------

-  ``pip install -r requirements.txt``
-  Place Google Voice username and password in secret.txt (USERNAME|||PASSWORD)
-  ``python dial.py``

Usage
-----

::
    dial.py [-h] [-l LISTEN] [-d DIAL]

    bespoke dial: old-timey speed dial

    optional arguments:
      -h, --help            show this help message and exit
      -l LISTEN, --listen LISTEN
                            listens for dialed numbers and initiates the call
                            after 10 numbers have been dialed
      -d DIAL, --dial DIAL  dial a number

Extra notes:

-  Special thanks to `Hard Hack 2012 <https://github.com/dshaw/hard-hack-2012>`_
