.. _acquisition_context:

7.4.1.6 Acquisition Context
+++++++++++++++++++++++++++

This normative section contains extensions to DICOM tags defined in the Acquisition Context module which are relevant to orthodontic image acquisition.

For orthodontic photography, we make use of the Acquisition Context module to store the conditions of the patient during the photographic acquisition session (lips and mouth open, closed, smiling, relaxed, etc), the occlusal relationship (centric occlusion, centric relation, see :ref:`definitions`), the Image View (projection) and the Image View Modifier (direct or indirect).

**References:**

+ `DICOM PS3.3: C.7.6.14 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.14>`_
+ Extensions in Table 7.4.1.6-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

.. list-table:: **Table 7.4.1.6-1 Acquisition Context Module Attribute Requirements**
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - Acquisition Context Sequence
      - (0040,0555)
      - R
      -  A Sequence of Items that describes the conditions present during the acquisition of the data of the SOP Instance.  Zero or more Items shall be included in this Sequence.
    * - > Concept Name Code Sequence
      - (0040,A043)
      - R+
      - 

.. toctree::
	:glob:
	:maxdepth: 1

	./*
