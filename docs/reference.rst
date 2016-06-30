=========
Reference
=========


_Nvd3Customizable
=================

.. class:: nvd3._Nvd3Customizable(name)

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

.. class:: nvd3.Line(name)

   Represents a ``nv.models.line()`` in NVD3. Available properties:

   .. attribute:: width

      :Is raw: false.

   .. attribute:: height

      :Is raw: false.

   .. attribute:: defined

      Allows a line to be not continuous when it is not defined.

      :Is raw: true.

   .. attribute:: interpolate

      Set the interpolation mode. The possible values are listed in the
      d3's `line.interpolate()`_ documentation. Default: ``'linear'``.

      :Is raw: false.

      .. note:: As now ``interpolate`` accepts only ``str``.
      
   .. attribute:: clipEdge

      If ``True``, masks lines within x and y scale.

      :Is raw: false.

   .. attribute:: margin

      :Is raw: false.

   .. attribute:: duration

      :Is raw: false.

   .. attribute:: isArea

      Decides if a line is an area or just a line.

      :Is raw: true.

   .. attribute:: x

      Accessor to get the x value from a data point.

      :Is raw: true.

   .. attribute:: y

      Accessor to get the y value from a data point.

      :Is raw: true.

   .. attribute:: color

      A function that returns a color.

      :Is raw: true.

.. _line.interpolate(): https://github.com/d3/d3-3.x-api-reference/blob/master/SVG-Shapes#line_interpolate

.. class:: nvd3.Axis(name)

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

.. class:: nvd3.Legend(name)

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

.. class:: nvd3.Tooltip(name)

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

.. class:: nvd3.Focus(name)

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

.. class:: nvd3.Pie(name)

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

.. class:: nvd3.Chart()

   Chart base class. Instantiate the object and set the various
   properties.

   .. method:: js()

      Returns the JavaScript code that create the relative SVG chart.
      The whole code is enveloped in a function that accept the data of
      the chart and return the chart object.

.. class:: nvd3.PieChart()

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

.. class:: nvd3.LineChart()

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
