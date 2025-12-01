.. _oip_integration_profile_options:

X.2 OIP Profile Options
=======================

Options that may be selected for each actor in this profile, if any, are listed in the Table X.2-1. Dependencies between options, when applicable, are specified in notes.

**Table X.2-1: OIP Profile Actors and Options**

.. list-table::
    :header-rows: 1

    * - **Actor**
      - **Option Name**
      - **Reference**
    * - Content Creator *(Note 1)*
      - A Option
      - Section X.2.1
    * - 
      - B Option
      - Section X.2.2
    * - 
      - C Option
      - Section X.2.3
    * - Content Consumer
      - No options defined
      - --
    * - Image Display
      - No options defined
      - --

*Note 1:* The Content Creator shall support at least one option.

X.2.1 A Option
--------------
The A Option applies to photography (visible light imaging) in orthodontics  A Content Creator that supports this option shall be able to acquire 2D photographs and create DICOM images that are compliant with the requirements in DEN TF-3: 7.3.1 VL Photographic Image IOD Definition.  <TO DO: list IODs here>

X.2.2 B Option
--------------
A Content Creator that supports the A Option shall be able to acquire 3D intraoral scans and create DICOM images that are compliant with the requirements in DEN TF-3: 7.a.y.  <TO DO: list IODs here>

X.2.3 C Option
--------------
A Content Creator that supports the A Option shall be able to generate scanned documents or generate scanned photographs from negatives or from paper and create DICOM objects that are compliant with the requirements in DEN TF-3: 7.a.y..  <TO DO: list IODs here>

X.3 OIP Required Actor Groupings
===============================
An actor from this profile (Column 1) shall implement all of the required transactions and/or content modules in this profile in addition to all of the requirements for the grouped actor (Column 2).

.. list-table::
    :header-rows: 1

    * - **OIP Actor**
      - **Profile/Actor(s) to be Grouped With**
      - **Reference**
    * - Content Creator
      - None
      - 
    * - Content Consumer
      - None
      - 
    * - Image Display
      - OIP / Content Consumer
      - Section X.1.1.2

Section X.5 describes some optional groupings that may be of interest for security considerations and Section X.6 describes some optional groupings in other related profiles.

*X.2 OIP Profile Options (to be moved to a future version of the profile...)*
============================================================================
*<<Discuss with Toni:  It is possible that you will want no options; however, the following shows one model for what it might look like if you wanted to introduce into your profile a step beyond 'content only', i.e. an actor could **choose** to implement one of these options (or not) to offer enhanced capabililities.   (the other model would be to introduce actual transactions into the profile as mandatory, which I don't think you want to do).*

Options that may be selected for each actor in this profile, if any, are listed in the Table X.2-1. Dependencies between options, when applicable, are specified in notes.

**Table X.2-1: OIP Profile Actors and Options**

.. list-table::
    :header-rows: 1

    * - **Actor**
      - **Option Name**
      - **Reference**
    * - Content Creator
      - Modality Worlist Option
      - Section X.2.1
    * - 
      - DICOM Storage Option
      - Section X.2.2
    * - Content Consumer
      - DICOM Storage Option
      - Section X.2.2


X.2.1 Modality Worklist Option
------------------------------
The Modality Worklist Option enables a Content Creator to use DICOM Modality Worklist to query for patient and order information from a Department System Scheduler/Order Filler and map the patient and order details into the DICOM image IODs it creates. 

A Content Creator that supports the Modality Worklist Option shall support the IHE RAD Query Modality Worklist [RAD-5] transaction (RAD TF-2: 4.5) in the Role of Acquisition Modality, i.e., it is able to support the DICOM Basic Worklist Management Service as an SCU.  Note that this includes all requirements in RAD TF-2: 4.5.4.1.2 Message Semantics and RAD TF-2: 4.5.4.1.2.2 Matching and Return Keys.  

*<<Discuss with Toni: rqmts for display of return keys on the SCU>>*

X.2.2 DICOM Storage Option
--------------------------
The DICOM Storage Option enables a Content Creator and Content Consumer to DICOM C-STORE to send and receive DICOM images compliant with the profile.

A Content Creator that supports the DICOM Storage Option shall support the IHE RAD Store Instances [RAD-8] transaction (RAD TF-2: 4.50) in the Role of sender, i.e., it is able to support DICOM Storage Service as an SCU.  

*<<Discuss with Toni:  would you like to pull in the requirements in RAD TF-2: 4.8.4.1.1.1 Study and Series UIDs ??>>*

*<<Discuss with Toni:  You may want mandate support for a *one of* a list of supported IODs here>>*

A Content Consumer that supports the DICOM Storage Option shall support the IHE RAD Store Instancess [RAD-50] transaction (RAD TF-2: 4.50) in the Role of Responder, i.e., it is able to support DICOM Storage Service as an SCP.

*<<Discuss with Toni:  You may want mandate support for a list of supported IODs here>>*


