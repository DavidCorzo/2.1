from git import Repo 
import os, yaml, time, datetime


def get_message():
    Periods = {
        "1": {
            "starts": datetime.time(hour=7,minute=1),
            "ends": datetime.time(hour=8,minute=30)
        },
        "2": {
            "starts": datetime.time(hour=8,minute=31),
            "ends": datetime.time(hour=10,minute=0)
        },
        "3": {
            "starts": datetime.time(hour=10,minute=1),
            "ends": datetime.time(hour=11,minute=30)
        },
        "4": {
            "starts": datetime.time(hour=11,minute=31),
            "ends": datetime.time(hour=13,minute=0)
        },
        "5": {
            "starts": datetime.time(hour=13,minute=1),
            "ends": datetime.time(hour=14,minute=30)
        },
        "6": {
            "starts": datetime.time(hour=14,minute=31),
            "ends": datetime.time(hour=16,minute=0)
        }, 
        "0": {
            "starts": datetime.time(hour=16,minute=1),
            "ends": datetime.time(hour=7,minute=0)
        } # other
    } 
    with open("dependencies_hours.yaml") as file:
        F = yaml.full_load(file)
        file.close()

    Master = {
        "monday":{},
        "tuesday":{},
        "wednesday":{},
        "thursday":{},
        "friday":{},
        "saturday":{},
        "sunday":{},
    }

    for k,v in F.items():
        for i in v:
            temp = i
            temp = temp.split("[")
            temp[1] = "[" + temp[1]
            Master[str(temp[0])].update({k:Periods[str(temp[1].replace('[','').replace(']',''))]})
    
    # for k,v in Master.items():
    #     print(k)
    #     for i in v:
    #         print(v,i)

    date = str(datetime.datetime.now().strftime("%A,%H,%M")).split(",") # day of the week, hour, minute
    time = datetime.time(hour=int(date[1]),minute=int(date[2]))

    activated = False
    message = ""
    if (bool(Master[str(date[0]).lower()])): # if it is empty dont do anything
        for course,class_times in Master[str(date[0]).lower()].items():
            if (class_times["starts"] <= time) and  (time <= class_times["ends"]):
                activated = True
                print(activated)
                message = str(time) + " @ " + course


    if (not activated):
        message = str(date[0] + " ") + str(time) + " @ " + "extracurricular"
        
    return message


def git_push():
    PATH_OF_GIT_REPO = os.getcwd() + "/.git"
    COMMIT_MESSAGE = get_message()
    
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        print("|!| Refs have been pushed to git. DGCM")
    except:
        print('Some error occured while pushing the code')    


if __name__ == "__main__":
    git_push()
