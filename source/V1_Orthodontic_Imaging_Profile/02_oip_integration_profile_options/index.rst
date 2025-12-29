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
      - Visible Light Option
      - Section X.2.1
    * - 
      - 3D Scanning Option
      - Section X.2.2
    * - 
      - 2D Scanning Option
      - Section X.2.3
    * - 
      - Scanned Radiograph Option
      - Section X.2.4
    * - Content Consumer
      - No options defined
      - --
    * - Image Display
      - Structured Dislay Option
      - Section X.2.5
    * - 
      - Hanging Protocol Option
      - Section X.2.6

*Note 1:* The Content Creator shall support at least one option.

<*DISCUSS: (1) Confirm/adjust the list of Creator options and the DICOM scope of each.   (2) Determine whether there should be options for the Content Consumer, or whether a Consumer that is compliant with this profile shalle be able to 'process' the types of images in all of the options*>

<*DISCUSS: This revision of the table proposes Options on the Display for support of Structured Display and Hanging Protocol.

X.2.1 Visible Light Option
-----------------------------
The Visible Light Option applies to photography (visible light imaging) in orthodontics.  

A Content Creator that supports this option shall be able to acquire 2D photographs and create DICOM images that are compliant with the requirements in DEN TF-3: 7.3.1 VL Photographic Image IOD Definition.  

X.2.2 3D Scanning Option
-----------------------------
The 3D Scanning Option Option applies to devices that acquire 3D intraoral surfaces.  

A Content Creator that supports this ption shall be able to acquire 3D intra-oral and extra-oral scans and create DICOM images that are compliant with the requirements in DEN TF-3: 7.3.2  

A Content Creator that supports this option shall be able to create one or more of these DICOM IODs:

+ Encapsulated STL IOD with Modality of M3D
+ Encapsulated OBJ IOD with Modality of M3D
+ Encapsulated MTL IOD with Modality of M3D

X.2.3 2D Scanning Option
------------------------
The 2D Scanning Option applies to scanners that generate scanned documents or generate scanned photographs from negatives or from paper.  

A Content Creator that supports this option shall be able to create DICOM objects that are compliant with the requirements in DEN TF-3: 7.3.3 

A Content Creator that supports this option shall be able to create:

+ Secondary Capture IOD with Modality of XC

X.2.4 Scanned Radiograph Option
-------------------------------
The Scanned Radiograph Option applies to scanners thatenerate higher quality medical-grade scanned radiographs from 2D film (cephalograms, bytewings, intraoral radiographs, panos, or other body parts).   

A Content Creator that supports this shall be able to create DICOM objects that are compliant with the requirements in DEN TF-3: 7.3.4 

A Content Creator that supports this option shall be able to create:

+ Secondary Capture IOD with Modality of OSS

X.2.5 Structured Display Option
-------------------------------
A Structured Display DICOM Object represents a standard method of encoding and exchanging a specific presentation layout of single screen that has been created for a Patient.  The Structured Display can be exchanged with images to allow for complete reproduction of the original exam.   See DICOM PS3.17: Section OO.1.1 for Informative Structured Display Use Cases for Dentistry.

DICOM Structured Display which enables a user to arrange a specific presentation layout of single screen that has been created for a Patient.  

An Image Display that supports the Structured Dislay Option shall be able to create a Basic Structured Display IOD, as defined in DICOM PS3.3 Section A.33.5.3, to specify an Instance of a single screen structured display that has been created for a Patient. 

An Image Display that supports the Structured Dislay Option shall be able to:
  + consume a Basic Structured Display IOD and the associated DICOM images, and
  + render for the user a static presentation that shows the layout of the screen the exactly as specified in the Basic Structured Display IOD.

X.2.6 Hanging Protocol Option
-----------------------------
A Hanging Protocol DICOM Object  defines the initial display arrangement of medical images on one or more display systems. It allows for the specification of how images should be positioned, sized, annotated, and organized when initially displayed to a user, while allowing users to subsequently manipulate and interact with the images.

An Image Display that supports the Hanging Protocol Option shall be able to create a Hanging Protocol IOD, as defined in DICOM PS3.3 Section A.44.3, to specify he creator of the display, the type of Study it addresses, the type of image sets to display, the intended display environment, and the intended layout for the screen(s).

An Image Display that supports the Hanging Protocol Option shall be able to:
  + consume a Hanging Protocol IOD and the associated DICOM images, and
  + render for the user an initial presentation that shows the layout of the images the exactly as specified in the Hanging Protocol IOD
  + enable the user to interact with the images in the display.

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


