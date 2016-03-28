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

# Script for extracting compressed files after they've been downloaded.
# Can be used with any torrent client, such as, Transmission, etc.

import os
import subprocess
import datetime

def findrar():
    for root, dirs, files in os.walk(torrentdir):
        for name in files:
            if name.find('264') and name.endswith('rar'):
                f.write(str(datetime.datetime.now()) + ' found file to extract: ' + os.path.join(torrentdir, name) + '\n')
                return name
       
torrentdir = os.path.join(os.environ['TR_TORRENT_DIR'], os.environ['TR_TORRENT_NAME'])
logfile = '/i-data/md0/downloads/post-download.log'
f = open(logfile, 'a')
f.write(str(datetime.datetime.now()) + ' completed downloading: ' + torrentdir + '\n')
if os.path.exists(torrentdir):
    filename =  findrar()
    f.write(str(datetime.datetime.now()) + ' start extracting: ' + filename + '\n')
    subprocess.call(['/ffp/bin/unrar', 'e', os.path.join(torrentdir, filename), '/i-data/md0/video/'])
    f.write(str(datetime.datetime.now()) + ' completed extracting: ' + torrentdir + '\n') 
else:
    f.write(str(datetime.datetime.now()) + ' directory does not exist: ' + torrentdir + '\n')   
