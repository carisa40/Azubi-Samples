select agents.country, agents.city, sum(agent_transactions.amount) as transaction_volume
from agents, agent_transactions
where (agent_transactions.when_created >= date_trunc('week', current_timestamp - interval '1 week'))
and agent_transactions.when_created < date_trunc('week', current_timestamp)
group by country, city;
