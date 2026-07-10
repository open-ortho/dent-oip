.. _oip_actors_transactions:

3.1 OIP Actors, Transactions, and Content Modules
-------------------------------------------------
This section defines the actors, transactions, and/or content modules in this profile. General definitions of actors are given in the Technical Frameworks General Introduction Appendix A. IHE Transactions can be found in the Technical Frameworks General Introduction Appendix B. Both appendices are located at https://profiles.ihe.net/GeneralIntro/index.html.

Figure 3.1-1 shows the actors directly involved in the OIP Profile. 

A product implementation using this profile may group actors from this profile with actors from a separate workflow or transport profile specify how images are exchanged between actors. 

.. figure:: ../../images-static/Figure_X.1-1_OIPActorDiagram.png
    :class: with-border with-shadow float-left
    :align: center

**Figure  3.1-1 OIP Actor Diagram**

Table 3.1-1 lists the transactions content module(s) defined in the OIP Profile. To claim support with this profile, an actor shall support all required content modules (labeled “R”) and may support optional content modules (labeled “O”). 

**Table 3.1-1 OIP Actors, Transactions, and Content Modules**

.. list-table::
    :header-rows: 1

    * - **Actors**
      - **Content Modules**
      - **Transactions**
      - **Optionality**
      - **Reference**
    * - Content Creator & Content Consumer
      - VL Photographic Image IOD Definition
      - --
      - R
      - DEN TF-3: 7.3.1
    * - Image Display
      - --
      - Display Visible Light Images [DEN-1]
      - R
      - DEN TF-2: 3.1
    * -
      - Structured Display IOD Definition
      - --
      - O *(Note 1)*
      - DEN TF-3: 7.3.2
    * -
      - Hanging Protocol IOD Definition
      - --
      - O *(Note 1)*
      - DEN TF-3: 7.3.3

*Note 1:* Structured Display and Hanging Protocol support are optional capabilities for the Image Display actor. See Section 3.2 for the corresponding options.

3.1.1 Actor Description and Actor Profile Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Most requirements are documented in DEN: TF-2: Transactions and DEN TF-3: Content Modules. This section documents any additional requirements on profile’s actors.

.. _content_creator_actor:

3.1.1.1 Content Creator
+++++++++++++++++++++++
In the OIP profile, the Content Creator is a system that acquires or converts visible light photographic images and encodes them as VL Photographic Image IODs compliant with the requirements in DEN TF-3: 7.3.1 of this profile.

In the 'real-world', an OIP Content Creator actor may be:

+ A DICOM-compliant camera, smartphone app, or imaging workstation that directly acquires and creates VL Photographic Image DICOM objects while a patient is present.

+ A system or software that interfaces to a non-DICOM ready device (e.g., a conventional SLR camera or a smartphone with a generic photo app) in order to integrate that device into dental care workflows by creating DICOM VL Photographic Image output compliant with this profile.

+ A system or software that converts existing contents of a non-DICOM archive into VL Photographic Image IODs compliant with this profile.

.. _content_consumer_actor:

3.1.1.2 Content Consumer
++++++++++++++++++++++++
In the OIP profile, the Content Consumer is a 'generic' actor for a system that consumes DICOM objects (e.g., images, movies, 3D models) that are compliant with the requirements in DEN TF-3: 7.3.x of this profile.   Using these DICOM objects, Content Consumer performs functions that are relevant to its application, e.g., rendering the images for a user, storing the DICOM objects in an archive, extracting information from the DICOM metadata for reporting purposes, etc.

.. _display_actor:

3.1.1.3 Image Display
+++++++++++++++++++++
The Image Display is a specialized Content Consumer that implements standardized display requirements to ensure consistent, clinically meaningful presentation of orthodontic photographs. ANSI/ADA Standard No. 1100 defines the viewsets (VS-01 through VS-04) and the associated layout expectations that clinical users rely on for assessment and treatment planning. The goal of the Image Display actor is to guarantee that any OIP-compliant viewer renders these viewsets in a predictable, standardized way regardless of vendor.

An Image Display actor in the OIP Profile shall implement all display requirements in DEN TF-2: 3.1.4.1.3. This provides mandatory support for Viewsets VS-01, VS-02, VS-03, and VS-04 as defined in ANSI/ADA Standard No. 1100 "Dentistry - 2D and 3D Orthodontic/Cranial/Forensic Photographic Views and View Sets".

An Image Display actor that supports the Structured Display Option or Hanging Protocol Option shall support the corresponding Basic Structured Display IOD or Hanging Protocol IOD as defined in DEN TF-3: 7.3.2 and 7.3.3, respectively, to exchange standardized viewset layouts and hanging protocol definitions aligned with ANSI/ADA Standard No. 1100.

