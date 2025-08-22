.. _reason_for_visit:

Reason For Visit
================

In orthodontics, the reason for a visit is typically obtained from the Practice Management System (PMS) and is associated with an appointment. Examples include "Initial Consultation", "Follow-up", "Debanding", or "Adjustment". These values represent the reason for the patient's visit and do not necessarily describe any imaging-specific procedures.

This differs from Requested Procedure Description (0032,1060), which is used in the Modality Worklist to describe the image-specific procedure to be performed. See :ref:`requested_procedure`.

Reason For Visit Code Sequence (0032,1067)
==========================================

- If the PMS uses values from a set, such as those used for billing, or a pre-programmed or customizable list, then (0032,1067) SHALL be used.
- If the PMS only provides free text, (0032,1066) MAY be used instead.
- This sequence allows multiple codes, but for orthodontic visits, typically only one code is used.

Reason For Visit (0032,1066)
============================

- When a coded value from the PMS is not available, (0032,1066) MAY be used alone. This MAY occur when the PMS only provides free text for the appointment type.
- This attribute can contain a character string that MAY include one or more paragraphs, and is considered "unlimited" in length. The actual limit is two bytes less than 4GB. Refer to `DICOM Value Representation (VR) <https://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html>`__ for more details.
