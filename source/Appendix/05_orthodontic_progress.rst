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

The mapping below provides a reference for translating orthodontic progress into codesets that DICOM can understand.

.. _progress_codes:
.. list-table:: Orthodontic progress code mapping
    :header-rows: 1

    * - orthodontic progress
      - description
      - event type
      - offset (days)
    * - First Time Observation
      - Patient has just registered with the practice for the first time and has not agreed any treatment yet. The provider collects first time records.
      - NCIt-C37948 Enrollment
      - 0
    * - Observation
      - Patient comes back for regular visits. The provider collects observation records.
      - NCIt-C37948 Enrollment
      - Number of days past the day the patient registers.
    * - Pretreatment
      - Images acquired before treatment starts. Only used when the patient and doctor have agreed to start a treatment. This should be treated as Observation above.
      - See Observation
      - See Observation
    * - Initial
      - Patient and provider agreed to start treatment. Records are taken to mark the Baseline for comparison with treatment progress.
      - SCT-1332161000 Orthodontic Treatment started
      - 0
    * - Progress
      - Images taken during treatment.
      - SCT-1332161000 Orthodontic Treatment started
      - Number of days past the day the treatment started.
    * - Final
      - Image taken at the end of active treatment (after appliance removal, if applicable). Sequence number is not required.
      - SCT-1340210007 Orthodontic Treatment stopped
      - 0
    * - Posttreatment
      - Image acquired after treatment.
      - SCT-1340210007 Orthodontic Treatment stopped
      - Number of days past the day the treatment ended (see Final above).


.. note::

  Distinguishing Pretreatment from Observation is not always straightforward. In some cases, there may be a clear Pretreatment definition by the provider, which could be properly coded in the practice management system. However, in many other cases, it may not be clearly defined, or what was considered Pretreatment might not lead to treatment.

  Consequently, the orthodontic domain experts of the working group have decided to disregard Pretreatment status and consider it as Observation.


Study Description (0008,1030)
-----------------------------

This is an optional DICOM tag, which can contain a Long String (64 character max), part of the General Study module. For the application of orthodontic photographs, Study Description is used to replicate the treatment progress, as defined above.

The *Study Description* is shown by most PACS system in the search results when listing studies after a query. It is therefore recommended to repeat the information contained in the Concept Codes described in :ref:`longitudinal_temporal_event_type`  and :ref:`longitudinal_temporal_event_type` also here, but in a more human readable form. For example, it would be acceptable to choose a *Study Description* by using progress name defined by the main practice management system in use by the practice who was responsible for initially acquiring the photographs. For example:

- Pre-treatment 1
- Initial
- Progress 12
- Final


.. note::
    - The Study Description is usually used by the medical provider which is treating the patient and has acquired the images.
    - Other software might also use *Study Description* and only 64 characters are allowed. It is recommended to keep the string shorter than 16 characters, which would allow other software systems to append their text to this one.
    - When importing images acquired by other institutions, it may happen and is exptected for the *Study Description* to not be relevant to the receiving practice.
    - *Study Description* is *not* a good tag to be relied upon for interoperability across systems and institutions.
    - For reliable interoperability,  refer to *Acquisition Context* codes as defined in :ref:`longitudinal_temporal_event_type`  and :ref:`longitudinal_temporal_event_type`.
