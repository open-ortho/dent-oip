.. _orthognatic_functional_conditions:

Orthognathic Functional Conditions
===============================================

Recommended. Zero or more functional conditions present during acquisition, such as position of lips, mandible position, mouth position. These include functional conditions that might influence the clinical treatment of jaws and/or alignment of teeth and SHOULD be present, if known.

.. list-table:: 
    :header-rows: 1

    * - Attribute Name
      - Tag
      - Value
      - Meaning
    * - > Acquisition Context Sequence Attribute
      - (0040,0555) 
      - 
      - 
    * - >> Concept Name Code Sequence Attribute
      - (0040,A043)
      - `DCM-ZZZZZZ <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_ZZZZZZ>`__
      - Orthognathic Functional Conditions
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID GGGG Orthognathic Functional Conditions
      - See :ref:`cid-GGGG` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

.. note:: 
  The Concept Name for CID-GGGG entries is defined in `TID FFFF VL Orthodontic Acquisition Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_c.html>`__ to be `DCM-ZZZZZZ Orthognathic Functional Conditions <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_ZZZZZZ>`__.

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The following are those codes of `DICOM CID GGGG <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_GGGG.html>`__ which are of interest to orthodontic photography.

.. _cid-GGGG:

.. list-table:: CID GGGG. Orthognathic Functional Conditions
    :header-rows: 1

    * - Code
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