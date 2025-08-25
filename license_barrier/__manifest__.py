{
    'name': "Odoo License Barrier",

    'summary': "Restrict access based on user roles across Sales, Purchase, and Employee modules.",

    'description': """
        This app helps overcome Odoo license limitations by managing user access (Salesperson, Buyer, Employee) across multiple modules. It allows centralized control without duplicating products or user records per branch. Note: This module is not intended for Odoo Online (SaaS) environments.
            Features:
            - Restricts access based on related user roles
            - Centralized control across Sales, HR, Purchase
            - No need for product duplication across branches
    """,


    'author': "Bdcalling IT Ltd.,  Nure Alam Niloy",
    'maintainer': "Nure Alam Niloy",
    'website': "https://www.linkedin.com/in/nurealamniloy/",

    'category': 'Extra Tools',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'price': 7.0,
    'currency': 'USD',

    'depends': [ 'base', 'portal', 'sale_management', 'sale', 'purchase', 'hr', ],

    'data': [
        "views/salesperson_domain.xml",
        "views/buyer_domain.xml",
        "views/releted_user_domain.xml",
    ],

    'images': ["static/description/banner.gif"],

    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': -99,
}
