# -*- test-case-name: test_nvd3 -*-
# Copyright (c) 2016 Marco Giusti
# See LICENSE for details.

__version__ = "0.1"


import json
import random
import textwrap


D3 = "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js"
NVD3 = "https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.4/nv.d3.min.js"
NVD3_CSS = "https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.4/nv.d3.min.css"


class Setter(object):

    def __init__(self, attr, mapping, raw=False):
        self.attr = attr
        self.mapping = mapping
        self.raw = raw

    def __call__(self, value):
        self.mapping[self.attr] = str(value) if self.raw else json.dumps(value)


class _Model(object):

    _option_names = ()
    _raw_options = ()

    def __init__(self, name):
        self.name = name
        self._options = {}

    def __getattr__(self, name):
        if name in self._option_names:
            raw = name in self._raw_options
            return Setter(name, self._options, raw)
        raise AttributeError(name)

    def js_options(self):
        name = self.name
        lines = []
        for opt, value in self._options.iteritems():
            lines.append("{name}.{opt}({value});".format(**locals()))
        return "\n".join(lines)


class Line(_Model):

    _option_names = (
        # TODO: scatter
        "width",
        "height",
        "defined",
        "interpolate",
        "clipEdge",
        "margin",
        "duration",
        "isArea",
        "x",
        "y",
        "color",
        #
        # "strokeWidth",
        # "dispatch",
    )
    _raw_options = (
        "defined",
        "isArea",
        "x",
        "y",
        "color",
        # "dispatch",
    )


class Axis(_Model):

    _option_names = (
        "axisLabelDistance",
        "staggerLabels",
        "rotateLabels",
        "rotateYLabel",
        "showMaxMin",
        "axisLabel",
        "height",
        "ticks",
        "width",
        "fontSize",
        "margin",
        "duration",
        "scale",
        # "dispatch",
        # "isOrdinal",

        # TODO: check
        "orient",
        "tickValues",
        "tickSubdivide",
        "tickSize",
        "tickPadding",
        "tickFormat",
        "domain",
        "range",
        "rangeBand",
        "rangeBands",
    )
    _raw_options = (
        "scale",
        "tickFormat",
    )


class Legend(_Model):

    _option_names = (
        "width",
        "height",
        "key",
        "keyFormatter",
        "align",
        "maxKeyLength",
        "rightAlign",
        "padding",
        "radioButtonMode",
        "expanded",
        "vers",
        "margin",
        "color",

        "updateState",
    )
    _raw_options = (
        "key",
        "keyFormatter",
        "color",
    )


class Tooltip(_Model):

    _option_names = (
        "duration",
        "gravity",
        "distance",
        "snapDistance",
        "classes",
        "enabled",
        "hideDelay",
        "contentGenerator",
        "valueFormatter",
        "headerFormatter",
        "keyFormatter",
        "headerEnabled",
        "position",
    )


class Focus(_Model):

    _option_names = (
        "width",
        "height",
        "showXAxis",
        "showYAxis",
        "brushExtent",
        "margin",
        "duration",
        "color",
        "interpolate",
        "xTickFormat",
        "yTickFormat",
        "x",
        "y",
        "rightAlignYAxis",
    )
    _raw_options = (
        "color",
        "interpolate",
        "xTickFormat",
        "yTickFormat",
        "x",
        "y",
    )


class Pie(_Model):

    _option_names = (
        "arcsRadius",
        "width",
        "height",
        "showLabels",
        "title",
        "titleOffset",
        "labelThreshold",
        "valueFormat",
        "x",
        "id",
        "endAngle",
        "startAngle",
        "padAngle",
        "cornerRadius",
        "donutRatio",
        "labelsOutside",
        "labelSunbeamLayout",
        "donut",
        "growOnHover",
        "margin",
        "y",
        "color",
        "labelType",
    )
    _raw_options = (
        "x",
        "y",
        "color",
        "valueFormat",
        "dispatch",
    )


class Scatter(_Model):

    _option_names = (
        "width",
        "height",
        "xScale",
        "yScale",
        "pointScale",
        "xDomain",
        "yDomain",
        "pointDomain",
        "xRange",
        "yRange",
        "pointRange",
        "forceX",
        "forceY",
        "forcePoint",
        "interactive",
        "pointActive",
        "padDataOuter",
        "padData",
        "clipEdge",
        "clipVoronoi",
        "clipRadius",
        "showVoronoi",
        "id",
        "interactiveUpdateDelay",
        "showLabels",
        "x",
        "y",
        "pointSize",
        "pointShape",
        "margin",
        "duration",
        "color",
        "useVoronoi",
    )
    _raw_options = (
        "x",
        "y",
        "pointSize",
        "pointShape",
    )


class Distribution(_Model):

    _option_names = (
    )
    _raw_options = (
    )


class MultiBar(_Model):

    _option_names = (
        "width",
        "height",
        "x",
        "y",
        "xScale",
        "yScale",
        "xDomain",
        "yDomain",
        "xRange",
        "yRange",
        "forceY",
        "stacked",
        "stackOffset",
        "clipEdge",
        "disabled",
        "id",
        "hideable",
        "groupSpacing",
        "fillOpacity",
        "margin",
        "duration",
        "color",
        "barColor",
    )
    _raw_options = (
        "x",
        "y",
    )


class InteractiveGuideline(_Model):

    _option_names = ()
    _raw_options = ()


class StackedArea(_Model):

    _option_names = (
        "width",
        "height",
        "defined",
        "clipEdge",
        "offset",
        "order",
        "interpolate",
        "x",
        "y",
        "margin",
        "color",
        "style",
        "duration"
    )
    _raw_options = (
        "x",
        "y",
    )


class DiscreteBar(_Model):

    _option_names = (
        "width",
        "height",
        "forceY",
        "showValues",
        "x",
        "y",
        "xScale",
        "yScale",
        "xDomain",
        "yDomain",
        "xRange",
        "yRange",
        "valueFormat",
        "id",
        "rectClass",
        "margin",
        "color",
        "duration"
    )
    _raw_option = (
        "x",
        "y",
    )


class Chart(_Model):
    # Abstract class

    tpl = textwrap.dedent("""\
        function(data) {{
            var {self.name} = nv.models.{self.factory}();
            {options}

            d3.select("#{self.container_id} svg")
                .datum(data)
                .transition().duration(350)
                .call({self.name});

            return {self.name};
        }}""")

    def __init__(self):
        _Model.__init__(self, name="chart")
        self.container_id = "nvd3_chart_" + str(random.randint(0, 2**10))

    def js(self):
        options = self.js_options()
        return self.tpl.format(self=self, options=options)


class PieChart(Chart):

    _option_names = (
        "arcsRadius",
        "width",
        "height",
        "showLabels",
        "title",
        "titleOffset",
        "labelThreshold",
        "valueFormat",
        "x",
        "id",
        "endAngle",
        "startAngle",
        "padAngle",
        "cornerRadius",
        "donutRatio",
        "labelsOutside",
        "labelSunbeamLayout",
        "donut",
        "growOnHover",
        "margin",
        "y",
        "color",
        "labelType",
    )
    _raw_options = (
        "x",
        "y",
        "valueFormat",
        "color",
        # "state",
        # "dispatch"
    )

    def __init__(self):
        Chart.__init__(self)
        self.factory = "pieChart"
        self.tooltip = Tooltip(self.name + ".tooltip")
        self.pie = Pie(self.name + ".pie")

    def js_options(self):
        return "\n".join([Chart.js_options(self),
                          self.tooltip.js_options(),
                          self.pie.js_options()])


class LineChart(Chart):

    _option_names = (
        "width",
        "height",
        "showLegend",
        "legendPosition",
        "showXAxis",
        "showYAxis",
        "rightAlignYAxis",
        "useInteractiveGuideline",
        "x",
        "y",
        "focusEnable",
        # "defaultState",
        "noData",
        # "focusHeight",
        # "focusShowAxisX",
        # "focusShowAxisY",
        # "brushExtent",
        "focusMargin",
        "margin",
        "duration",
        # "color",
        # "interpolate",
        "xTickFormat",
        "yTickFormat",
    )
    _raw_options = (
        "x",
        "y",
        "noData",
        # "color",
        "xTickFormat",
        "yTickFormat",
    )
    factory = "lineChart"

    def __init__(self):
        Chart.__init__(self)
        self.xaxis = Axis(self.name + ".xAxis")
        self.yaxis = Axis(self.name + ".yAxis")
        self.legend = Legend(self.name + ".legend")
        # self.interactive_layer = InteractiveGuideLine()
        self.tooltip = Tooltip(self.name + ".tooltip")
        # self.focus = Focus(Line())

    def js_options(self):
        return "\n".join([Chart.js_options(self),
                          self.xaxis.js_options(),
                          self.yaxis.js_options(),
                          self.legend.js_options(),
                          # self.interactive_layer.js_options(),
                          self.tooltip.js_options(),
                          # self.focus.js_options(),
                         ])


class ScatterChart(Chart):

    _option_names = (
        "width",
        "height",
        # "container",
        "showDistX",
        "showDistY",
        "showLegend",
        "showXAxis",
        "showYAxis",
        # "defaultState",
        "noData",
        "duration",
        "showLabels",
        "margin",
        # "rightAlignYAxis",
        "color",
    )
    _raw_options = (
        "noData",
        "color",
    )
    factory = "scatterChart"

    def __init__(self):
        Chart.__init__(self)
        self.scatter = Scatter(self.name + ".scatter")
        self.xaxis = Axis(self.name + ".xAxis")
        self.yaxis = Axis(self.name + ".yAxis")
        self.legend = Legend(self.name + ".legend")
        self.distx = Distribution(self.name + ".distX")
        self.disty = Distribution(self.name + ".distY")
        self.tooltip = Tooltip(self.name + ".tooltip")

    def js_options(self):
        return "\n".join([Chart.js_options(self),
                          self.scatter.js_options(),
                          self.xaxis.js_options(),
                          self.yaxis.js_options(),
                          self.legend.js_options(),
                          self.distx.js_options(),
                          self.disty.js_options(),
                          self.tooltip.js_options()
                         ])


class StackedAreaChart(Chart):

    _option_names = (
        "width",
        "height",
        "showLegend",
        "showXAxis",
        "showYAxis",
        "defaultState",
        "noData",
        "showControls",
        "controlLabels",
        "controlOptions",
        "showTotalInTooltip",
        "totalLabel",
        "focusEnable",
        "focusHeight",
        "brushExtent",
        "margin",
        "focusMargin",
        "duration",
        "color",
        "x",
        "y",
        "rightAlignYAxis",
        "useInteractiveGuideline",
    )
    _raw_options = (
        # "noData",
        # "color",
        "x",
        "y",
    )
    factory = "stackedAreaChart"

    def __init__(self):
        Chart.__init__(self)
        self.stacked = StackedArea(self.name + ".stacked")
        self.xaxis = Axis(self.name + ".xAxis")
        self.yaxis = Axis(self.name + ".yAxis")
        self.legend = Legend(self.name + ".legend")
        self.controls = Legend(self.name + ".controls")
        # self.interactiveLayer = nv.interactiveGuideline()
        self.tooltip = Tooltip(self.name + ".tooltip")
        # self.focus = nv.models.focus(nv.models.stackedArea())

    def js_options(self):
        return "\n".join([Chart.js_options(self),
                          self.stacked.js_options(),
                          self.xaxis.js_options(),
                          self.yaxis.js_options(),
                          self.legend.js_options(),
                          self.controls.js_options(),
                          # self.interactiveLayer.js_options(),
                          self.tooltip.js_options(),
                          # self.focus.js_options()
                         ])


class DiscreteBarChart(Chart):

    _option_names = (
        "width",
        "height",
        "showLegend",
        "staggerLabels",
        "rotateLabels",
        "wrapLabels",
        "showXAxis",
        "showYAxis",
        "noData",
        "margin",
        "duration",
        "color",
        "x",
        "y",

        # "defaultState",
        # "showControls",
        # "controlLabels",
        # "controlOptions",
        # "showTotalInTooltip",
        # "totalLabel",
        # "focusEnable",
        # "focusHeight",
        # "brushExtent",
        # "focusMargin",
        # "rightAlignYAxis",
        # "useInteractiveGuideline",
    )
    _raw_options = (
        # "noData",
        # "color",
        "x",
        "y",
    )
    factory = "discreteBarChart"

    def __init__(self):
        Chart.__init__(self)
        self.discretebar = DiscreteBar(self.name + ".discretebar")
        self.xAxis = Axis(self.name + ".xAxis")
        self.yAxis = Axis(self.name + ".yAxis")
        self.legend = Legend(self.name + ".legend")
        self.tooltip = Tooltip(self.name + ".tooltip")

    def js_options(self):
        return "\n".join([Chart.js_options(self),
                          self.discretebar.js_options(),
                          self.xAxis.js_options(),
                          self.yAxis.js_options(),
                          self.legend.js_options(),
                          self.tooltip.js_options(),
                         ])


class MultiBarChart(Chart):

    _option_names = (
        "width",
        "height",
        "showLegend",
        "showControls",
        "controlLabels",
        "showXAxis",
        "showYAxis",
        "defaultState",
        "noData",
        "reduceXTicks",
        "rotateLabels",
        "staggerLabels",
        "wrapLabels",
        "margin",
        "duration",
        "color",
        "rightAlignYAxis",
        "useInteractiveGuideline",
        "barColor",
    )
    factory = "multiBarChart"

    def __init__(self):
        Chart.__init__(self)
        self.multibar = MultiBar(self.name + ".multibar")
        self.xaxis = Axis(self.name + ".xAxis")
        self.yaxis = Axis(self.name + ".yAxis")
        self.interactive_layer = InteractiveGuideline(self.name +
                                                      ".interactiveLayer")
        self.legend = Legend(self.name + ".legend")
        self.controls = Legend(self.name + ".controls")
        self.tooltip = Tooltip(self.name + ".tooltip")

    def js_options(self):
        return "\n".join([Chart.js_options(self),
                          self.multibar.js_options(),
                          self.xaxis.js_options(),
                          self.yaxis.js_options(),
                          self.interactive_layer.js_options(),
                          self.legend.js_options(),
                          self.controls.js_options(),
                          self.tooltip.js_options(),
                         ])


def _str_dimention(val):
    val = str(val)
    if not val.endswith(("%", "px")):
        val += "px"
    return val


def style_dimentions(width=None, height=None):
    style = w = h = ""
    if width is not None:
        width = _str_dimention(width)
        w = "width:{0};".format(width)
    if height is not None:
        height = _str_dimention(height)
        h = "height:{0};".format(height)
    if w or h:
        style = 'style="{w}{h}"'.format(w=w, h=h)
    return style


class Container(object):

    tpl = ('<div id="{self.chart.container_id}">'
           '<svg {self.style}></svg>'
           '</div>'
           '<script>{jscode}</script>')

    def __init__(self, chart, data_supplier, width=400, height=500):
        self.chart = chart
        self.data_supplier = data_supplier
        self.style = style_dimentions(width, height)

    def html(self):
        code = self.data_supplier.js(self.chart)
        return self.tpl.format(self=self, jscode=code)

    def js(self):
        return ('<script src="' + D3 + '"></script>\n'
                '<script src="' + NVD3 + '"></script>')

    def css(self):
        t = '<link rel="stylesheet" type="text/css" href="' + NVD3_CSS + '"/>'
        return t


class IPythonContainer(object):

    tpl = textwrap.dedent("""\
            <div id="{self.chart.container_id}">
                <svg {self.style}></svg>
            </div>
            """)

    def __init__(self, chart, data_supplier, width=None, height=None):
        self.chart = chart
        self.data_supplier = data_supplier
        self.style = style_dimentions(width, height)

    def html(self):
        return self.tpl.format(self=self)

    def js(self):
        return self.data_supplier.js(self.chart)

    def _ipython_display_(self):
        from IPython.display import display_javascript, display_html
        from IPython.display import Javascript

        jscode = self.js()
        display_javascript(Javascript(jscode, lib=[D3, NVD3], css=[NVD3_CSS]))
        display_html(self.html(), raw=True)


def render_data_supplier(self, chart):
    return self.tpl.format(self=self, chart=chart, factory=chart.js())


class StaticDataSupplier(object):

    tpl = textwrap.dedent("""\
        nv.addGraph(function() {{
            var data_{chart.name} = {self.data};
            ({factory})(data_{chart.name});
        }});""")

    def __init__(self, data):
        self.data = json.dumps(data)

    def js(self, chart):
        return render_data_supplier(self, chart)


class JsonDataSupplier(object):

    tpl = textwrap.dedent("""\
        d3.json('{self.url}', function(error, data) {{
            {self.error_handler}
            nv.addGraph(function() {{
                return ({factory})(data);
            }});
        }});""")

    def __init__(self, url, error_handler=""):
        self.url = url
        self.error_handler = error_handler

    def js(self, chart):
        return render_data_supplier(self, chart)
