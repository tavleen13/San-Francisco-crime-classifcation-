@@ -0,0 +1,45 @@
__author__ = 'tavleen'
#converted pdf to text by the following command
#************pdf2txt.py -o output.txt TOC_MIDTERM.pdf*******
import re
list_name= []
marks_list=[]
#file = open("output.txt" , "w")
#pdf = pyPdf.PdfFileReader(open("../TOC_MIDTERM.pdf", "rb"))
#for page in pdf.pages:
    #print page.extractText()
 #   file.write(page.extractText())
pattern = re.compile("[A-Z]{3,}\d{1,2}(\.\d{1}?)?")
with open("../output.txt", "r") as f:
    lines = f.readlines()
    #print lines
for line in lines:
    #print line
    #string = line.split('\t')
    #print string
    for match in re.finditer(pattern, line):
        word = match.group(0)
        #print word
        list_name.append(word)
print list_name
total_students = len(list_name)
value = re.compile("\d{1,2}(\.\d{1}?)?")
for mark in list_name:
    m = re.search(value, mark)
    score = m.group(0)
    marks_list.append(score)
print marks_list
count = 0
count = float(count)
for num in marks_list:
    num = float(num)
    count = count + num
print count
average_TOC = count/total_students
print average_TOC





