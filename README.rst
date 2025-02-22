PySOEM
======

PySOEM is a Cython wrapper for the Simple Open EtherCAT Master Library (https://github.com/OpenEtherCATsociety/SOEM).

Introduction
------------

PySOEM enables basic system testing of EtherCAT slave devices with Python.

Features

* input process data read and output process data write
* SDO read and write
* EEPROM read and write
* FoE read and write

Todo

* EoE

Beware that real-time applications need some special considerations.

Requirements
------------

Linux
^^^^^

* Python 3
* GCC (installed on your machine)
* Python scripts that use PySOEM must be executed under administrator privileges

Windows
^^^^^^^

* Python 3 / 64 Bit
* `Npcap <https://nmap.org/npcap/>`_ [*]_ or `WinPcap <https://www.winpcap.org/>`_

.. [*] Make sure you check "Install Npcap in WinPcap API-compatible Mode" during the install

Installation
------------
::

  python -m pip install pysoem

or

::

  pip install pysoem

Consider using a `virtualenv <https://virtualenv.pypa.io>`_.


Usage
-----
Although there are some pieces missing, the documentation is hosted on "Read the Docs" at: `pysoem.readthedocs.io <https://pysoem.readthedocs.io>`_.

Please also have a look at `the examples on GitHub <https://github.com/bnjmnp/pysoem/tree/master/examples>`_.

Contribution
------------

Any contributions are welcome and highly appreciated.
Let's discuss any (major) API change, or large piles of new code first.
Using `this pysoem chat room on gitter <https://gitter.im/pysoem/pysoem>`_ is one communication channel option.


Changes
-------

v1.0.3
^^^^^^^
* Fix the FoE password issue

v1.0.2
^^^^^^^
* Licence change to MIT licence
* Introduces configurable timeouts for SDO read and SDO write
* Improved API docs
  
v1.0.1
^^^^^^^
* API change: remove the size parameter for `foe_write`
* Introduces overlap map support

v1.0.0
^^^^^^^
* No Cython required to install the package from the source distribution

v0.1.1
^^^^^^^
* Introduces FoE

v0.1.0
^^^^^^^
* Update of the underlying SOEM

v0.0.18
^^^^^^^
* Fixes bug when Ibytes = 0 and Ibits > 0

v0.0.17
^^^^^^^
* Exposes ec_DCtime (`dc_time`) for DC synchronization

v0.0.16
^^^^^^^
* Improvement on SDO Aborts

v0.0.15
^^^^^^^
* SDO info read

v0.0.14
^^^^^^^
* Readme update only

v0.0.13
^^^^^^^
* Initial publication
