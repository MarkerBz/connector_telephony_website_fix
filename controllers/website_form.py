# -*- coding: utf-8 -*-
from odoo.addons.website_form.controllers.main import WebsiteForm


class WebsiteFormExt(WebsiteForm):
    
    def __init__(self):
        # Get original method
        identity = self._input_filters.get('char')
        # Extend original dictionary
        self._input_filters.update({
            'phone': identity,
            'mobile': identity,
            'fax': identity,
        })
