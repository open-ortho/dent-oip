#!/usr/bin/env python

import os
import sys
import sqlite3
import csv

PATH_TABLES = os.path.join('.','source','tables')
PATH_TABLES_GENERATED = os.path.join(PATH_TABLES, 'generated')
CSV_SNOMED = os.path.join(PATH_TABLES,'codes_snomed.csv')
CSV_DICOM = os.path.join(PATH_TABLES,'codes_dicom.csv')
CSV_DICOM_TAGS = os.path.join(PATH_TABLES,'tags_dicom.csv')
CSV_VIEWS = os.path.join(PATH_TABLES,'views.csv')
DBFILE='views.db'
T_VIEWS='ortho_views'
T_SNOMED='codes_snomed'
T_DICOM='codes_dicom'
T_DICOM_TAGS='tags_dicom'

# Columns
C_VIE = "view_name"
C_POR = "patient_orientation"
C_LAT = "laterality"
C_ARS = "anatomic_region_sequence"
C_ARM = "anatomic_region_modifier_sequnce"
C_PAM = "primary_anatomic_structure_sequence"
C_DEV = "device_sequence"
C_AQV = "acquisition_view"
C_IMV = "image_view"
C_FCA = "functional_condition_present_during_acquisition"
C_OCR = "occlusal_relationship"

con = sqlite3.connect(DBFILE)
cur = None

def initdb(cur):
    cur.execute(f'''
    CREATE TABLE {T_VIEWS}(
        {C_VIE} text,
        {C_POR} text,
        {C_LAT} text,
        {C_ARS} text,
        {C_ARM} text,
        {C_PAM} text,
        {C_DEV} text,
        {C_AQV} text,
        {C_IMV} text,
        {C_FCA} text,
        {C_OCR} text)
        ''')

    cur.execute(f'''
    CREATE TABLE {T_SNOMED}(
        id text,
        code int,
        meaning text)
        ''')
    load_snomed_codes(cur)

    cur.execute(f'''
    CREATE TABLE {T_DICOM}(
        id text,
        code int,
        meaning text)
        ''')
    load_dicom_codes(cur)

    cur.execute(f'''
    CREATE TABLE {T_DICOM_TAGS}(
        id text,
        attribute_name text,
        tag text)
        ''')
    load_dicom_tags(cur)

def load_snomed_codes(cur):
    with open(CSV_SNOMED,'r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['id'],i['code'], i['meaning']) for i in dr]
    cur.executemany(f"INSERT INTO {T_SNOMED} (id, code, meaning) VALUES (?, ?, ?);", to_db)

def load_dicom_codes(cur):
    with open(CSV_DICOM,'r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['id'],i['code'], i['meaning']) for i in dr]
    cur.executemany(f"INSERT INTO {T_DICOM} (id, code, meaning) VALUES (?, ?, ?);", to_db)

def load_dicom_tags(cur):
    with open(CSV_DICOM_TAGS,'r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['id'],i['attribute_name'], i['tag']) for i in dr]
    cur.executemany(f"INSERT INTO {T_DICOM_TAGS} (id, attribute_name, tag) VALUES (?, ?, ?);", to_db)

def load_views(cur):
    with open(CSV_VIEWS,'r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(
            i[C_VIE],
            i[C_POR],
            i[C_LAT],
            i[C_ARS],
            i[C_ARM],
            i[C_PAM],
            i[C_DEV],
            i[C_AQV],
            i[C_IMV],
            i[C_FCA],
            i[C_OCR]
            ) for i in dr]
    cur.executemany(f'''
    INSERT INTO {T_VIEWS} (
        {C_VIE},
        {C_POR},
        {C_LAT},
        {C_ARS},
        {C_ARM},
        {C_PAM},
        {C_DEV},
        {C_AQV},
        {C_IMV},
        {C_FCA},
        {C_OCR})
        VALUES (?,?,?,?,?,?,?,?,?,?,?);''', to_db)

def close_connection():
    con.commit()
    con.close()

def create_view(cur, view_type):

    query_view = f'''
-- SQLite
CREATE TEMP TABLE _temp (
    id text,
    attribute_name text,
    tag text,
    code_value text,
    meaning text
);
--
INSERT INTO _temp (id, attribute_name, tag)
SELECT id,
    attribute_name,
    tag
FROM tags_dicom;
-- Patient Orientation
UPDATE _temp
SET code_value = patient_orientation.code,
    meaning = patient_orientation.meaning
FROM (
        SELECT codes_dicom.code,
            codes_dicom.meaning
        FROM ortho_views
            INNER JOIN codes_dicom ON codes_dicom.id = ortho_views.patient_orientation
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as patient_orientation
WHERE id = 'patient_orientation';
-- Laterality
UPDATE _temp
SET code_value = laterality.code,
    meaning = laterality.meaning
FROM (
        SELECT codes_dicom.code,
            codes_dicom.meaning
        FROM ortho_views
            INNER JOIN codes_dicom ON codes_dicom.id = ortho_views.laterality
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as laterality
WHERE id = 'laterality';
-- Anatomic Region Sequence
UPDATE _temp
SET code_value = 'SCT-' || anatomic_region_sequence.code,
    meaning = anatomic_region_sequence.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.anatomic_region_sequence
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as anatomic_region_sequence
WHERE id = 'anatomic_region_sequence';
-- Anatomic Region Modifier Sequence
UPDATE _temp
SET code_value = 'SCT-' || anatomic_region_modifier_sequnce.code,
    meaning = anatomic_region_modifier_sequnce.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.anatomic_region_modifier_sequnce
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as anatomic_region_modifier_sequnce
WHERE id = 'anatomic_region_modifier_sequnce';
'''
    output_file = os.path.join(PATH_TABLES_GENERATED,view_type + '.csv')
    cur.executescript(query_view)
    cur.execute('''SELECT
        attribute_name AS "Attribute Name",
        tag AS 'Tag',
        code_value AS 'Value',
        meaning AS 'Meaning'
    FROM _temp;
    ''')
    with open(output_file,'w') as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        # write header
        csv_out.writerow([d[0] for d in cur.description])
        # write data
        for result in cur:
            csv_out.writerow(result)

def main(args):
    print("Main")
    cur = con.cursor()
    initdb(cur)
    load_views(cur)
    create_view(cur, 'IV-03')

    close_connection()

if __name__ == "__main__":
    main(sys.argv[1:])