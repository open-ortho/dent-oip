.. _oip_integration_profile_options:

3.2 OIP Profile Options
-----------------------

Options that may be selected for each actor in this profile, if any, are listed in the Table 3.2-1. Dependencies between options, when applicable, are specified in notes.

**Table 3.2-1: OIP Profile Actors and Options**

.. list-table::
    :header-rows: 1

    * - **Actor**
      - **Option Name**
      - **Reference**
    * - Content Creator *(Note 1)*
      - Direct Photography Option
      - Section 3.2.1
    * - 
      - Direct Motion Picture Option
      - Section 3.2.2
    * - 
      - 3D Scan for Appliances Option
      - Section 3.2.3
    * - 
      - 3D Intraoral / Extraoral Scan Option
      - Section 3.2.4
    * - 
      - True Color Scan Option
      - Section 3.2.5
    * - 
      - Scanned Radiograph Option
      - Section 3.2.6
    * - Content Consumer
      - No options defined
      - --
    * - Image Display
      - No options defined
      - --

*Note 1:* The Content Creator shall support at least one option.

.. toctree::
    :maxdepth: 1

    direct_photography_option
    direct_motion_picture_option
    3d_scan_for_appliances_option
    3d_intraoral_extraoral_scan_option
    true_color_scan_option
    scanned_radiographs_option

3.3 OIP Required Actor Groupings
--------------------------------
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
      - Section 3.1.1.2

Section 3.6 describes some optional groupings in other related profiles.

*x.2 OIP Profile Options (to be moved to a future version of the profile...)*
-----------------------------------------------------------------------------
*<<Discuss with Toni:  Ehe following shows one model for what it might look like if you wanted to introduce into your profile a step beyond 'content only', i.e. an actor could **choose** to implement one of these options (or not) to offer enhanced capabililities.   (the other model would be to introduce actual transactions into the profile as mandatory, which I don't think you want to do).*

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Modality Worklist Option enables a Content Creator to use DICOM Modality Worklist to query for patient and order information from a Department System Scheduler/Order Filler and map the patient and order details into the DICOM image IODs it creates. 

A Content Creator that supports the Modality Worklist Option shall support the IHE RAD Query Modality Worklist [RAD-5] transaction (RAD TF-2: 4.5) in the Role of Acquisition Modality, i.e., it is able to support the DICOM Basic Worklist Management Service as an SCU.  Note that this includes all requirements in RAD TF-2: 4.5.4.1.2 Message Semantics and RAD TF-2: 4.5.4.1.2.2 Matching and Return Keys.  

*<<Open Issue:  Determine rqmts for display of return keys on the SCU>>*

X.2.2 DICOM Storage Option
~~~~~~~~~~~~~~~~~~~~~~~~~~
The DICOM Storage Option enables a Content Creator and Content Consumer to DICOM C-STORE to send and receive DICOM images compliant with the profile.

A Content Creator that supports the DICOM Storage Option shall support the IHE RAD Store Instances [RAD-50] transaction (RAD TF-2: 4.50) in the Role of sender, i.e., it is able to support DICOM Storage Service as an SCU.  The Content Creator stores DICOM instances associated with the options it supports; see Table 3.2-1: OIP Profile Actors and Options.

A Content Consumer that supports the DICOM Storage Option shall support the IHE RAD Store Instancess [RAD-50] transaction (RAD TF-2: 4.50) in the Role of Responder, i.e., it is able to support DICOM Storage Service as an SCP.  The Content Consumer shall support storing all DICOM IODs associated with the OIP profile:

- VL Photographic Image IOD
- Video Photographc IOD
- Encapsulated 3D Manufacturing Model IOD
- Surface Scan Mesh IOD
- Multi-frame True Secondary Capture IOD
- Secondary Capture IOD
