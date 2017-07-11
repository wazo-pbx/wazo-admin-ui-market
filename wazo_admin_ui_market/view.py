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
        payload = request.get_json()
        search = payload.get('search')
        namespace = payload.get('namespace')
        installed = payload.get('installed')
        results = self.service.market(search=search, namespace=namespace, installed=installed)['items']
        return render_template('plugin/list_plugins.html', market=results)
