# Copyright (c) 2016 Marco Giusti
# See LICENSE for details.

from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

import nvd3


CSS_TAG = '<link rel="stylesheet" href="{0}"/>'
JS_TAG = '<script src="{0}"></script>'

register = template.Library()


@register.simple_tag
def nvd3_static(use_cdnjs=False):
    """
    Load the required JavaScript and CSS files.

    Usage::

        <html>
        <head>
            ...
            {# serve the static files yourself... #}
            {% nvd3_static %}
            {# ...or use cdnjs #}
            {% nvd3_static use_cdnjs=True %}
            ...
        </head>
        <body>
            ...
    """

    if use_cdnjs:
        d3js = JS_TAG.format(nvd3.D3)
        nvd3js = JS_TAG.format(nvd3.NVD3)
        cssjs = CSS_TAG.format(nvd3.NVD3_CSS)
    else:
        d3js = JS_TAG.format(static("django_nvd3/d3.min.js"))
        nvd3js = JS_TAG.format(static("django_nvd3/nv.d3.min.js"))
        cssjs = CSS_TAG.format(static("django_nvd3/nv.d3.min.css"))
    return mark_safe("\n".join([d3js, nvd3js, cssjs]))


@register.simple_tag
def nvd3_static_data(chart, data, width=500, height=400):
    """
    Include the chart in the page with the given data.

    :param chart: The chart to render.
    :type chart: :class:`nvd3.Chart`
    :param data: the data to pass to the chart.
    :param width: SVG tag width.
    :param height: SVG tag height.

    Usage::

        {% nvd3_static_data chart data 400 300 %}
    """

    supplier = nvd3.StaticDataSupplier(data)
    container = nvd3.Container(chart, supplier, width, height)
    return mark_safe(container.html())


@register.simple_tag
def nvd3_remote_json(chart, url, width=400, height=500):
    """
    Include the chart in the page loading the data from a server.

    :param chart: The chart to render.
    :type chart: :class:`nvd3.Chart`
    :param str url: the url where to retrieve the data.
    :param width: SVG tag width.
    :param height: SVG tag height.

    Usage::

        {% nvd3_remote_json chart url 400 300 %}
    """

    supplier = nvd3.JsonDataSupplier(url)
    container = nvd3.Container(chart, supplier, width, height)
    return mark_safe(container.html())
