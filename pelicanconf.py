#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guillaume Pellerin'
SITENAME = u"Yomguy's blog"
# SITEURL = 'http://yomix.org'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
# SITEURL = 'http://yomix.org'
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
          ('Python', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('Django', 'https://www.djangoproject.com/'),
          )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/yomguy/'),
          ('Google+', 'https://plus.google.com/+GuillaumePellerin'),
          ('LinkedIn', 'http://www.linkedin.com/in/guillaumepellerin'),
          ('GitHub', 'https://github.com/yomguy/'),
          ('FaceBook', 'https://www.facebook.com/yomguy75'),
          ('LastFM', 'http://lastfm.com/user/yomguy'),
          )

DISQUS_SITENAME='yomguysblog'
GITHUB_USER = 'yomguy'
TWITTER_CARDS = True
TWITTER_USERNAME = 'yomguy'
TWITTER_WIDGET_ID = '516222825451888640'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'gallery', 'render_math',
            'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           ]
SITEMAP = {

    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Content licensing: CC-BY
CC_LICENSE = "CC-BY"

GOOGLE_ANALYTICS = 'UA-6573030-16'

GALLERY_PATH = './content/images/gallery/'
