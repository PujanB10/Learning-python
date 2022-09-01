import urllib.request 
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data=my_request.read()
    courses = json.loads(data)
    output=[]
    for elements in courses:
        total=0
        for numbers in elements["exercises"]:
            total+=int(numbers)
        if elements["enabled"]:
            output.append((elements["fullName"],elements["name"],elements["year"],total))
    return output

def retrieve_course(course_name: str):
    url=f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request= urllib.request.urlopen(url)
    courses= json.loads(my_request.read())
    total_hours=0
    total_exercises=0
    max_student=0
    for elements in courses:
        if courses[elements]["students"]>max_student:
            max_student=courses[elements]["students"]
        total_hours+=courses[elements]["hour_total"]
        total_exercises+=courses[elements]["exercise_total"]
    return{
        "weeks": len(courses),
        "students": max_student,
         "hours" : total_hours,
         "hours_average" : int(total_hours/max_student),
         "exercises" : total_exercises,
         "exercises_average" : int(total_exercises/max_student)
    }
  
if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))
