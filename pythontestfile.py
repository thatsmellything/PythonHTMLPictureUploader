import glob

print("Hello world")

#File objects
#f = open('test.txt', "r")
#print(f.name)
#f.close()

#for each f in pics
jpgfiles = []
for file in glob.glob("pics/*.txt"):
    jpgfiles.append("Add html img tag here"+file)
print(jpgfiles)

#Writes up the HTML File and stores it into a variable
with open('testforpicturesP1.html', 'r') as file:
    data1 = file.read().replace('\n', '')
									
with open('testforpicturesP2.html', 'r') as file:
    data2 = file.read().replace('\n', '')



#Writes the list to the file
with open('testforpictures.html', 'w') as f:
    f.write(data1)
    for item in jpgfiles:
        f.write("%s\n" % item)
    f.write(data2)

f.close()