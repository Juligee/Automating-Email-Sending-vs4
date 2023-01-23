''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

#Import all modules 

import schedule
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

# send email message 'msg' to coworkers
def message(subject="Python Notification",
			text="", img=None, attachment=None):
	
	# build message contents
	msg = MIMEMultipart()
	
	# Add Subject
	msg['Subject'] = subject
	
	# Add text contents
	msg.attach(MIMEText(text))

	# Check if we have anything
	# given in the img parameter
	if img is not None:

		# Check whether we have the
		# lists of images or not!
		if type(img) is not list:
			
			# if it isn't a list, make it one
			img = [img]

		# Now iterate through our list
		for one_img in img:
			
			# read the image binary data
			img_data = open(one_img, 'rb').read()  #Open and read image as binary file
			
			# Attach the image data to MIMEMultipart
			# using MIMEImage,
			# we add the given filename use os.basename
			msg.attach(MIMEImage(img_data,
								name=os.path.basename(one_img))) #one_img is replaced the intended file in your directory

	# Do the same for attachments
	# as was done for images
	if attachment is not None:

		# Check whether we have the
		# lists of attachments or not!
		if type(attachment) is not list:
			
			# if it isn't a list, make it one
			attachment = [attachment]

		for one_attachment in attachment:

			with open(one_attachment, 'rb') as f:
				
				# Read in the attachment using MIMEApplication
				file = MIMEApplication(
					f.read(),
					name=os.path.basename(one_attachment)
				)
			file['Content-Disposition'] = f'attachment;\
			filename="{os.path.basename(one_attachment)}"'
			
			# Add the attachment to our message object
			msg.attach(file)
	return msg


def mail():
	
	# initialize connection to the email server,
	# we will use gmail here
	smtp = smtplib.SMTP('smtp.gmail.com', 421) # To establish connection to the email server the right port number and server name must be known
	smtp.ehlo()
	smtp.starttls()  #To establish a connection, we use the protocol command starttls
	
	#Mailender Login with your email and password
	smtp.login('gweggyo****b@gmail.com', 'Heml***')

	# Call the message function, defined previously
	msg = message("Good day!", "Hello there!, the work process have been sent.",
				r"C:\Users\Grego\Desktop\Brainnest\bkgplkin.jpg",
				r"C:\Users\Grego\Desktop\Brainnest\Project_Files\Week01_DPfiles\Automating File Transfer.py")
	
	#Get a list of emails, where to send mail to
	to = ["gre***@gmail.com",
		"joa***petals", "nyonge***en6@gmail.com"]
	#for receiver in to:

	# Provide some data to the sendmail function!
	smtp.sendmail(from_addr="gregoryswit4@gmail.com",
				to_addrs=to, msg=msg.as_string())
	
	# Finally, close the connection
	smtp.quit()

#Finally, schedule email messages for sending everyday

schedule.every().day.at("10:30").do(mail)
while True:
	schedule.run_pending()
	time.sleep(1)
