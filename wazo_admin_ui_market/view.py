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
        results = self.service.market(search=search)['items']
        return render_template('plugin/list_plugins.html', market=results)

    @route('/filter_plugin/', methods=['POST'])
    def filter_plugin(self):
        filter_ = request.get_json().get('value')

        if filter_ == 'installed':
            results = self.service.market(installed=True)['items']
        elif filter_ == 'not_installed':
            results = self.service.market(installed=False)['items']
        else:
            results = self.service.market()['items']

        return render_template('plugin/list_plugins.html', market=results)

    @route('/show_only_official/', methods=['POST'])
    def show_only_official(self):
        results = self.service.market(namespace='official')['items']
        return render_template('plugin/list_plugins.html', market=results)
