import numpy as np 
import pandas as pd
n=int(input("Enter Number Of Students:"))
stu_det=[]
for i in range(n):
    name=input("Name:")
    m_m=int(input("marks(mathematics):"))
    m_p=int(input("marks(physics:)"))
    m_c=int(input("marks(chemistry:)"))
    arr=np.array([m_m,m_p,m_c])
    if (m_c>35 and m_m>35) and m_p>35:
        result="Pass"
    else:
        result="Fail"
    avg=np.mean(arr)
    if avg>85:
        grade="A"
    elif avg>70 and avg<85:
        grade="B"
    else:
        grade="C"
    dict1={"name":name,"marks_m":m_m,"marks_p":m_p,"marks_c":m_c,"average":avg,"Result":result,"Grade":grade}
    stu_det.append(dict1)
s=input("if you want each student details press yes otherwise no")
if s=="yes":
    print("Average percentage:",dict1["average"])
    print("Rank:",dict1["Result"])
    print("Grade:",dict1["Grade"])
else:
    df = pd.DataFrame(stu_det)
    print(df)

    
    