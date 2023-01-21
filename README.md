RETRO COFFEE SHOP Management System

A java application for coffee shops to make their management and working easier and efficient.

This application allows the user to make use of the various features provided for ensuring convenient customer experience such as,

$) Accepts Customer's Order Entry for beverage and snacks Purchases.

$) Generates Bill Receipt with Item-wise Cost and tax applicable.

$) Generates Customer Points based on Customer visit to the shop.
   10 points for every Rs.100 spent.
   
$) Generates a Daily Sales Report.

$) Helps in Data Setup Configuration - Customer, Items, Cost, GST% .

DATABASE

This project makes use of a MySQL database for storage of customer and product details.The database that we've created for this project contains the following tables:
$)cust* table(Cid,LName,FName,Addr,City,Cpoints)
$)ord** table(oid,bname,bcost,qty,tcost,fcag)
$)menu table(bname,bcat,bcost)


*customer
**order
