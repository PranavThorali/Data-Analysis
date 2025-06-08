select Age, COUNT(*) from dbo.[Depression+Student+Dataset]
group by Age
order by Age desc

alter table [dbo].[Depression+Student+Dataset]
add Age_group varchar(max)

select * from [dbo].[Depression+Student+Dataset]

update [dbo].[Depression+Student+Dataset]
set Age_group =
case when Age between 18 and 24 then 'A1'
else case when Age between 25 and 30 then 'A2'
else 'A3'
end
end

select * from [dbo].[Depression+Student+Dataset]

select Age_group, COUNT(*) from dbo.[Depression+Student+Dataset]
group by Age_group