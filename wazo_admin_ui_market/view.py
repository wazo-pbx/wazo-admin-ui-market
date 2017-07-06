# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import render_template
from flask import request
from flask import jsonify
from flask_menu.classy import classy_menu_item
from flask_classful import route

from wazo_admin_ui.helpers.classful import BaseView


class PluginView(BaseView):

    @classy_menu_item('.plugins', 'Plugins', order=0, icon="cubes")
    def index(self):
        return render_template('plugin/list.html')

    def list_plugin(self):
        return render_template('plugin/list_plugins.html', market=[])

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
        search = request.get_json().get('value')
        available_plugins = self.service.market()['items']

        results = [plugin for plugin in available_plugins if search in plugin.values()]
        return render_template('plugin/list_plugins.html', market=results)

    @route('/filter_plugin/', methods=['POST'])
    def filter_plugin(self):
        filter_ = request.get_json().get('value')

        available_plugins = self.service.market()['items']
        installed_plugins = self.service.list()['items']

        results = self._get_filtered_plugins(filter_, available_plugins, installed_plugins)
        return render_template('plugin/list_plugins.html', market=results)

    @route('/show_only_official/', methods=['POST'])
    def show_only_official(self):
        available_plugins = self.service.market(search='official')['items']
        installed_plugins = self.service.list()['items']

        results = self._merge_plugins(available_plugins, installed_plugins)
        return render_template('plugin/list_plugins.html', market=results)

    def _get_filtered_plugins(self, filter_, available_plugins, installed_plugins):
        results = self._merge_plugins(available_plugins, installed_plugins)

        if filter_ == 'installed':
            results = [plugin for plugin in results if plugin['is_installed']]
        elif filter_ == 'not_installed':
            results = [plugin for plugin in results if not plugin['is_installed']]

        return results

    def _merge_plugins(self, available_plugins, installed_plugins):
        for plugin in available_plugins:
            plugin['is_installed'] = False

        for plugin in installed_plugins:
            plugin['is_installed'] = True

        for available in available_plugins:
            for installed in installed_plugins:
                if available.get('namespace') == installed.get('namespace') and \
                   available.get('name') == installed.get('name'):
                    available['is_installed'] = True
                    installed_plugins.remove(installed)

        return available_plugins + installed_plugins
