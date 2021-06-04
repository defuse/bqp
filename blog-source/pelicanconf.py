#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Taylor Hornby'
SITENAME = 'BQP'

# Use relative paths.
SITEURL = 'https://bqp.io'
# For the staging environment. ./render-publish.sh changes this!
RELATIVE_URLS = True

# All of the blog posts go in .md files inside content/.
PATH = 'content'

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'en'

THEME = "./themes/taylor"

# TODO: enable feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# The blog's static HTML gets rendered to this folder.
OUTPUT_PATH = '../www/'

DISQUS_SITENAME = "bqpio"

DEFAULT_DATE_FORMAT = "%A, %B %d, %Y"

STATIC_PATHS = ['images']

DELETE_OUTPUT_DIRECTORY = True

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {
      'title': 'Table of contents:'
    },
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}
