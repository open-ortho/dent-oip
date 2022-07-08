#!/usr/bin/env python3
"""Generate the Intraoral and Extraoral view pages found in the Appendix.

The scripts loads data from CSV files into a temporary SQLite DB, which is used to format the data in the proper format for the Appendix. 

Overview
--------

Initially, we had all the views in a single table, which grew very large. It was hard to read, but easy to maintain. Having many tables, one for each view, would have made the information a lot easier to understand, but it would have been a nightmare to maintain: every single change would have required search and replace operations, and the possibility of generating inconsistent pages and introducing errors would have been really high.

The appendix tables needed to be generated programmatically. By using this script, we can keep and maintain the views from a single CSV file, and programmatically generating the readable appendix tables.

Procedure
---------

Data is maintained ``source/tables`` folder. The ``views.csv`` contains all the orthodontic views. See :ref:`Tables` below. When running this script, this is what it will do:

1. Create empty tables in an SQLite DB. This is done with the ``initdb()``.
2. Load data from CSV files into the DB tables. This is done with the ``load_*()`` functions.
3. Iterate through all views, and for each view:
4. Populate an "output" table (called ``_temp``, because it gets overwritten for each view iteration), one view at a time, using the ``query_*()`` functions.
5. During population, tooth examples are converted to proper SNOMED codes with meanings with the ``format_example()`` function.
6. 

Tables
------

``views.csv``
^^^^^^^^^^^^^
The full list of all orthodontic views. Edit this to make any changes. However, this file makes use of codes and abbreviations for many things. For example, the values in ``patient_orientation`` are taken from ``codes_dicom.csv`` by using the ``id``column.

There is a teeth_example column used to add teeth to use as examples. The format for this column is ``AA^BB^CC...`` where ``AA``, ``BB`` and ``CC`` are tooth numbers. For example: ``54^55^84^85``.

``codes_dicom.csv``
^^^^^^^^^^^^^^^^^^^^
List of DICOM codes, which aren't actually codes, but more like enumerated values, or whatever they are called in DICOM. Things like ``L`` for Left and ``P`` for Posterior. The ``id`` column is used to refer to these codes in ``views.csv``.

``codes_snomed.csv``
^^^^^^^^^^^^^^^^^^^^^
Full list of all SNOMED codes used. The ``id`` column is the one that you will see in ``views.csv``.

``tags_dicom.csv``
^^^^^^^^^^^^^^^^^^^
A list of DICOM tag names with their tag ID. We use this in the views, because we want to make our tables in the Appendix look as similar to DICOM tables as possible.

Like in DICOM, sequences here should start with a ``>``.

``CID-4018.csv`` and ``CID-4019.csv``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The DICOM tables containing the codes used for tooth numbering. These are copied and pasted directly from DICOM standard.


``

"""

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
RST_EXTRAORAL_VIEWS = os.path.join(PATH_APPENDIX, "extraoral_views.rst")
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
    
    :param example: A string containing a sequence of teeth numbers, separated by the caret ``^`` character.
    :type example: str

    :return: A string containing the teeth from ``example`` expressed as SNOMED codes and formatted in RestructuredText.
    """

    rs = """Example:

Patient may show the following teeth in this view:

"""
    for tooth in example.split("^"):
        cur.execute(f"SELECT code,meaning from {T_SNOMED} WHERE id = {tooth};")
        code,code_meaning = cur.fetchall()[0]
        rs += f"* {tooth} SCT: {code} ({code_meaning})\n"
    
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
    """Returns an SQL string to insert new DICOM tag into _temp table.
    
    This assumes that the DICOM codes have been imported into a table called "tags_dicom". The function ``load_dicom_tags()``

    Parameters
    ----------
    :param column: The name of the column in the _temp table containing all views. You would use the ``C_*``variables here, like ``C_AQV`` or ``C_IMV``.
    :type column: str
    
    :param view_type: The name of the view, like IV-01.
    :type view_type: str

    :return: An SQL string to insert new DICOM tag into _temp table.
    :rtype: str
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

    This would typically be used to read the SNOMED code value and meaning from the CSV file, and store it into a _temp table, used only for the purpose of generating RST files.
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
    Sphinx will then render into html. Not all columns from the source ``views.csv``
    file will be imported here. For example, the Full Name or Teeth Example
    column do not need to be in these tables.
    
    Parameters
    ----------
    :param cur: The database cursor
    :type cur: cursor

    :param view_type: The name of the view, like IV-01. It is used to name the output files.
    :type view_type: str
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
    cur.executescript(query_add_attribute(C_POR,view_type))
    cur.executescript(query_add_attribute(C_LAT,view_type))
    for ars in cur.execute(f"SELECT {C_ARS} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(ars) > 0 and ars != "na": cur.executescript(query_insert_sequence(column=C_ARS,code_id=ars))
    for arm in cur.execute(f"SELECT {C_ARM} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(arm) > 0 and arm != "na": cur.executescript(query_insert_sequence(column=C_ARM,code_id=arm))
    for pam in cur.execute(f"SELECT {C_PAM} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(pam) > 0 and pam != "na": cur.executescript(query_insert_sequence(column=C_PAM,code_id=pam))
    for dev in cur.execute(f"SELECT {C_DEV} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(dev) > 0 and dev != "na": cur.executescript(query_insert_sequence(column=C_DEV,code_id=dev))
    cur.executescript(query_add_snomed_code(C_AQV,view_type))
    cur.executescript(query_add_snomed_code(C_IMV,view_type))
    for fca in cur.execute(f"SELECT {C_FCA} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(fca) > 0 and fca != "na": cur.executescript(query_insert_sequence(column=C_FCA,code_id=fca))
    for ocr in cur.execute(f"SELECT {C_OCR} FROM ortho_views WHERE view_name = '{view_type}';").fetchone()[0].split("^"):
        if len(ocr) > 0 and ocr != "na": cur.executescript(query_insert_sequence(column=C_OCR,code_id=ocr))
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
