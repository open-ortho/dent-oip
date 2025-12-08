.. _patient_study:


References:  DICOM PS3.3 C.7.1.1   Note:  Extensions in Table X.y z-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

**Table X.y.z-1 Patient Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - Patient's Name
      - (0010,0010)
      - R+
      - SHALL include the patient’s legal name; if anonymized, SHALL follow DICOM’s Attribute Confidentiality Profiles (Normative) in Part 15 Chapter E
    * - Patient's Birth Date
      - (0010,0030)
      - R+
      - SHALL include the patient’s date of birth; if anonymized, SHALL follow DICOM’s Attribute Confidentiality Profiles (Normative) in Part 15 Chapter E


Patient Study
=============

This normative section contains a description of the DICOM tags relevant to orthodontic photography pertaining to the Patient Study module.

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

.. toctree::
	:glob:
	:maxdepth: 2

	./*
