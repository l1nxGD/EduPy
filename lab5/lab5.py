import re

def getText(name):
    f = open(name)
    text = f.read()
    f.close()
    return text

text1 = getText("task1-en.txt")
text2 = getText("task2.html")
text3 = getText("task3.txt")
text4 = getText("task_add.txt")

#task 1
task11 = len(re.findall(r"Fig\.?\d?(?:\([a-z]\)){0,1}", text1))
task12 = len(re.findall(r'\b\w{4}\b', text1))
print(task11, task12, sep='\n')

#task 2
font_style = re.findall(r'font-style: ?\w{1,};', text2)
font_weight = re.findall(r'font-weight: ?\d{1,};', text2)
print(font_style, font_weight, sep='\n')

#task 3
#id; surname; email; date; link
id = re.findall(r"[a-zA-Z/ ]\d{1,}[a-zA-Z/ ]", text3)
surname = re.findall(r"[A-Z][a-z]{1,} ?", text3)#[mzogft]
email = re.findall(r"[a-zA-Z][a-zA-Z0-9-]{1,}@[a-zA-Z0-9-]{1,}[.]{1}\w{2,3}[zgtmfo]", text3)
date = re.findall(r"\d{4}-\d{2}-\d{2}", text3)
link = re.findall(r"https?://[a-zA-Z0-9.-]{1,}/", text3)

f = open('table.csv', 'w')
f.write("id;name;mail;date;link\n")
for i in range(10000):
    s = str(i + 1) + ";" + surname[i] + ";" + email[i] + ";" + date[i] + ";" + link[i] + "\n"
    f.write(s)
f.close()

#task 4
email_4 = re.findall(r" [a-zA-Z0-9./-]{1,}@[a-zA-Z0-9./-]{1,}[.]{1}\w{1,}", text4)
date_4 = re.findall(r"\d{2,4}[-./ ]\d{2}[-./ ]\d{2}", text4)
link_4 = re.findall(r"https?://[a-zA-Z0-9-]{1,}\.[a-zA-Z]{1,5}", text4)

print((email_4))
print((link_4))
print((date_4))