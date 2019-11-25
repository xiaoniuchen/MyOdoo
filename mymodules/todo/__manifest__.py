# -*- coding: utf-8 -*-
{
    'name': "todo",

    'summary': """
        这个是todo测试项目""",

    'description': """
        这个是todo测试项目
    """,

    'author': "SmartTony",
    'website': "http://www.smarttony.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/formviews.xml',
        'views/templates.xml',
        'views/menus.xml',
        'views/searchviews.xml',
        'security/todo_security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'applacation':True,
}