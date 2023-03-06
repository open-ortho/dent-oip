''' Test classes vm
'''

import unittest
import os
import logging
import sqlite3
import view_maker as vm

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
        try:
            vm.initdb(vm.cur)
        except sqlite3.OperationalError:
            pass
        vm.load_views(vm.cur)
        views = vm.cur.execute(f"SELECT view_name FROM ortho_views;").fetchall()
        self.assertEqual(len(views),77)
        self.assertEqual(views[0][0],"IV-01")


