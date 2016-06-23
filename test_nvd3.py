# Copyright (c) 2016 Marco Giusti
# See LICENSE for details.


import json
import textwrap
import unittest

import nvd3


class MyCls(nvd3._Nvd3Customizable):

    _option_names = ("a", "b")
    _raw_options = ("a", )


class TestCustomizable(unittest.TestCase):

    def test_invalid_option(self):
        obj = MyCls("myobj")
        with self.assertRaises(AttributeError):
            obj.c

    def test_set_raw(self):
        obj = MyCls("myobj")
        f = "function() { alert(boom); }"
        obj.a(f)
        self.assertEqual(obj._options["a"], f)

    def test_set_data(self):
        obj = MyCls("myobj")
        m = {"a": 42}
        obj.b(m)
        self.assertIsInstance(obj._options["b"], str)
        self.assertEqual(json.loads(obj._options["b"]), m)

    def test_js_options(self):
        obj = MyCls("myobj")
        obj.a("() => alert('boom')")
        obj.b({"a": 42})
        exp = "myobj.a(() => alert('boom'));\nmyobj.b({\"a\": 42});"
        self.assertMultiLineEqual(obj.js_options(), exp)
        # self.assertEqual(obj.js_options(), exp)


class TestPieChart(unittest.TestCase):

    def test_pie(self):
        chart = nvd3.PieChart()
        chart.pie.width(400)
        self.assertEqual(chart.pie._options["width"], "400")

    def test_set_pie_option(self):
        chart = nvd3.PieChart()
        chart.pie.width(400)
        rendered = chart.js()
        self.assertIn("chart.pie.width(400)", rendered)
