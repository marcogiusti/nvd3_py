===================================
Welcome to nvd3_py's documentation!
===================================

The goal of this project is to offer a simple API to create NVD3_
charts. Simple, in this context, means an API that mimics the NVD3's
one. Look at this simple comparison from `NVD3's pie chart example`_:

.. code-block:: javascript

   // Regular pie chart example
   nv.addGraph(function() {
     var chart = nv.models.pieChart()
         .x(function(d) { return d.label })
         .y(function(d) { return d.value })
         .showLabels(true);

       d3.select("#chart svg")
           .datum(exampleData())
           .transition().duration(350)
           .call(chart);

     return chart;
   });

   // Pie chart example data. Note how there is only a single array of
   // key-value pairs.
   function exampleData() {
     return  [
         { 
           "label": "One",
           "value" : 29.765957771107
         } , 
         { 
           "label": "Two",
           "value" : 0
         } , 
         { 
           "label": "Three",
           "value" : 32.807804682612
         } , 
         { 
           "label": "Four",
           "value" : 196.45946739256
         } , 
         { 
           "label": "Five",
           "value" : 0.19434030906893
         } , 
         { 
           "label": "Six",
           "value" : 98.079782601442
         } , 
         { 
           "label": "Seven",
           "value" : 13.925743130903
         } , 
         { 
           "label": "Eight",
           "value" : 5.1387322875705
         }
       ];
   }


`Python version`_ (values are trimmed for simplicity):

.. code-block:: python

   import nvd3

   # prepare the data
   x = ["One", "Two", "Three", "Four", "Five", "Six", "Seven","Eight"]
   y = [29.76, 0, 32.80, 196.45, 0.19, 98.07, 13.92, 5.138]
   data = [{"label": l, "value": v} for l, v in zip(x, y)]
   # build the chart
   pie_chart = nvd3.PieChart()
   pie_chart.x("function(d) { return d.label; }")
   pie_chart.y("function(d) { return d.value; }")
   pie_chart.showLabels(True)
   # show the HTML
   data_supplier = nvd3.StaticDataSupplier(data)
   nvd3.Container(pie_chart, data_supplier)


Installation
============

The package will not published to PyPI until an acceptable stability and
completeness is reached. The package could be anyway installed using
`pip+git`_:

.. code-block:: console

   $ pip install git+https://github.com/marcogiusti/nvd3_py@master#egg=nvd3_py


Development
===========

The development take place in Github_. The code is still incomplete,
undocumented and not tested, use it with care.


Contents:
=========

.. toctree::
   :maxdepth: 2

   django
   reference
   examples/index


.. _NVD3: http://nvd3.org/
.. _NVD3's pie chart example: http://nvd3.org/examples/pie.html
.. _Python version: https://github.com/marcogiusti/nvd3_py/blob/master/examples/pie_chart.ipynb
.. _Github: https://github.com/marcogiusti/nvd3_py
.. _pip+git: https://pip.pypa.io/en/stable/reference/pip_install/#git
