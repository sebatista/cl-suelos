# -*- coding: utf-8 -*-
from openupgradelib import openupgrade
import logging

_logger = logging.getLogger(__name__)


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    env.cr.execute(
        """
            --- Marcar los periodos existentes como no validos, no los pude borrar...
            update account_period
            set name='periodo no valido 01'
            where id = 58;
            update account_period
            set name='periodo no valido 02'
            where id = 59;
            update account_period
            set name='periodo no valido 03'
            where id = 62;

            --- Ponerle fechas fuera del periodo para que no den errores de solapamiento,
            update account_period
                set date_start='2000-01-01', date_stop='2000-01-01'
            where id in (58,59,62);

        """
    )

    # boton de crear periodos mensuales
    fiscalyear = env['account.fiscalyear'].search([('code', '=', '2021')])
    fiscalyear.create_period()

    period_01 = env['account.period'].search([('name', '=', '01/2021')])
    period_02 = env['account.period'].search([('name', '=', '02/2021')])
    period_03 = env['account.period'].search([('name', '=', '03/2021')])

    def make_domain(month, date_name):
        day = 28 if month == '02' else 31
        domain = []
        domain.append((date_name, '>=', '2021-%s-01' % month))
        domain.append((date_name, '<=', '2021-%s-%s' % (month, day)))
        return domain

    def fix_model(model_name, date_name):

        _logger.info('Fixing %s %s', model_name, date_name)

        recs = env[model_name].search(make_domain('01', date_name))
        for rec in recs:
            rec.period_id = period_01

        recs = env[model_name].search(make_domain('02', date_name))
        for rec in recs:
            rec.period_id = period_02

        recs = env[model_name].search(make_domain('03', date_name))
        for rec in recs:
            rec.period_id = period_03


    fix_model('account.bank.statement', 'date')
    fix_model('account.invoice', 'date_invoice')
    fix_model('account.move', 'date')
    #fix_model('account.invoice.report', 'date')
    fix_model('account.voucher', 'date')

#--select period_id from account_journal_period
#--select period_id from account_entries_report
#--select period_id from report_account_type_sales
# --select period_id from report_account_sales
# --select period_id from account_treasury_report
