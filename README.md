# numpy-student-marks-analysis
student marks analysis using numpy(avg,min,max,pass/fail)
-> The objective of this project is to perform a student marks analysis using NumPy for calculations and Pandas for displaying results in a tabular format. The program calculates average marks, decides pass/fail, assigns grades, and stores all student information.
Program Flow
1.Input Number of Students
 The program first asks the user to enter the total number of students whose data needs to be analyzed.
2.Collect Student Details
  For each student, the program collects:
  1.Name of the student
  2.Marks in subjects like Mathematics, Physics, and Chemistry

3.Calculate Average Marks
  Using NumPy, the program calculates the average marks of each student.
4.Decide Pass or Fail
  The program determines whether the student passes or fails based on their marks in all subjects. Typically, marks above a     minimum threshold (like 35) are considered a pass.
5.Assign Grades
  Based on the average marks, grades are assigned:
  A: Average > 85
  B: Average > 70 and <= 85
  C: Average <= 70
6.Store Student Information
  The program stores each student's information, including name, marks, average, result, and grade, in a structured format.
7.Display Results in Table Format
  Finally, Pandas is used to display all student details neatly in a tabular format, making it easy to read and analyze.
->Libraries Used
  NumPy: For numerical operations like average, minimum, and maximum calculations.
  Pandas: For storing data in tabular format and displaying results neatly.
