.. _orthodontic_progress:


Orthodontic Progress (Informative)
===================================

During orthodontic treatment, it is common for providers to monitor progress by regularly collecting records such as photographs or intra-oral surface scans [provide reference]. Identifying the timing of these records in relation to the treatment is crucial. Specifically, the provider needs to know if, at the time of acquisition, the patient:

- was undergoing treatment (progress photos)
- had never undergone treatment before (observation/pretreatment photos)
- had completed treatment (posttreatment photos)

Orthodontic photograph progress shall be stored in three key areas:

- Longitudinal Temporal Event Type (Registration, Treatment, Posttreatment)
- Longitudinal Temporal Offset From Event (in days)
- :ref:`study_description`

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
