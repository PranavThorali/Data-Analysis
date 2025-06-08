select * from [Depression+Student+Dataset]

alter table [Depression+Student+Dataset]
add Index_Column int identity(1,1)

update [Depression+Student+Dataset]
set Depression = 'No' where Depression = 0

select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME LIKE 'Depression+Student+Dataset'

ALTER TABLE [Depression+Student+Dataset]
ALTER COLUMN Depression VARCHAR(MAX)

update [Depression+Student+Dataset]
set Depression = 'Yes' where Depression = 1