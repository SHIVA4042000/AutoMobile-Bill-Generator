# AutoMobile-Bill-Generator-Using-Python-Tkinter
For running this Application 'Clone'('HTTPS' Preferred ) or 'download' to your local PC
Then extract and run in your prefered 'Editor' or 'IDE'
If you don't have MYSQl Database then Install MYSQl Workbench.
Then create connection or connect to 'localhost' with 'root' user and if 'password' required provide the appropriate password if root password then provide the password that you have provided at the time of installation of MYSQL.
Then click on 'Server' on the top Menu then click on 'Data Import'.
Then Click on 'Import from Self-Contained File' in 'Import Options' under'Import From Disk' Menu1 Browse with three given with it and select file 'Dump20200526.sql' from this Repository folder
Keep rest of the things as Default
Verify that its selected 'Dump Structure and data' both
Then click on menu2 'Import Progress'
Then Finally Click on 'Start Import' Button
Make sure Connection ='localhost' database='bill' user ='root' password='login' (if your password not login then change the password in the program files('login.py','bill.py')* as your DB password)
Rest of the Code won't make problem in running the program

#How to Use this Application?
First run the File name 'start.py'
Then 'Sign In' Page appears enter USER ID ='login' Password='login'
Then main page 'Automobile Billing Services' will appear
In this page 'Registration Number' of a vehical is the Key get the work done, all the functionality depends on registratin Number
It first conforms whether the'registration no'is present or not in the database if not then 'add new customer' button gets activated
Else if'add new Job' button gets activated
Past record of Registration No. will be shown
It saves all the job done in the Data base and it also prints the bill
It generates the bill in the form of pdf you can easily save or print the pdf
The bill can be generated with the help of any 'browser' or any 'pdf' opening software like Adobe Acrobat DC it is directly dependent on your system's default 'open with' pdf option you can change as if you want.
It has clear button which clears the whole data and gets the cursor to the start
It has autocalculation function which performs automatic calculation of inputed data and it is dynamic
It has exit button which terminates the program
It is only User side code, I will complete and upload the admin part soon....
