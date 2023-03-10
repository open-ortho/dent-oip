''' Test classes vm
'''

import unittest
import os
import logging
import sqlite3
import view_maker as vm
import view_maker_dcm as vmd
from pydicom import dcmread

class Test(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s: %(message)s')
        logging.getLogger().setLevel('DEBUG')
        vm.cur = vm.con.cursor()

    def tearDown(self):
        try:
            os.remove(vm.DBFILE)
        except FileNotFoundError:
            pass

    def test_initdb(self):
        ''' Test DB initialization

        '''
        vm.initdb(vm.cur)
        tables = vm.cur.execute(f"SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';").fetchall()
        for table in tables:
            logging.debug(table)
        self.assertEqual(len(tables),4)

    def test_load_views(self):
        ''' Load views into DB.
        
        '''
        try:
            vm.initdb(vm.cur)
        except sqlite3.OperationalError:
            pass
        vm.load_views(vm.cur)
        views = vm.cur.execute(f"SELECT view_name FROM ortho_views;").fetchall()
        self.assertEqual(len(views),77)
        self.assertEqual(views[0][0],"IV-01")


    def test_generate_tables_in_csv(self):
        vmd.generate_tables_in_csv()

    def _dicom(self):
        ignore_values_of = [
            "(0008,0018)",
            "(0020,000d)",
            "(0020,000e)",
        ]
        def show_dataset(ds, indent):
            for elem in ds:
                tag = str(elem.tag).replace(" ","")
                if elem.keyword != "PixelData":
                    if elem.VR == "SQ" or tag in ignore_values_of:
                        value = ""
                    else:
                        value = elem.value
                    attr_name = f"{indent} {elem.name}".strip()
                    print(f'"{attr_name}","{tag}","{value}",""')
                if elem.VR == "SQ":
                    indent += ">"
                    for item in elem:
                        show_dataset(item, indent)
                    indent = indent[1:]

        def print_dataset(file_name):
            ds = dcmread(file_name)
            show_dataset(ds, indent="")

        print('"Attribute Name","Tag","Value","Meaning"')
        print_dataset("test.dcm")