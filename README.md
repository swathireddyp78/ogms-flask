OGMS:

This is the departmental graduate student portal. This website maintains a database ogms.sql that records data about students, assistantships, courses, and enrollments. 

This website has the following functionality:
1. Graduate Director retrieves students from PAWS for the department
2. Graduate Director retrieves courses from PAWS for the department
3. Graduate Director retrieves enrollments from PAWS for the department
4. Graduate Director awards assistantship to student (this should also submit this information to the PAWS system by calling the REST service there).
5. Graduate Director requests department level statistics (you may hard code "GSU" and "CSC"; Allow user to choose term and year from pull down list; no login required for this option as well)
6. Faculty member submits grade for a student (sends data to REST service at PAWS); Faculty member need not have a login.

OGMS provides the following REST Web service:
1. Given sid, return assistantship ('yes' or 'no').
