--EXERCISES

--1
--Write a query that generates a virtual auxiliary table of 10 numbers in the range 1 through 10 without
--using a looping construct. You do not need to guarantee any order of the rows in the output of your
--solution.

--Me
	SELECT ROW_NUMBER() OVER (ORDER BY 'n')
--Book:
	SELECT n
	FROM (VALUES(1),(2),(3),(4),(5),(6),(7),(8),(9),(10)) AS Nums(n);

	--Or
	SELECT 1 AS n
	UNION ALL SELECT 2 AS P -- This column name will be discarded because the columns for the left set are taken
	UNION ALL SELECT 3
	UNION ALL SELECT 4
	UNION ALL SELECT 5
	UNION ALL SELECT 6
	UNION ALL SELECT 7
	UNION ALL SELECT 8
	UNION ALL SELECT 9
	UNION ALL SELECT 10;

--2 Write a query that returns customer and employee pairs that had order activity in January 2008 but
--not in February 2008.

	--Customer and Employee
	--Order Activity
	--	January 2008
	--	Not in February 2008
	use TSQL2012
	select custid,empid,orderdate
	from sales.Orders
	where orderdate BETWEEN '20080101' AND '20080131'


	--solution
	(select custid,empid
	from sales.Orders
	where orderdate BETWEEN '20080101' AND '20080131')
	--Key: You want to take out guys in the above set (i.e.where orderdate BETWEEN '20080101' AND '20080131')
			--who placed orders in February 2008
    EXCEPT
	(select custid,empid
	from sales.Orders
	where orderdate >= '20080201' AND orderdate < '20080301')

	

	--NB: BETWEEN includes the range values
	--select * 
	--from sales.Orders
	--where orderdate BETWEEN '20080101' AND '20080201'
	--order by custid asc, empid asc

	--INSERT INTO Sales.Orders
	--VALUES (1,1,'20080101 00:00:00:00','20080101 00:00:00:00','20080101 00:00:00:00',3,999,'TestShip','TestAdd',
	--'TestCit','TestShipRegi',999,'Praise')

--	3
--Write a query that returns customer and employee pairs that had order activity in both January 2008
--and February 2008.
	select custid,empid
	from sales.Orders
	where (orderdate BETWEEN '20080101' AND '20080201') AND
		  (orderdate BETWEEN '20080201' AND '20080301') --Wont work because I'm trying to evaluate a Column for Two different
														--conditions at the same time. IT CANNOT BE IN TWO STATES AT THE TIME!!
	
	--Works
	SELECT custid,empid
	from Sales.Orders
	where (orderdate BETWEEN '20080101' AND '20080201')
	INTERSECT
	SELECT custid,empid
	from Sales.Orders
	where (orderdate BETWEEN '20080201' AND '20080301')

--4 Write a query that returns customer and employee pairs that had order activity in both January 2008
--and February 2008 but not in 2007.

	--Customer and Employee
	--Order Activity
	--	January 2008; and
	--	February 2008
	--Not in 2007

	(SELECT custid,empid
	FROM Sales.Orders
	where (orderdate BETWEEN '20080101' AND '20080201')
		INTERSECT
	SELECT custid,empid
	FROM Sales.Orders
	where (orderdate BETWEEN '20080201' AND '20080301'))
		EXCEPT -- You need to explictly exclude the members of the set that you don't want(those who are member on the 2007 set)
	SELECT custid,empid
	FROM Sales.Orders
	WHERE Year(orderdate) = 2007 -- Needed because you get custid and empids that placed orders in 2007 and subtract from the above ser

--5 (Optional, Advanced)
--You are given the following query.
	--Add logic
		--Rows from Employees are displayed first
			--The supplier rows
		--Sort by country, region, city per segment
	(SELECT country , region, city
	FROM HR.Employees
	ORDER BY country asc, region, city) 
	UNION ALL
	(SELECT country , region, city
	FROM Production.Suppliers
	ORDER BY country asc, region ,city);

	---Me
	((SELECT country, region, city
	FROM HR.Employees)
	UNION ALL
	(SELECT country, region, city
	FROM Production.Suppliers))
	ORDER BY country, region, city

	--Book
	SELECT country, region, city
	FROM (SELECT 1 AS sortcol, country, region, city
	FROM HR.Employees
	UNION ALL
	SELECT 2, country, region, city
	FROM Production.Suppliers) AS D
	ORDER BY sortcol, country, region, city;
	