=========
Reference
=========


_Nvd3Customizable
=================

.. class:: _Nvd3Customizable(name)

   This class represent a model in NVS3. A model in NVD3 is an object
   with some settable options. These options are callables, to be more
   correct, they are setters. In python they are setters too: if you
   normally write ``chart.showLabels(true)`` in JavaScript, this become
   ``chart.showLabels(True)`` in Python.

   .. attribute:: name

      The name of the object. It is in the form ``myobj`` for the main
      objects and in the form ``myobj.attr`` for the attributes.
   
   .. attribute:: _option_names

      Tuple of options that the model supports.

   .. attribute:: _raw_options

      Tuple of raw options that should not be trasformed in some kind of
      javascript object.

   .. method:: js_options()

      Returns the JavaScript representation of this model. This
      representation does not instantiate the object but is a collection
      of function calls to set the properties of the object.


Base models
===========

.. class:: Line(name)

   Represents a ``nv.models.line()`` in NVD3. Available properties:
      
   - ``width``
   - ``height``
   - ``defined``
   - ``interpolate``
   - ``clipEdge``
   - ``margin``
   - ``duration``
   - ``isArea``
   - ``x``
   - ``y``
   - ``color``

.. class:: Axis(name)

   Represents a ``nv.models.axis()`` in NVD3. Available properties:

   - ``axisLabelDistance``
   - ``staggerLabels``
   - ``rotateLabels``
   - ``rotateYLabel``
   - ``showMaxMin``
   - ``axisLabel``
   - ``height``
   - ``ticks``
   - ``width``
   - ``fontSize``
   - ``margin``
   - ``duration``
   - ``scale``
   - ``dispatch``
   - ``isOrdinal``
   - ``orient``
   - ``tickValues``
   - ``tickSubdivide``
   - ``tickSize``
   - ``tickPadding``
   - ``tickFormat``
   - ``domain``
   - ``range``
   - ``rangeBand``
   - ``rangeBands``

.. class:: Legend(name)

   Represents a ``nv.models.legend()`` in NVD3. Available properties:

   - ``width``
   - ``height``
   - ``key``
   - ``keyFormatter``
   - ``align``
   - ``maxKeyLength``
   - ``rightAlign``
   - ``padding``
   - ``radioButtonMode``
   - ``expanded``
   - ``vers``
   - ``margin``
   - ``color``
   - ``updateState``

.. class:: Tooltip(name)

   Represents a ``nv.models.tooltip()`` in NVD3. Available properties:

   - ``duration``
   - ``gravity``
   - ``distance``
   - ``snapDistance``
   - ``classes``
   - ``enabled``
   - ``hideDelay``
   - ``contentGenerator``
   - ``valueFormatter``
   - ``headerFormatter``
   - ``keyFormatter``
   - ``headerEnabled``
   - ``position``

.. class:: Focus(name)

   Represents a ``nv.models.focus()`` in NVD3. Available properties:

   - ``width``
   - ``height``
   - ``showXAxis``
   - ``showYAxis``
   - ``brushExtent``
   - ``margin``
   - ``duration``
   - ``color``
   - ``interpolate``
   - ``xTickFormat``
   - ``yTickFormat``
   - ``x``
   - ``y``
   - ``rightAlignYAxis``

.. class:: Pie(name)

   Represents a ``nv.models.pie()`` in NVD3. Available properties:

   - ``arcsRadius``
   - ``width``
   - ``height``
   - ``showLabels``
   - ``title``
   - ``titleOffset``
   - ``labelThreshold``
   - ``valueFormat``
   - ``x``
   - ``id``
   - ``endAngle``
   - ``startAngle``
   - ``padAngle``
   - ``cornerRadius``
   - ``donutRatio``
   - ``labelsOutside``
   - ``labelSunbeamLayout``
   - ``donut``
   - ``growOnHover``
   - ``margin``
   - ``y``
   - ``color``
   - ``labelType``


Charts
======

.. class:: Chart()

   Chart base class. Instantiate the object and set the various
   properties.

   .. method:: js()

      Returns the JavaScript code that create the relative SVG chart.
      The whole code is enveloped in a function that accept the data of
      the chart and return the chart object.

.. class:: PieChart()

   Represents a ``nv.models.pieChart()`` in NVD3. Available properties:

   - ``arcsRadius``
   - ``width``
   - ``height``
   - ``showLabels``
   - ``title``
   - ``titleOffset``
   - ``labelThreshold``
   - ``valueFormat``
   - ``x``
   - ``id``
   - ``endAngle``
   - ``startAngle``
   - ``padAngle``
   - ``cornerRadius``
   - ``donutRatio``
   - ``labelsOutside``
   - ``labelSunbeamLayout``
   - ``donut``
   - ``growOnHover``
   - ``margin``
   - ``y``
   - ``color``
   - ``labelType``

.. class:: LineChart()

   Represents a ``nv.models.lineChart()`` in NVD3. Available properties:

   - ``width``
   - ``height``
   - ``showLegend``
   - ``legendPosition``
   - ``showXAxis``
   - ``showYAxis``
   - ``rightAlignYAxis``
   - ``useInteractiveGuideline``
   - ``x``
   - ``y``
   - ``focusEnable``
   - ``defaultState``
   - ``noData``
   - ``focusHeight``
   - ``focusShowAxisX``
   - ``focusShowAxisY``
   - ``brushExtent``
   - ``focusMargin``
   - ``margin``
   - ``duration``
   - ``color``
   - ``interpolate``
   - ``xTickFormat``
   - ``yTickFormat``


Data suppliers
==============

.. TODO


Containers
==========

.. TODO
