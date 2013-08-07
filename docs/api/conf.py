import sys
import os
sys.path.append(os.path.abspath('../..'))
from docs.conf import *  # noqa


project = u'Firefox Marketplace API v1'
version = release = '1.0'  # Should correspond to the API version number

import mdn_theme
html_theme_path = [mdn_theme.get_theme_dir()]
html_theme = 'mdn'

html_static_path = ['../_static']

intersphinx_mapping = {}
