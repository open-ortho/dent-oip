.. _orthodontic treatment progress:

CID-xxx5 Orthodontic Treatment Progress
***************************************

.. warning:: 
  Table at bottom is missing proper SNOMED Codes.

During an orthodontic treatment, it is common for the provider to keep
track of treatment progress by regularly collecting records (such as
photographs or intra-oral surface scans) [provide reference]. It is
therefore useful to identify when, relative to an orthodontic treatment,
the records were taken. 


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
      - One of :ref:`cid-xxx5` below. 
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


.. _concept code sequence attribute:

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The allowed values for this tag have been taken from `DICOM Table CID6146 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_6146.html>`__ and applied in the :ref:`Progress Table above <cid-xxx5>`

Below is a list of the types of progresses used by the orthodontic domain and
how to properly encode them in a DICOM object.

.. _cid-xxx5:
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
