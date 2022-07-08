#!/usr/bin/env python

"""
VectorDrawable2Svg
This script convert your VectorDrawable to a Svg

Usage: drop one or more vector drawable onto this script to convert them to svg format
"""

from xml.dom.minidom import Document, parse
import sys

def convert_paths(vd_container,svg_container,svg_xml):
    vd_paths = vd_container.getElementsByTagName('path')
    for vd_path in vd_paths:
        atributes = vd_path.attributes

        if vd_path.parentNode == vd_container:
            svg_path = svg_xml.createElement('path')
            svg_path.attributes['d'] = atributes['android:pathData'].value
        if vd_path.hasAttribute('android:fillColor'):
            svg_path.attributes['fill'] = atributes['android:fillColor'].value
        else:
            svg_path.attributes['fill'] = 'none'
        if vd_path.hasAttribute('android:strokeLineJoin'):
            svg_path.attributes['stroke-linejoin'] = atributes['android:strokeLineJoin'].value
        if vd_path.hasAttribute('android:strokeLineCap'):
            svg_path.attributes['stroke-linecap'] = atributes['android:strokeLineCap'].value
        if vd_path.hasAttribute('android:strokeMiterLimit'):
            svg_path.attributes['stroke-miterlimit'] = atributes['android:strokeMiterLimit'].value
        if vd_path.hasAttribute('android:strokeWidth'):
            svg_path.attributes['stroke-width'] = atributes['android:strokeWidth'].value
        if vd_path.hasAttribute('android:strokeColor'):
            svg_path.attributes['stroke'] = atributes['android:strokeColor'].value
        svg_container.appendChild(svg_path)


def convert_vd(vd_file_path):

    svg_xml = Document()
    svg_node = svg_xml.createElement('svg')
    svg_xml.appendChild(svg_node)
    vd_xml = parse(vd_file_path)
    vd_node = vd_xml.getElementsByTagName('vector')[0]

    svg_node.attributes['xmlns'] = 'http://www.w3.org/2000/svg'
    svg_node.attributes['width'] = vd_node.attributes['android:viewportWidth'].value
    svg_node.attributes['height'] = vd_node.attributes['android:viewportHeight'].value
    svg_node.attributes['viewBox'] = "0 0 {vd_node.attributes['android:viewportWidth'].value} {vd_node.attributes['android:viewportHeight'].value}"

    vd_groups = vd_xml.getElementsByTagName('group')
    for vd_group in vd_groups:
        svg_group = svg_xml.createElement('g')
        if vd_group.hasAttribute('android:translateX'):
            svg_group.attributes['transform'] = f"translate({vd_group.attributes['android:translateX'].value},{vd_group.attributes['android:translateY'].value})"
        convert_paths(vd_group,svg_group,svg_xml)
        svg_node.appendChild(svg_group)

    convert_paths(vd_node, svg_node, svg_xml)

    svg_xml.writexml(open(vd_file_path + '.svg', 'w'),indent="",addindent="  ",newl='\n')

if len(sys.argv)>1:
    iterArgs = iter(sys.argv)
    next(iterArgs)
    for arg in iterArgs:
        convert_vd(arg)
else:
    print("You have to pass me something")
    sys.exit()
