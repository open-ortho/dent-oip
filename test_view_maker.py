''' Test classes vm
'''

import unittest
import logging
import view_maker as vmd
from pydicom import dcmread

class Test(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s: %(message)s')
        logging.getLogger().setLevel('DEBUG')

    def tearDown(self):
        pass

    def test_generate_tables_in_csv(self):
        vmd.generate_tables_in_csv()

    def test_generate_rst_pages(self):
        vmd.generate_rst_pages()
