import re
file = open('file.html')
line = file.readline()
regex = r'[A-Za-z0-9]+([\.-]{1})?\w+@\w+\.\w+'
while line:
  line = file.readline()
  if bool(re.search(regex, line)):
    email=line.split()
    print (*email)
file.close()