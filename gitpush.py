from git import Repo 
import os

PATH_OF_GIT_REPO = os.getcwd() + "/.git"
COMMIT_MESSAGE = 'automatic commit'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        print(1)
        repo.git.add(update=True)
        print(2)
        repo.index.commit(COMMIT_MESSAGE)
        print(3)
        origin = repo.remote(name='origin')
        print(4)
        origin.push()
        print(5)
    except:
        print('Some error occured while pushing the code')    

git_push()
