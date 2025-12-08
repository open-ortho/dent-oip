.. _oip_actors_transactions:

X.1 OIP Actors, Transactions, and Content Modules
=================================================
This section defines the actors, transactions, and/or content modules in this profile. General definitions of actors are given in the Technical Frameworks General Introduction Appendix A. IHE Transactions can be found in the Technical Frameworks General Introduction Appendix B. Both appendices are located at https://profiles.ihe.net/GeneralIntro/index.html.

Figure X.1-1 shows the actors directly involved in the OIP Profile. 

A product implementation using this profile may group actors from this profile with actors from a workflow or transport profile to be functional. The grouping of the content module described in this profile to an Image Display actor is described in Section X.1.1.3.

.. figure:: ../../images-static/Figure_X.1-1_OIPActorDiagram.jpg
    :class: with-border with-shadow float-left
    :align: center

**Figure  X.1-1 OIP Actor Diagram**

Table X.1-1 lists the transactions content module(s) defined in the OIP Profile. To claim support with this profile, an actor shall support all required content modules (labeled “R”) and may support optional content modules (labeled “O”). 

**Table X.1-1 OIP Actors, Transactions, and Content Modules**

.. list-table::
    :header-rows: 1

    * - **Actors**
      - **Content Modules**
      - **Transactions**
      - **Optionality**
      - **Reference**
    * - Content Creator
      - VL Photographic Image IOD Definition
      - --
      - R
      - DEN TF-3: 7.3.1 
    * - Content Consumer
      - VL Photographic Image IOD Definition
      - --
      - R
      - DEN TF-3: 7.3.1
    * - Image Display
      - --
      - Display OIP Images [DEN-1]
      - R
      - DEN TF-2: 3.1

X.1.1 Actor Description and Actor Profile Requirements
------------------------------------------------------
Most requirements are documented in DEN: TF-2: Transactions and DEN TF-3: Content Modules. This section documents any additional requirements on profile’s actors.

X.1.1.1 Content Creator
~~~~~~~~~~~~~~~~~~~~~~~
In the OIP profile, the Content Creator is a 'generic' actor for a system that creates DICOM images that are compliant with the requirements in DEN TF-3: 7.3.1 of this profile.   

In the 'real-world' an OIP Content Creator actor may be:

+ *Acquisition Modality* -- A system that acquires and creates medical images while a patient is present; this includes, for example, devices such as cameras or interoral scanners.  A modality may also create other evidence objects such as Grayscale Softcopy Presentation States for the consistent viewing of images or Evidence Documents containing measurements, etc.  In orthodontic care, modalities acquire diagnostic information such as images and/or evidence documents. Some examples of these may include still visible light photography, visible light motion picture with audio, radiographs, etc.

+ *Acquisition Modality Importer* -- A system that interfaces to a non-DICOM ready modality in order to integrate that modality into dental care workflows.

To identify which type(s) of DICOM images that a system supports, the Content Creator shall support one or more of the Options in Table X.2-1.

X.1.1.2 Content Consumer
~~~~~~~~~~~~~~~~~~~~~~~~
In the OIP profile, the Content Consumer is a 'generic' actor for a system that consumes DICOM images that are compliant with the requirements in DEN TF-3: 7.3.1 of this profile.   Using the DICOM images, Content Consumer performs functions that are relevant to its application, e.g., rendering the images for a user, storing the images in an archive, extracting information from the DICOM images for reporting purposes, etc.

<*DISCUSS:   A common pattern is for a Consumer to support all of the variations of content that a Content Creator can produce (following a pattern of Clients can choose, Servers support all).   Alternatively, you could choose to introduce Options as we are doing the the Creator to enable a Content Consumer to declare (in its product documentation) which types of content it supports.=*>

X.1.1.3 Image Display
~~~~~~~~~~~~~~~~~~~~~
The Image Display is a specialized Content Consumer that implements requirements to provide standardized display functionality to ensure *<TO DO: Describe to goal of standardized display requirements here.   You may want to point to the ADA spec driving these requirements.>*

An Image Display in the OIP Profile shall implement all display requirements in DEN TF-2: 3.1.4.1.3.  This provides mandatory support for Viewsets VS-01, VS-02, VS-03, and VS-04 as defined in ANSI/ADA Standard No. 1100 "Dentistry - 2D and 3D Orthodontic/Cranial/Forensic Photographic Views and View Sets".

An Image Display may optionally support Standard Display and/or the Hanging Protocol.  See Table X.2-1.



