#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license


import os
import settings
from koldocta.factory import get_app as koldocta_app


def get_app(config=None):
    """App factory.

    :param config: configuration that can override config from `settings.py`
    :return: a new Koldocta app instance
    """
    if config is None:
        config = {}

    config['APP_ABSPATH'] = os.path.abspath(os.path.dirname(__file__))

    for key in dir(settings):
        if key.isupper():
            config.setdefault(key, getattr(settings, key))

    media_storage = None
    if 'AMAZON_CONTAINER_NAME' in config:
        from koldocta.storage.amazon.amazon_media_storage import AmazonMediaStorage
        media_storage = AmazonMediaStorage

    config['DOMAIN'] = {
        'people': {}
    }

    app = koldocta_app(config, media_storage)
    return app
