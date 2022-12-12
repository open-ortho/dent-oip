.. _acquisition_context_sequence:

Acquisition Context Sequence (0040,0555)
========================================

For orthodontic photography, we make use of the `Acquisition Context Sequence (0040,0555) <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.14.html>`__ to store the treatment progress and the conditions of the lips and mouth (open, closed, smiling, relaxed, etc).

Orthodontic Treatment Progress
******************************

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
      - DCM-126072
      - Time Point Type
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID6146 values. 
      - See :ref:`notes <concept code sequence attribute>` below.
    * - > Acquisition Context Sequence Attribute
      - (0040,0555) 
      - 
      - This sequence is omitted for "Initial" and "Final", as there are no progresses.
    * - >> Concept Name Code Sequence Attribute
      - (0040,A043)
      - DCM-126073
      - Time Point Order
    * - >> Numeric Value Attribute 
      - (0040,A30A)
      - 1,2,3,...
      - An integer representing the sequence number of the progress.

Below is a list of the types of progresses used by the orthodontic domain and
how to properly encode them in a DICOM object.

.. _table_progress_values:
.. list-table:: Progress Values
    :header-rows: 1

    * - type
      - description
      - code
    * - Under Observation
      - Baseline. Images used for general documentation. Not part of regular treatment records. Sequence number is not required.
      - UMLS-C1442488
    * - Pretreatment
      - Images acquired before treatment starts. Only used when the patient and doctor have agreed to start a treatment. Initial would be the last "pretreatment" image acquired before treatment starts.
      - UMLS-C3539076
    * - Progress
      - Images taken during treatment.
      - ?
    * - Final
      - Image taken at the end of active treatment (after appliance removal, if applicable). Sequence number is not required.
      - ?
    * - Posttreatment
      - Image acquired after treatment.
      - DCM-126074

.. note::

   The lack of a row for "Initial" is intentional. All Pre-treatment images are essentially initials and initial can be considered as a synonym for pretreatment. There is no need for coding Initial in the image. The last pretreatment image acquired before treatment starts would be the initial.


.. _concept code sequence attribute:

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The allowed values for this tag have been taken from `DICOM Table CID6146 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_6146.html>`__ and applied in the :ref:`Progress Table above <table_progress_values>`

Functional Condition Present During Acquisition
******************************************************

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
      - DCM-130324
      - Functional condition present during acquisition
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID-91 values. 
      - See :ref:`notes <cid-91>` below.
    * - Acquisition Context Description
      - (0040,0556)
      - 
      - Optional. See notes below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

.. note:: 
  The Concept Name for CID-91 entries is defined in `TID 3460 Projection Radiography Acquisition Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_c.html>`__ to be `DCM-130324 Functional condition present during acquisition <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_130324>`__.

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The following are those codes of `DICOM CID 91 <http://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_91.html>`__ which are of interest to orthodontic photography.

.. note::
  These codes have been added to DICOM via CP-1570.


.. _cid-91:

.. list-table:: CID-91
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - SCT 789314008
      - Photographic image of face with lips in relaxed position
      - 
    * - SCT 787607005
      - Photographic image with lips closed
      - 
    * - SCT 789130005
      - Photographic image with mouth partially opened position and teeth apart
      - 
    * - SCT 225583004
      - Smile
      - 
    * - SCT 262016004
      - Open Mouth
      - 
    * - SCT 47162009
      - Mouth Closed
      - 



Acquisition Context Description (0040,0556)
-------------------------------------------

.. warning:: 

  Missing explanation of description.
