select Gender, COUNT(*) from [dbo].[Depression+Student+Dataset]
group by Gender

update [dbo].[Depression+Student+Dataset]
set Gender = 'F' where Gender = 'Female'

update [dbo].[Depression+Student+Dataset]
set Gender = 'M' where Gender = 'Male'

select * from [dbo].[Depression+Student+Dataset]
where Gender is null

select * from [dbo].[Depression+Student+Dataset]
where Gender = ''