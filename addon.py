#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
import os
import sys
import urlparse
import xbmc
import xbmcaddon

reload(sys)
sys.setdefaultencoding('utf8')

LIB_DIR = xbmc.translatePath(
    os.path.join(xbmcaddon.Addon(id="plugin.video.dumpert").getAddonInfo('path'), 'resources', 'lib'))
sys.path.append(LIB_DIR)

from dumpert_const import ADDON, DATE, VERSION

# Get plugin settings
DEBUG = xbmcaddon.Addon(id=ADDON).getSetting('debug')

# Parse parameters...
if len(sys.argv[2]) == 0:
    #
    # Main menu
    #
    if DEBUG == 'true':
        xbmc.log("[ADDON] %s, Python Version %s" % (ADDON, str(sys.version)), xbmc.LOGNOTICE)
        xbmc.log("[ADDON] %s v%s (%s) is starting, ARGV = %s" % (ADDON, VERSION, DATE, repr(sys.argv)),
                 xbmc.LOGNOTICE)
    import dumpert_main as plugin
else:
    action = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['action'][0]
    #
    # Themas
    #
    if action == 'list-themas':
        import dumpert_list_themas as plugin
    #
    # List
    #
    elif action == 'list':
        import dumpert_list as plugin
    #
    # Play
    #
    elif action == 'play':
        import dumpert_play as plugin

    #
    # Search
    #
    elif action == 'search':
        import dumpert_search as plugin

plugin.Main()
