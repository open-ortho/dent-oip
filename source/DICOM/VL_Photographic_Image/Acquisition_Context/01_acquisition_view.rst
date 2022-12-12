.. _dental acquisition view:

CID xxx1 Dental Acquisition View
================================

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
      - ????
      - Dental Acquisition View
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID-xxx1 values. 
      - See :ref:`notes <cid-xxx1>` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

.. warning::
  The code for this concept name is still undefined.

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------


.. note::
  These codes have been added to DICOM via CP-1570.

.. _cid-xxx1:

.. list-table:: 
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - SCT 30730003
      - Sagittal
      - 
    * - SCT 81654009
      - Coronal
      - 
    * - SCT 710098004
      - Occlusal projection
      - 

