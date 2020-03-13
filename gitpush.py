from git import Repo 
import os

PATH_OF_GIT_REPO = os.getcwd() + "/.git"
COMMIT_MESSAGE = 'automatic commit'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()
