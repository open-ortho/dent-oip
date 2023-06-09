.. _functional conditions present during acquisition:

Functional Condition Present During Acquisition
===============================================

A functional condition present during acquisition, such as phonation, weight bearing, voiding of the bladder or hemodynamic physiological challenges.

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
      - `DCM-130324 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_130324>`__
      - Functional condition present during acquisition
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID xxx3 values. 
      - See :ref:`notes <cid-91>` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

.. note:: 
  The Concept Name for CID-91 entries is defined in `TID 3460 Projection Radiography Acquisition Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_c.html>`__ to be `DCM-130324 Functional condition present during acquisition <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_130324>`__.

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The following are those codes of `DICOM CID 91 <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_91.html>`__ which are of interest to orthodontic photography.

.. _cid-91:

.. list-table:: CID 91
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - `SCT XXXXXXXXX <https://browser.ihtsdotools.org/?perspective=full&conceptId1=XXXXXXXXX&edition=MAIN&release=&languages=en>`__
      - Face with lips in relaxed position 
      - Still waiting for SNOMED-CT code. Should be an observable entity or finding.
    * - `SCT XXXXXXXXX <https://browser.ihtsdotools.org/?perspective=full&conceptId1=XXXXXXXXX&edition=MAIN&release=&languages=en>`__
      - Face with lips in closed position
      - Still waiting for SNOMED-CT code. Should be an observable entity or finding.
    * - `SCT XXXXXXXXX <https://browser.ihtsdotools.org/?perspective=full&conceptId1=XXXXXXXXX&edition=MAIN&release=&languages=en>`__
      - Mouth in partially open position and teeth apart
      - Still waiting for SNOMED-CT code. Should be an observable entity or finding.
    * - `SCT 262016004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=262016004&edition=MAIN&release=&languages=en>`__
      - Open Mouth (finding)
      - 
    * - `SCT XXXXXXXXX <https://browser.ihtsdotools.org/?perspective=full&conceptId1=XXXXXXXXX&edition=MAIN&release=&languages=en>`__
      - Mandible postured forward (observable entity)
      - Still waiting for SNOMED-CT code. Should be an observable entity or finding.
    * - `SCT 225583004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=225583004&edition=MAIN&release=&languages=en>`__
      - Smiles (finding)
      - 
    * - `SCT 110320000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=110320000&edition=MAIN&release=&languages=en>`__
      - Centric occlusion (observable entity)
      - Optional. If present, *Centric relation* cannot be present. See :ref:`Centric Relation and Centric Occlusion Definition <centric occlusion>`.
    * - `SCT 736783005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=736783005&edition=MAIN&release=&languages=en>`__
      - Centric relation (observable entity)
      - Optional. If present, *Centric occlusion* cannot be present. See :ref:`Centric Relation and Centric Occlusion Definition <centric occlusion>`.
    * - `SCT 276470008 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=276470008&edition=MAIN&release=&languages=en>`__
      - Skin mark (disorder)
      - Optional. Use this code or SNOMED-CT children of this code if some kind of skin mark is present. For example: Birthmark, slap mark, ...
    * - `SCT 341000119102 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=341000119102&edition=MAIN&release=&languages=en>`__
      - Tattoo of skin (finding)
      - Optional. Use this code if a tattoo is present on the skin inside the field of view.

