firstname = input("enter the firstname\n")
#"\n" allowes the program to run the next line
surname =input("enter the surname \n")
exammarks = int(input("enter exam marks\n"))
if (exammarks > 80) and (exammarks < 100) :
    print(firstname,surname,"gradeA-Outstanding")
elif (exammarks >60) and (exammarks <79) :
    print(firstname,surname,"GradeB_Satisfactory")
elif (exammarks >50) and (exammarks <59) :
    print(firstname,surname,"gradeC_pass")
elif (exammarks >0) and (exammarks) :
    print(firstname,surname,"gradeD_Fail\n")
