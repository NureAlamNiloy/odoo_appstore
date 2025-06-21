{
    'name': "Odoo License Barrier",

    'summary': "Odoo License Barrier",

    'description': """ This apps for Overcome odoo license barreir """,

    'author': "Nure Alam Niloy",
    'maintainer': 'Nure Alam Niloy',
    'website': "https://www.linkedin.com/in/nurealamniloy/",

    'category': 'Tutorial',
    'version': '0.1',
    'License': 'LGPL-3',
    'price': '7.0',
    'currency': 'USD',
    'depends': ['base', 'portal', 'sale_management', 'sale', 'purchase', 'hr'],

    'data': [
        "views/salesperson_domain.xml",
        "views/buyer_domain.xml",
        "views/releted_user_domain.xml",
    ],
    'images': ["licence_barrier/static/banner.png"],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'sequence': -99,
}
