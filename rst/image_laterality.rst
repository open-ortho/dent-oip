.. _scroll-bookmark-6:

Image Laterality (0020,0062)
============================

Laterality of (possibly paired) body part (as described in Anatomic
Region Sequence (0008,2218)) examined.

1. Shall be consistent with any laterality information contained in
   Primary Anatomic Structure Modifier Sequence (0008,2230). `DICOM PS
   3.3 Section 10.5 General Anatomy
   Macros <http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_10.5.html>`__
   discusses the relationship between Image Laterality (0020,0062) and
   Primary Anatomic Structure Modifier Sequence (0008,2230):

   1. *"Laterality is often encoded in a separate Attribute, Image
      Laterality (0020,0062) or Frame Laterality (0020,9072), rather
      than in Anatomic Region Modifier Sequence (0008,2220) or Primary
      Anatomic Structure Modifier Sequence (0008,2230)." This means that
      even thought the Laterality should be encoded in the Anatomic
      Region Modifier Sequence, it is often encoded in Image Laterality.
      Since these two shall be consistent, DICOM provides a mapping
      between the two (see below, one is an enumerated value as CS the
      other a code sequence).*

   2. *The section references*\ `Part 16 Table
      L-5 <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html#table_L-5>`__\ *,
      a table which relates a specific anatomic region is to be
      considered a paired structure or not. Below, we report a table of
      those body parts relevant to orthodontic visible light images*

2. Laterality (0020,0060) (a Series level Attribute) must be absent,
   because

   1. this series could contain images of different Laterality and

   2. because Laterality (0020,0060) only allows 'L' and 'R' enumerated
      values, which are not sufficient to describe these images.

(excerpt from DICOM `Part 16 Table
L-5 <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html#table_L-5>`__\ with
orthodontic domain relevant regions)

+------------------------+------------------------+------------------+
| SNOMED Code Value      | Code Meaning           | Paired Structure |
+========================+========================+==================+
| `                      | Buccal region of face  | N                |
| 60819002 <http://snome |                        |                  |
| d.info/id/60819002>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Face                   | N                |
| 89545001 <http://snome |                        |                  |
| d.info/id/89545001>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Head                   | N                |
| 69536005 <http://snome |                        |                  |
| d.info/id/69536005>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `774007 <http://sno    | Head and Neck          | N                |
| med.info/id/774007>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `661005 <http://sno    | Jaw region             | N                |
| med.info/id/661005>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Mandible               | N                |
| 91609006 <http://snome |                        |                  |
| d.info/id/91609006>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Mastoid bone           | Y                |
| 59066005 <http://snome |                        |                  |
| d.info/id/59066005>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Maxilla                | Y                |
| 70925003 <http://snome |                        |                  |
| d.info/id/70925003>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `12                    | Mouth                  | N                |
| 3851003 <http://snomed |                        |                  |
| .info/id/123851003>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Skull                  | N                |
| 89546000 <http://snome |                        |                  |
| d.info/id/89546000>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Sella turcica          | N                |
| 42575006 <http://snome |                        |                  |
| d.info/id/42575006>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `17                    | Submental              | N                |
| 0887008 <http://snomed |                        |                  |
| .info/id/170887008>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Temporomandibular      | Y                |
| 53620006 <http://snome | joint                  |                  |
| d.info/id/53620006>`__ |                        |                  |
+------------------------+------------------------+------------------+
| `                      | Tongue                 | N                |
| 21974007 <http://snome |                        |                  |
| d.info/id/21974007>`__ |                        |                  |
+------------------------+------------------------+------------------+

.. warning::

   The above table was copied from the DICOM standard. However, the
   recommendation for usage of SNOMED CT codes is to always use the most
   granular code possible for what the code is describing. The
   implementer shall follow the codes as defined in this document.

+---+----------+-----------------------------------------------------+
| U | Unpaired | Used for most images.                               |
+---+----------+-----------------------------------------------------+
| L | Left     | Only use if this Series is of Mastoid bone, Maxilla |
|   |          | or Temporomandibular joint. For all other anatomic  |
|   |          | regions containing one or both sides, set to 'U'.   |
+---+----------+-----------------------------------------------------+
| R | Right    | Only use if this Series is of Mastoid bone, Maxilla |
|   |          | or Temporomandibular joint. For all other anatomic  |
|   |          | regions containing one or both sides, set to 'U'.   |
+---+----------+-----------------------------------------------------+
| B | Both     | Only use if this Series is of Mastoid bone, Maxilla |
|   |          | or Temporomandibular joint. For all other anatomic  |
|   |          | regions containing one or both sides, set to 'U'.   |
|   |          | This is almost never used.                          |
|   |          |                                                     |
|   |          | For example, a frontal face smiling photograph,     |
|   |          | would have Image Laterality of 'U'. However, an     |
|   |          | image which would contain both the left Maxilla and |
|   |          | the right Maxilla in the same frame (image) (for    |
|   |          | example making use of mirrors or by merging two     |
|   |          | images into one) would have an Image Laterality of  |
|   |          | 'B'.                                                |
+---+----------+-----------------------------------------------------+

+------------------------------+--------------------------------------+
| Image Laterality (0020,0062) | Coded Modifier                       |
+==============================+======================================+
| L                            | `(7771000, SCT,                      |
|                              | "Left"                               |
|                              | ) <http://snomed.info/id/7771000>`__ |
+------------------------------+--------------------------------------+
| R                            | `(24028007, SCT,                     |
|                              | "Right")                             |
|                              |  <http://snomed.info/id/24028007>`__ |
+------------------------------+--------------------------------------+
| U                            | `(66459002, SCT,                     |
|                              | "Unilateral")                        |
|                              |  <http://snomed.info/id/66459002>`__ |
+------------------------------+--------------------------------------+
| B                            | `(51440002, SCT,                     |
|                              | "Bilateral")                         |
|                              |  <http://snomed.info/id/51440002>`__ |
+------------------------------+--------------------------------------+
