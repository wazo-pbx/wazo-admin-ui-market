# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint

from .service import PluginService
from .view import PluginView

plugin = create_blueprint('plugin', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        PluginView.service = PluginService()
        PluginView.register(plugin, route_base='/plugins')
        register_flaskview(plugin, PluginView)

        core.register_blueprint(plugin)
