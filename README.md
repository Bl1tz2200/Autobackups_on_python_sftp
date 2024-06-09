# Autobackups_on_python_sftp
I made autobackup service on python. I used SFTP to transmit files.

# Create settings file
First run **backup_settings_set.py** to create settings file.<br>
That will create file with parameters. Parameters are used in **save_files.py**.<br>

# Save files
After running **save_files.py** files will be saved to remote host's path with adding date and time (year-month-day hours:minutes) to the tail of the filename.<br>
If something is wrong files won't save and error won't raise. Be careful with settings.<br>

# Auto save
To make files automatically save you can use crontab if you use linux.<br>
For Windows system you can use Windows Task Scheduler.

# Addition
Files from py folder won't run if you don't have python installed, that's why you can use **.exe** ones.<br>
