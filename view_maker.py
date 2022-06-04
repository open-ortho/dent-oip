#!/usr/bin/env python3

import os
import sys
import sqlite3
import csv

# Prefixes
PREFIX_SNOMED = "SCT "
PREFIX_DICOM = "DCM "

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
    return f"""
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
    return f"""UPDATE _temp
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
--
INSERT INTO _temp (id, attribute_name, tag)
SELECT id,
    attribute_name,
    tag
FROM tags_dicom;
"""
    try:
        os.makedirs(PATH_TABLES_GENERATED)
    except FileExistsError:
        pass
    output_file = os.path.join(PATH_TABLES_GENERATED, view_type + ".csv")
    try:
        # Create the single tables for each view.
        cur.executescript(query_view)
        # TODO: Here i need to split the ^-separated items in the sequences, to
        # add more rows for the sequences, like in DICOM documentation.
        cur.executescript(query_add_attribute(C_POR,view_type))
        cur.executescript(query_add_attribute(C_LAT,view_type))
        cur.executescript(query_add_snomed_code(C_ARS,view_type))
        cur.executescript(query_add_snomed_code(C_ARM,view_type))
        cur.executescript(query_add_snomed_code(C_PAM,view_type))
        cur.executescript(query_add_snomed_code(C_DEV,view_type))
        cur.executescript(query_add_snomed_code(C_AQV,view_type))
        cur.executescript(query_add_snomed_code(C_IMV,view_type))
        cur.executescript(query_add_snomed_code(C_FCA,view_type))
        cur.executescript(query_add_snomed_code(C_OCR,view_type))

    except sqlite3.OperationalError as e:
        print("An error occured: ", e)
        print(query_view)
        exit(1)

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
