# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import requests


def get_market():

    r = requests.get('http://apps.wazo.community/index.json')
    market = {'items': {}}

    if r.status_code == 200:
        market = r.json()

    return market
