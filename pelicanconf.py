#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'William Culver'
AUTHOR_EMAIL = 'wculver@cedeon.co.uk'

SITENAME = 'One Byte Too Many'
SITESUBTITLE = 'Linux Specialists, Cambridge UK'
#SITEURL = 'https://blog.onebytetoomany.co.uk'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Computer Repair', '/computer-repair/'),
          ('Network Installation', '/network-installation/'),
          ('Linux Migration', '/linux-migration/'),
          ('Blog', '/blog/'),)

# Social widget
DISQUS_SITENAME = "blog-obtm" ##TODO:
PDF_GENERATOR = False
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
TWITTER_USERNAME = 'cedeon'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'svbtle_cedeon'

# Note.. plugin path is in a fragile state on live server
PLUGIN_PATH = '/home/cedeon/venv/pelican-env/pelican-plugins'
PLUGINS = ['assets', 'sitemap', 'gravatar', 'gzip_cache' ]

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'static',
    'extra/robots.txt',
]

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

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
