.. _dicom_tags:

7. DICOM Content Definitions
=============================

This normative section contains a description of the DICOM tags which are
necessary to fully describe orthodontic views (photographs) and to request for these photographs to be taken (acquired).

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

*The
DICOM Content Definitions constrain the use of instances of specific DICOM IODs (also referred to as DICOM objects). This typically means placing requirements on the creators of those instances, although requirements may also be placed on the receivers and users.

The most common such requirements are to:

+ Make a module that is optional (U) in a DICOM IOD be required or conditional,
+ Make an attribute that is optional (Type 3) in a DICOM Module be required or conditional,
+ Require that an attribute that is optional (Type 3) in a DICOM Module be absent
+ Constrain the content of an attribute to be empty
+ Constrain the content of an attribute to be populated in a certain way, such as:
++ Constraining the value to be taken from a specific table
++ Constraining the value to be copied from a specific source
++ Constraining the value to encode certain information
+	Require that an attribute be displayed/accessible to the operator

Reiterating DICOM requirements is kept to a minimum sufficient to provide context for the IHE requirements.  Implementers are still required to be familiar with, and conform to, the underlying DICOM specification. 
Content Definitions may be referenced from a Profile independent of transactions to constrain content without specifying the transport.  Content Definitions may also be referenced from within a Transaction specification to constrain the content without duplicating the same constraint text across multiple related transactions.
For attributes that are optional, the creator is permitted but not required to include them, and the receiver is permitted but not required to ignore them.

7.1	Conventions
+++++++++++++++

DICOM Conventions are defined in Appendix E.2 to the IHE Technical Frameworks General Introduction. See https://profiles.ihe.net/GeneralIntro/ch-E.html#E.2.

*TODO:   Add tables from template

7.1	Conventions
+++++++++++++++

This section contains DICOM IOD specifications referenced in profiles of the IHE Dental domain, specifying the parts of the DICOM Standard used and the extended IHE requirements.

.. toctree::
	:glob:
	:maxdepth: 1

	*/index
