Use Cases for Orthodontic Images
=================================================

The uses cases below refer to the use cases listed in  ADA Technical Report No. 1065 for Use Cases of the Orthodontic Electronic Health Record, and is limited to those involving orthodontic imaging. Please refer to the ADA Technical Report for more details on each use case.

ADA Standard No. 1100 "Dentistry - 2D and 3D Orthodontic/Craniofacial/Forensic Photographic Views and Viewsets" also contains two use cases that are relevant to orthodontic imaging.

Creating Digital Orthodontic Records
-------------------------------------------------

From ADA TR 1065 Use Case No. 03 - Creating Digital Orthodontic Records:

This use case outlines both direct and indirect workflows for creating digital orthodontic records, either through direct capture with imaging devices or by digitizing analog records. It details how acquired images and models are tagged with standard metadata and integrated into the patient’s EHR for proper storage and retrieval. The process supports efficient transformation between digital and analog formats for clinical applications such as 3D printing. 


.. note::
   The following use cases are based on ADA Standard No. 1100 and may be outdated. Please refer to the latest release of ADA1100 for the most current information.

Routine Orthodontic Photography Workflow (ADA1100 Use Case No. 2.1)
---------------------------------------------------------------------

    """
    A routine set of facial and intraoral photographs is ordered by the practitioner. A suitable
    view set is chosen in the practitioner's software application. The practitioner and
    photographer may not be the same person. The software prompts the specifications of each
    photograph in sequence and the photographer acquires and uploads each image by means
    of a conventional camera or mobile phone. The software labels the image and creates the
    desired view set out of the individual images.
    """

Referral and Image Transfer Workflow (ADA1100 Use Case No. 2.2)
------------------------------------------------------------------

    """
    The practitioner orders a referral of the patient to a colleague for evaluation and selects
    clinically relevant information including certain extraoral and intraoral photographs in the
    electronic health record. The referring practitioner's software manages the transmission of
    the information and the individual photographs labelled with the naming codes described in
    this white paper. The receiving computer in the colleague's office accepts the photographs
    and files the transmitted photographs into an alternate view set preferred by the colleague.
    Thus, the colleague's software receives photographs identical to those present in the
    referring office but presents them in a different display without the need for a human to view
    the individual files and sort them.
    """