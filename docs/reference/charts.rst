======
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
