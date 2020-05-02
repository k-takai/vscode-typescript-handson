import os
import os.path
import time

from invoke import task
import yaml

os_user = "ubuntu"

@task
def build_environment(c):
    settings_file = "/root/settings/settings.yaml"
    if not os.path.exists(settings_file):
        return
    if os.path.exists(f"/home/{os_user}/.git"):
        return

    with open(settings_file) as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    sudo = f"sudo -u {os_user}"

    with c.cd(f"/home/{os_user}/"):

        if "repo" in settings:
            repo = settings["repo"]
            c.run(f"{sudo} git init")
            c.run(f"{sudo} git remote add origin {repo}")
            c.run(f"{sudo} git fetch origin")
            c.run(f"{sudo} git checkout origin/master")

        for command in settings.get("commands", []):
            c.run(f"{sudo} npm install ")

        for user in settings.get("users", []):
            c.run(f"{sudo} mkdir -p users/{user}")
            for file in settings.get("files", []):
                c.run(f"{sudo} cp -rf {file} users/{user}/")

        if "authorized_keys" in settings:
            with open(f"/home/{os_user}/.ssh/authorized_keys", "w") as f:
                for key in settings["authorized_keys"]:
                    f.write( key + "\n")

        c.run(f"chown -R {os_user}:{os_user} .")

@task
def start_sshd(c):
    c.run("/usr/sbin/sshd -D")

@task
def start(c):
    build_environment(c)
    start_sshd(c)
