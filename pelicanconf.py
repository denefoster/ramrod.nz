#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dane foster'
SITENAME = u'Team CAR RAMROD'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

THEME_PATHS = ["themes",]
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_FLUID = True
BOOTSTRAP_THEME = 'spacelab'
#BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
#HIDE_SIDEBAR = True
SITELOGO = 'static/carramrod.png'
SITELOGO_SIZE = '28'
#BANNER = 'static/carramrod.png'
#BANNER_SUBTITLE = 'SAY IT'
#ABOUT_ME = '<img src="/static/carramrod.png" width="48"/>'
SHOW_ARTICLE_AUTHOR = True
#TYPOGRIFY = True
STATIC_PATHS = ['static',
                'extra/robots.txt',
                'extra/favicon.ico',
                'code',]

EXTRA_PATH_METADATA = {
    'extra/robots.txt':  {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}


PLUGIN_PATHS = ["plugins",]
PLUGINS = ["related_posts",
           "tipue_search",
           "sitemap",
#           "better_figures_and_images",
#           "optimize_images",
           "photos",
           "pelican_dynamic",
#           "thumbnailer",
           "pelican_youtube"]
DIRECT_TEMPLATES = ['index', 'archives', 'search']
RESPONSIVE_IMAGES = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GOOGLE_ANALYTICS = 'UA-102917539-1'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
CC_LICENSE = 'CC-BY'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PHOTO_LIBRARY = "/Users/dene/devel/ramrod.nz/images"
#PHOTO_GALLERY = (1024, 768, 80)
#PHOTO_ARTICLE = ( 760, 506, 80)
#PHOTO_THUMB = (192, 144, 60)
#MARKDOWN = {
#        'extension_configs': {
#            'mdx_video': {},
#            },
#        'output_format': 'html5'
#        }
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
