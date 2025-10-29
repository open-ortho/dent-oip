.. _oip_actors_transactions:

OIP Actors, Transactions, and Content Modules
=============================================
This section defines the actors, transactions, and/or content modules in this profile. General definitions of actors are given in the Technical Frameworks General Introduction Appendix A. IHE Transactions can be found in the Technical Frameworks General Introduction Appendix B. Both appendices are located at https://profiles.ihe.net/GeneralIntro/index.html.

Figure X.1-1 shows the actors directly involved in the OIP Profile and the direction that the content is exchanged. 
A product implementation using this profile may group actors from this profile with actors from a workflow or transport profile to be functional. The grouping of the content module described in this profile to specific actors is described in more detail in Required Actor Groupings Section X.6 or in Cross Profile Considerations Section X.6.


Table X.1-1 lists the content module(s) defined in the <Profile Acronym> Profile. To claim support with this profile, an actor shall support all required content modules (labeled “R”) and may support optional content modules (labeled “O”). 

.. list-table::
    :header-rows: 1

    * - Actors
      - Content Modules
      - Optionality
      - Reference
    * - Content Creator
      - <Content Module Name>
      - R
      - DEN TF-3: 6.x.x
    * - Content Consumer
      - <Content Module Name>
      - R
      - DEN TF-3: 6.x.x

X.1.1 Actor Description and Actor Profile Requirements
======================================================
Most requirements are documented in DEN: TF-3 T Content Modules. This section documents any additional requirements on profile’s actors.

Content Creator
---------------
In the OIP profile, the Content Creator is a 'generic' actor for a system that creates DICOM images that are compliant with the requirements in DEN TF-3: 6.x.c of this profile.   In the 'real-world' an OIP Content Creator actor may be:

==> Acquisition Modality -- A system that acquires and creates medical images while a patient is present. A modality may also create other evidence objects such as Grayscale Softcopy Presentation States for the consistent viewing of images or Evidence Documents containing measurements, etc. In orthodontic care, modalities acquire diagnostic information such as images and/or evidence documents. Some examples of these may include still visible light photography, visible light motion picture with audio, radiographs, etc.

==> Acquisition Modality Importer -- A system that interfaces to a non-DICOM ready modality in order to integrate that modality into dental care workflows.

Department System Scheduler/Order Filler
----------------------------------------

A department-based system that provides functions related to the management of orders received from external systems or through the department system's user interface. A dental or orthodontic example of a department based system could be a dental Practice Management System (PMS). 

