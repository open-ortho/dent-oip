.. _acquisition_context:

7.4.1.6 Acquisition Context
+++++++++++++++++++++++++++

This normative section contains extensions to DICOM tags defined in the Acquisition Context module.

For orthodontic photography, we make use of the Acquisition Context module to encode the conditions of the patient during the photographic acquisition session (lips and mouth open, closed, smiling, relaxed, etc), the occlusal relationship (centric occlusion, centric relation, see :ref:`definitions`), the Image View (projection) and the Image View Modifier (direct or indirect) during the photographic acquisition session.  

Each of these is encoded as a sequence item in the Acquisition Context Sequence.  

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
      - R+
      - Zero or more Items shall be included in this Sequence.   Each sequence item describes one to store one discreet, coded acquisition context value of the photographic acquisition session.
    * - > Concept Name Code Sequence
      - (0040,A043)
      - R+
      - Each sequence item is encoded using the DICOM `Content Item With Modifiers Macro <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_10.2.1-1>`_ .  Section 7.4.1.6.1 :ref:`acquisition_context_sequence_items` identifies how each sequence item encodes a single acquisition context value.

.. _acquisition_context_sequence_items:

7.4.1.6.1 Acquisition Context Sequence Items
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Each sequence item describes one or more of the following, using the specifications and codes in the subsections below.

+ Orthognathic Functional Conditions - e.g., lips and mouth open, closed, smiling, relaxed, etc)
+ Finding by Inspection - artifact on the patient which is identified as part of the inspection during a visit or encounter
+ Observable Entity 
+ Dental Occlusion - centric occlusion, centric relation, see :ref:`definitions`
+ Longitudinal Temporal Event Type
+ Longitudinal Temporal Offset from Event

7.4.1.6.1.1 Orthognathic Functional Conditions
**********************************************

**Optionality:**  Recommended

Zero or more functional conditions present during acquisition, such as position of lips, mandible position, mouth position. These include functional conditions that might influence the clinical treatment of jaws and/or alignment of teeth and SHOULD be present, if known.

.. list-table:: 
    :header-rows: 1

    * - **Attribute Name**
      - **Tag**
      - **Value**
      - **Meaning**
    * - > Acquisition Context Sequence Attribute
      - (0040,0555) 
      - 
      - 
    * - >> Concept Name Code Sequence Attribute
      - (0040,A043)
      - `DCM-130325 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html#>`__
      - Orthognathic Functional Conditions  (Note: Zero or more conditions may be specified in this sequence.
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID 4066 Orthognathic Functional Conditions
      - See :ref:`cid-4066`.



.. toctree::
	:glob:
	:maxdepth: 1

	./*
