3.4.2 Use Cases for Orthodontic Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADA Technical Report No. 1065 "Use Cases of the Orthodontic Electronic Health Record" contains use cases that describe orthodontic workflows, both imaging and non-imaging. Within 1065, Use Case No. 03 specifically addresses the creation of digital orthodontic records, which includes the imaging workflows. ADA Standard No. 1100 "Dentistry - 2D and 3D Orthodontic/Craniofacial/Forensic Photographic Views and Viewsets" is specific for visible light images.

Please refer to the original ADA documents for more details on the use cases
in Sections 3.4.2.1 through 3.4.2.3. Sections 3.4.2.4 and 3.4.2.5 describe
additional DENT-OIP scenarios for reusable display templates and saved
patient-specific presentations.

.. note::

   Sections 3.4.2.4 and 3.4.2.5 are draft use cases awaiting working-group
   approval. They were developed during the review of Structured Display
   and Hanging Protocol behavior and the Display Configuration Creator
   actor tracked in issue 55.

3.4.2.1 ADA TR 1065 Use Case No. 03 - Creating Digital Orthodontic Records
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This use case outlines both direct and indirect workflows for creating digital orthodontic records, either through direct capture with imaging devices or by digitizing analog records. It details how acquired images and models are tagged with standard metadata and integrated into the patient’s EHR for proper storage and retrieval. The process supports efficient transformation between digital and analog formats for clinical applications such as 3D printing.
3.4.2.2 ADA 1100 Use Case No. 2.1 - Routine Orthodontic Photography Workflow
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    """
    A routine set of facial and intraoral photographs is ordered by the
    practitioner. A suitable view set is chosen in the practitioner's software
    application. The practitioner and photographer may not be the same person.
    The software prompts the specifications of each photograph in sequence and
    the photographer acquires and uploads each image by means of a conventional
    camera or mobile phone. The software labels the image and creates the
    desired view set out of the individual images.
    """

3.4.2.3 ADA 1100 Use Case No. 2.2 - Referral and Image Transfer Workflow
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    """
    The practitioner orders a referral of the patient to a colleague for
    evaluation and selects clinically relevant information including certain
    extraoral and intraoral photographs in the electronic health record. The
    referring practitioner's software manages the transmission of the
    information and the individual photographs labelled with the naming codes
    described in this white paper. The receiving computer in the colleague's
    office accepts the photographs and files the transmitted photographs into an
    alternate view set preferred by the colleague. Thus, the colleague's
    software receives photographs identical to those present in the referring
    office but presents them in a different display without the need for a human
    to view the individual files and sort them.
    """

The receiving practitioner may review the photographs using their own
preferred template, as described in :ref:`Section 3.4.2.4
<shared_display_template_use_case>`. The sender may also provide a saved
patient-specific presentation so that the recipient can reproduce the
sender's arrangement, as described in :ref:`Section 3.4.2.5
<saved_patient_presentation_use_case>`.

.. _shared_display_template_use_case:

3.4.2.4 Using the Same Display Template Across Applications
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clinical Scenario
^^^^^^^^^^^^^^^^^

Dr. Patel reviews orthodontic photographs in her imaging software. She
chooses a pre-programmed display template based on VS-01 for both initial
and progress photographs and customizes it to suit her practice.

Her practice management software also supports image review. When she opens
the photograph viewer for a patient there, the photographs appear using the
same template she selected in the imaging software. She does not need to
configure the layout again or manually sort the photographs. Changes to her
saved template can likewise be made available to both applications.

Technical Realization
^^^^^^^^^^^^^^^^^^^^^

Either application may create or update the shared template as a DICOM
Hanging Protocol instance. The protocol is stored in a central DICOM
repository, such as a PACS or medical imaging management and processing
system (MIMPS), accessible to both applications.

Each application's Image Display uses the protocol's selection and
presentation rules to arrange the applicable patient images. The protocol
preserves reusable preferences rather than a fixed selection of images
from one patient.

The four required ADA 1100 viewsets, VS-01 through VS-04, provide baseline
layouts. They do not limit the additional arrangements that display
templates may support.

This scenario illustrates shared access to display configuration. This
revision of DENT-OIP does not prescribe the repository or the network
transactions used to store and obtain the protocol.

.. _saved_patient_presentation_use_case:

3.4.2.5 Preserving and Sharing a Patient-Specific Presentation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

A patient-specific presentation may be generated from a reusable template
or created from scratch. The following sub-use cases distinguish these two
creation paths; both produce a presentation that can be archived or shared
with its selected photographs.

3.4.2.5.1 Generating a Presentation from a Display Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Clinical scenario**

Dr. Patel prepares an orthognathic referral. She opens the patient's
photographs using her usual display template and selects the treatment
timepoint or acquisition date. The software automatically populates the
presentation with the corresponding facial and intraoral photographs in
the order specified by the template.

She reviews the populated presentation and saves it in the patient's record
for sharing with the consulting surgeon. She does not need to select and
position each photograph manually.

**Technical realization**

The application applies a DICOM Hanging Protocol to the images for the
selected patient and timepoint. Its selection and presentation rules
determine the image instances and their arrangement. The application then
saves the resulting patient-specific presentation as a DICOM Basic
Structured Display instance, recording the layout and references to the
selected image instances.

The Structured Display records the result of applying the protocol to this
patient's images. It does not require the recipient to obtain or reapply
the originating Hanging Protocol.

3.4.2.5.2 Creating a Presentation from Scratch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Clinical scenario**

For another referral, Dr. Patel wants to highlight changes in a patient's
facial asymmetry that are not readily shown by her usual templates. She
starts with an empty presentation, selects particular photographs from
the initial and progress records, and places them side by side in the
order she wants the consulting surgeon to review them.

She saves this case-specific presentation in the patient's record for
sharing. She does not need to create or modify a reusable template for
this one case.

**Technical realization**

The application creates a DICOM Basic Structured Display instance directly
from the clinician's image selection and arrangement. It records references
to those particular image instances and their positions in the presentation.
This creation path does not require a Hanging Protocol.

3.4.2.5.3 Archiving and Sharing the Saved Presentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Clinical scenario**

In either case, Dr. Patel sends the saved presentation and its photographs
to the consulting surgeon. When the surgeon opens it, the selected
photographs appear in the arrangement Dr. Patel intended, without requiring
the surgeon to reconstruct it. Dr. Patel can also reopen the same
presentation later as part of the archived referral record.

The surgeon can separately arrange the photographs using their own
preferred template for further review.

**Technical realization**

The Structured Display and its referenced VL Photographic Image instances
are preserved and made available together for archiving or sharing. The
receiving Image Display uses the Structured Display to reproduce the
recorded arrangement using the referenced images, rather than a flattened
composite image of the presentation.

The required ADA 1100 viewsets provide baseline layouts without limiting
other patient-specific presentations. Storage and transfer mechanisms
remain outside the scope of this revision.
