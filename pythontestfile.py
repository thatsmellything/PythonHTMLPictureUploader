import glob

print("Hello world")

#File objects
#f = open('test.txt', "r")
#print(f.name)
#f.close()

#for each f in pics


jpgfiles = []
for file in glob.glob("pics/*.txt"):
    jpgfiles.append(file)
print(jpgfiles)

#Writes the list to the file
with open('listofjpg.txt', 'w') as f:
    for item in jpgfiles:
        f.write("%s\n" % item)