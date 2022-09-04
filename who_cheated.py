import csv
from datetime import datetime, timedelta
def final_points():
    start_date={}
    submission_time={}
    result={}
    with open("start_times.csv") as read_start:
        for line in csv.reader(read_start, delimiter=";"):
            start_date[line[0]]=datetime.strptime(line[1],"%H:%M")
    
    with open("submissions.csv") as submission_file: 
        for line in csv.reader(submission_file, delimiter=";"):
            name= line[0]
            key = line[1]
            value = int(line[2])
            time_of=datetime.strptime(line[-1],"%H:%M")

            #checking if submission time has exceeded 3 hours
            if time_of - start_date[name] < timedelta(hours=3):

                #adding the student into dictionary if not already added and creating nested dictionary for different parts
                if name not in submission_time:
                    submission_time[name] = {}
                    submission_time[name][key] = value
                else:
                #if already in dictionary, checking if the value of the part is greater and if it is replacing the previous value
                    if key in submission_time[name]:
                        if value > submission_time[name][key]:
                            submission_time[name][key] = value
                    else:
                        submission_time[name][key] = value

    #iterating through the dictionary to find total and store it in result as a dictionary
    for names in submission_time:
        result[names] = sum(submission_time[names].values())
    return result
        

if __name__ == "__main__":
    print(final_points())








