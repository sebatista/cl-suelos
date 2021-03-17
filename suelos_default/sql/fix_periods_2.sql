-- SELECT * from account_fiscalyear

-- periodos del año 2021
--SELECT * from account_period
--where fiscalyear_id = 5;


-- Borrar los no usados
--delete from account_period
--where id in (62)


-- SELECT id, period_id from account_invoice

-- Facturas del año 2021
--select period_id from account_invoice
--where period_id in (59,62)

-- Todas las tablas que hay que arreglar
-- Sacando las que no tienen registros o no existen

-- nada
--select period_id from account_bank_statement
--where period_id in (58)

--
--select period_id from account_invoice
--where period_id in (58)
--
select period_id,* from account_journal_period
where period_id in (58)
--
--select period_id from account_move
--where period_id in (58)
--
--select period_id from account_entries_report
--where period_id in (59,62)
--
--select period_id from account_invoice_report
--where period_id in (59,62)
--
--select period_id from report_account_type_sales
--where period_id in (59,62)
--
--select period_id from report_account_sales
--where period_id in (59,62)
--
--select period_id from account_treasury_report
--where period_id in (59,62)
--
--select period_id from account_voucher
--where period_id in (59,62)
