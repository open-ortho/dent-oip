
.. toctree::
	:glob:
	:maxdepth: 1

	*/index

1 Introduction to Volume 2
==========================
This document, Volume 2 of the IHE Dental (DEN) Technical Framework, defines
transactions used in IHE Dental Domain profiles.

1.1 Introduction to IHE
-----------------------
Integrating the Healthcare Enterprise (IHE) is an international initiative to promote the use of
standards to achieve interoperability among health information technology (HIT) systems and
effective use of electronic health records (EHRs). IHE provides a forum for care providers, HIT
experts and other stakeholders in several clinical and operational domains to reach consensus on
standards-based solutions to critical interoperability issues.

The primary output of IHE is system implementation guides, called IHE Profiles. IHE publishes 
each profile through a well-defined process of public review and trial implementation and
gathers profiles that have reached final text status into an IHE Technical Framework, of which
this volume is a part.

For general information regarding IHE, refer to `www.ihe.net <http://www.ihe.net/>`_. It is strongly recommended that,
prior to reading this volume, the reader familiarizes themselves with the concepts defined in the 
`IHE Technical Frameworks General Introduction <https://profiles.ihe.net/GeneralIntro/index.html>`_.

1.2 Intended Audience
---------------------
The intended audience of IHE Technical Frameworks Volume 2 is:

• IT departments of healthcare institutions
• Developers and technical staff of vendors participating in the IHE initiative
• Experts involved in standards development

1.3 Overview of Technical Framework Volume 2
--------------------------------------------
Volume 2 is comprised of several distinct sections:
  
• Section 1 provides background and reference material.
• Section 2 presents the conventions used in this volume to define the transactions.
• Section 3 defines Dental transactions in detail, specifying the roles for each actor, the standards employed, the information exchanged, and in some cases, implementation options for the transaction.
• The appendices provide clarification of technical details of the IHE data model and transactions.

For a brief overview of other Technical Framework Volumes (TF-1, TF-3), please see
the IHE Technical Frameworks General Introduction, `Section 5 - Structure of the IHE Technical
Frameworks <https://profiles.ihe.net/GeneralIntro/ch-5.html>`_.

1.4 Comment Process
-------------------
*TO DO: specify here how this will work in for Dental profile text.*

1.5 Copyright Licenses
----------------------
IHE technical documents refer to, and make use of, a number of standards developed and
published by several standards development organizations. Please refer to the IHE Technical
Frameworks General Introduction, `Section 9 - Copyright Licenses <https://profiles.ihe.net/GeneralIntro/ch-9.html>`_ for copyright license
information for frequently referenced base standards. Information pertaining to the use of IHE
International copyrighted materials is also available there.

1.6 Trademark
-------------
IHE® and the IHE logo are trademarks of the Healthcare Information Management Systems
Society in the United States and trademarks of IHE Europe in the European Community. Please
refer to the IHE Technical Frameworks General Introduction, `Section 10 - Trademark <https://profiles.ihe.net/GeneralIntro/ch-10.html>`_ for
information on their use.

1.7 Disclaimer Regarding Patent Rights
--------------------------------------
Attention is called to the possibility that implementation of the specifications in this document
may require use of subject matter covered by patent rights. By publication of this document, no
position is taken with respect to the existence or validity of any patent rights in connection
therewith. IHE International is not responsible for identifying Necessary Patent Claims for which
a license may be required, for conducting inquiries into the legal validity or scope of Patents
Claims or determining whether any licensing terms or conditions provided in connection with
submission of a Letter of Assurance, if any, or in any licensing agreements are reasonable or
non-discriminatory. Users of the specifications in this document are expressly advised that
determination of the validity of any patent rights, and the risk of infringement of such rights, is
entirely their own responsibility. Further information about the IHE International patent
disclosure process including links to forms for making disclosures is available at
http://www.ihe.net/Patent_Disclosure_Process. Please address questions about the patent
disclosure process to the secretary of the IHE International Board: secretary@ihe.net.

1.6 History of Document Changes
-------------------------------

.. list-table::
    :header-rows: 1

    * - **Date**
      - **Document Revision**
      - **Change Summary**
    * - TBD
      - TBD
      - TBD

2 Conventions
=============
This document has adopted the following conventions for representing the framework concepts
and specifying how the standards upon which the IHE Technical Framework is based shall be
applied.

2.1 Transaction Modeling and Profile Conventions
------------------------------------------------
In order to maintain consistent documentation, modeling methods for IHE transactions and510
profiling conventions for frequently used standards are maintained in the IHE Technical
Frameworks General Introduction, `Appendix E - Standards Profiling and Documentation
Conventions <https://profiles.ihe.net/GeneralIntro/ch-E.html>`_. Methods described include the Unified Modeling Language (UML) and standards
conventions include DICOM, HL7 v2.x, HL7 Clinical Document Architecture (CDA)
Documents, etc. These conventions are critical to understanding this volume and should be515
reviewed prior to reading this text.

2.2 Use of Coded Entities and Coding Schemes
--------------------------------------------
Where applicable, coding schemes required by the DICOM ®, HL7®, LOINC®, and SNOMED®
standards are used in IHE Profiles. In the cases where such resources are not explicitly identified
by standards, implementations may utilize any resource (including proprietary or local) provided
any licensing/copyright requirements are satisfied.

3 IHE Dental Transactions
=========================
This section defines each transaction in detail, specifying the standards used, and the information
transferred.

.. toctree::
	:glob:
	:maxdepth: 1

	*/index
