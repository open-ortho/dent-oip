.. _acquisition_context:

7.4.1.6 Acquisition Context
+++++++++++++++++++++++++++

This normative section contains extensions to DICOM tags defined in the Acquisition Context module.

For orthodontic photography, we make use of the Acquisition Context module to encode the conditions of the patient during the photographic acquisition session (lips and mouth open, closed, smiling, relaxed, etc), the occlusal relationship (centric occlusion, centric relation, see :ref:`definitions`), the Image View (projection) and the Image View Modifier (direct or indirect) during the photographic acquisition session.  

Each of these is encoded as a sequence item in the Acquisition Context Sequence.  Table 7.4.1.6-1 and Section 7.4.1.6.1 specifiy how each acquisition context is encoded.

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
      - O+
      - Zero or more Items shall be included in this Sequence.   Each sequence item is encoded using the `Content Item Macro <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_10-2>`_ that describes one discreet, coded acquisition context value of the photographic acquisition session.
    * - > Value Type
      - (0040,A040)
      - R+
      - Shall be "CODE", unless the Concept Name Code is (128740, DCM, "Longitudinal Temporal Offset from Event"), in wich case the value shall be "NUMERIC".
    * - > Concept Name Code Sequence
      - (0040,A043)
      - R+
      - Coded concept name of this name-value Item.   Only a single Item shall be included in this Sequence. The coded value is taken from `DICOM TID 3465 VL Orthodontic Acquisition Context <https://dicom.nema.org/medical/dicom/current/output/html/part16.html#sect_TID_3465>`_.  Each sequence item is encoded using the DICOM `Content Item With Modifiers Macro <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_10.2.1-1>`_ .  
    * - > Concept Code Sequence
      - (0040,A168)
      - R+
      - Coded concept value of this name-value Item.  Only a single Item shall be included in this Sequence.   See :ref:`acquisition_context_sequence_items` for coded values under each Concept Name Code

.. _acquisition_context_sequence_items:

7.4.1.6.1 Acquisition Context Sequence Items
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Each sequence item describes one or more of the following, using the specifications and codes in the subsections below.

+ **Orthognathic Functional Conditions** - e.g., lips and mouth open, closed, smiling, relaxed, etc)
+ **Orthodontic Finding by Inspection** - artifact on the patient which is identified as part of the inspection during a visit or encounter
+ **Orthodontic Observable Entity** 
+ **Dental Occlusion** - centric occlusion, centric relation, see :ref:`definitions`
+ **Longitudinal Temporal Event Type**
+ **Longitudinal Temporal Offset from Event**

7.4.1.6.1.1 Orthognathic Functional Conditions
**********************************************

**Optionality:**  Recommended.  Zero or more functional conditions present during acquisition, such as position of lips, mandible position, mouth position. These include functional conditions that might influence the clinical treatment of jaws and/or alignment of teeth and SHOULD be present, if known.

This section specifies coded values in DICOM CID 4066 that can be used when Concept Name Code in (0040,A043) is **(130325, DCM, "Orthognathic Functional Condition")**.

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
      - (130325, DCM, "Orthognathic Functional Condition")
      - 
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID 4066 Orthognathic Functional Conditions
      - See :ref:`cid-4066`.

7.4.1.6.1.2 Orthodontic Finding by Inspection
*********************************************

**Optionality:** Optional  Zero or more findings MAY be specified. A finding by inspection is an artifact on the patient which is identified as part of the inspection during a visit or encounter. 

This section specifies coded values in DICOM CID 4067 that can be used when Concept Name Code in (0040,A043) is **(118243007, SCT, "Finding by inspection")**.

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
      - (118243007, SCT, "Finding by inspection")
      - 
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID 4067 Finding by inspection
      - See :ref:`cid-4067`.

7.4.1.6.1.3 Orthodontic Observable Entity
*****************************************

**Optionality:** Optional

This section specifies coded values in DICOM CID 4068 that can be used when Concept Name Code in (0040,A043) is **(363787002, SCT, "Observable entity")**.

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
      - (363787002, SCT, "Observable entity")
      - 
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID 4068 Orthodontic Observable Entity
      - See :ref:`cid-4068`.

7.4.1.6.1.4 Dental Occlusion
****************************

**Optionality:** Recommended. SHOULD be present, if known.  Defines the dental occlusion. Only one value is allowed.

This section specifies coded values in DICOM CID 4069 that can be used when Concept Name Code in (0040,A043) is **(25272006, SCT, "Dental occlusion")**.

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
      - (25272006, SCT, "Dental occlusion")
      - 
    * - >> Concept Code Sequence Attribute
      - One of CID 4069 Orthodontic Observable Entity
      - See :ref:`cid-4069`.
      - 

.. toctree::
	:glob:
	:maxdepth: 1

	./*
