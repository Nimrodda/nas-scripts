#!/ffp/bin/python

# Copyright 2016 Nimrod Dayan www.codepond.org
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 

# Script for deleting old files from a specific folder after certain period 
# of time has past. This script is designed to be used in conjunction with
# cron.

import os
import logging
import time

DAYS = 7
CLEANUP_INTERVAL = DAYS * 24 * 60 * 60
LOGFILE = '/ffp/var/log/cleanup.log'
CLEANUP_DIR = '/i-data/md0/video'

logging.basicConfig(filename=LOGFILE, format='%(levelname)s:%(asctime)s %(message)s', level=logging.INFO)
logging.info('cron cleanup job started...')

now = time.time()
deleted = 0
for file in os.listdir(CLEANUP_DIR):
    file = os.path.join(CLEANUP_DIR, file)
    filetime = os.path.getctime(file)
    if now > filetime + CLEANUP_INTERVAL:
	logging.info('deleting file: %s', file)
	deleted = deleted + 1
	os.remove(file)

if deleted > 0:
    logging.info(str.format('{0} files have been deleted', deleted))
else:
    logging.info('no files have been deleted')
logging.info('cron cleanup job ended')
