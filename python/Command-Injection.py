# Non-Compliant Code
import os, subprocess

def create_file(username, filename):
    os.system('touch tmp/' + username + '/' + filename)
    file.close()


# Compliant Code
import os, subprocess

def create_file(username, filename):
    # os.system('touch tmp/' + username + '/' + filename) # OS calls raise risk of OS injection
    file = open(f'tmp/{username}/{filename}', 'w')
    file.close()
