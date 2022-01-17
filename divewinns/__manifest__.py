# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "DiveWinns",
    "author": "istarii",
    "summary": "DiveWinns customisations",
    "description": """DiveWinns customisations""",
    "version": "15.0.5",
    "depends": ["base", "product", "purchase", "stock", "event", "calendar", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_product.xml",
        "views/event_event.xml",
        "views/training_date.xml",
        "views/calendar_event.xml",
        "views/calendar.xml",
        "views/menu.xml",
    ],
    "auto_install": False,
    "installable": True,
}
