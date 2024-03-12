	
--CHAPTER 3 EXCERCISE

--1-1
--Write a query that generates five copies of each employee row.
	
	use TSQL2012
	go
	
	SELECT EMPS.empid, EMPS.firstname, EMPS.lastname		
	FROM HR.Employees AS EMPS
		CROSS JOIN Nums AS NOS --Cartesian product between the numbers and the employees
	WHERE NOS.n <= 5 -- Only return the 5 of all the cartesian products per employee
	ORDER BY empid

--1-2 (Optional, Advanced)
--Write a query that returns a row for each employee and day in the range June 12, 2009 through
--June 16, 2009.

	--Get all the days in the range
	--Cartesian product of the employees to the days
	use TSQL2012
	go

	SELECT CUSTS.custid,DATEADD(day,NoOFDays.n -1,'20090612') AS dt --Get all the days in the range
																			  --Add to the days(defined by the NoOFDays.n) in the dat
																			  --[NoOFDays.n -1 becaause we start counting from 1]								   
	FROM Sales.Customers AS CUSTS
		CROSS JOIN Nums AS NoOFDays
	WHERE NoOFDays.n <= DATEDIFF(day,'20090612','20090616') + 1 				  -- Ensuring days in range do no exceed my auxilary numbers
		AND CUSTS.custid <= 9																		  --Note: Its the Righ date - the left date
																				  --+1 is to ensure we get the last day
	ORDER BY custid

	SELECT * from Sales.Customers

--2
--Return United States customers, and for each customer return the total number of orders and total
--quantities.
	use TSQL2012
	go

	SELECT CUSTS.custid, COUNT (ORDRS.orderid) AS numOfOrders, SUM(ORDRSDETAILS.qty) AS TotalQuantity
	FROM Sales.Customers AS CUSTS
		INNER JOIN Sales.Orders AS ORDRS
		ON CUSTS.custid = ORDRS.custid
			INNER JOIN Sales.OrderDetails AS ORDRSDETAILS
				ON ORDRS.orderid = ORDRSDETAILS.orderid
	WHERE CUSTS.country = 'USA'
	GROUP BY CUSTS.custid;

	SELECT C.custid, COUNT(DISTINCT O.orderid) AS numorders, SUM(OD.qty) AS totalqty -- Note the  COUNT(DISTINCT O.orderid). This is because the
												--orderid is repeated per order line in order details. WE only want the one occurence.
	FROM Sales.Customers AS C
		JOIN Sales.Orders AS O
		ON O.custid = C.custid
			JOIN Sales.OrderDetails AS OD
			ON OD.orderid = O.orderid
	WHERE C.country = N'USA'
	GROUP BY C.custid;

--3
--Return customers and their orders, including customers who placed no orders.

	use TSQL2012
	go

	SELECT CUSTS.custid, CUSTS.companyname, ORDRS.orderid, ORDRS.orderdate
	FROM Sales.Customers AS CUSTS
		LEFT OUTER JOIN Sales.Orders AS ORDRS
		ON CUSTS.custid = ORDRS.custid

--4
--Return customers who placed no orders.
	use TSQL2012
	go

	SELECT CUSTS.custid, CUSTS.companyname
	FROM Sales.Customers AS CUSTS
		LEFT OUTER JOIN Sales.Orders AS ORDRS
		ON CUSTS.custid = ORDRS.custid
	WHERE ORDRS.orderid IS NULL

--5
--Return customers with orders placed on February 12, 2007, along with their orders.

	use TSQL2012
	go

	SELECT CUSTS.custid, CUSTS.companyname, ORDRS.orderdate, ORDRS.orderid
	FROM Sales.Customers AS CUSTS
		LEFT OUTER JOIN Sales.Orders AS ORDRS
		ON CUSTS.custid = ORDRS.custid
	WHERE ORDRS.orderdate = '20070212';

--6 (Optional, Advanced)
--Return customers with orders placed on February 12, 2007, along with their orders. Also return customers
--who didn�t place orders on February 12, 2007.

	use TSQL2012
	go

	SELECT CUSTS.custid, CUSTS.companyname, ORDRS.orderdate, ORDRS.orderid
	FROM Sales.Customers AS CUSTS
		LEFT OUTER JOIN Sales.Orders AS ORDRS
		ON CUSTS.custid = ORDRS.custid AND ORDRS.orderdate = '20070212' -- Simply move the date filter 
	--ORDER BY CASE orderdate WHEN '20070212' THEN 0 ELSE 1 END;
	
--7 (Optional, Advanced)
--Return all customers, and for each return a Yes/No value depending on whether the customer placed
--an order on February 12, 2007.

	--INVESTIGATE AGAIN

	use TSQL2012
	go

	SELECT DISTINCT CUSTS.custid, CUSTS.companyname,
		CASE 
			WHEN ORDRS.orderdate = '20070212' THEN 'Yes'
			ELSE 'No'
		END AS 'HasOrderOn20070212'
	FROM Sales.Customers AS CUSTS
		 LEFT OUTER JOIN Sales.Orders AS ORDRS
		ON CUSTS.custid = ORDRS.custid 
	--Correct solution

	SELECT DISTINCT C.custid, C.companyname,
		CASE WHEN O.orderid IS NOT NULL THEN 'Yes' 
		ELSE 'No' 
		END AS [HasOrderOn20070212]
	FROM Sales.Customers AS C
		LEFT OUTER JOIN Sales.Orders AS O
		ON O.custid = C.custid AND O.orderdate = '20070212';