7.3 IOD Definitions
===================
This section contains DICOM (Information Object Defintion) IOD specifications referenced in profiles of the IHE Dental domain.  

Each IOD definition contains a table that identifies Modules comprising the IOD, including the baseline Modules requirements defined in DICOM, and Modules where requirements are extended by Dental domain profiles.  

**Usage Values in the Module Tables:**

In Column 4 of the tables below, the values of **M**, **U**, and **C** for 'Usage' are defined in `DICOM PS3.3: A.1.3 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/chapter_A.html#sect_A.1.3>`_.  

In Column 5, these additional 'Usage' values are defined:

- **R** - The Module is defined as Conditional (C) or User Option (U) in DICOM; however, this Requirement is an IHE extension of the DICOM requirements, and the Module shall be present.
- **RC** - The Module is defined as Conditional (C) or User Option (U) in DICOM; however, this requirement is an IHE extension of the DICOM requirements, and the Module shall be present when the specified conditions apply.

**IOD Definitions specified in this section:**

+ :ref:`Section 7.3.1 VL Photographic Image IOD Definition <vl_photographic_image_iod_definition>`
+ :ref:`Section 7.3.2 Structured Display IOD Definition <structured_display_iod_definition>`
+ :ref:`Section 7.3.3 Hanging Protocol IOD Definition <hanging_protocol_iod_definition>`

.. toctree::
    :maxdepth: 1

    vl_photographic_image_iod_definition
    structured_display_iod_definition
    hanging_protocol_iod_definition
