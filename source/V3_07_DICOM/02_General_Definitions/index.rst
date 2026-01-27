.. _general_definitions:

.. _dicom_coded_values:

7.2  DICOM Coded Values
-----------------------
*Note: Codes are added here for now; they may find a new home*

.. _cid_4028:

7.2.1 Table CID 4028 - Craniofacial Anatomic Region
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These values are used in the Anatomic Region Sequence (0008,2218) and are a subset of DICOM CID 4028.  

When applied to orthodontic photographs, the anatomic region is *Mouth* for intraoral views, and *Head/Neck* for extraoral views.

.. _cid-4028a:
.. list-table:: **Table CID 4028. Craniofacial Anatomic Region**
    :header-rows: 1

    * - Code Scheme Designator
      - Code Value
      - Code Meaning
      - Notes
    * - SCT
      - 123851003
      - Mouth region structure (body structure)
      - Used for IV-* intraoral views. 
    * - SCT
      - 774007
      - Structure of head and/or neck (body structure)
      - Used for EV-* extraoral views. This code was selected, because it is the most detailed code that includes the ear as well since the ear is present in both frontal and lateral extra oral views.

.. _cid_247:

7.2.2 Table CID 247 - Laterality Left-Right Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: **Table CID 247. Laterality Left-Right Only**
    :header-rows: 1

    * - Code Scheme Designator
      - Code Value
      - Code Meaning
      - Notes
    * - SCT
      - 24028007
      - Right 
      - 
    * - SCT
      - 7771000
      - Left 
      - 

.. _cid_244:

7.2.3 Table CID 244 - Laterality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In DICOM, *laterality* is used to define body parts which come in pairs, for
example knees, ears, eyes, etc. It is not used to describe the side of the body
being imaged. For example, an image of the left side of the right eye would have
laterality right, even though the image is portraying the left side of the eye. In other words, this is the laterality of (possibly paired) body part examined (as
described in Anatomic Region Sequence (0008,2218)).

The values in CID 244 are used in Image Laterality (0020,0062).

Note:  The attribute Patient Orientation (0020,0020) should be enough to define the side of the anatomy being viewed.  See Section 7.2.5.

.. list-table:: **Table CID 244. Laterality**
    :header-rows: 1

    * - DICOM Enumerated Value
      - SNOMED CODE
    * - L
      - (77771000,SCT,"Left")
    * - R
      - (66459002,SCT,"Right")
    * - U
      - (24028007,SCT,"Unilateral")
    * - B
      - (51440002,SCT,"Bilateral")

Note:  When creating the DICOM object, DICOM requires an enumerated value (aka string) for this tag. You should therefore always use the string in the DICOM Enumerated Value column of the table above.

7.2.3.1 Choosing the Correct Laterality
+++++++++++++++++++++++++++++++++++++++
Consider the following logic when choosing laterality.

+-----+----------+-----------------------------------------------------+
| U   | Unpaired | Used for most orthodontic images.                   |
+-----+----------+-----------------------------------------------------+
| L   | Left     | Only use if this Series is of Mastoid bone, Maxilla |
|     |          | or Temporomandibular joint. For all other anatomic  |
|     |          | regions containing one or both sides, set to 'U'.   |
+-----+----------+-----------------------------------------------------+
| R   | Right    | Only use if this Series is of Mastoid bone, Maxilla |
|     |          | or Temporomandibular joint. For all other anatomic  |
|     |          | regions containing one or both sides, set to 'U'.   |
+-----+----------+-----------------------------------------------------+
| B   | Both     | Only use if this Series is of Mastoid bone, Maxilla |
|     |          | or Temporomandibular joint. For all other anatomic  |
|     |          | regions containing one or both sides, set to 'U'.   |
|     |          | This is almost never used.                          |
|     |          |                                                     |
|     |          | For example, a frontal face smiling photograph,     |
|     |          | would have Image Laterality of 'U'. However, an     |
|     |          | image which would contain both the left Maxilla and |
|     |          | the right Maxilla in the same frame (image) (for    |
|     |          | example making use of mirrors or by merging two     |
|     |          | images into one) would have an Image Laterality of  |
|     |          | 'B'.                                                |
+-----+----------+-----------------------------------------------------+

The above table was compiled using the following considerations:

1. Image Laterality (0020,0062) Shall be consistent with any laterality
   information contained in Primary Anatomic Structure Modifier Sequence
   (0008,2230). `DICOM PS3.3: Section 10.5 General Anatomy Macros
   <http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_10.5.html>`__
   discusses the relationship between Image Laterality (0020,0062) and Primary
   Anatomic Structure Modifier Sequence (0008,2230):

   1. *"Laterality is often encoded in a separate Attribute, Image
      Laterality (0020,0062) or Frame Laterality (0020,9072), rather
      than in Anatomic Region Modifier Sequence (0008,2220) or Primary
      Anatomic Structure Modifier Sequence (0008,2230)." This means that
      even thought the Laterality should be encoded in the Anatomic
      Region Modifier Sequence, it is often encoded in Image Laterality.
      Since these two shall be consistent, DICOM provides a mapping
      between the two (see below, one is an enumerated value as CS the
      other a code sequence).*

   2. The section references `Part 16 Table L-5 <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html#table_L-5>`__,
      a table which defines whether a specific anatomic region is to be
      considered a paired structure or not. Below, we report a table of those
      body parts relevant to orthodontic visible light images.

2. Laterality (0020,0060) (a Series level Attribute) must be absent,
   because

   1. this series could contain images of different Laterality and

   2. because Laterality (0020,0060) only allows 'L' and 'R' enumerated
      values, which are not sufficient to describe these images.

(excerpt from DICOM `PS3.16: Table L-5 <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html#table_L-5>`__ with
orthodontic domain relevant regions)

+---------------------------+-----------------------+------------------+
|     SNOMED Code Value     |     Code Meaning      | Paired Structure |
+===========================+=======================+==================+
|                           | Buccal region of face | N                |
| `60819002 <http://snome   |                       |                  |
| d.info/id/60819002>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Face                  | N                |
| `89545001 <http://snome   |                       |                  |
| d.info/id/89545001>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Head                  | N                |
| `69536005 <http://snome   |                       |                  |
| d.info/id/69536005>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
| `774007 <http://sno       | Head and Neck         | N                |
| med.info/id/774007>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
| `661005 <http://sno       | Jaw region            | N                |
| med.info/id/661005>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Mandible              | N                |
| `91609006 <http://snome   |                       |                  |
| d.info/id/91609006>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Mastoid bone          | Y                |
| `59066005 <http://snome   |                       |                  |
| d.info/id/59066005>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Maxilla               | Y                |
| `70925003 <http://snome   |                       |                  |
| d.info/id/70925003>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Mouth                 | N                |
| `123851003 <http://snomed |                       |                  |
| .info/id/123851003>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Skull                 | N                |
| `89546000 <http://snome   |                       |                  |
| d.info/id/89546000>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Sella turcica         | N                |
| `42575006 <http://snome   |                       |                  |
| d.info/id/42575006>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Submental             | N                |
| `170887008 <http://snomed |                       |                  |
| .info/id/170887008>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Temporomandibular     | Y                |
| `53620006 <http://snome   | joint                 |                  |
| d.info/id/53620006>`__    |                       |                  |
+---------------------------+-----------------------+------------------+
|                           | Tongue                | N                |
| `21974007 <http://snome   |                       |                  |
| d.info/id/21974007>`__    |                       |                  |
+---------------------------+-----------------------+------------------+

.. _cid_4061:

7.2.4 Table CID 4061 - Head and/or Neck Primary Anatomic Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These values are used in the Primary Anatomic Structure Sequence (0008,2228) and are a subset of DICOM CID 4061.

.. list-table:: **Table CID 4061. Head and/or Neck Primary Anatomic Structure**
    :header-rows: 1

    * - Code Scheme Designator
      - Code Value
      - Code Meaning
      - Notes
    * - SCT
      - 89545001
      - Face 
      - Used for EV-* extraoral views.
    * - SCT
      - 74262004
      - oral cavity 
      - Used for IV-* intraoral views.
    * - SCT
      - 88176008
      - Mandibular dental arch
      - Used for IV-* intraoral views.
    * - SCT
      - 39481002
      - Maxillary dental arch
      - Used for IV-* intraoral views.
    * - SCT
      - 261063000
      - Structure of buccal space 
      - Used for IV-* intraoral views.
    * - SCT
      - 7652006
      - Structure of frenulum labii 
      - Used for IV-* intraoral views.

.. _patient_orientation:

7.2.5 Patient Orientation
~~~~~~~~~~~~~~~~~~~~~~~~~
These values are used in Patient Orientation (0020,0020).

.. list-table::
   :header-rows: 1

   * - Meaning
     - DICOM Enumerated Value
     - SNOMED Code
   * - Anterior
     - A
     - `(255549009, SCT, "Anterior") <http://snomed.info/id/255549009>`__
   * - Posterior
     - P
     - `(255551008, SCT, "Posterior") <http://snomed.info/id/255551008>`__
   * - Left
     - L
     - `(7771000, SCT, "Left") <http://snomed.info/id/7771000>`__
   * - Right
     - R
     - `(24028007, SCT, "Right") <http://snomed.info/id/24028007>`__
.. See TROSD-65
   * - Top (towards the head)
     - H
     - `(421812003, SCT, "Top") <http://snomed.info/id/421812003>`__
.. See TROSD-65
   * - Bottom (towards the lower limbs)
     - F
     - `(421610009, SCT, "Bottom") <http://snomed.info/id/421610009>`__

7.2.5.1 Specifying the Correct Patient Orientation
++++++++++++++++++++++++++++++++++++++++++++++++++
The following requirements come from `DICOM PS3.3: Section C.7.6.1.1.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.1.1.1>`_:

Patient Orientation (0020,0020) relative to the image plane shall be 
specified by two values that designate the anatomical direction of the
positive row axis (left to right) and the positive column axis (top to
bottom).

-  The first entry is the direction of the rows, given by the direction
   of the last pixel in the first row from the first pixel in that row.

-  The second entry is the direction of the columns, given by the
   direction of the last pixel in the first column from the first pixel
   in that column.

**For example:** a Right Profile photograph of the face, would have Patient
Orientation set to ['A','F']

.. _cid-4066:

7.2.6 Orthognathic Functional Conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: CID 4066. Orthognathic Functional Conditions
    :header-rows: 1

    * - SNOMED Code
      - Meaning
      - Notes
    * - `SCT 1336028006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1336028006&edition=MAIN&release=&languages=en>`__
      - Upper and lower lips in relaxed position
      - 
    * - `SCT 1336029003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1336029003&edition=MAIN&release=&languages=en>`__
      - Upper and lower lips in closed position
      - 
    * - `SCT 1332210001 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1332210001&edition=MAIN&release=&languages=en>`__
      - Mouth in partially open position
      - 
    * - `SCT 262016004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=262016004&edition=MAIN&release=&languages=en>`__
      - Open Mouth (finding)
      - 
    * - `SCT 1336026005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1336026005&edition=MAIN&release=&languages=en>`__
      - Mandible postured forward
      - 
    * - `SCT 225583004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=225583004&edition=MAIN&release=&languages=en>`__
      - Smiles (finding)
      - 
