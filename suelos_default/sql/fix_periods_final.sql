-- Marcar los periodos como no validos

update account_period set name='periodo no valido 01' where id = 58;
update account_period set name='periodo no valido 02' where id = 59;
update account_period set name='periodo no valido 03' where id = 62;

update account_period
    set date_start='2000-01-01', date_stop='2000-01-01'
where id in (58,59,62);
