.. _06_longitudinal_temporal_offset_from_event:

Longitudinal Temporal Offset from Event
=======================================

- Recommended. SHOULD be present if :ref:`longitudinal_temporal_event_type` is present. 
- If present, :ref:`longitudinal_temporal_event_type` SHALL be present.

During an orthodontic treatment, it is common for the provider to keep track of treatment progress by regularly collecting records (such as photographs or intra-oral surface scans) [provide reference]. It is therefore useful to identify when, relative to an orthodontic treatment, the records were taken. In particular, the orthodontic provider is interested in knowing if, when the photographs were acquired, the patient: 

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

The Concept Name the values is defined in `TID 1502 Time Point Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_A.html#sect_TID_1502>`__ to be `DCM-128740 Longitudinal Temporal Offset from Event <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_128741>`__ and its values are defined to be `NUMERICAL` in units of days.

.. _numeric_value_attribute:

Numeric Value Attribute (0040,A30A)
-------------------------------------------

