import os

path = (os.path.expanduser('~')+"/.prefs")
for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))
