#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Shashank Kumar'
SITEURL = 'http://localhost:8000'
SITENAME = 'Shanky\'s Brainchild'
SITETITLE = SITENAME
SITEDESCRIPTION = 'Some of what Shashank Kumar ( realslimshanky ) stumbles upon or thinks intentionally lies here on the blog.'
SITELOGO = '/images/profile.jpg'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'colorful'

ROBOTS = 'index, follow'

THEME = 'theme/flex'
PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
OG_LOCALE = 'en_IN'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/shashankkumarkushwaha/'),
          ('github', 'https://github.com/realslimshanky'),
          ('key', 'https://keybase.io/realslimshanky'),
          ('rss', '//blog.shanky.dev/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2025

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'PDFs', 'videos']
