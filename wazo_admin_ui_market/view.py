# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import render_template
from flask import request
from flask import jsonify
from flask_menu.classy import classy_menu_item
from flask_classful import route

from wazo_admin_ui.helpers.classful import LoginRequiredView


class PluginView(LoginRequiredView):

    @classy_menu_item('.plugins', 'Plugins', order=0, icon="cubes")
    def index(self):
        return render_template('plugin/list.html')

    @route('/install_plugin/', methods=['POST'])
    def install_plugin(self):
        body = request.get_json()
        plugin = self.service.install(body)
        return jsonify(plugin)

    @route('/remove_plugin/', methods=['POST'])
    def remove_plugin(self):
        body = request.get_json()
        plugin = self.service.uninstall(body)
        return jsonify(plugin)

    @route('/search_plugin/', methods=['POST'])
    def search_plugin(self):
        payload = request.get_json()
        search = payload.get('search')
        namespace = payload.get('namespace')
        installed = payload.get('installed')
        available_plugins = self.service.market(search=search, namespace=namespace, installed=installed)['items']
        installed_plugins = self.service.list(search=search, namespace=namespace, installed=installed)['items']
        results = self._merge_plugins(available_plugins, installed_plugins)
        return render_template('plugin/list_plugins.html', market=results)

    def _merge_plugins(self, available_plugins, installed_plugins):
        for available in available_plugins:
            for installed in installed_plugins:
                if available.get('namespace') == installed.get('namespace') and \
                   available.get('name') == installed.get('name'):
                    installed_plugins.remove(installed)

        return available_plugins + installed_plugins
