.. _dicom_tags:

7. DICOM Content Definitions
=============================
The DICOM Content Definitions constrain the use of instances of specific DICOM IODs (also referred to as DICOM objects). This typically means placing requirements on the creators of those instances, although requirements may also be placed on the receivers and users.

The most common such requirements are to:

+ Make a module that is optional (U) in a DICOM IOD be required or conditional,
+ Make an attribute that is optional (Type 3) in a DICOM Module be required or conditional,
+ Require that an attribute that is optional (Type 3) in a DICOM Module be absent
+ Constrain the content of an attribute to be empty
+ Constrain the content of an attribute to be populated in a certain way, such as:
	+ Constraining the value to be taken from a specific table
	+ Constraining the value to be copied from a specific source
	+ Constraining the value to encode certain information
+	Require that an attribute be displayed/accessible to the operator

Reiterating DICOM requirements is kept to a minimum sufficient to provide context for the IHE requirements.  Implementers are still required to be familiar with, and conform to, the underlying DICOM specification. 

Content Definitions may be referenced from a Profile independent of transactions to constrain content without specifying the transport.  Content Definitions may also be referenced from within a Transaction specification to constrain the content without duplicating the same constraint text across multiple related transactions.

For attributes that are optional, the creator is permitted but not required to include them, and the receiver is permitted but not required to ignore them.

7.1	Conventions
+++++++++++++++

DICOM Conventions are defined in Appendix E.2 to the IHE Technical Frameworks General Introduction. See https://profiles.ihe.net/GeneralIntro/ch-E.html#E.2.

**Table 7.1-1**

.. list-table:: 
    :header-rows: 1

    * - Usage
      - Meaning
    * - M / C / U
      - As defined in DICOM PS 3.3
    * - R
      - The Module is defined as Conditional (C) or User Option (U) in DICOM. The Requirement is an IHE extension of the DICOM requirements, and the module shall be present.
    * - RC
      - TThe Module is defined as Conditional (C) or User Option (U) in DICOM. The Requirement is an IHE extension of the DICOM requirements, and the module shall be present when the specified conditions apply.

**Table 7.1-2**

.. list-table:: 
    :header-rows: 1

    * - Usage
      - Meaning
    * - O
      - The attribute or its value is optional, i.e., in DICOM it is Type 2 or 3. 
    * - O+*
      - The attribute or its value is optional, i.e., in DICOM it is Type 2 or 3. 
    * - R
      - The attribute is required, and is not an IHE extension of the DICOM requirements; i.e., it is already Type 1 in DICOM, but additional constraints are placed by IHE, for example on the value set that may be used for the attribute. 
    * - R+
      - The Requirement is an IHE extension of the DICOM requirements, and the attribute shall be present, i.e., is Type 1, whereas the DICOM requirement may be Type 2 or 3. 
    * - RC+
      - The Requirement is an IHE extension of the DICOM requirements, and the attribute shall be present when the condition is satisfied, i.e., is Type 1C, whereas the DICOM requirement may be Type 2 or 3. If the condition is not fulfilled, the DICOM definitions apply. Note, that this means that the attribute may be present / have a value also in case the condition does not apply.
    * - -
      - No IHE extension of the DICOM requirements is defined. The attribute is listed for better readability or similar purpose.
    * - X+
      - The attribute information is required to be absent. DICOM Type 2 attributes shall be present with no value. DICOM Type 3 attributes shall be absent.

7.2 General Definitions
+++++++++++++++++++++++
Intentionally left blank.

7.3 IOD Definitions
++++++++++++++++++++
This section contains DICOM IOD specifications referenced in profiles of the IHE Dental domain, specifying the parts of the DICOM Standard used and the extended IHE requirements.

This normative section contains a description of the DICOM tags which are
necessary to fully describe orthodontic views (photographs) and to request for these photographs to be taken (acquired).

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

.. toctree::
	:glob:
	:maxdepth: 1

	*/index
