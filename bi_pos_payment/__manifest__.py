# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "POS Invoice and Register Payment",
    "version" : "15.0.0.0",
    "category" : "Point of Sale",
    "depends" : ['base','sale','point_of_sale'],
    "author": "BrowseInfo",
    'summary': 'point of sales payment methods pos invoice payment pos accounting payment pos register payment pos voucher payment pos Multiple and partial payments pos payment methods POS payments point of sales payments POS screen register payment on pos advance payment',
    "price": 49,
    "currency": 'EUR',
    "description": """
    pos invoice payment pos accounting payment pos register payment pos voucher payment pos payment 
    pos payment from pos screen invoice payment from POS screen register payment from pos screen
    pay invoice from POS screen accounting payment from POS screen
    point of sale invoice payment point of sale accounting payment point of sale register payment
    point of sale voucher payment point of sale payment payment from point of sale screen
    pos invoice payment from point of sale screen register payment from point of sale screen
    pay invoice from point of sale screen accounting payment from point of sale screen pos multiple invoice payment
    pos mass invoice payment point of sales multiple invoice payment point of sales mass invoice payment
    Purpose :- 
    """,
    "website" : "https://www.browseinfo.in",
    "data": [
        'security/ir.model.access.csv',
        'views/custom_pos_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            "bi_pos_payment/static/src/css/pos.css" ,
            "bi_pos_payment/static/src/js/pos_payment.js",
            "bi_pos_payment/static/src/js/Widget/CreatePaymentButtonWidget.js",
            "bi_pos_payment/static/src/js/Widget/SeeAllInvoicesButtonWidget.js",
            "bi_pos_payment/static/src/js/Popup/RegisterInvoicePaymentPopupWidget.js",
            "bi_pos_payment/static/src/js/Popup/PosInvoiceDetail.js",
            "bi_pos_payment/static/src/js/Popup/RegisterPaymentPopupWidget.js",
            "bi_pos_payment/static/src/js/Screens/POSInvoiceScreen.js",
            "bi_pos_payment/static/src/js/Screens/ClientListScreen.js",
            "bi_pos_payment/static/src/js/Screens/POSInvoice.js",
        ],
        'web.assets_qweb': [
            'bi_pos_payment/static/src/xml/**/*',
        ],
    },
    "auto_install": False,
    "installable": True,
    "live_test_url": "https://youtu.be/fAfbBu8IgGU",
    "images":['static/description/Banner.png'],
    'license': 'OPL-1',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
