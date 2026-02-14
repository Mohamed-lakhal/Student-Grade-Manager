# School: Higher  school of technology-Méknes
Name: MOHAMED_LAKHAL


Sector: Web development



General introduction:
Dear reader, I hope you are well. In this report
I will explain the role of this program, which is a student manager where professors can save allot of time when they use this program who calculate average by details for each student and he decide after that  if the student is PASS or FAIL as-well this program  give professors opportunity to save they students data(information) or if they have already a file contain students data they can upload it on the program and keeping working on .

NOTE: this program was programmed by PYTHON language and that after 10 days of studying this lang, but with professor H. BENNIS efforts in basics of C language the problems I faced were at the level. 



Technology's:

> LOOPS

> Conditional  statements

> Functions

> parallel lists
 _________________________________________________ 
 
 Built with:
 > Python 🐍

 . < os > (for file search)
 
 . < time > (for the time exact)


 STUDENTGRADE MANAGER
 
1.Intoductions to the problem:

Imagine you are a teacher whit 30 students.
Each student has 3 test grades. you need to:
1.calculate each student’s average 
2.find who passed (10/20 or higher) or failed 
3.rank the top students
4.calculate class statistics
Doing that manually:
•	for 30 students *3 grades = 90 calculations
•	30 average to compute by hand
•	High chance of mistakes
•	Hours of work each time grades change 
Real example:
Student: Ahmed - Grades: 14, 16, 18
Manual calculation: (14+16+18) ÷3 = 48÷3 = 16.00
Status: PASS (16≥10)
Now repeat these 29 more times...

Imagine doing that for 100 students!
This why we created the student grade manager.


 2.why this project was made

We wanted to solve these 4 main problems:
1.	Time waste 
Teachers spend hours calculating when computers can do it in second.
2.	Human errors
People make mistakes in math, especially many numbers.
3.	No organization
Paper lists get lost. Excel files get confusing   
4.	No quicks insights 
Hard quickly see:” How many failed?” or “Who are the top 3?”

My solution: One program that does everything automatically.

3.system interface: The menu
When you open the program, you see this:

            STUDENT GRADE MANAGER
[1] ADD NEW STUDENT
[2] VIEW ALL STUDENTS  
[3] SEARCH STUDENT
[4] CALCULATE CLASS AVERAGE
[5] STUDENTS STATISTICS
[6] FIND TOP STUDENTS
[7] FILE MANAGEMENT (Save/Load)
[0] EXIT
Your choice please: _

A friendly interface whit multiple choice [0-7].

[1] ADD NEW STUDENT:

In this choice user can add a new student to database 
in this program I worked by 2 parallels array which the first contain students name I called it STD_NAME and the second one to save grades 
on it I called it STD_GRADE.

How did I storage the data in two independent lists?

So to store data I asked for:
name 
grades(3grades)
confirmation (save or cancel) 
problems solved:
•	empty names: program says “name cannot be empty “
•	wrong grades: Only accepts numbers 1-20
•	duplicate names: Won’t add the same name twice
•	change mind: Can cancel before saving
but the main idea is to append name and grades to STD_NAME and 
STD_GRADE in the same moment to who make sure the index of the name in STD_NAME still the same index in STD_GRADE, that give us the opportunity to get-back the information if we need, but if one of problems we talked on it before still present the transaction will cancel    

Example:
STUDENT NAME: Ali
ENTER grade: 15 ✓
ENTER grade: 16 ✓  
ENTER grade: 17 ✓
DROP I TO FINISH OR I TO CANCEL: E
Added: ALI with grades [15, 16, 17]


[2] VIEW ALL STUDENTS

This function shows all student you added but, I added some magic on it:
I work on two deferent ways to view:
[D] for detailed list (shows everything)
[Q] for quick list (shows only name, average and pass/fail)

Detailed list shows:

•	Name 
•	All 3grades 
•	Average (calculated automatically)
•	Pass or Fail status

Quick list shows:

ALI       → 16.00/20 → PASS

SARAH     → 14.33/20 → PASS






[3] SEARCH STUDENT

Finds one specific student.
How it works:
•	Type the student’s name 
•	Program shows their grades and average 
•	If not found, you can try again or cancel 
•	
Example:

STUDENT NAME: ali
FOUND:
NAME: ALI
GRADES: [15, 16, 17]
AVERAGE: 16.00/20
STATUS: PASS
 Problem we solved: Case doesn’t matter (ali = ALI = Ali)




[4] CALCULATE CLASS AVERAGE

•	Calculates the average of the whole class
•	Requirement Need at least 2 students

What you see:

CLASS AVERAGE: 14.50/20
NOTE: Good performance overall.
Notes shown:
•	16+ => “Excellent!”
•	14-16 => “Very good”
•	12-14 => “Good performance”
•	10-12 => “Satisfactory”
•	Below 10 => “Needs improvement”

[5] STUDENTS STATISTICS

•	Shows pass/Fail percentages.
=====================================
CLASS STATISTICS 
TOTAL STUDENTS: 3

PASSED (3 – 100.0%):
 AHMED – MOHAMED – SARA

FAILED (0 – 0.0%):

NOTE: GOOD JOB PROFESSOR!
================================== 

•	Also gives teacher feedback

Mostly passed → “GOOD JOB PROFESSOR!”
About half passed → “NEED SOME EFFORT!”
Mostly failed → “NEED BIG SUPPORT!”



[6] FIND TOP STUDENTS

	Finds 1st.2nd and 3rd place

What if two students have same average?
  both get same rank 







Example:
TOP STUDENTS 
FIRST PLACE:
 ALI – KHALID – 13.0/20

SECOND PLACE:
 MOHAMED – MARWA – 12.0/20

THIRD PLACE:
 AHMED – MAROUAN – 11.0/20
Total Students: 6 | Date: [06-02-2026]


Also, we add real DATE in the bottom!


[7&8] FILE MANAGEMENT (Save/Load)


⚠️ MOST IMPORATANT OPTION⚠️


This option gives you the opportunity to save your students data so you don’t lose it.

There is to option appears:

FOR SAVE AS A FILE DROP [S]
FOR LOAD FROM A FILE [L]

To save: Press S Data saved by default to “STUDENT.txt” or you can give a special name to your file it’s depend on you like user.

Why this is critical: Without saving, all data disappears when you close the program!

Actually, I divided it into two functions because of some problems.
	[7] SAVE_DATA
	[8] LOAD_DATA






[0] EXIT: Close the program safely

	Always remember do this:
1.	Choose 7 to save first
2.	Then choose 0 to exist
3.	Your work will be there next time!



---

 📊 Program Output Sample
> This is a preview of the final statistics generated by the system:

```text
=========================================
        FINAL CLASS STATISTICS
=========================================
   Total Students : 6
   Status         : Data Saved Successfully
   Date           : 06-02-2026
=========================================
