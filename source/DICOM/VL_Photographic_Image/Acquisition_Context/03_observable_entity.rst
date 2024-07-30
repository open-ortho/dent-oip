.. _observable_entity:

Observable entity
===============================================

Optional. Zero or more observable entities.

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
      - `SCT-363787002 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=363787002&edition=MAIN&release=&languages=en>`__
      - Observable entity
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID KKKK Observable Entities
      - See :ref:`cid-KKKK` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

.. note:: 
  The Concept Name for CID-KKKK entries is defined in `TID FFFF VL Orthodontic Acquisition Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_c.html>`__ to be `SCT-363787002 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=363787002&edition=MAIN&release=&languages=en>`__.


Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The following are those codes of `DICOM CID KKKK <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_KKKK.html>`__ which are of interest to orthodontic photography.

.. _cid-KKKK:

.. list-table:: CID KKKK. Observable Entities
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - `SCT 193093009 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=193093009&edition=MAIN&release=&languages=en>`__
      - Bell's palsy (disorder)
      - Optional.
    