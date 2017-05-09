# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from wazo_admin_ui.helpers.plugind import plugind


logger = logging.getLogger(__name__)


class PluginService(object):

    def install_plugin(self, plugin):
        return plugind.plugins.install(plugin['url'], plugin['method'])

    def uninstall_plugin(self, plugin):
        return plugind.plugins.uninstall(plugin['namespace'], plugin['name'])
