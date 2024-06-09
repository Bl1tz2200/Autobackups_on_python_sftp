import paramiko
from datetime import datetime

def upload(hostname, username, password, local_file_path, remote_file_path):
    ssh = paramiko.SSHClient()
    # ssh.load_host_keys(/path/to/host/key) # Add host key from local path
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host keys (not secure for production)

    # Connect to the server
    ssh.connect(hostname=hostname, username=username, password=password)

    # Establish the SFTP client
    sftp = ssh.open_sftp()
    sftp.put(local_file_path, remote_file_path)

    sftp.close() # Stop connections
    ssh.close()



def main ():
        with open("backup_settings.txt", "r") as backup_settings:
            for line in backup_settings:
                settings = line.split(";")

                #Get settings from file
                hostname = settings[0]
                username = settings[1]
                password = settings[2]
                local_file_path = settings[3]
                remote_file_path = settings[4]

                #Add data and time to saved file
                index = -1
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                format_remote_file_path = ""
                for i in remote_file_path[::-1]:
                    if i != ".":
                        index -= 1
                    else:
                        format_remote_file_path = f'{remote_file_path[:index:]} {now}{remote_file_path[index::]}'
                        break

                upload(hostname, username, password, local_file_path, format_remote_file_path)




if __name__ == "__main__":
    main()
