#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# Ready configuration file
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# Set project parameter
#prj_path = read_config.getValue('projectConfig','project_path')
# Set project parameter
#prj_path = '/' + os.path.dirname(os.path.abspath(__file__)).strip('/config')
prj_path = '/' + os.path.dirname(os.path.abspath(__file__))[:-7]


# Path of log
log_path = os.path.join(prj_path, 'report', 'log')
# Path of screenshot
img_path = os.path.join(prj_path, 'report', 'image')
# Path of test report
report_path = os.path.join(prj_path, 'report', 'testreport')

'''
# Default browser - run Selenium on local
#browser = 'chrome'

# Change default broswer to "RChrome" to run Remote Selenium 
browser = 'RChrome'
remoteAddress = 'localhost:4444'

# Change default broswer to "RFireFox" to run Remote Selenium 
browser = 'RIE'
remoteAddress = 'localhost:4444'
'''


# Change default broswer to "RFireFox" to run Remote Selenium 
browser = 'RChrome'
remoteAddress = 'localhost:4444'


# Path of test data
data_path = os.path.join(prj_path, 'data', 'testdata')