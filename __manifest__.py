# -*- coding: utf-8 -*-
{
    'name': 'Style Rent Car',
    'summary': 'Style rentcar management software',
    'description': """Style rentcar management software""",
    'author': "My Company",
    'website': "http://srikandiart.com",
    
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/stylerent_views.xml',
        'views/stylerent_pemeliharaan.xml',
        'views/stylerent_pegawai.xml',
        'views/stylerent_customer.xml',
        'views/stylerent_order.xml'
    ],
}