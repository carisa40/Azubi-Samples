select sum(send_amount_scalar) as send_volume, wallets.ledger_location, transfers.kind
from transfers, wallets
where  (transfers.when_created = date_trunc ('week', current_timestamp - interval '1 week'))
group by kind, ledger_location
