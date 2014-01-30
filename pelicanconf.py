#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'William Culver'
AUTHOR_EMAIL = 'wculver@cedeon.co.uk'

SITENAME = 'One Byte Too Many'
SITE_TITLE = 'Linux Specialists'
SITE_TITLE_APPEND = 'Cambridge, UK'
SITESUBTITLE = SITE_TITLE + ' - ' + SITE_TITLE_APPEND
SITE_FULL_TITLE = SITENAME + ' | ' + SITESUBTITLE

SITE_PHONE = '01638 745147'
#SITEURL = 'https://blog.onebytetoomany.co.uk'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Categories
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Computer Repair', '/computer-repair-services-cambridge.html'),
          ('Network Installation', '/network-and-wifi-installation-cambridge.html'),
          ('Linux Migration', '/linux-migration-services-cambridge.html'),
          ('Security Research', '/category/security.html'),
          ('Blog', '/category/blog.html'),)

# Social widget
SOCIAL = (('github', 'http://github.com/cedeon'),)
DISQUS_SITENAME = 'onebytetoomany'
GPLUS_PAGE = 'https://www.google.com/+OneByteTooManyBurwell'
FACEBOOK_PAGE = 'https://www.facebook.com/OneByteTooMany'
TWITTER_PAGE = 'https://twitter.com/cedeon/'
TWITTER_USERNAME = 'cedeon'
PDF_GENERATOR = False

GOOGLE_ANALYTICS = 'UA-24085046-3'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'svbtle_cedeon'

# Note.. plugin path is in a fragile state on live server
PLUGIN_PATH = '/home/walden/venv/pelican-plugins'
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
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.6
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
