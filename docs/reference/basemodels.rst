===========
Base models
===========


_Model
======

.. class:: nvd3._Model(name)

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


NVD3 base models
================

.. class:: nvd3.Line(name)

   Represents a ``nv.models.line()`` in NVD3. Available properties:

   .. attribute:: width

      :Is raw: no.
      :type: ``int``.

   .. attribute:: height

      :Is raw: no.
      :type: ``int``.

   .. attribute:: defined

      Allows a line to be not continuous when it is not defined.

      :Is raw: yes.

   .. attribute:: interpolate

      Set the interpolation mode. The possible values are listed in the
      d3's `line.interpolate()`_ documentation. Default: ``'linear'``.

      :Is raw: no.

      .. note:: As now ``interpolate`` accepts only ``str``.
      
   .. attribute:: clipEdge

      If ``True``, masks lines within x and y scale.

      :Is raw: no.

   .. attribute:: margin

      Valid keys are: ``top``, ``right``, ``bottom`` and ``left``,
      values must be ``int``\ s.

      :Is raw: no.
      :type: ``dict``.

   .. attribute:: duration

      :Is raw: no.

   .. attribute:: isArea

      Decides if a line is an area or just a line.

      :Is raw: yes.

   .. attribute:: x

      Accessor to get the x value from a data point.

      :Is raw: yes.

   .. attribute:: y

      Accessor to get the y value from a data point.

      :Is raw: yes.

   .. attribute:: color

      A function that returns a color.

      :Is raw: yes.

.. _line.interpolate(): https://github.com/d3/d3-3.x-api-reference/blob/master/SVG-Shapes#line_interpolate

.. class:: nvd3.Axis(name)

   Represents a ``nv.models.axis()`` in NVD3. Available properties:

   .. attribute:: axisLabelDistance

      :Is raw: no.
      :type: ``int``.

   .. attribute:: staggerLabels

      :Is raw: no.
      :type: ``bool``.

   .. attribute:: rotateLabels

      :Is raw: no.
      :type: ``int``.

   .. attribute:: rotateYLabel

      :Is raw: no.
      :type: ``bool``.

   .. attribute:: showMaxMin

      :Is raw: no.
      :type: ``bool``.

   .. attribute:: axisLabel

      :Is raw: no.
      :type: ``str``.

   .. attribute:: height

      Only used for tickLabel currently.

      :Is raw: no.
      :type: ``int``.

   .. attribute:: ticks

      Control how ticks are generated for the axis.

      :Is raw: no.
      :type: ``int``.

      .. TODO: control this

   .. attribute:: width

      Only used for tickLabel currently.

      :Is raw: no.
      :type: ``int``.

   .. attribute:: fontSize

      :Is raw: no.
      :type: ``str``.

   .. attribute:: margin

      See :attr:`nvd3.Line.margin` for a valid format.

      :Is raw: no.

   .. attribute:: duration
   .. attribute:: scale
   .. attribute:: dispatch
   .. attribute:: isOrdinal
   .. attribute:: orient
   .. attribute:: tickValues
   .. attribute:: tickSubdivide
   .. attribute:: tickSize
   .. attribute:: tickPadding
   .. attribute:: tickFormat
   .. attribute:: domain
   .. attribute:: range
   .. attribute:: rangeBand
   .. attribute:: rangeBands

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
