# -*- test-case-name: test_nvd3 -*-
# Copyright (c) 2016 Marco Giusti
# See LICENSE for details.

__version__ = "0.1"


import json
import random
import textwrap


D3 = "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js"
NVD3 = "https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.3/nv.d3.min.js"
NVD3_CSS = "https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.3/nv.d3.min.css"


class Setter(object):

    def __init__(self, attr, mapping, raw=False):
        self.attr = attr
        self.mapping = mapping
        self.raw = raw

    def __call__(self, value):
        self.mapping[self.attr] = str(value) if self.raw else json.dumps(value)


class _Nvd3Customizable(object):

    _option_names = ()
    _raw_options = ()

    def __init__(self):
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


class Line(_Nvd3Customizable):

    _option_names = (
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
        # "getX",
        # "getY",
        # "dispatch",
    )
    _raw_options = (
        "x",
        "y",
        "color",
        # "getX",
        # "getY",
        # "dispatch",
    )


class Axis(_Nvd3Customizable):

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
    )
    _raw_options = (
        "scale",
    )


class Legend(_Nvd3Customizable):

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


class Tooltip(_Nvd3Customizable):

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
    name = "chart.tooltip"


class Focus(_Nvd3Customizable):

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


class Pie(_Nvd3Customizable):

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
    name = "chart.pie"


class Chart(_Nvd3Customizable):
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
    name = "chart"

    def __init__(self, data):
        _Nvd3Customizable.__init__(self)
        self.data = data
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

        # // depreciated after 1.7.1
        # pieLabelsOutside: {get: function(){return labelsOutside;}, set: function(_){
        # // depreciated after 1.7.1
        # donutLabelsOutside: {get: function(){return labelsOutside;}, set: function(_){
        # // deprecated after 1.7.1
        # labelFormat: {get: function(){ return valueFormat;}, set: function(_) {
        # // options that require extra logic in the setter
    )
    _raw_options = (
        "x",
        "y",
        "valueFormat",
        "color",
        # "state",
        # "dispatch"
    )

    def __init__(self, data):
        Chart.__init__(self, data)
        self.factory = "pieChart"
        self.tooltip = Tooltip()
        self.pie = Pie()

    def js_options(self):
        return "\n".join([Chart.js_options(self),
                          self.tooltip.js_options(),
                          self.pie.js_options()])


class Container(object):

    tpl = ('<div id="{self.chart.container_id}">'
           '<svg style="height:500px;width:400px"></svg>'
           '</div>')

    def __init__(self, chart, data_supplier):
        self.chart = chart
        self.data_supplier = data_supplier

    def html(self, chart):
        return self.tpl.format(self=self)

    def _ipython_display_(self):
        from IPython.display import display_javascript, display_html
        from IPython.display import Javascript

        display_html(self.html(self.chart), raw=True)
        js = Javascript(data=self.data_supplier.js(self.chart), lib=[D3, NVD3],
                        css=[NVD3_CSS])
        display_javascript(js)


class StaticDataSupplier(object):

    tpl = textwrap.dedent("""\
        nv.addGraph(function() {{
            var data_{chart.name} = {data};
            ({factory})(data_{chart.name});
        }});""")

    def __init__(self, data):
        self.data = data

    def js(self, chart):
        data = json.dumps(self.data)
        return self.tpl.format(data=data, chart=chart, factory=chart.js())
