# -*- coding: utf-8 -*-
{
    'name': "Fithub Subscription",
    'summary': "Manage subscription of Fithub",
    'description': """""",
    'author': "Sami Adam",
    'website': "https://www.linkedin.com/in/sami-adam-9ab3a598/",
    'category': 'Fithub',
    'version': '0.1',
    'depends': ['account'],
    'application': True,
    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/menus.xml',
        'views/account_move.xml',
        'views/res_partner.xml',
        'views/product_product.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

