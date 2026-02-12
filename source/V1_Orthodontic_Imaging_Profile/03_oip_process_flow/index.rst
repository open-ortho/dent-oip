.. _oip_process_flow:

3.4 OIP Overview
----------------
The Orthodontic Imaging Profile ... *TO DO:  Provide a short intro to concepts here*

3.4.1 Concepts
~~~~~~~~~~~~~~
This section provides an overview of the concepts that provide necessary background for understanding the profile.

3.4.1.1 Orthodontic Progress (Informative)
++++++++++++++++++++++++++++++++++++++++++

During orthodontic treatment, it is common for providers to monitor progress by regularly collecting records such as photographs or intra-oral surface scans [provide reference]. Identifying the timing of these records in relation to the treatment is crucial. Specifically, the provider needs to know if, at the time of acquisition, the patient:

- was undergoing treatment (progress photos)
- had never undergone treatment before (observation/pretreatment photos)
- had completed treatment (posttreatment photos)

Orthodontic photograph progress shall be stored in three key areas:

- Longitudinal Temporal Event Type (Registration, Treatment, Posttreatment)
- Longitudinal Temporal Offset From Event (in days)
- Study Description; see Section 3.4.1.2

Table 3.4.1.1-1 provides a reference for translating orthodontic progress into codesets that DICOM can understand.

.. _progress_codes:
.. list-table:: **Table 3.4.1.1-1 Orthodontic Progress Code Mapping**
    :header-rows: 1

    * - orthodontic progress
      - description
      - event type
      - offset (days)
    * - First Time Observation
      - Patient has just registered with the practice for the first time and has not agreed any treatment yet. The provider collects first time records.
      - SCT-184047000 Patient registration
      - 0
    * - Observation
      - Patient comes back for regular visits. The provider collects observation records.
      - SCT-184047000 Patient registration
      - Number of days past the day the patient registers.
    * - Pretreatment
      - Images acquired before treatment starts. Only used when the patient and doctor have agreed to start a treatment. This should be treated as Observation above.
      - See Observation
      - See Observation
    * - Initial
      - Patient and provider agreed to start treatment. Records are taken to mark the Baseline for comparison with treatment progress.
      - SCT-1332161000 Orthodontic Treatment started
      - 0
    * - Progress
      - Images taken during treatment.
      - SCT-1332161000 Orthodontic Treatment started
      - Number of days past the day the treatment started.
    * - Final
      - Image taken at the end of active treatment (after appliance removal, if applicable). Sequence number is not required.
      - SCT-1340210007 Orthodontic Treatment stopped
      - 0
    * - Posttreatment
      - Image acquired after treatment.
      - SCT-1340210007 Orthodontic Treatment stopped
      - Number of days past the day the treatment ended (see Final above).


**Note:**  Distinguishing Pretreatment from Observation is not always straightforward. In some cases, there may be a clear Pretreatment definition by the provider, which could be properly coded in the practice management system. However, in many other cases, it may not be clearly defined, or what was considered Pretreatment might not lead to treatment.  Consequently, the orthodontic domain experts of the working group have decided to disregard Pretreatment status and consider it as Observation.

3.4.1.2 Study Description (0008,1030)
+++++++++++++++++++++++++++++++++++++

This optional DICOM tag, part of the General Study module, can contain a Long String (up to 64 characters). In the context of orthodontic photographs, the *Study Description* is used to represent treatment progress as defined above.

Most PACS systems display the *Study Description* in search results when listing studies after a query. Therefore, it is recommended to include the information from the Concept Codes described in :ref:`longitudinal_temporal_event_type` and :ref:`longitudinal_temporal_offset_from_event` here, in a more human-readable form. For example, you might choose a *Study Description* based on progress names defined by the main practice management system used by the practice that initially acquired the photographs. Examples include:

- Pre-treatment 1
- Initial
- Progress 12
- Final

.. note::
    - The *Study Description* is typically used by the medical provider who treats the patient and acquires the images.
    - Other software may also use the *Study Description*. But with the limit of 64 characters, it is advisable to keep the string under 16 characters to allow other systems to append their own text.
    - When importing images from other institutions, the *Study Description* may not be relevant to the receiving practice.
    - The *Study Description* is *not* a reliable tag for ensuring interoperability across systems and institutions.
    - For reliable interoperability, refer to *Acquisition Context* codes as defined in :ref:`longitudinal_temporal_event_type` and :ref:`longitudinal_temporal_offset_from_event`.


3.4.1.3 Image Views/Request Procedure Codes
++++++++++++++++++++++++++++++++++++++++++++

Orthodontic photographs are typically taken in a standardized manner to ensure
consistent and comparable results. The American Dental Association (ADA) has
published a standard, ADA Standard No. 1100, which defines the views that could
be taken for orthodontic photographs. These views are referred to as *Image
Views* in that standard. However, in DICOM, these views are best represented as
*Scheduled Protocol Codes*.

The orthodontic provider needs to be able to programmatically distinguish the
different types of images, in order to compare them both with other images of
the same series and over time to monitor treatment progress. While the types of
images can be defined by their anatomical and other view type tags in DICOM,
saving a coded version of the name of the type of image along with the image is
useful both for human readability and for developers who need to
programmatically process the images. When and if a code is available, that one
can be used to identify the image (if known).

There is a distinction between the anatomical and view information defined in
the DICOM tags and the type of image: the anatomical and view information is
used to define what is in the image, while the type of image is used to define
what the original intention of that image was. The image type code is therefore
well suited to be used as a protocol for a scheduled procedure, and represents
what the provider has scheduled before the acquisition of the image. Then, once
the photograph is taken, the DICOM tags are used to define what was actually
taken. The resulting DICOM image would thus contain both the scheduled protocol
code, as well as the anatomical and view information in the DICOM tags. In the
domain of orthodontics, these two should, for the vast majority of cases, match.

When the provider schedules for an appointment, once the patient has arrived for
that appointment, the practice management system can trigger the generation of a
DICOM Modality Worklist, and populate it with the scheduled procedure codes. The
imaging device can then use this information to pre-populate the fields in the
DICOM image, including the scheduled procedure code. This code can then be used
to identify the type of image that was taken.

Within the DICOM IOD (the DICOM image), the Scheduled Procedure Code Sequence
(0040,0008) is contained within the Requested Attributes Sequence (0040,0275),
in the General Series Module. Therefore, it cannot be used to define a specific
type of image (instance). Instead, it must contain all the views that are part
of the same series. This is because the Scheduled Procedure Code Sequence is
shared by all instances in the series. Then Instance Number (0020,0013), which
is part of the General Image module, is used to differentiate between the
different views in the series.

In the orthodontic domain, it is expected for the photographs to be taken in a
specific sequence in order to optimize the workflow. This order can be defined
in the Scheduled Procedure Code Sequence, such that image acquisition devices
(such as DICOM enabled cameras) can present the operator with the images in the
same order. Once the image is acquired, the Instance Number, a unique integer
for each image in the series, can be used to preserve the same order as the on
in the Requested Procedure Code Sequence. See :ref:`instance_number` for more
information.

3.4.2 Use Cases for Orthodontic Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADA Technical Report No. 1065 "Use Cases of the Orthodontic Electronic Health Record" contains use cases that describe orthodontic workflows, both imaging and non-imaging. Within 1065, Use Case No. 03 specifically addresses the creation of digital orthodontic records, which includes the imaging workflows. ADA Standard No. 1100 "Dentistry - 2D and 3D Orthodontic/Craniofacial/Forensic Photographic Views and Viewsets" is specific for visible light images.

Please refer to the original ADA documents for more details on each use case.

3.4.2.1 ADA TR 1065 Use Case No. 03 - Creating Digital Orthodontic Records
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This use case outlines both direct and indirect workflows for creating digital orthodontic records, either through direct capture with imaging devices or by digitizing analog records. It details how acquired images and models are tagged with standard metadata and integrated into the patient’s EHR for proper storage and retrieval. The process supports efficient transformation between digital and analog formats for clinical applications such as 3D printing. 


.. note::
   *The use cases in Sections 3.4.2.2 and 3.4.2.3 are based on ADA Standard No. 1100 and may be outdated. Please refer to the latest release of ADA 1100 for the most current information.*

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
