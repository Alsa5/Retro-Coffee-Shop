**RETRO COFFEE SHOP _Management System_**
______________________________________________________________________________________________________________________________________________________________________

A java application for coffee shops to make their management and working easier and efficient.

This application allows the user to make use of the various features provided for ensuring convenient customer experience such as,

**$)** Accepts Customer's Order Entry for beverage and snacks Purchases.

**$)** Generates Bill Receipt with Item-wise Cost and tax applicable.

**$)** Generates Customer Points based on Customer visit to the shop.
   10 points for every Rs.100 spent.
   
**$)** Generates a Daily Sales Report.

**$)** Helps in Data Setup Configuration - Customer, Items, Cost, GST% .
\
\
\
**ABOUT PROJECT**
______________________________________________________________________________________________________________________________________________________________________

This project has been developed in the Java IntelliJ IDE with a JDBC driver connection to the database.\
This consists of four classes,\
\
**$)** OrderNbill class\
\
**$)** Main class (JDBC driver connection takes place in the main class).\
\
\
\
**DATABASE**
______________________________________________________________________________________________________________________________________________________________________

This project makes use of a ***MySQL*** database for storage of customer and product details.MySQL which is a relational database management system is connected with the IntelliJ using JDBC connectivity.The database that we've created for this project contains the following tables:

**$)** cust table(Cid,LName,FName,Addr,City,Cpoints)

**$)** ord table(oid,bname,bcost,qty,tcost,fcag)

**$)** menu table(bname,bcat,bcost)


