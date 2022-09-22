import os
error_msg = "Error, Rerun Program"

apps = "excel.exe", "mspub.exe", "onenote.exe", "outlook.exe", "powerpnt.exe", "winword.exe"
apps_list = list(apps)

print("MICROSOFT OFFICE APPS: ")
count = 0

for app in apps_list:
	count = count + 1
	print(str(count) +" "+ app)
	
option = input("\nEnter Here :_")
option = int(option)
count = -1

try:		
	if option <= len(apps_list):
		count = count + option
		count = int(count)
		app_to_start = apps_list[count]
		os.system("start " + app_to_start)
		
	else:
		print(error_msg)
		
except:
	print(error_msg) 
