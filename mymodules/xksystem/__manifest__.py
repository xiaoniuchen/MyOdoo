# -*- coding: utf-8 -*-
{
    'name': "xksystem",

    'summary': """
        选课系统
        """,

    'description': """
        选课系统
    """,

    'author': "Tony Chen",
    'website': "http://www.smarttony.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/formviews.xml',
        'views/treeviews.xml',
        'views/templates.xml',
        'views/menus.xml',
        'security/xksystem_security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}