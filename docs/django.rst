==================
Django integration
==================


The package includes a Django app to help integrating nvd3_py in Django.


Quick start
===========

1. Add "django_nvd3" to your INSTALLED_APPS settings like this:

.. code-block:: python

   INSTALLED_APPS = [
      ...
      "django_nvd3",
   ]

2. Load the tags in your template:

.. code-block:: django

   {% load nvd3_tags %}

3. Use it.


Reference
=========

.. autofunction:: django_nvd3.templatetags.nvd3_tags.nvd3_static
.. autofunction:: django_nvd3.templatetags.nvd3_tags.nvd3_static_data
.. autofunction:: django_nvd3.templatetags.nvd3_tags.nvd3_remote_json
