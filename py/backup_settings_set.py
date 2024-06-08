def file_write(mode):
    with open("backup_settings.txt", mode) as backup_settings:
        #Set settins in file
        hostname = str(input("Enter your host's address: \n"))
        username = str(input("Enter your username: \n"))
        password = str(input("Enter your password: \n"))

        local_file_path = str(input("Enter your path to local file: \n"))
        remote_file_path = str(input("Enter your path to remote file: \n"))

        backup_settings.write(f"{hostname};{username};{password};{local_file_path};{remote_file_path};\n")

def file_read():
    with open("backup_settings.txt", "r") as backup_settings:
        i = 0
        for line in backup_settings:
            i+=1
            settings = line.split(";")

            #Get settings from file
            hostname = settings[0]
            username = settings[1]
            password = settings[2]
            local_file_path = settings[3]
            remote_file_path = settings[4]

            #Check of parameters by User
            print(f"\nYour info in line {i}:\n")
            print("hostname:\n", f"\t{hostname}")
            print("username:\n", f"\t{username}")
            print("password:\n", f"\t{password}")
            print("local_file_path:\n", f"\t{local_file_path}")
            print("remote_file_path:\n", f"\t{remote_file_path}")

            print("\nCheck all parameters, files won't save if something is wrong.")

def main ():
    file_write('w')
    file_read()

    adding_bool = True
    while adding_bool:

        adding = str(input("\nWant you add something more?(Y/n)\n"))
        adding_bool = True

        if adding.lower() in ["y", "yes", "ye", "es", "e", "s", "ys"]:

            file_write('a')
            file_read()

        else:
            adding_bool = False

    exit = input("\n\nPress enter to exit.")





if __name__ == "__main__":
    main()