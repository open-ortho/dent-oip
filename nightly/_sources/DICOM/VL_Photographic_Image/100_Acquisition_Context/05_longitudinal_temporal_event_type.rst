.. _longitudinal_temporal_event_type:

Longitudinal Temporal Event Type
===============================================


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
      - DCM-128741
      - Longitudinal Temporal Event Type
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of :ref:`CID-280 <cid-280>` below. 
      - See :ref:`notes <concept code sequence attribute>` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

The Concept Name for CID-280 entries is defined in `TID 1502 Time Point Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_A.html#sect_TID_1502>`__ to be `DCM-128741 Longitudinal Temporal Event Type <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_128741>`__.


.. _concept code sequence attribute:

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The allowed values for this tag have been taken from `DICOM Table CID280 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_280.html>`__ and applied in the :ref:`Progress Table above <cid-280>`

.. _cid-280:
.. list-table:: CID-280 Longitudinal Temporal Event Type
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - NCIt-C37948
      - Enrollment
      - 
    * - DCM-121079
      - Baseline
      - 
    * - `SCT 184047000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=184047000&edition=MAIN&release=&languages=en>`__
      - Patient registration
      - 
    * - `SCT 1332161000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1332161000&edition=MAIN&release=&languages=en>`__
      - Orthodontic Treatment started
      - 
    * - `SCT 1340210007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1340210007&edition=MAIN&release=&languages=en>`__
      - Orthodontic Treatment stopped
      - 
