# -*- coding: utf-8 -*-
import os
from sphinx.jinja2glue import SphinxFileSystemLoader

def builder_inited(app):
    extdir = os.path.dirname(os.path.abspath(__file__))
    jsdir = os.path.join(extdir, 'static')
    app.builder.config.html_static_path.append(jsdir)

    loader = app.builder.templates
    templatedir = os.path.join(extdir, 'templates')
    loader.pathchain.insert(0, templatedir)
    loader.loaders.insert(0, SphinxFileSystemLoader(templatedir))
    loader.templatepathlen += 1

def setup(app):
    app.connect('builder-inited', builder_inited)
    app.add_javascript('tiny_segmenter.js')

