# -*- coding: utf-8 -*-
import os
from sphinx.jinja2glue import SphinxFileSystemLoader

def setup(app):

    def builder_inited(app_):
        if app_.builder.name != 'html':
            return
        extdir = os.path.dirname(os.path.abspath(__file__))
        templatedir = os.path.join(extdir, 'templates')
        jsdir = os.path.join(extdir, 'static')
        loader = app_.builder.templates
        loader.pathchain.insert(0, templatedir)
        loader.loaders.insert(0, SphinxFileSystemLoader(templatedir))
        loader.templatepathlen += 1
        app_.builder.config.html_static_path.append(jsdir)
        app_.add_javascript('tiny_segmenter.js')
    app.connect('builder-inited', builder_inited)
