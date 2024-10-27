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
        'views/fithub_subscription.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

