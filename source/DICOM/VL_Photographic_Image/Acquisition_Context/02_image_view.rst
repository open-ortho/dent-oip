.. _dental image view:

CID xxx2 Dental Image View Modifier
===================================

Modifier for Image View.

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
      - `DCM-111032 <https://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_111032>`__
      - Image View Modifier
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID xxx2 values. 
      - See :ref:`notes <cid-xxx2>` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

A DICOM code is used (instead of a SNOMED-CT code), because the Concept Name "`Image View Modifier <https://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_111032>`__" already exists in DICOM and can be found througout `DICOM Part 16 <https://dicom.nema.org/medical/dicom/current/output/html/part16.html>`__ 

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

Photographs in orthodontics are not always taken directly: sometimes there is a
device between the patient and the camera lens, like a mirror, to be able to see
specific regions.


.. _cid-xxx2:
.. list-table:: CID-xxx2
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - `SCT 255589003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=255589003&edition=MAIN&release=&languages=en>`__
      - Direct (qualifier value)
      - Traditional photograph, nothing between lens and anatomy.
    * - `SCT 255541007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=255541007&edition=MAIN&release=&languages=en>`__
      - Indirect (qualifier value)
      - Light from anatomy is reflected on a mirror before reaching camera lens.
