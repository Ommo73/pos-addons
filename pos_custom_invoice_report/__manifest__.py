# Copyright 2020 Artem Rafailov <https://it-projects.info/team/Ommo73/>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Custom invoice report""",
    "summary": """Custom invoice report""",
    "category": "Point of Sale",
    # "live_test_url": "http://apps.it-projects.info/shop/product/pos-invoice-pay?version=12.0",
    "images": [],
    "version": "12.0.1.0.0",
    "application": False,
    "author": "IT-Projects LLC, Artem Rafailov",
    "support": "pos@it-projects.info",
    "website": "it-projects.info",
    "license": "LGPL-3",
    # "price": 9.00,
    # "currency": "EUR",
    "depends": ["point_of_sale", "sale_stock"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/report_template.xml",
    ],
    "qweb": [],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
    "demo_title": "",
    "demo_addons": [],
    "demo_addons_hidden": [],
    "demo_url": "",
    "demo_summary": "",
    "demo_images": [""],
}
