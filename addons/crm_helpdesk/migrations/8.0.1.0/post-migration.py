# -*- coding: utf-8 -*-
# © 2016 Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import pooler, SUPERUSER_ID
from openupgradelib import openupgrade, openupgrade_80


@openupgrade.migrate()
def migrate(cr, version):
    pool = pooler.get_pool(cr.dbname)
    uid = SUPERUSER_ID
    openupgrade_80.set_message_last_post(cr, uid, pool, ['crm.helpdesk'])
    openupgrade.map_values(
        cr, 'priority', openupgrade.get_legacy_name('priority'),
        [('1', '0'), ('2', '1'), ('3', '2'), ('4', '2')], table='crm_helpdesk')
