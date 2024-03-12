use TSQL2012
go

--CHAPTER 2 EXCERCISE

--1 Write a query against the Sales.Orders table that returns orders placed in June 2007.
	use TSQL2012
	go

	SELECT orderid,orderdate,custid,empid
		FROM Sales.Orders
			WHERE Orderdate >= '20070601' AND orderdate < '20070701'
	ORDER BY orderdate;

--2 Write a query against the Sales.Orders table that returns orders placed on the last day of the month.
	use TSQL2012
	go

	SELECT orderid,orderdate,custid,empid
		FROM Sales.Orders
			WHERE orderdate = EOMONTH(orderdate);

	--Alternative, check it out later
		SELECT orderid, orderdate, custid, empid
		FROM Sales.Orders
		WHERE orderdate = DATEADD(month, DATEDIFF(month, '19991231', orderdate), '19991231');
--3 Write a query against the HR.Employees table that returns employees with last name containing the letter a twice or more

	use TSQL2012
	go	

	SELECT empid,firstname,lastname
	FROM HR.Employees
	WHERE (LEN(lastname) - (LEN(REPLACE(lastname,'a','')))) >= 2;

	--Alternative: Clearner solution %a%a%' = means anything in between or before the a's
	SELECT empid, firstname, lastname
	FROM HR.Employees
	WHERE lastname LIKE '%a%a%';

--4 Write a query against the Sales.OrderDetails table that returns orders with total value (quantity * unitprice) 
--greater than 10,000, sorted by total value.

	--Loook again


	EXEC sys.sp_help
	@objname = N'Sales.Orderdetails';--Quick way to get the details of a table you do not know anything about

	use TSQL2012
	go

	SELECT orderid,(qty*unitprice) AS TotalValue
	FROM Sales.OrderDetails
	WHERE (qty*unitprice) > 10000
	ORDER BY TotalValue;

	--Correct solutions
		--NB: Remeber HAVING is used to filter groups
	SELECT orderid, SUM(qty*unitprice) AS totalvalue
	FROM Sales.OrderDetails
	GROUP BY orderid
	HAVING SUM(qty*unitprice) > 10000
	ORDER BY totalvalue DESC;

--5 Write a query against the Sales.Orders table that returns the three shipped-to countries with the highest
--  average freight in 2007.

	EXEC sys.sp_help
	@objname = N'Sales.Orders';

	use TSQL2012
	go

	SELECT TOP(3) shipcountry, AVG(Freight) AS FreightAverage
	FROM Sales.Orders
	WHERE orderdate >= '20070101' AND orderdate <='20071231'
	GROUP BY shipcountry
	ORDER BY FreightAverage DESC;
		
--Remember that in SQL Server 2012 you can use the standard OFFSET-FETCH option instead of the
--proprietary TOP option. Here�s the revised solution using OFFSET-FETCH. 
--Standard Approach
	SELECT shipcountry, AVG(freight) AS avgfreight
	FROM Sales.Orders
	WHERE orderdate >= '20070101' AND orderdate < '20080101'
	GROUP BY shipcountry
	ORDER BY avgfreight DESC
	OFFSET 0 ROWS FETCH FIRST 3 ROWS ONLY;

--6 Write a query against the Sales.Orders table that calculates row numbers for orders based on order
--date ordering (using the order ID as the tiebreaker) for each customer separately.

	--calculate row numbers for orders
	--on  date ordering
	--Per customer
	--NB:order ID is the tie breaker
	--NB: Not complete

	use TSQL2012
	go

	SELECT custid,orderid,orderdate, Count(*) AS rownum
	FROM Sales.Orders
	GROUP BY custid, orderid,orderdate
	ORDER BY orderdate ,orderid ASC

	--Correct solution
	use TSQL2012
	go

	SELECT custid, orderdate, orderid,
	ROW_NUMBER() OVER(PARTITION BY custid ORDER BY orderdate, orderid) AS rownum
	FROM Sales.Orders
	ORDER BY custid, rownum;

--7
--Using the HR.Employees table, figure out the SELECT statement that returns for each employee the
--gender based on the title of courtesy. For �Ms. � and �Mrs.� return �Female�; for �Mr. � return �Male�; and
--in all other cases (for example, �Dr. �) return �Unknown�.

	use TSQL2012
	go

	SELECT empid,firstname, lastname, titleofcourtesy,
			CASE titleofcourtesy 
				WHEN 'Ms.' THEN 'Female'
				WHEN 'Mrs.' THEN 'Female'
				WHEN 'Mr.' THEN 'Male'
				WHEN 'Dr.' THEN 'Unknown'
				ELSE 'Value Not Found'
			END AS 'gender'
    FROM HR.Employees
	
--8
--Write a query against the Sales.Customers table that returns for each customer the customer ID and
--region. Sort the rows in the output by region, having NULL marks sort last (after non-NULL values).
--Note that the default sort behavior for NULL marks in T-SQL is to sort first (before non-NULL values).

	--Look again
	use TSQL2012
	go

	SELECT custid, region
	FROM Sales.Customers
	ORDER BY region DESC	 

	--Correct solution
	use TSQL2012
	go

	SELECT custid, region
	FROM Sales.Customers
	ORDER BY
	CASE WHEN region IS NULL THEN 1 ELSE 0 END, region;