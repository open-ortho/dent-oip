Volume 2 - Transactions
=======================

This document is Volume 2 of the Dentistry Orthodontic Imaging Profile
(DENT-OIP), which is being developed as an ADA/ANSI standard. It defines the
transactions used by the Orthodontic Imaging Profile (OIP).

DENT-OIP uses an IHE-compatible organization and section numbering to simplify
possible future conversion into an IHE Profile.

**Contents**

+ :ref:`Section 1 - Introduction to Volume 2 <introduction_to_volume_2>`
+ :ref:`Section 2 - Conventions <conventions>`
+ :ref:`Section 3 - Transactions <oip_transactions>`
+ :ref:`Section 3.1 - Display Visible Light Images [DEN-1] <den_1>`

.. _introduction_to_volume_2:

1 Introduction to Volume 2
==========================

1.1 Introduction to IHE
-----------------------
Integrating the Healthcare Enterprise (IHE) is an international initiative
that promotes standards-based interoperability among health information
technology systems. IHE provides a forum for care providers, developers, and
other stakeholders to reach consensus on solutions to interoperability issues.

IHE publishes implementation guides called IHE Profiles through public review
and trial implementation, and incorporates profiles that reach Final Text into
domain Technical Frameworks. DENT-OIP is not currently an IHE Profile or part
of an IHE Technical Framework. It follows IHE-compatible organization and
conventions to support possible future conversion into an IHE Profile.

For general information and definitions of IHE framework concepts referenced
by this standard, see the `IHE Technical Frameworks General Introduction
<https://profiles.ihe.net/GeneralIntro/index.html>`_.

1.2 Intended Audience
---------------------
The intended audience for Volume 2 of DENT-OIP includes:

- IT departments of healthcare institutions, where available
- Developers and technical staff of vendors
- Experts involved in standards development

1.3 Overview of Volume 2
------------------------
Volume 2 comprises the following sections:

- Section 1 provides background and reference material.
- Section 2 presents the conventions used to define transactions.
- Section 3 defines DENT-OIP transactions, including actor roles, referenced
  standards, information exchanged, and implementation requirements.

Volume 1 defines the OIP actors, options, and process flows. Volume 3 defines
the DICOM content and constraints referenced by the transactions in this
volume.

1.4 Comment Process
-------------------

The American Dental Association welcomes comments on this document during the
public review process. Once the standard is published, if someone would like to
propose a revision, they can contact standards@ada.org.


1.6 Trademarks
--------------
The following trademarks are referenced in this document:

- DICOM® is the registered trademark of the National Electrical Manufacturers
  Association for its standards publications relating to digital
  communications of medical information.
- HL7® and CDA® are registered trademarks of Health Level Seven International.
- IHE® and the IHE logo are trademarks of the Healthcare Information
  Management Systems Society in the United States and of IHE Europe in the
  European Community.
- LOINC® is a registered United States trademark of Regenstrief Institute,
  Inc.
- SNOMED CT® is a registered trademark of the International Health Terminology
  Standards Development Organisation (IHTSDO), trading as SNOMED
  International.

Use of these marks does not imply endorsement of DENT-OIP by their owners.

1.7 Disclaimer Regarding Patent Rights
--------------------------------------
Attention is called to the possibility that implementation of this standard
may require the use of subject matter covered by patent rights. This document
does not take a position on the existence or validity of any patent rights.
Implementers are responsible for determining whether licenses are required and
for assessing the risk of infringement. Questions about patent disclosures for
this ADA/ANSI standards project may be sent to standards@ada.org.

1.8 History of Document Changes
-------------------------------

This section is reserved for the publication history of a future IHE Profile.
No IHE revisions currently exist.

.. _conventions:

2 Conventions
=============
This document uses the following conventions to represent OIP concepts and to
specify how referenced standards are applied.

2.1 Transaction Modeling and Profile Conventions
------------------------------------------------
To provide consistent transaction specifications and simplify possible future
conversion into an IHE Profile, DENT-OIP adopts applicable modeling and
documentation conventions from the `IHE Technical Frameworks General
Introduction, Appendix E - Standards Profiling and Documentation Conventions
<https://profiles.ihe.net/GeneralIntro/ch-E.html>`_. These include the Unified
Modeling Language (UML) and conventions for applying standards such as DICOM,
HL7 v2.x, and HL7 Clinical Document Architecture (CDA). Implementers should
review the cited conventions when interpreting transaction diagrams and
requirements in this volume.

2.2 Use of Coded Entities and Coding Schemes
--------------------------------------------
Where applicable, DENT-OIP uses coding schemes required by DICOM®, HL7®,
LOINC®, and SNOMED CT®. When neither a base standard nor DENT-OIP explicitly
identifies a coding resource, implementations may use a proprietary or local
resource, provided that applicable licensing and copyright requirements are
satisfied.

.. _oip_transactions:

3 OIP Transactions
==================
This section defines each transaction in detail, specifying the standards used, and the information
transferred.

.. _den_1:

3.1 Display Visible Light Images [DEN-1]
----------------------------------------
3.1.1 Scope
~~~~~~~~~~~
This transaction is used to present DICOM VL Photographic Image IOD
instances to a dental professional for clinical review. It applies to
individual visible light photographs and collections of photographs,
including extraoral and intraoral photographs.

The Image Display is required to support viewsets VS-01 through VS-04 as
baseline standardized layouts. These required viewsets do not restrict the
transaction to those layouts; the transaction may also be used to present
other visible light photographs and viewsets.

Radiographic images, including intraoral radiographs, panoramic
radiographs, and cone beam computed tomography data, are outside the scope
of this transaction.

The VL Photographic Image IOD instances rendered in this transaction are
produced by an OIP Content Creator actor supporting the
:ref:`DEN TF-1: 3.2.1 Direct Photography Option
<direct_photography_option>`.

This transaction is not a typical network-based transaction between two devices; instead, the primary focus of the requirements is on the behavior of the display application rather than messaging between two actors. This can be thought
of as an “informational transaction” between a display device and a user.

Methods that the Display uses to select and obtain the data to be displayed are outside the scope of this transaction.

The Display may have behaviors in addition to those required by this transaction.

3.1.2 Actor Roles
~~~~~~~~~~~~~~~~~
The roles in this transaction are defined in the following table and may be played by the actors shown here:

**Table 3.1.2-1: Actor Roles**

.. list-table::
    :header-rows: 0

    * - **Role**
      - Display:
           Presents results visually to a user.

    * - **Actor(s)**
      - The following actors may play the role of Display:
           Image Display

3.1.3 Referenced Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~
+ `ANSI/ADA Standard No. 1100, Rev. July 2025, "Dentistry - 2D and 3D
  Orthodontic/Cranial/Forensic Photographic Views and View Sets"
  <https://webstore.ansi.org/standards/ada/ansiada11002025>`_

3.1.4 Messages
~~~~~~~~~~~~~~

.. figure:: ../images-static/Figure_3.1.4-1_InteractionDiagram.png
    :class: with-border with-shadow float-left
    :align: center

**Figure  3.1.4-1 Interaction Diagram**

3.1.4.1 Display Results
+++++++++++++++++++++++
The Display presents one or more DICOM studies to the user.

3.1.4.1.1 Trigger Events
^^^^^^^^^^^^^^^^^^^^^^^^
A user or an automated function determines that one or more studies should be presented.

3.1.4.1.2 Message Semantics
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The DICOM VL Photographic Image IODs are encoded as described in :ref:`DEN TF-3: 7.3.1 VL Photographic Image IOD Definition <vl_photographic_image_iod_definition>`.

This transaction does not depend on how the DICOM images were transferred to the Display. If the Display
receives results by a profiled mechanism such as DICOM C-STORE, the messaging protocol is specified in that corresponding transaction. If results are accessed by being grouped with another actor such as a Content Consumer or an Image Manager / Image Archive, there is no messaging protocol involved.

3.1.4.1.3 Expected Actions (i.e., Display Requirements)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The behaviors in this section are specified as baseline capabilities.  Displays may have additional or alternate capabilities that may be invoked or configured.

Displays shall support the capabilities described in this section for DICOM images encoded in instances of the following:

* VL Photographic Image IOD as defined in :ref:`DEN TF-3: 7.3.1 VL Photographic Image IOD Definition <vl_photographic_image_iod_definition>.

3.1.4.1.3.1 General Display Requirements
****************************************

For each displayed VL Photographic Image IOD instance, the Image Display shall
display, in association with that instance:

- the human-readable image type specified in :ref:`Section 7.4.2.1.1
  <view_code_sequence>`; and
- Image Comments (0020,4000), when present, as specified in :ref:`Section
  7.4.1.7 <general_image>`.

The displayed information shall not obscure clinically relevant image content.

3.1.4.1.3.2 Viewset VS-01
*************************
VS-01 (from DICOM correction package 1571) is the template preferred by the ABO for Case Submission and Display. It is the viewset most commonly used by orthodontic practitioners and vendors of orthodontic software.

The Display shall be able to display for the user Viewset VS-01, with eight images and one text box, as defined in **ANSI/ADA Standard No. 1100**, Section 10.

3.1.4.1.3.3 Viewset VS-02
*************************
VS-02 is a custom craniofacial viewset has greatest use for documentation of orthognathic and craniofacial surgery treatment.

The Display shall be able to display for the user Viewset VS-02, with 13 views as defined in **ANSI/ADA Standard No. 1100**, Section 10.

3.1.4.1.3.4 Viewset VS-03
*************************
VS-03 is a custom supplementary patient record display, presents specific views commonly requested by insurance companies for documentation of automatic qualifiers (such as excessive overjet or impinging deep bite).

The Display shall be able to display for the user Viewset VS-03, with 13 image boxes as defined in **ANSI/ADA Standard No. 1100**, Section 10.

3.1.4.1.3.5 Viewset VS-04
*************************
VS-04 is a custom supplementary patient record display, was designed to facilitate assessment of craniofacial asymmetries.

The Display shall be able to display for the user Viewset VS-04, with 12 image boxes as defined in **ANSI/ADA Standard No. 1100**, Section 10.
