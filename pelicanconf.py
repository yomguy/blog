#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guillaume Pellerin'
SITENAME = u"Yomguy's blog"
SITEURL = 'http://yomix.org'
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'united'
# THEME = 'themes/notmyidea'
# CUSTOM_CSS = 'themes/bootswatch/slate/slate/bootstrap.css'
PATH = 'content/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'
DEFAULT_DATE = 'fs'

SUMMARY_MAX_LENGTH = 127
SLUGIFY_SOURCE = 'title'
# DEFAULT_PAGINATION = 5

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('Django', 'https://www.djangoproject.com/'),
          )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/yomguy/'),
          ('Google+', 'https://plus.google.com/+GuillaumePellerin'),
          ('LinkedIn', 'http://www.linkedin.com/in/guillaumepellerin'),
          ('GitHub', 'https://github.com/yomguy/'),
          ('LastFM', 'http://lastfm.com/user/yomguy'),
          ('FaceBook', 'https://www.facebook.com/yomguy75'),
          )

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISQUS_SITENAME='yomguysblog'
GITHUB_USER = 'yomguy'
TWITTER_CARDS = True
TWITTER_USERNAME = 'yomguy'
TWITTER_WIDGET_ID = '516222825451888640'
