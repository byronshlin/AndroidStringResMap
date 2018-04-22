# AndroidStringResMap
python AndroidStringResMap zh-rTW in

It scans all strings resources inside the follows folder
values
values-zh-rTW
values-in


then generates a csv file, 'output.csv'

for example

values/strigns.xml
<string name="app_name">Movie</string>

values-zh-rTW/strigns.xml
<string name="app_name">電影</string>

values-in/strigns.xml
<string name="app_name">Film</string>

values-es/strigns.xml
<string name="app_name">Película</string>


output.csv as followings:

resources, en, zh-rTW, in, es
app_name,Movie,電影,Film,Película

