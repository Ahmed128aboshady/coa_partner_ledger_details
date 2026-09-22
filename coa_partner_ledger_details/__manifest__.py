# -*- coding: utf-8 -*-
{
    'name': 'COA Partner Ledger Invoice Drill-down',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Expand any invoice line in the Partner Ledger to see individual product lines with quantity and total',
    'description': """
COA Partner Ledger Invoice Drill-down
======================================
Extends the Odoo Enterprise Partner Ledger report so that every invoice
line becomes expandable. Click the arrow next to any invoice to instantly
reveal all product lines with their quantity, unit of measure, and line total.
Built using the official Odoo report framework - no hacks, no broken IDs.
Requires Odoo Enterprise (account_reports module).
    """,
    'author': 'Community of accountants (COA-Egypt)',
    'website': 'https://www.coa-egy.com',
    'support': 'info@coa-egy.com',
    'images': ['static/description/banner.png'],
    'depends': ['account'],
    'data': [],
    'price': 49.00,
    'currency': 'USD',
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
}
