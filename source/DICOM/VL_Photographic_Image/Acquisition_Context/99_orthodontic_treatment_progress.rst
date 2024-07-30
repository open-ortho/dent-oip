.. _orthodontic treatment progress:

Orthodontic Treatment Progress
==============================

During an orthodontic treatment, it is common for the provider to keep
track of treatment progress by regularly collecting records (such as
photographs or intra-oral surface scans) [provide reference]. It is
therefore useful to identify when, relative to an orthodontic treatment,
the records were taken. In particular, the orthodontic provider is interest in knowing if when the photographs were acquired, the patient 

- was in treatment (progress photos)
- never had treatment before (observation/pretreatment photos)
- had treatment before (posttreatment).

There are three places where progress shall be stored for orthodontic photographs:

- Longitudinal Temporal Event Type (Registration,Treatment,Posttreatment)
- Longitudinal Temporal Offset From Event (in days)
- :ref:`study_description`

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
    * - > Acquisition Context Sequence Attribute
      - (0040,0555) 
      - 
      - This sequence is omitted for "Initial" and "Final", as there are no progresses.
    * - >> Concept Name Code Sequence Attribute
      - (0040,A043)
      - DCM-128740
      - Longitudinal Temporal Offset from Event
    * - >> Numeric Value Attribute
      - (0040,A30A)
      - 1,2,3,...
      - Number of days past the Event Type.


Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

The Concept Name for CID-280 entries is defined in `TID 1502 Time Point Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_A.html#sect_TID_1502>`__ to be `DCM-128741 Longitudinal Temporal Event Type <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_128741>`__.

The Concept Name the values is defined in `TID 1502 Time Point Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_A.html#sect_TID_1502>`__ to be `DCM-128740 Longitudinal Temporal Offset from Event <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_128741>`__ and its values are defined to be `NUMERICAL` in units of days.

.. _concept code sequence attribute:

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

The allowed values for this tag have been taken from `DICOM Table CID280 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_280.html>`__ and applied in the :ref:`Progress Table above <cid-280>`

.. _cid-280:
.. list-table:: CID-280 Longitudinal Temporal Event Type
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - 2023 status in CID-280
    * - NCIt
      - C37948
      - Enrollment
      - Present. Not ideal.
    * - DCM
      - 121079
      - Baseline
      - Present. Not ideal.
    * - DCM
      - 126074
      - Posttreatment
      - Present in CID-6146, but not CID-280.
    * - SCTID
      - 184047000
      - Patient registration (procedure)
      - Not Present. Could substitute NCIt-C37948 Enrollment
    * - SCTID
      - 122452007
      - Comprehensive orthodontic treatment (procedure)
      - Not Present. Could substitute DCM-121079 Baseline

The below mapping provides a reference for translating orthodontic progresses in codesets that DICOM can understand.

.. note::

  It is not always trivial to distinguish Pretreatment from Observation. In some cases, there could be a clear Pretreatment definition by the provider, and it could be properly coded in the practice management system, however in many other cases it may not, or what was considered pretreatment might not end up in treatment. 
  
  The orthodontic domain experts of the working group therefore decided to disregard pretreatment status, and consider it as an observation.

.. _progress_codes:
.. list-table:: Orthodontic progress code mapping
    :header-rows: 1

    * - orthodontic progress
      - description
      - event type
      - offset (days)
    * - First Time Observation
      - Patient has just registered with the practice for the first time and has not agreed any treatment yet. The provider collects first time records.
      - NCIt-C37948 Enrollment (ideally SCTID-184047000 Patient registration)
      - 0
    * - Observation
      - Patient comes back for regular visits. The provider collects observation records.
      - NCIt-C37948 Enrollment (ideally SCTID-184047000 Patient registration)
      - Number of days past the day the patient registers.
    * - Pretreatment
      - Images acquired before treatment starts. Only used when the patient and doctor have agreed to start a treatment. This should be treated as Observation above.
      - See Observation
      - See Observation
    * - Initial
      - Patient and provider agreed to start treatment. Records are taken to mark the Baseline for comparison with treatment progress.
      - DCM-121079 Baseline (ideally SCTID-122452007 Comprehensive orthodontic treatment)
      - 0
    * - Progress
      - Images taken during treatment.
      - DCM-121079 Baseline (ideally SCTID-122452007 Comprehensive orthodontic treatment)
      - Number of days past the day the treatment started.
    * - Final
      - Image taken at the end of active treatment (after appliance removal, if applicable). Sequence number is not required.
      - DCM-126074 Posttreatment
      - 0
    * - Posttreatment
      - Image acquired after treatment.
      - DCM-126074
      - Number of days past the day the treatment ended (see Final above).


Study Description (0008,1030)
-----------------------------

Refer to :ref:`Study Description <study_description>`.