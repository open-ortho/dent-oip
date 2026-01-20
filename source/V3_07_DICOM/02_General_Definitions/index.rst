.. _general_definitions:

7.2  DICOM Coded Values
=======================
*Note: Codes are added here for now; they may find a new home*

7.2.1 Table CID 4028 - Craniofacial Anatomic Region
---------------------------------------------------
These values are used in Anatomic Region Sequence (0008,2218) and are a subset of DICOM CID 4028.  

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
------------------------------------------------

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
-----------------------------------------------------------------
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

