import git
import os, yaml, datetime
import subprocess



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


def git_push(COMMIT_MESSAGE):
    PATH_OF_GIT_REPO = os.getcwd() + "/.git"
    try:
        repo = git.Repo(PATH_OF_GIT_REPO)
        print(repo.git.status())
        repo.git.add(update=True)
        print(repo.git.status())
        repo.index.commit(COMMIT_MESSAGE)
        print(repo.git.status())
        origin = repo.remote(name='origin')
        print(repo.git.status())
        origin.push()
        print(repo.git.status())
        return "|!| Refs have been pushed to git. DGCM"
    except: 
        return 'Some error occured while pushing the code'


def git_pull():
    repo = git.Repo(os.getcwd() + "/.git")
    try:
        repo.remotes.origin.pull()
        current = repo.head.commit
        print(repo.git.status())
        repo.remotes.origin.pull()
        print(repo.git.status())
        if current != repo.head.commit:
            print("|!| Changed, pull in order!")
        return "Done"
    except:
        return "Error courred!"
