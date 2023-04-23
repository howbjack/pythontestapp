with open('C:\downloads\File1.txt', encoding="utf8") as f:
    file1 = f.readlines()

with open('C:\downloads\File2.txt',encoding="utf8") as f:
    file2 = f.readlines()

print(f"Contents of file1, length: {len(file1)}")
#print(file1)
print(f"Contents of file2, length: {len(file2)}")
#print(file2)
if len(file1) < len(file2):
    combo_len = len(file1)
    #single_len = len(file2) - len(file1)
    FileLonger = "file2"
else:
    combo_len = len(file2)
    #single_len = len(file1) - len(file2)
    FileLonger = "file1"

f = open('C:\downloads\FileCombo.txt','w+',encoding="utf8")

for i in range(combo_len):
    combo_line = file1[i].strip() + " " + file2[i]
    #print(i)
    print(combo_line)
    f.write(combo_line)
#f.write('\n')

if FileLonger == "file1":
    f.write('\n')
    #print(combo_len, len(file1))
    for i in range(combo_len,len(file1)):
        # print(file1[i])
        f.write(file1[i])
else:
    #print(combo_len, len(file2))
    for i in range(combo_len,len(file2)):
        print(file2[i])
        f.write(file2[i])

f.close()

wordcount = 0
with open("C:\downloads\FileCombo.txt", encoding="utf8") as f:
    line = f.read()
    print(line)
    wordcount += len(line.split(" "))
print(f"Combined file FileCombo.txt written, total number of words is: {word_count}")
