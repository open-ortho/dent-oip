.. _finding_by_inspection:

Finding By Inspection
===============================================

Optional. Zero or more findings MAY be present.

A finding by inspection is an artifact on the patient which is identified as part of the inspection during a visit or encounter. 

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
      - `SCT-118243007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=118243007&edition=MAIN&release=&languages=en>`__
      - Finding by Inspection
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID HHHH Finding by Inspection
      - See :ref:`cid-HHHH` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

.. note:: 
  The Concept Name for CID-HHHH entries is defined in `TID FFFF VL Orthodontic Acquisition Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_c.html>`__ to be `SCT-118243007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=118243007&edition=MAIN&release=&languages=en>`__.


Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The following are those codes of `DICOM CID HHHH <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_HHHH.html>`__ which are of interest to orthodontic photography.

.. _cid-HHHH:

.. list-table:: CID HHHH. Finding by Inspection
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - `SCT 276470008 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=276470008&edition=MAIN&release=&languages=en>`__
      - Skin mark (disorder)
      - Optional. MAY be present if some kind of skin mark is present. SNOMED-CT children of this code are also allowed, e.g. birthmark, slap mark, ...
    * - `SCT 341000119102 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=341000119102&edition=MAIN&release=&languages=en>`__
      - Tattoo of skin (finding)
      - Optional. MAY be present if a tattoo is present on the skin within the field of view.
    * - `SCT 4356008 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=4356008&edition=MAIN&release=&languages=en>`__
      - Gingival recession (disorder)
      - Optional. MAY be present.
    * - `SCT 710793000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=710793000&edition=MAIN&release=&languages=en>`__
      - Cant of occlusal plane (observable entity)
      - Optional. MAY be present.
    * - `SCT 1264188003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1264188003&edition=MAIN&release=&languages=en>`__
      - Local exogenous pigmentation of left buccal mucosa
      - Optional. MAY be present.
    * - `SCT 1264193000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1264193000&edition=MAIN&release=&languages=en>`__
      - Local exogenous pigmentation of right buccal mucosa
      - Optional. MAY be present.
    * - `SCT 1260043007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1260043007&edition=MAIN&release=&languages=en>`__
      - Local exogenous pigmentation of mucosa of soft palate
      - Optional. MAY be present.
    * - `SCT 1260047008 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1260047008&edition=MAIN&release=&languages=en>`__
      - Local exogenous pigmentation of mucous membrane of lower lip
      - Optional. MAY be present.
    * - `SCT 1260049006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1260049006&edition=MAIN&release=&languages=en>`__
      - Local exogenous pigmentation of mucous membrane of upper lip    
      - Optional. MAY be present.