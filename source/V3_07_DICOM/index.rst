.. _dicom_tags:

7. DICOM Content Definitions
=============================
The DICOM Content Definitions constrain the use of instances of specific DICOM IODs (also referred to as DICOM objects). This typically means placing requirements on the creators of those instances, although requirements may also be placed on the receivers and users.

The most common such requirements are to:

+ Make a module that is optional (U) in a DICOM IOD be required or conditional,
+ Make an attribute that is optional (Type 3) in a DICOM Module be required or conditional,
+ Require that an attribute that is optional (Type 3) in a DICOM Module be absent
+ Constrain the content of an attribute to be empty
+ Constrain the content of an attribute to be populated in a certain way, such as
	+ Constraining the value to be taken from a specific table
	+ Constraining the value to be copied from a specific source
	+ Constraining the value to encode certain information
+	Require that an attribute be displayed/accessible to the operator

Reiterating DICOM requirements is kept to a minimum sufficient to provide context for the IHE requirements.  Implementers are still required to be familiar with, and conform to, the underlying DICOM specification. 

Content Definitions may be referenced from a Profile independent of transactions to constrain content without specifying the transport.  Content Definitions may also be referenced from within a Transaction specification to constrain the content without duplicating the same constraint text across multiple related transactions.

For attributes that are optional, the creator is permitted but not required to include them, and the receiver is permitted but not required to ignore them.


.. toctree::
	:glob:
	:maxdepth: 1

	*/index
