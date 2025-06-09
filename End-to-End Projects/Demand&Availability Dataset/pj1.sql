

create database test_env

use test_env

select * from [dbo].Products

select * from dbo.[Test+Environment+Inventory+Dataset]

select distinct [Order_Date_DD_MM_YYYY] from dbo.[Test+Environment+Inventory+Dataset]

select distinct [Availability] from dbo.[Test+Environment+Inventory+Dataset]

select distinct [Demand] from dbo.[Test+Environment+Inventory+Dataset]

----------------------------------------------

select a.Order_Date_DD_MM_YYYY,
a.Product_ID, a.Availability, a.Demand, b.Product_Name,
b.Unit_Price
from dbo.[Test+Environment+Inventory+Dataset] as a
left join Products as b on a.Product_ID = b.Product_ID


select * into new_Table from 
(select a.Order_Date_DD_MM_YYYY,
a.Product_ID, a.Availability, a.Demand, b.Product_Name,
b.Unit_Price
from dbo.[Test+Environment+Inventory+Dataset] as a
left join Products as b on a.Product_ID = b.Product_ID) x


--------------------------------------------

select * from new_Table






