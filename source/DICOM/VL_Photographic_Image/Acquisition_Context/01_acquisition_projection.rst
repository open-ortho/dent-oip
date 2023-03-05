.. _dental acquisition projection:

CID xxx1 Dental acquisition projection
======================================

.. Why do we need a new table for Sagittal and Coronal view? How does this differ from Patient Orientation?

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
      - `SCT 260419006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260419006&edition=MAIN&release=&languages=en>`__
      - Projection
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID-xxx1 values. 
      - See :ref:`notes <cid-xxx1>` below.


Concept Code Sequence Attribute (0040,A168)
-------------------------------------------


.. note::
  These codes have been added to DICOM via CP-1570.

.. _cid-xxx1:

.. list-table:: 
    :header-rows: 1

    * - Code
      - Meaning
      - Type
    * - `SCT 260499007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260499007&edition=MAIN&release=&languages=en>`__
      - Occlusal projection
      - qualifier value 
    * - `SCT 399033003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399033003&edition=MAIN&release=&languages=en>`__
      - Frontal projection
      - qualifier value
    * - `SCT 399173006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399173006&edition=MAIN&release=&languages=en>`__
      - Left lateral projection
      - qualifier value
    * - `SCT 399198007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399198007&edition=MAIN&release=&languages=en>`__
      - Right lateral projection
      - qualifier value

