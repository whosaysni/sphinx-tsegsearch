sphinx-tsegsearch
===================

A Sphinx extension for tokenize japanese query word with TinySegmenter.js

This extension tweaks searchtools.js of sphinx-generated html document
to tokenize Japanese composite words.

Since Japanese is an agglutinative language, query word for document search
usually becomes composite form like 'システム標準' (system standard).
This makes difficult to search pages containing phrase such as
'システムの標準', '標準システム', because TinySegmenter.py (Sphinx's default
Japanese index tokenizer) tokenizes 'システム' and '標準' as indexes.

sphinx-tsegsearch patches searchtools.js to override query tokinization
step so that query input is re-tokenized by TinySegmenter.js (original
JavaScript implementation of TinySegmenter).
As a result, roughly say, this tiny hack improves recall of Japanese
document search in exchange of precision.

Usage:

#. Add 'sphinx_tsegsearch' in conf.extensions
#. Rebuild document.
