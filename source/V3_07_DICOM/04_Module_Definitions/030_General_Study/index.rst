.. _general_study:

General Study
=============

This normative section contains extensions to DICOM tags defined in the General Study module DICOM tags which are relevant to orthodontic photography.

**References:**

+ `DICOM PS3.3: C.7.2.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.2.1>`_
+ Extensions in Table X.y z-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

**Table X.y.z-1 General Study Module Attribute Requirements**

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
	:maxdepth: 2

	./*
