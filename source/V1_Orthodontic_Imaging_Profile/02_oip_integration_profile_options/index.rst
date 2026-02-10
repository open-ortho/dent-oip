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
      - Structured Display Option
      - Section 3.2.7
    * - 
      - Hanging Protocol Option
      - Section 3.2.8

*Note 1:* The Content Creator shall support at least one option.

.. _direct_photography_option:

3.2.1 Direct Photography Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Visible Light Option applies to direct photography (visible light imaging) in orthodontics.  

A Content Creator that supports this option shall be able to acquire 2D photographs and create DICOM images that are compliant with the requirements in DEN TF-3: 7.3.1 VL Photographic Image IOD Definition. 

.. _direct_motion_picture_option:

3.2.2 Direct Motion Picture Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Direct Motion Picture Option applies to devices that capture motion picture, movies, and/or video in orthodontics.  

A Content Creator that supports this option shall be able to acquire 2D photographs and create DICOM images that are compliant with the requirements in DEN TF-3: 7.3.2 Video Photograpic Image IOD Definition.  

.. _3d_scan_for_appliances_option:

3.2.3 3D Scan for Appliances Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The 3D Scan Option applies to for aligners and study models needed to produce orthodontic appliances. These are surfaces produced by devices and systems (M3D), where the data comes from different tools, for example treatment planning, or orthodontic appliance design for production/manufacturing.

A Content Creator that supports this option shall be able to create DICOM images that are compliant with the requirements in DEN TF-3: 7.3.3 Encapsulated 3D Manufacturing Model IOD Definition.

.. _3d_intraoral_extraoral_scan_option:

3.2.4 3D Intraoral / Extraoral Scan Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The 3D Intraoral / Extraoral Scan Option applies to devices that capture 3D intraoral or extraoral surface scans directly from a patient

A Content Creator that supports this option shall be able to create DICOM images that are compliant with the requirements in DEN TF-3: 7.3.4 Surface Scan Mesh IOD Definition.

.. _true_color_scan_option:

3.2.5 True Color Scan Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The True Color Scan Option applies devices that scan film, negatives, or positive photographs.  
A Content Creator that supports this option shall be able to create DICOM images that are compliant with the requirements in DEN TF-3: 7.3.5 Multi-frame True Color Secondary Capture Image IOD Definition.

.. _scanned_radiographs_option:

3.2.6 Scanned Radiographs Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The 2D Scan Option applies to scanners that generate a digitized image of a film emulsion radiograph (cephalograms, bytewings, intraoral radiographs, panos, or other body parts, e.g., hand-wrist).   

A Content Creator that supports this option shall be able to create DICOM objects that are compliant with the requirements in DEN TF-3: 7.3.6  Secondary Capture Image IOD Definitions with a Modality type of OSS.

.. _structured_display_option:

3.2.7 Structured Display Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A Structured Display DICOM Object represents a standard method of encoding and exchanging a specific presentation layout of single screen that has been created for a Patient.  The Structured Display can be exchanged with images to allow for complete reproduction of the original exam.   See `DICOM PS3.17: Section OO.1.1 <https://dicom.nema.org/medical/dicom/current/output/html/part17.html#sect_OO.1.1>`_ for Informative Structured Display Use Cases for Dentistry.

DICOM Structured Display which enables a user to arrange a specific presentation layout of single screen that has been created for a Patient.  

An Image Display that supports the Structured Dislay Option shall be able to create a Basic Structured Display IOD, as defined in `DICOM PS3.3 Section A.33.5.3 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.33.5.3>`_ , to specify an Instance of a single screen structured display that has been created for a Patient. 

An Image Display that supports the Structured Dislay Option shall be able to:
  + consume a Basic Structured Display IOD and the associated DICOM images, and
  + render for the user a static presentation that shows the layout of the screen the exactly as specified in the Basic Structured Display IOD.

.. _hanging_protocol_option:

3.2.8 Hanging Protocol Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A Hanging Protocol is a specialized DICOM Information Object Definition (IOD) that defines the initial display arrangement of medical images on one or more display systems. It allows for the specification of how images should be positioned, sized, annotated, and organized when initially displayed to a user.

Unlike the :ref:`Basic Structured Display <structured_display_option>`, which defines a static presentation that contains references to specific image instances, Hanging Protocols provide instructions for the initial layout and the generic types of images that should be placed in the specific areas or boxes. 
 
Hanging Protocols are useful in clinical workflows where specific viewing configurations are preferred for different examination types or specialties.

Hanging Protocols are particularly valuable:

* when a system allows the user to customize the display of images, this customization can be saved as a Hanging Protocol, exported and re-imported in different systems, allowing the clinicians to preserve their preferred display settings, without having to re-configure the display on the new system;
* when a practice is using more than one system that requires the visualization of images and allows the user to customize the display, the Hanging Protocol can be used transferred and synchronized between the systems to ensure that the images are displayed in the same way on all systems, without requiring the user to re-configure the display on each system.

The Hanging Protocol DICOM IOD works in conjunction with display systems to streamline image interpretation and enhance workflow efficiency, providing a standardized presentation that can be applied to any image set.

An Image Display that supports the Hanging Protocol Option shall be able to create a Hanging Protocol IOD, as defined in `DICOM PS3.3 Section A.44.3 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.44.3>`_, to specify the creator of the display, the type of Study it addresses, the type of image sets to display, the intended display environment, and the intended layout for the screen(s).

An Image Display that supports the Hanging Protocol Option shall be able to:
  + consume a Hanging Protocol IOD and the associated DICOM images, and
  + render for the user an initial presentation that shows the layout of the images the exactly as specified in the Hanging Protocol IOD
  + enable the user to interact with the images in the display.

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



