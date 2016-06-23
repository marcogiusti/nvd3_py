===============
NVD3 for Python
===============

|travis|
|coveralls|
|rtfd|

This module is an attempt to build NVD3 charts from python. The API
mimics the NVD3's one, for an example of use look at
`examples/pie_chart.ipynb`_.

The project includes also a django app that implements few tags to help
using nvd3 within Django.


Install
=======

This package is still very experimental. It will not published to PyPI
until a stable release is reached. It can anyway installed with
``pip``::

   $ pip install git+https://github.com/marcogiusti/nvd3_py#egg=nvd3_py


License
=======

The code is released under the MIT license. See LICENSE for more
details.


.. _examples/pie_chart.ipynb: https://github.com/marcogiusti/nvd3_py/blob/master/examples/pie_chart.ipynb

.. |travis| image:: https://travis-ci.org/marcogiusti/nvd3_py.svg?branch=master
    :target: https://travis-ci.org/marcogiusti/nvd3_py

.. |coveralls| image:: https://coveralls.io/repos/github/marcogiusti/nvd3_py/badge.svg?branch=master
   :target: https://coveralls.io/github/marcogiusti/nvd3_py?branch=mast

.. |rtfd| image:: https://readthedocs.org/projects/nvd3-py/badge/?version=latest
   :target: http://nvd3-py.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
