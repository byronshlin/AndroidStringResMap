## AndroidStringResMap

# StringsResCSVGen

shell> python AndroidStringResMap zh-rTW in

It scans all strings resources inside the following folders,<br>
values  
values-zh-rTW  
values-in  


then generates a csv file, 'output.csv'

If we want to create a string map csv for the following folder:

values/strigns.xml<br>
>  \<string name="app_name">Movie\</string>

values-zh-rTW/strigns.xml<br>
>\<string name="app_name">電影\</string>

values-in/strigns.xml<br>
>\<string name="app_name">Film\</string>

values-es/strigns.xml<br>
>\<string name="app_name">Película\</string>

Please input command,  
>python AndroidStringResMap zh-rTW in es

output.csv as followings:
<br>
```
resources, en, zh-rTW, in, es
app_name,Movie,電影,Film,Película
```

# StringsResXMLGen
process the output.xml from StringsResCSVGen.

[TODO] not support empty string resource..


