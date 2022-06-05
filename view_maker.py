#!/usr/bin/env python3

import os
import sys
import sqlite3
import csv

# Prefixes
PREFIX_SNOMED = "SCT "
PREFIX_DICOM = "DCM "

# Snomed name, version and number to appear in the code sequences.
SNOMED_NAME = "SNOMED CT"
SNOMED_VERSION = "3.25"
SNOMED_YEAR = "2022"

# Files and paths
PATH_TABLES = os.path.join(".", "source", "tables")
PATH_APPENDIX = os.path.join(".", "source", "Appendix")
PATH_TABLES_GENERATED = os.path.join(PATH_TABLES, "generated")
RST_INTRAORAL_VIEWS = os.path.join(PATH_APPENDIX, "intraoral_views.rst")
RST_EXTRAORAL_VIEWS = os.path.join(PATH_APPENDIX, "extraoral_views_gen.rst")
CSV_SNOMED = os.path.join(PATH_TABLES, "codes_snomed.csv")
CSV_DICOM = os.path.join(PATH_TABLES, "codes_dicom.csv")
CSV_DICOM_TAGS = os.path.join(PATH_TABLES, "tags_dicom.csv")
CSV_VIEWS = os.path.join(PATH_TABLES, "views.csv")
DBFILE = "views.db"

# Database Tables
T_VIEWS = "ortho_views"
T_SNOMED = "codes_snomed"
T_DICOM = "codes_dicom"
T_DICOM_TAGS = "tags_dicom"

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
C_FUL = "view_full_name"
C_THE = "teeth_example"

con = sqlite3.connect(DBFILE)
cur = None


def ev_write_rst(title, filename, number, example):
    """ Write Extraoral Views to RestructuredText file.
    
    This function is very similar to iv_write_rst and has been kept separate on
    purpose, to allow for customization.
    """
    if example != "":
        example = format_example(example)

    ev_rst = f"""
{h1(title)}
    
.. image:: {filename}
    :class: with-border
    :align: center
    :alt: Line drawing of {title}
    
    
.. csv-table:: {number}
   :file: ../tables/generated/{number}.csv
   :widths: 40, 10, 10, 40
   :header-rows: 1
    
    
Primary Anatomic Structure Sequence
:::::::::::::::::::::::::::::::::::
    
See section :ref:`primary anatomic structure sequence`
    
{example}
"""
    with open(RST_EXTRAORAL_VIEWS, "a") as rst_out:
        rst_out.write(ev_rst)

def iv_write_rst(title, filename, number, example):
    """ Write Intraoral Views to RestructuredText file.

    This function is very similar to ev_write_rst and has been kept separate on
    purpose, to allow for customization.
    """
    if example != "":
        example = format_example(example)

    iv_rst = f"""
{h1(title)}
    
.. image:: {filename}
    :class: with-border
    :align: center
    :alt: Line drawing of {title}
    
    
.. csv-table:: {number}
   :file: ../tables/generated/{number}.csv
   :widths: 40, 10, 10, 40
   :header-rows: 1
    
    
Primary Anatomic Structure Sequence
:::::::::::::::::::::::::::::::::::
    
See section :ref:`primary anatomic structure sequence`
    
{example}
"""
    with open(RST_INTRAORAL_VIEWS, "a") as rst_out:
        rst_out.write(iv_rst)

def format_example(example):
    """ Converts a string of ISO numbered teeth into an RST formatted example text.
    """

    rs = """Example:

Patient may show the following teeth in this view:

"""
    for tooth in example.split("^"):
        cur.execute(f"SELECT code,meaning from {T_SNOMED} WHERE id = {tooth};")
        code,code_meaning = cur.fetchall()[0]
        rs += f"* {tooth} SCT: {code}\n"
    
    return rs

def initdb(cur):
    cur.execute(
        f"""
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
        {C_OCR} text,
        {C_FUL} text,
        {C_THE} text)
        """
    )

    cur.execute(
        f"""
    CREATE TABLE {T_SNOMED}(
        id text,
        code int,
        meaning text)
        """
    )
    load_snomed_codes(cur)

    cur.execute(
        f"""
    CREATE TABLE {T_DICOM}(
        id text,
        code int,
        meaning text)
        """
    )
    load_dicom_codes(cur)

    cur.execute(
        f"""
    CREATE TABLE {T_DICOM_TAGS}(
        id text,
        attribute_name text,
        tag text)
        """
    )
    load_dicom_tags(cur)


def load_snomed_codes(cur):
    with open(CSV_SNOMED, "r") as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i["id"], i["code"], i["meaning"]) for i in dr]
    cur.executemany(
        f"INSERT INTO {T_SNOMED} (id, code, meaning) VALUES (?, ?, ?);", to_db
    )


def load_dicom_codes(cur):
    with open(CSV_DICOM, "r") as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i["id"], i["code"], i["meaning"]) for i in dr]
    cur.executemany(
        f"INSERT INTO {T_DICOM} (id, code, meaning) VALUES (?, ?, ?);", to_db
    )


def load_dicom_tags(cur):
    with open(CSV_DICOM_TAGS, "r") as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i["id"], i["attribute_name"], i["tag"]) for i in dr]
    cur.executemany(
        f"INSERT INTO {T_DICOM_TAGS} (id, attribute_name, tag) VALUES (?, ?, ?);", to_db
    )


def load_views(cur):
    with open(CSV_VIEWS, "r") as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [
            (
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
                i[C_OCR],
                i[C_FUL],
                i[C_THE],
            )
            for i in dr
        ]
    cur.executemany(
        f"""
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
        {C_OCR},
        {C_FUL},
        {C_THE})
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);""",
        to_db,
    )


def close_connection():
    con.commit()
    con.close()

def query_add_attribute(column,view_type):
    """ Returns an SQL string to insert new tag which is based on a DICOM code.
    """
    return f"""
INSERT INTO _temp (id, attribute_name, tag)
SELECT id,
    attribute_name,
    tag
FROM tags_dicom
WHERE
    id = '{column}';

UPDATE _temp
SET code_value = {column}.code,
    meaning = {column}.meaning
FROM (
        SELECT codes_dicom.code,
            codes_dicom.meaning
        FROM ortho_views
            INNER JOIN codes_dicom ON codes_dicom.id = ortho_views.{column}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {column}
WHERE id = '{column}';
    """

def query_add_snomed_code(column,view_type):
    """ Returns an SQL string to insert a new SNOMED CT based attribute, which
    is not a sequence.
    """
    return f"""
INSERT INTO _temp (id, attribute_name, tag)
SELECT id,
    attribute_name,
    tag
FROM tags_dicom
WHERE
    id = '{column}';

UPDATE _temp
SET code_value = {column}.code,
    meaning = {column}.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.{column}
        WHERE ortho_views.view_name LIKE '{view_type}'
    ) as {column}
WHERE id = '{column}';
"""

def query_insert_sequence(column,code_id):
    """ Return an SQL query string to add entire code sequence.
    """
    # IDs to use for each new row in the temp table
    cv_id  = f"{column}_code_value_{code_id}"
    csd_id = f"{column}_coding_scheme_designator_{code_id}"
    csv_id = f"{column}_coding_scheme_version_{code_id}"
    qs = f"""
-- Insert the Sequence Name
INSERT INTO _temp (id, attribute_name, tag)
SELECT id,
    attribute_name,
    tag
FROM tags_dicom
WHERE
    id = '{column}';
    
-- Insert the sequence code value
INSERT INTO _temp (id)
VALUES ('{cv_id}');

-- Add the Code Value tag name and attribute
UPDATE  _temp
SET attribute_name = tags_dicom.attribute_name,
    tag = tags_dicom.tag
FROM (
        SELECT attribute_name, tag
        FROM tags_dicom
        WHERE tags_dicom.id LIKE 'code_value'
    ) AS tags_dicom
WHERE id = '{cv_id}';

-- Add the Code Value value and meaning
UPDATE  _temp
SET code_value = codes_snomed.code,
    meaning = codes_snomed.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM codes_snomed
        WHERE codes_snomed.id LIKE '{code_id}'
    ) as codes_snomed
WHERE id = '{cv_id}';

-- Insert the sequence coding scheme designator
INSERT INTO _temp (id)
VALUES ('{csd_id}');

-- Add the Coding Scheme Designator Name Tag, Value and Meaning
UPDATE  _temp
SET attribute_name = tags_dicom.attribute_name,
    tag = tags_dicom.tag,
    code_value = '{PREFIX_SNOMED.rstrip()}',
    meaning = '{SNOMED_NAME}'
FROM (
        SELECT attribute_name, tag
        FROM tags_dicom
        WHERE tags_dicom.id LIKE 'coding_scheme_designator'
    ) AS tags_dicom
WHERE id = '{csd_id}';

-- Insert the sequence coding scheme Version
INSERT INTO _temp (id)
VALUES ('{csv_id}');

-- Add the Coding Scheme Designator Name Tag, Value and Meaning
UPDATE  _temp
SET attribute_name = tags_dicom.attribute_name,
    tag = tags_dicom.tag,
    code_value = '{SNOMED_VERSION}',
    meaning = '{SNOMED_YEAR}'
FROM (
        SELECT attribute_name, tag
        FROM tags_dicom
        WHERE tags_dicom.id LIKE 'coding_scheme_version'
    ) AS tags_dicom
WHERE id = '{csv_id}';
"""
    return qs

def create_view(cur, view_type):
    """ Creates the CSV file with attributes and tags for a single view.

    This function will generate the CSV file for the current view_type, which
    Sphynx will then render into html. Not all columns from the source views.csv
    file will be imported here. For example, the Full Name or Teeth Example
    column do not need to be in these tables.
    """

    query_view = f"""
-- SQLite
CREATE TEMP TABLE IF NOT EXISTS _temp (
    id text,
    attribute_name text,
    tag text,
    code_value text,
    meaning text
);
"""
    try:
        os.makedirs(PATH_TABLES_GENERATED)
    except FileExistsError:
        pass
    output_file = os.path.join(PATH_TABLES_GENERATED, view_type + ".csv")
    cur.executescript(query_view)
    cur2 = con.cursor()
    cur.executescript(query_add_attribute(C_POR,view_type))
    cur.executescript(query_add_attribute(C_LAT,view_type))
    for ars in cur2.execute(f"SELECT {C_ARS} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(ars) > 0 and ars != "na": cur.executescript(query_insert_sequence(column=C_ARS,code_id=ars))
    r = cur2.execute(f"SELECT {C_ARM} FROM ortho_views WHERE view_name = '{view_type}';") 
    for arm in cur2.execute(f"SELECT {C_ARM} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(arm) > 0 and arm != "na": cur.executescript(query_insert_sequence(column=C_ARM,code_id=arm))
    for pam in cur2.execute(f"SELECT {C_PAM} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(pam) > 0 and pam != "na": cur.executescript(query_insert_sequence(column=C_PAM,code_id=pam))
    for dev in cur2.execute(f"SELECT {C_DEV} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(dev) > 0 and dev != "na": cur.executescript(query_insert_sequence(column=C_DEV,code_id=dev))
    cur.executescript(query_add_snomed_code(C_AQV,view_type))
    cur.executescript(query_add_snomed_code(C_IMV,view_type))
    for fca in cur2.execute(f"SELECT {C_FCA} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(fca) > 0 and fca != "na": cur.executescript(query_insert_sequence(column=C_FCA,code_id=fca))
    cur.executescript(query_add_snomed_code(C_OCR,view_type))
    # except sqlite3.OperationalError as e:
    #     print("An error occured: ", e)
    #     print(query_view)
    #     exit(1)

    cur.execute(
        """SELECT
        attribute_name AS "Attribute Name",
        tag AS 'Tag',
        code_value AS 'Value',
        meaning AS 'Meaning'
    FROM _temp;
    """
    )
    with open(output_file, "w") as out_csv_file:
        print(f"Writing to file {output_file}")
        csv_out = csv.writer(out_csv_file)
        # write header
        csv_out.writerow([d[0] for d in cur.description])
        # write data
        for result in cur:
            csv_out.writerow(result)
    cur.execute("DELETE FROM _temp")


def h1(h_text):
    return h_text + f"\n{'-' * len(h_text)}"


def main(args):
    print("Main")
    global cur
    cur = con.cursor()
    initdb(cur)
    load_views(cur)

    cur2 = con.cursor()
    # This will overwrite the current rst file with header.
    with open(RST_INTRAORAL_VIEWS, "w") as rst_iv:
        rst_iv_head = """.. _intraoral views:

Intraoral Views
===============
"""
        rst_iv.write(rst_iv_head)

    with open(RST_EXTRAORAL_VIEWS, "w") as rst_ev:
        rst_ev_head = """.. _extraoral views:

Extraoral Views
===============
"""
        rst_ev.write(rst_ev_head)

    for view in cur2.execute(f"SELECT {C_VIE},{C_FUL},{C_THE} FROM {T_VIEWS}"):
        create_view(cur, view[0])
        if view[0].startswith('IV'):
            iv_write_rst(title=view[1], filename=f"../images/{view[0]}.png", number=view[0], example=view[2])
        if view[0].startswith('EV'):
            ev_write_rst(title=view[1], filename=f"../images/{view[0]}.png", number=view[0], example=view[2])

    close_connection()


if __name__ == "__main__":
    main(sys.argv[1:])
