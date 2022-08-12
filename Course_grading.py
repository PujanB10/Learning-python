
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_info=input("Exam points: ")


def to_points(points):
    return points//4

def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
 
    return a

name={}
with open(student_info) as new_file:
     for lines in new_file:
        lines = lines.replace("\n", "")
        list_of_name=lines.split(";")
        if list_of_name[0]=="id":
            continue
        name[list_of_name[0]]=list_of_name[1]+" "+list_of_name[2]

    
exercise={}
with open(exercise_data) as new_files:
    for lines in new_files:
        sum=0
        lines = lines.replace("\n", "")
        list_of_ex=lines.split(";")
        if list_of_ex[0]=="id":
            continue
        for i in range(1,len(list_of_ex)):
            sum+=int(list_of_ex[i])
        exercise[list_of_ex[0]]=sum



exam={}
with open(exam_info) as exam_file:
    for lines in exam_file:
        sum=0
        lines = lines.replace("\n","")
        list_of_exam= lines.split(";")
        if list_of_exam[0]=="id":
            continue
        for i in range(1,len(list_of_exam)):
            sum+=int(list_of_exam[i])
        exam[list_of_exam[0]]=sum



print("name"+" "*26+"exec_nbr"+"  "+"exec_pts."+" "+"exm_pts."+"  "+"tot_pts."+"  "+"grade")
for id,names in name.items():
    print(f"{names:30}{exercise[id]:<10}{to_points(exercise[id]):<10}{exam[id]:<10}{to_points(exercise[id])+exam[id]:<10}{grade(to_points(exercise[id])+exam[id]):<10}")

