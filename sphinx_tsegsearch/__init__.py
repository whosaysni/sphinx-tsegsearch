# -*- coding: utf-8 -*-
import os

import sphinx
from sphinx.jinja2glue import SphinxFileSystemLoader
from sphinx.search.ja import SearchJapanese

_extdir = os.path.dirname(os.path.abspath(__file__))
_jsdir = os.path.join(_extdir, 'static')

with open(os.path.join(_jsdir, 'splitQuery.js')) as js:
    js_splitter_code = js.read()


class SearchJapaneseWithJSSplitter(SearchJapanese):
    js_splitter_code = js_splitter_code


def setup(app):
    def builder_inited(app_):
        if app_.builder.name != 'html':
            return

        if 'version_info' in dir(sphinx) and sphinx.version_info >= (1, 8):
            add_js_file = app_.add_js_file
        else:
            add_js_file = app_.add_javascript
        app_.builder.config.html_static_path.append(_jsdir)
        add_js_file('tiny_segmenter.js')

        if 'version_info' in dir(sphinx) and sphinx.version_info >= (3, 0, 0):
            app_.add_search_language(SearchJapaneseWithJSSplitter)
        else:
            templatedir = os.path.join(_extdir, 'templates')

            loader = app_.builder.templates
            loader.pathchain.insert(1, templatedir)
            loader.loaders.insert(1, SphinxFileSystemLoader(templatedir))
            loader.templatepathlen += 1

            add_js_file('splitQuery.js')

    app.connect('builder-inited', builder_inited)
