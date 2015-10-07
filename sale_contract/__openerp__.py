# -*- coding: utf-8 -*-
##############################################################################
#
#   www.vertel.se
#
##############################################################################

{
    'name': 'Sale Contract',
    'version': '1.0',
    'category': 'Sale',
    'description': """
Manage your contract.
=========================================================================================================
    """,
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['account_analytic_analysis', 'website_quote'],
    'data': [
        'views/sale_contract.xml',
       ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: