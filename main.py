from dotenv import load_dotenv
load_dotenv()
from time import sleep
from github import Github, Auth
from os import getenv, system, remove

GIT = Github(auth=Auth.Token(getenv("TOKEN")))
REPO_NAME = "LineageOS"
MY_REPO = "Project-FelineX"
meowcheck = False

lineage = GIT.get_organization(REPO_NAME)
org = GIT.get_organization(MY_REPO)
try:
    remove("logs.txt")
except:
    pass
logFile = open("logs.txt", "a")
for repo in lineage.get_repos():
    repomain = repo.full_name.replace(f"{REPO_NAME}/", "")
    if "device" not in repomain and "kernel" not in repomain:
        print(f"{REPO_NAME}/{repomain}")
        try:
            meowcheck = org.get_repo(repomain)
        except:
            meowcheck = False
        if meowcheck:
            meowcheck.delete()
            logFile.write(f"[DELETED] - {repomain}")
            print("Deleted")
        sleep(5)
        try:
            org.create_fork(repo, default_branch_only=True)
            logFile.write(f"[FORKED] - {repomain}")
            print("Forked!")
        except Exception as e:
            logFile.write(f"[ERROR] - {repomain}")
            print("skipped")
    else:
        continue
logFile.close()
