.. _longitudinal_temporal_offset_from_event:

Longitudinal Temporal Offset from Event
=======================================

- Recommended. SHOULD be present if :ref:`longitudinal_temporal_event_type` is present. 
- If present, :ref:`longitudinal_temporal_event_type` SHALL be present.

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
      - 0,1,2,3,...
      - Number of days past the Event Type.


Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

The Concept Name the values is defined in `TID 1502 Time Point Context <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_A.html#sect_TID_1502>`__ to be `DCM-128740 Longitudinal Temporal Offset from Event <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#DCM_128741>`__ and its values are defined to be `NUMERICAL` in units of days.

.. _numeric_value_attribute:

Numeric Value Attribute (0040,A30A)
-------------------------------------------

Required. This field SHALL be populated and part of this Acquisition Context Sequence (0040,0555) if the Concept Name Code Sequence Attribute (0040,A043) with value *DCM-128740 Longitudinal Temporal Offset from Event* is also part of this same Sequence.

Zero or a positive integer, in units of days.

- If value is unknown, the entire sequence should be omitted.
- If value is zero (0), the integer zero SHALL be used.
- This Acquisition Context Sequence (0040,0555) without a Numeric Value Attribute (0040,A30A) SHALL be considered invalid, malformed and disregarded. Interpreting it as a zero is a violation of this standard.
