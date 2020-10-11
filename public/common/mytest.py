#coding=utf-8

import unittest
import os
from public.common import pyselenium
from config import globalparam
from public.common.log import Log



class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        #run Selenium on local
        #self.dr = pyselenium.PySelenium(globalparam.browser)
        #run Remote Selenium
        self.dr = pyselenium.PySelenium(globalparam.browser, globalparam.remoteAddress)
      

    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')
