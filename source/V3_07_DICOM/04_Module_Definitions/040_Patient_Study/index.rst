.. _patient_study:


Patient Study Module
=====================

This normative section contains extensions to DICOM tags defined in the Patient Study module .

Encoding Reason for Visit
+++++++++++++++++++++++++

In orthodontics, the reason for a visit is typically obtained from the Practice Management System (PMS) and is associated with an appointment. Examples include "Initial Consultation", "Follow-up", "Debanding", or "Adjustment". These values represent the reason for the patient's visit and do not necessarily describe any imaging-specific procedures.

This differs from Requested Procedure Description (0032,1060), which is used in the Modality Worklist to describe the image-specific procedure to be performed. See :ref:`requested_procedure`.

**References:**

+ `DICOM PS3.3: C.7.1.1  <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.2.2>`_ "Patient Study Module"
+ Extensions in Table X.y z-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

**Table X.y.z-1 Patient Study Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - Reason for Visit
      - (0032,1066)
      - RC+
      - When a coded value from the PMS is not available to encode in the Reason for Visit Code Sequence (0032,1067), then Reason for Visit (0032,1066) MAY be used alone. This may occur when the PMS only provides free text for the appointment type.  This attribute can contain a character string that MAY include one or more paragraphs, and is considered "unlimited" in length. The actual limit is two bytes less than 4GB. Refer to `DICOM PS3.5: Section 6.2 <https://dicom.nema.org/medical/dicom/current/output/html/part05.html#sect_6.2>`__ "DICOM Value Representation (VR)" for more details.
    * - Reason for Visit Code Sequence
      - (0032,1067)
      - RC+
      - If the PMS uses values from a set, such as those used for billing, or a pre-programmed or customizable list, then (0032,1067) SHALL be used. This sequence allows multiple codes, but for orthodontic visits, typically only one code is used.

.. toctree::
	:glob:
	:maxdepth: 2

	./*
