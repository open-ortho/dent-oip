.. _general_definitions:

7.2  DICOM Coded Values
-----------------------
*Note: Codes are added here for now; they may find a new home*

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

7.2.2 Table CID 247 - Laterality Left-Right Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _cid-247a:
.. list-table:: **Table CID 247. Laterality Left-Right Only**
    :header-rows: 1

    * - Code Scheme Designator
      - Code Value
      - Code Meaning
      - Notes
    * - SCT
      - 24028007
      - Right (qualifier value)
      - 
    * - SCT
      - 7771000
      - Left (qualifier value)
      - 

7.2.3 Table CID 4061 - Head and/or Neck Primary Anatomic Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These values are used in the Primary Anatomic Structure Sequence (0008,2228) and are a subset of DICOM CID 4061.

.. _cid-4061:
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
