
select name, revenue, isnull(cnt.cnt_office, 0)
from companies
left join 
(select company_id, count(location_id) as cnt_office
from offices
group by company_id) cnt
on companies.company_id = cnt_office.company_id
where cnt.cnt_office < 5
order by cnt.cnt_office