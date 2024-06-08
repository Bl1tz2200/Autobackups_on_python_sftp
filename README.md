# Autobackups_on_python
I made autobackup service on python. I used SFTP.

# Create settings file
First run **backup_settings_set.py** to create settings file.<br>
That will create file with parameters. Parameters are used in **save_files.py**.<br>

# Save files
After running **save_files.py** files will be saved to the remote host's path.<br>
If something is wrong files won't save and error won't raise. Be careful with settings.<br>

# Addition
Files won't run if you don't have python installed, that's why you can use **.exe** ones.<br>
