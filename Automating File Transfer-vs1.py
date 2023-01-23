''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''

#Begin Project Script:


def transfer_ftpfiles():
    #Function to print the whole script to run the 
    # file transfer process to completion


#Connect to the external FTP server and list the files in the directory.
    from ftplib import FTP

    ftp = FTP('ftp.us.debian.org') # Host name of ftp server

    ftp.login() #Log in to the host server anonymously 

    # changing directory
    ftp.cwd('debian')

    ftp.retrlines('LIST') #Files and directories are listed

    ftp.quit()  #Close connection

    #Use the os library to check for the existence of a local directory where the files will be stored.

    import os.path

    # Path
    path = 'C:\\Users\Grego\Desktop\Brainnest\Project_Files\Week01_DPfiles'

    # Check whether the path is an existing directory
    isdir = os.path.isdir(path)
    print(isdir)

    #Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    #Program for downloading the file in FTP Server into local file: 
    # Import Module
    import ftplib

    # Fill Required Information
    HOSTNAME = "ftp.us.debian.org"  # This is the FTP remote server name
    USERNAME = "debian@xz.com"       # Host’s email address
    PASSWORD = "eUj8GeW55SvYooDSm5v6N" # Host’s password. This might change with time, check host website

    # Connect FTP Server
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

    # force UTF-8 encoding
    ftp_server.encoding = "utf-8"

    # Enter local file name with extension – stored in client’s computer
    filename = "serverdoc.txt"

    # Write to client's local file in binary mode
    for one_file in ftp_server:
        with open(filename, "wb") as file:
        # Downloading the FTP server file "RETR filename" to local file 
            ftp_server.retrbinary(f"RETR {filename}", file.write)

    # Get list of files
    ftp_server.dir()

    # Display the content of downloaded file
    file= open(filename, "r")
    print('File Content:', file.read())

    # Close the Connection
    ftp_server.quit()

    # Use the shutil library to move the files from the local directory to the internal network.

    # Python program to explain shutil.move() method
        
    # importing os module
    import os

    # importing shutil module
    import shutil

    # path
    path = 'C:\\Users\Grego\Desktop\Brainnest\Project_Files\Week01_DPfiles'
    # List files and directories
    # in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
    print("Before moving file:")
    print(os.listdir(path))


    # Source path
    source = 'C:\\Users\Grego\Desktop\Brainnest\Project_Files\Week01_DPfiles\serverdoc.txt'

    # Destination path
    destination = 'C:/Users/*********************/destination' #Company's in

    # Move the content of source to destination
    dest = shutil.move(source, destination)

    # List files and directories
    # in "C:/Users / Rajnish / Desktop / GeeksforGeeks"
    print("After moving file:")
    print(os.listdir(path))

    # Print path of newly
    # created file
    print("Destination path:", dest)



#To schedule the entire script to run everyday, downloading FTP server files to company's internal network at 4:30AM

import schedule
import time

schedule.every().day.at("04:30").transfer_ftpfiles()
while True:
	schedule.run_pending()
	time.sleep(1)
