#! /usr/bin/python
# Filename:backup_ver3.py

import os
import time

# 1. The files and directories to be backed up are specified in a list
source = ['/home/zjw/bin/script/', '/home/zjw/bin/test/']

# 2. The backup must be stored in a main backup directory
target_dir = '/home/zjw/bin/backup/'

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = raw_input('Enter a comment -->')
if len(comment) == 0: # check if a comment was entered
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', ' ') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory', today

# 5. We use the zip command to put these files into a zip file
zip_command = "zip -qr '%s' %s" %(target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
