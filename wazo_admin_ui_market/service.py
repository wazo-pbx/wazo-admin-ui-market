# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from wazo_admin_ui.helpers.plugind import plugind


logger = logging.getLogger(__name__)


class PluginService(object):

    def install(self, plugin):
        return plugind.plugins.install(url=plugin.get('url'), method=plugin['method'], options=plugin.get('options'))

    def uninstall(self, plugin):
        if 'namespace' in plugin and 'name' in plugin:
            return plugind.plugins.uninstall(plugin['namespace'], plugin['name'])

    def list(self):
        return plugind.plugins.list()

    def market(self, search=None, **kwargs):
        return plugind.market.list(search, **kwargs)
