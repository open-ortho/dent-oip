#!/usr/bin/env python

import os
import sys
import sqlite3
import csv

# Prefixes
PREFIX_SNOMED='SCT '
PREFIX_DICOM='DCM '

# Files and paths
PATH_TABLES = os.path.join('.','source','tables')
PATH_TABLES_GENERATED = os.path.join(PATH_TABLES, 'generated')
CSV_SNOMED = os.path.join(PATH_TABLES,'codes_snomed.csv')
CSV_DICOM = os.path.join(PATH_TABLES,'codes_dicom.csv')
CSV_DICOM_TAGS = os.path.join(PATH_TABLES,'tags_dicom.csv')
CSV_VIEWS = os.path.join(PATH_TABLES,'views.csv')
DBFILE='views.db'

# Database Tables
T_VIEWS='ortho_views'
T_SNOMED='codes_snomed'
T_DICOM='codes_dicom'
T_DICOM_TAGS='tags_dicom'

# Database Columns
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
CREATE TEMP TABLE IF NOT EXISTS _temp (
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
SET code_value = {C_POR}.code,
    meaning = {C_POR}.meaning
FROM (
        SELECT codes_dicom.code,
            codes_dicom.meaning
        FROM ortho_views
            INNER JOIN codes_dicom ON codes_dicom.id = ortho_views.{C_POR}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_POR}
WHERE id = '{C_POR}';
-- Laterality
UPDATE _temp
SET code_value = {C_LAT}.code,
    meaning = {C_LAT}.meaning
FROM (
        SELECT codes_dicom.code,
            codes_dicom.meaning
        FROM ortho_views
            INNER JOIN codes_dicom ON codes_dicom.id = ortho_views.{C_LAT}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_LAT}
WHERE id = '{C_LAT}';
-- Anatomic Region Sequence
UPDATE _temp
SET code_value = '{PREFIX_SNOMED}' || {C_ARS}.code,
    meaning = {C_ARS}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{C_ARS}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_ARS}
WHERE id = '{C_ARS}';
-- Anatomic Region Modifier Sequence
UPDATE _temp
SET code_value = '{PREFIX_SNOMED}' || {C_ARM}.code,
    meaning = {C_ARM}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{C_ARM}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_ARM}
WHERE id = '{C_ARM}';
-- Primary Anatomic Structure Sequence
UPDATE _temp
SET code_value = '{PREFIX_SNOMED}' || {C_PAM}.code,
    meaning = {C_PAM}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{C_PAM}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_PAM}
WHERE id = '{C_PAM}';
-- Device Sequence
UPDATE _temp
SET code_value = '{PREFIX_SNOMED}' || {C_DEV}.code,
    meaning = {C_DEV}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{C_DEV}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_DEV}
WHERE id = '{C_DEV}';
-- Acquisition View
UPDATE _temp
SET code_value = '{PREFIX_SNOMED}' || {C_AQV}.code,
    meaning = {C_AQV}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{C_AQV}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_AQV}
WHERE id = '{C_AQV}';
-- Image View
UPDATE _temp
SET code_value = '{PREFIX_SNOMED}' || {C_IMV}.code,
    meaning = {C_IMV}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{C_IMV}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_IMV}
WHERE id = '{C_IMV}';
-- Functional Condition Present During Acquisition
UPDATE _temp
SET code_value = '{PREFIX_SNOMED}' || {C_FCA}.code,
    meaning = {C_FCA}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{C_FCA}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_FCA}
WHERE id = '{C_FCA}';
-- Occlusal Relationship
UPDATE _temp
SET code_value = '{PREFIX_SNOMED}' || {C_OCR}.code,
    meaning = {C_OCR}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{C_OCR}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {C_OCR}
WHERE id = '{C_OCR}';
'''
    output_file = os.path.join(PATH_TABLES_GENERATED,view_type + '.csv')
    try:
        cur.executescript(query_view)
    except sqlite3.OperationalError as e:
        print("An error occured: ", e)
        print(query_view)
        exit(1)

    cur.execute('''SELECT
        attribute_name AS "Attribute Name",
        tag AS 'Tag',
        code_value AS 'Value',
        meaning AS 'Meaning'
    FROM _temp;
    ''')
    with open(output_file,'w') as out_csv_file:
        print(f"Writing to file {output_file}")
        csv_out = csv.writer(out_csv_file)
        # write header
        csv_out.writerow([d[0] for d in cur.description])
        # write data
        for result in cur:
            csv_out.writerow(result)
    cur.execute("DELETE FROM _temp")

def main(args):
    print("Main")
    cur = con.cursor()
    initdb(cur)
    load_views(cur)

    cur2 = con.cursor()
    for view in cur2.execute(f"SELECT view_name FROM {T_VIEWS}"):
        create_view(cur, view[0])

    close_connection()

if __name__ == "__main__":
    main(sys.argv[1:])