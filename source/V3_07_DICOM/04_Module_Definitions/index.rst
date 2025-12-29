.. _vl_photographic_image:

7.4 Module Definitions
======================

This section defines each DICOM Module used in the Dental domain in detail,
specifying the standards used and the information defined.

This normative section contains a description of the DICOM tags which are
necessary to fully describe orthodontic views (photographs).

This section also specifies the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

7.4.1.1 General (Common) Modules
++++++++++++++++++++++++++++++++
This section contains IHE constraints on Modules that are common to all DICOM Composite IODs.

7.4.1.1 Patient Module
++++++++++++++++++++++

This normative section contains extensions to DICOM tags defined in the Patient module which are relevant to orthodontic photography.

**References:**

+ `DICOM PS3.3: C.7.1.1  <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.1.1>`_ "Patient Module"
+ Extensions in 7.4.1.1-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1 and the IHE Technical Framework

**Table 7.4.1.1-1 Patient Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - Patient's Name
      - (0010,0010)
      - R+
      - IHE requires that this element be present. This element is one of the primary patient identifying elements, and assuch, all DICOM objects with the same Study Instance
UID, must have the same value in this element.Equipment which creates new series based on other series
(i.e., resampled series, new structure sets, plans, etc.) must preserve the value of this element to adhere to this profile.  If anonymized, shall follow DICOM’s Attribute Confidentiality Profiles (Normative) in DICOM PS3.15 Chapter E.
    * - Patient ID
      - (0010,0020)
      - R+
      - See Patient ID (0010,0010).  If anonymized, shall follow DICOM’s Attribute Confidentiality Profiles (Normative) in DICOM PS3.15 Chapter E.
    * - Patient's Birth Date
      - (0010,0030)
      - R+
      - See Patient ID (0010,0010).  If anonymized, shall follow DICOM’s Attribute Confidentiality Profiles (Normative) in DICOM PS3.15 Chapter E.

7.4.1.2 General Study Module
+++++++++++++++++++++++++++

This normative section contains extensions to DICOM tags defined in the General Study module DICOM tags which are relevant to orthodontic photography.

**References:**

+ `DICOM PS3.3: C.7.2.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.2.1>`_
+ Extensions in Table 7.4.1.2-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

**Table 7.4.1.2-1 General Study Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - Accession Number
      - (0008,0050)
      - ??
      - See :ref:`mwl_accession_number`.
    * - Study Description
      - (0008,1030)
      - RC+
      - Shall be present if orthodontic progress is known and set in the Acquisition Context Sequence (0040,0555). The value SHOULD represent the :ref:`orthodontic_progress`, in a human readable form. The string SHOULD be limited to 16 characters. If a Study Description is already present, the system MAY prefix the existing Study Description with this one.



.. toctree::
	:glob:
	:maxdepth: 1

	*/index
