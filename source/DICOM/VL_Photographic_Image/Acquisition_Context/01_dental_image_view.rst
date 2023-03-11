.. _dental image view:

CID xxx1 Dental Image View
==========================

The projection of the anatomic region of interest on an image receptor.

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
      - `DCM-111031 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_111031>`__
      - Image View
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID-xxx1 values. 
      - See :ref:`notes <cid-xxx1>` below.


Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

A DICOM code is used (instead of a SNOMED-CT code), because the Concept Name "`Image View <https://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_111031>`__" already exists in DICOM and can be found througout `DICOM Part 16 <https://dicom.nema.org/medical/dicom/current/output/html/part16.html>`__ 

.. note::
  Use one of the lateral projections for photographs of the buccal (cheek) region.
  
  *Buccal projection* is not present in SNOMED-CT, but there are various lateral projections. *Buccal (intended site)* `SCT 763825005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=763825005&edition=MAIN&release=&languages=en>`__ in the anatomic region sequence is enough to specify un-ambiguosly that this photograph is a buccal view. 


.. _cid-xxx1:

.. list-table:: CID-xxx1
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - `SCT 260499007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260499007&edition=MAIN&release=&languages=en>`__
      - Occlusal projection (qualifier value)
      - 
    * - `SCT 399033003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399033003&edition=MAIN&release=&languages=en>`__
      - Frontal projection (qualifier value)
      - 
    * - `SCT 399173006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399173006&edition=MAIN&release=&languages=en>`__
      - Left lateral projection (qualifier value)
      - For left buccal photographs
    * - `SCT 399198007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399198007&edition=MAIN&release=&languages=en>`__
      - Right lateral projection (qualifier value)
      - For right buccal photographs

