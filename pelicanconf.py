#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

THEME = os.path.expanduser('~/devel/pelican-themes/pelican-cait')

AUTHOR = u'Martin Contento'
SITENAME = u'Nerio Games'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GOOGLE_ANALYTICS_CODE = 'UA-38709647-1'
GOOGLE_ANALYTICS = GOOGLE_ANALYTICS_CODE

DEFAULT_LANG = u'en'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

PAGE_LANG_URL = '{lang}/{slug}'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
