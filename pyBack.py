#!/usr/bin/python

import sys

if len(sys.argv) != 3:
	print "No file to load or no output file. Ending."
	sys.exit()

file = open(sys.argv[1], "r")

out = open(sys.argv[2], "w")

lines = file.readlines()

file.close()

name = ""
phone = ""
vcard = ""

i=1

for line in lines:
	if line.__contains__("N;CHARSET=UTF-8;"):
		wholename = line.split(":")[1]
		wholename = wholename.split("\r\n")[0]
		#print wholename.split(";")
		wholename = wholename.split(";")
		if(len(wholename) == 1):
			name = wholename[0]
		else:
			name = wholename[0] + " " + wholename[1]

		print name

	if line.__contains__("TEL;PREF"):
		phone = line.split(":")[1]
		phone = phone.split("\r\n")[0]
		print phone

		vcard = "BEGIN:VCARD\nVERSION:2.1\nX-GAMMU-LOCATION:"+str(i)+"\nX-GAMMU-MEMORY:ME\nTEL;PREF;CELL:" + phone + "\n"
		vcard = vcard + "N;CHARSET=UTF-8:;" + name + "\nEND:VCARD\n\n"

		out.write(vcard)

		i=i+1

		

out.close()

