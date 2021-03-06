#! /usr/bin/python
# Filename:backup_ver1.py

import os
import time

# 1. The files and directories to be backed up are sepecified in a list
source = ['/home/zjw/bin/script', '/home/zjw/bin/test']

# 2. The backup must be stored in a main backup directory
target_dir = '/home/zjw/bin/recovery/'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command to put the files in a zip file
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
