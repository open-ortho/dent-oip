.. _dental_occlusion_function:

Dental occlusion, function
===============================================

Recommended. SHOULD be present, if known.

Defines the dental occlusion. Only one value is allowed.

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
      - `SCT-25272006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=25272006&edition=MAIN&release=&languages=en>`__
      - Dental occlusion, function
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID LLLL Dental Occlusion
      - See :ref:`cid-LLLL` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

.. note:: 
  The Concept Name for CID-LLLL entries is defined in `TID FFFF VL Orthodontic Acquisition Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_c.html>`__ to be `SCT-25272006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=25272006&edition=MAIN&release=&languages=en>`__.


Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The following are those codes of `DICOM CID LLLL <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_LLLL.html>`__ which are of interest to orthodontic photography.

.. _cid-LLLL:

.. list-table:: CID LLLL. Dental Occlusion
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - `SCT 110320000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=110320000&edition=MAIN&release=&languages=en>`__
      - Centric occlusion (observable entity)
      - If present, *Centric relation* cannot be present. See :ref:`Centric Relation and Centric Occlusion Definition <centric occlusion>`.
    * - `SCT 736783005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=736783005&edition=MAIN&release=&languages=en>`__
      - Centric relation (observable entity)
      - If present, *Centric occlusion* cannot be present. See :ref:`Centric Relation and Centric Occlusion Definition <centric occlusion>`.




