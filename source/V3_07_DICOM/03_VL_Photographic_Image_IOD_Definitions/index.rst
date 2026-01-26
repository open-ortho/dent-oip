.. _iod_definitions:

7.3 IOD Definitions
===================
This section contains DICOM (Information Object Defintion) IOD specifications referenced in profiles of the IHE Dental domain.  

+ :ref:`vl_photographic_image_iod_definition`
+ :ref:`video_photographic_image_iod_definition`
+ :ref:`encapsulated_3d_manufacturing_model_iods_definition`
+ :ref:`surface_scan_mesh_iod_definition`
+ :ref:`multi-frame_true_color_secondary_capture_mage_iod_definition`
+ :ref:`secondary_capture_image_iod_definition`

Each IOD definition contains a table that identifies Modules comprising the IOD, including the baseline Modules requirements defined in DICOM, and Modules where requirements are extended by Dental domain profiles.  

In Column 4 of the tables below, the values of **M**, **U**, and **C** for 'Usage' are defined in `DICOM PS3.3: A.1.3 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.1.3>`_.  

In Column 5, these additional 'Usage' values are defined:

- **R** - The Module is defined as Conditional (C) or User Option (U) in DICOM; however, this Requirement is an IHE extension of the DICOM requirements, and the Module shall be present.
- **RC** - The Module is defined as Conditional (C) or User Option (U) in DICOM; however, this requirement is an IHE extension of the DICOM requirements, and the Module shall be present when the specified conditions apply.

.. _vl_photographic_image_iod_definition:

7.3.1 VL Photographic Image IOD Definition
+++++++++++++++++++++++++++++++++++++++++++

This normative section contains a description of the DICOM tags which are
necessary to fully describe orthodontic views (photographs) and to request for these photographs to be taken (acquired).

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

The baseline requirements for the VL Photographic Image IOD are defined in `DICOM PS3.3: A.32.4.3 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.32.4.3>`_ .  In Table 7.3.1-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements.   

*<Discuss:  This profile defines many constraints on the modules listed in this table.   In Col 5, add a reference to the section containing those constraints (otherwise, a quick glance at this table implies, for example, that there is no difference between DICOM and OIP for the General Study, Patient, Acquisition Context, etc modules, which is not the case)>* 

.. list-table:: **Table 7.3.1-1 - IHE constraints on DICOM Modules for VL Photographic Image IODs**
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - OIP Profile Usage
   * - Patient
     - Patient
     - C.7.1.1
     - M
     - M 

       See Section 7.4.1.1
   * - 
     - Clinical Trial Subject
     - C.7.1.3
     - U
     - U
   * - Study
     - General Study
     - C.7.2.1
     - M
     - M

       See Section 7.4.1.2
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - U

       See Section 7.4.1.3
   * - 
     - Clinical Trial Study
     - C.7.2.3
     - U
     - U
   * - Series
     - General Series
     - C.7.3.1
     - M
     - M

       See Section 7.4.1.4
   * - 
     - Clinical Trial Series
     - C.7.3.2
     - U
     - U
   * - Equipment
     - General Equipment
     - C.7.5.1
     - M
     - M

       See Section 7.4.1.5
   * - 
     - VL Photographic Equipment
     - C.8.12.10
     - U
     - U
   * - Acquisition
     - General Acquisition
     - C.7.10.1
     - M
     - M
   * - Image
     - General Image
     - C.7.6.1
     - M
     - M 

       See Section 7.4.1.7
   * - 
     - General Reference
     - C.12.4
     - U
     - U
   * - 
     - Image Pixel
     - C.7.6.3
     - M
     - M
   * - 
     - Acquisition Context
     - C.7.6.14
     - M
     - M

       See Section 7.4.x
   * - 
     - Device
     - C.7.6.12
     - U
     - RC

       See Section 7.4.x
   * - 
     - Specimen
     - C.7.6.22
     - C - Required if Imaging Subject is a specimen
     - C
   * - 
     - VL Image
     - C.8.12.1
     - M
     - M

       See Section 7.4.x
   * - 
     - VL Photographic Acquisition
     - C.8.12.11
     - U
     - R

       See Section 7.4.x
   * - 
     - VL Photographic Geolocation
     - C.8.12.12
     - U
     - U

7.3.1.1 VL Photographic Image IOD Acquisition Requirements
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Reference:**  <question for Toni:  Where did these requirement originate?>

#. Each DICOM *Study* SHALL represent a specific orthodontic progress (rather than necessarily an orthodontic visit). The same *Study* SHALL NOT span across multiple visits, or multiple progresses.

#. Each DICOM *Series* SHALL represent a specific photographic capturing session. In an orthodontic visit (one during which photographs are captured), a set of intra-oral and extra-oral photographs are usually taken in a single session, considered as a unit. Such unit is best represented as a DICOM Series.

#. If during the orthodontic visit the photograph acquisition session is split between intra-oral and extra-oral, the intra-oral session SHALL Be portrayed as one DICOM Series and the extra-oral as another DICOM Series, as long as they are both part of the same DICOM Study (i.e. visit), 

#. Intra-oral and extra-oral photographs MAY be part of the same Series, as long as they represent the same clinical context. DICOM Series SHALL portray a single clinical context. 

#. When two separate acquisition devices (cameras) are used (as could easily happen, since EVs are usually captured with the patient standing and a special background to prevent shadows, while the IVs are often taken with the patient on the chair), the Series SHOULD be part of the same Study (Study with the same Study Instance UID). The camera SHOULD get the Study Instance UID from the Modality Work List (coming from the practice management software), and both series would therefore be part of the same Study. 

#. In the case in which Modality Worklists are not impleented, each camera MAY produce a new Study Instance UID, as long as it is properly tagged with the *Orthodontic Progress*, date and Acession Number.

#. When two progresses are collected during the same orthodontic visit (the practice might acquire a set of images just before removing braces, and another set just after removing braces during the same patient encounter), the software shall create two separate DICOM Studies, one for each progress. Each progress is distinguished by making use of the :ref:`Acquisition Context Module <acquisition_context>`

.. _video_photographic_image_iod_definition:

7.3.2 Video Photograpic Image IOD Definition 
++++++++++++++++++++++++++++++++++++++++++++

This normative section contains a description of the DICOM tags which are
necessary to capture motion picture, movies, and/or video in orthodontics.

The baseline requirements for Video Photographic Image IODs are defined in `DICOM PS3.3: A.32.7.3 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.32.7.3>`_ . In Table 7.3.2-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

.. list-table:: **Table 7.3.2-1 - IHE constraints on DICOM Modules for Video Photograpic Image IODs**
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - OIP Profile Usage
   * - Patient
     - Patient
     - C.7.1.1
     - M
     - M 

       See Section 7.4.1.1
   * - 
     - Clinical Trial Subject
     - C.7.1.3
     - U
     - U
   * - Study
     - General Study
     - C.7.2.1
     - M
     - M

       See Section 7.4.1.2
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - U

       See Section 7.4.1.3
   * - 
     - Clinical Trial Study
     - C.7.2.3
     - U
     - U
   * - Series
     - General Series
     - C.7.3.1
     - M
     - M

       See Section 7.4.1.4
   * - 
     - Clinical Trial Series
     - C.7.3.2
     - U
     - U
   * - Frame of Reference
     - Synchronization
     - C.7.4.2
     - U
     - U
   * - Equipment
     - General Equipment
     - C.7.5.1
     - M
     - M 

       See Section 7.4.1.5
   * - Acquisition
     - General Acquisition
     - C.7.10.1
     - M
     - M
   * - Image
     - General Image
     - C.7.6.1
     - M
     - M 

       See Section 7.4.1.7
   * - 
     - General Reference
     - C.12.4
     - U
     - U
   * - 
     - Cine
     - C.7.6.5
     - M
     - M
   * - 
     - Multi-frame
     - C.7.6.6
     - M
     - M
   * - 
     - Image Pixel
     - C.7.6.3
     - M
     - M
   * - 
     - Acquisition Context
     - C.7.6.14
     - M
     - M

       See Section 7.4.x
   * - 
     - Device
     - C.7.6.12
     - U
     - U

       See Section 7.4.x
   * - 
     - Specimen
     - C.7.6.22
     - C - Required if Imaging Subject is a specimen
     - C
   * - 
     - VL Image
     - C.8.12.1
     - M
     - M

       See Section 7.4.x
   * - 
     - ICC Profile
     - C.11.15
     - U
     - U
   * - 
     - SOP Common
     - C.12.1
     - M
     - M
   * - 
     - Common Instance Reference
     - C.12.2
     - U
     - U
   * - 
     - Frame Extraction
     - C.12.3
     - C - Required if the SOP Instance was created in response to a Frame-Level retrieve request
     - C

.. _encapsulated_3d_manufacturing_model_iods_definition:

7.3.3 Encapsulated 3D Manufacturing Models IODs Definition
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The baseline requirements for Encapsulated 3D Manufacturing Model IODs are defined in `DICOM PS3.3: A.85 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.85>`_ , specifially:

+ **Encapsulated STL IOD** in `DICOM PS3.3: A.85.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.85.1>`_ - The Encapsulated STL IOD describes a 3D model in Stereolithography (STL) format that has been encapsulated within a DICOM Information Object.
+ **Encapsulated OBJ IOD** in `DICOM PS3.3: A.85.2 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.85.2>`_ - The Encapsulated OBJ IOD describes a 3D model in OBJ format. *(Note:  Any supporting material library file (MTL) and supporting 2D texture map image files are addressed in other DICOM IODs..)*
+ **Encapsulated MTL IOD** in `DICOM PS3.3: A.85.3 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.85.3>`_ . The Encapsulated MTL IOD describes in MTL format a materials library used by an Encapsulated OBJ 3D model (see `DICOM PS3.3: A.85.2.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.85.2.1>`_).

The IOD Module requirements are the same for all 3 of these IODs.  In Table 7.3.3-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

.. list-table:: **Table 7.3.3-1 - IHE constraints on DICOM Encapsulated 3D Manufacturing Model IODs**
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - OIP Profile Usage
   * - Patient
     - Patient
     - C.7.1.1
     - M
     - M 

       See Section 7.4.1.1
   * - 
     - Clinical Trial Subject
     - C.7.1.3
     - U
     - U
   * - Study
     - General Study
     - C.7.2.1
     - M
     - M

       See Section 7.4.1.2
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - U

       See Section 7.4.1.3
   * - 
     - Clinical Trial Study
     - C.7.2.3
     - U
     - U
   * - Series
     - Encapsulated Document Series
     - C.24.1
     - M
     - M
   * - 
     - Clinical Trial Series
     - C.7.3.2
     - U
     - U
   * - Frame of Reference
     - Frame of Reference
     - C.7.4.1
     - M
     - M
   * - Equipment
     - General Equipment
     - C.7.5.1
     - M
     - U

       See Section 7.4.1.5
   * - 
     - Enhanced General Equipment
     - C.7.5.2
     - M
     - M
   * - Encapsulated Document
     - Encapsulated Document 
     - C.24.2
     - M
     - M
   * - 
     - Manufacturing 3D Model
     - C.35.1
     - M
     - M
   * - 
     - ICC Profile
     - C.11.14
     - U
     - U
   * - 
     - SOP Common
     - C.12.1
     - M
     - M
   * - 
     - Common Instance Reference
     - C.12.1
     - C - Required if other Instances are referenced
     - C
   * - Acquisition *<note:  currently not in DICOM; needed before including this IOD in the profile>*
     - Acquisition Context 
     - C.7.6.14
     - X
     - M  -  See Section 7.4.x


7.3.3.1 Additional Encoding Requirements
++++++++++++++++++++++++++++++++++++++++

If any...to be determined...

.. _surface_scan_mesh_iod_definition:

7.3.4 Surface Scan Mesh IOD Definition
+++++++++++++++++++++++++++++++++++++++

This normative section contains a description of the DICOM tags which are
necessary to capture 3D intraoral or extraoral surface scans directly from a patient.

The baseline requirements for Surface Scan Mesh IODs are defined in `DICOM PS3.3: A.68 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.68>`_ . In Table 7.3.4-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

.. list-table:: **Table 7.3.4-1 - IHE constraints on DICOM Modules for Surface Scan Mesh IODs**
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - OIP Profile Usage
   * - Patient
     - Patient
     - C.7.1.1
     - M
     - M 

       See Section 7.4.1.1
   * - 
     - Clinical Trial Subject
     - C.7.1.3
     - U
     - U
   * - Study
     - General Study
     - C.7.2.1
     - M
     - M

       See Section 7.4.1.2
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - U

       See Section 7.4.1.3
   * - 
     - Clinical Trial Study
     - C.7.2.3
     - U
     - U
   * - Series
     - General Series
     - C.7.3.1
     - M
     - M

       See Section 7.4.1.4
   * - 
     - Clinical Trial Series
     - C.7.3.2
     - U
     - U
   * - 
     - Optical Surface Scanner Series
     - C.8.29.2
     - M
     - M
   * - Frame of Reference
     - Frame of Reference
     - C.7.4.1
     - M
     - M
   * - Equipment
     - General Equipment
     - C.7.5.1
     - M
     - M

       See Section 7.4.1.5
   * - 
     - Enhanced General Equipment
     - C.7.5.2
     - M
     - M
   * - Surface
     - Surface Mesh
     - C.27.1
     - M
     - M
   * - 
     - UV Mapping
     - C.27.6
     - U
     - U
   * - 
     - Scan Procedure
     - C.8.29.2
     - M
     - M
   * - 
     - Specimen
     - C.7.6.22
     - U
     - U
   * - 
     - SOP Common
     - C.12.1
     - M
     - M

7.3.4.1 Additional Encoding Requirements
++++++++++++++++++++++++++++++++++++++++

If any...to be determined...

.. _multi-frame_true_color_secondary_capture_mage_iod_definition:

7.3.5 Multi-frame True Color Secondary Capture Image IOD Definition
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This normative section contains a description of the DICOM tags which are
necessary to capture scan film, negatives, or positive photographs. 

The baseline requirements for Multi-frame True Color Secondary Capture Image IODs are defined in `DICOM PS3.3: A.68 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.8.5>`_ . In Table 7.3.5-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

.. list-table:: **Table 7.3.5-1 - IHE constraints on DICOM Modules for Multi-frame True Color Secondary Capture IODs**
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - OIP Profile Usage
   * - Patient
     - Patient
     - C.7.1.1
     - M
     - M 

       See Section 7.4.1.1
   * - 
     - Clinical Trial Subject
     - C.7.1.3
     - U
     - U
   * - Study
     - General Study
     - C.7.2.1
     - M
     - M

       See Section 7.4.1.2
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - U

       See Section 7.4.1.3
   * - 
     - Clinical Trial Study
     - C.7.2.3
     - U
     - U
   * - Series
     - General Series
     - C.7.3.1
     - M
     - M

       See Section 7.4.1.4
   * - 
     - Clinical Trial Series
     - C.7.3.2
     - U
     - U
   * - Frame of Reference
     - Frame of Reference
     - C.7.4.1
     - C - Required if Pixel Measures or Plane Position (Patient) or Plane Orientation (Patient) Functional Group Macros Present
     - C
   * - 
     - Synchronization
     - C.7.4.2
     - U
     - U
   * - Equipment
     - General Equipment
     - C.7.5.1
     - M
     - M

       See Section 7.4.1.5
   * - 
     - SC Equipment
     - C.8.6.1
     - M
     - M
   * - Image
     - General Image
     - C.7.6.1
     - M
     - M

       See Section 7.4.1.7
   * - 
     - General Reference
     - C.12.4
     - U
     - U
   * - 
     - Cine
     - C.7.6.5
     - C - Required if Frame Increment Pointer (0028,0009) is Frame Time (0018,1063) or Frame Time Vector (0018,1065)
     - C
   * - 
     - Multi-frame
     - C.7.6.6
     - M
     - M
   * - 
     - Frame Pointers
     - C.7.6.9
     - U
     - U
   * - 
     - Device
     - C.7.6.12
     - U
     - U

       See Section 7.4.x
   * - 
     - Multi-frame Functional Groups
     - C.7.6.16
     - U
     - U
   * - 
     - Multi-frame Dimension
     - C.7.16.7
     - U
     - U
   * - 
     - Specimen
     - C.7.6.22
     - U
     - U
   * - 
     - SC Image
     - C.8.6.2
     - U
     - U
   * - 
     - SC Multi-frame Image
     - C.8.6.3
     - M
     - M
   * - 
     - ICC Profile
     - C.11.15
     - U
     - U
   * - 
     - SOP Common
     - C.12.1
     - M
     - M
   * - 
     - Common Instance Reference
     - C.12.2
     - U
     - U
   * - 
     - Frame Extraction
     - C.12.3
     - C - Required if the SOP Instance was created in response to a Frame-Level retrieve request
     - C

.. _secondary_capture_image_iod_definition:

7.3.6 Secondary Capture Image IOD Definition
++++++++++++++++++++++++++++++++++++++++++++

This normative section contains a description of the DICOM tags which are necessary to capture scanned study models or other body parts (i.e. face)

The baseline requirements for Secondary Capture Image IODs are defined in `DICOM PS3.3: A.8.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.8.1>`_ . In Table 7.3.6-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

.. list-table:: **Table 7.3.6-1 - IHE constraints on DICOM Modules for Secondary Capture Image IODs**
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - OIP Profile Usage
   * - Patient
     - Patient
     - C.7.1.1
     - M
     - M 

       See Section 7.4.1.1
   * - 
     - Clinical Trial Subject
     - C.7.1.3
     - U
     - U
   * - Study
     - General Study
     - C.7.2.1
     - M
     - M

       See Section 7.4.1.2
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - U

       See Section 7.4.1.3
   * - 
     - Clinical Trial Study
     - C.7.2.3
     - U
     - U
   * - Series
     - General Series
     - C.7.3.1
     - M
     - M

       See Section 7.4.1.4
   * - 
     - Clinical Trial Series
     - C.7.3.2
     - U
     - U
   * - Frame of Reference
     - Frame of Reference
     - C.7.4.1
     - C - Required if Image Position (Patient) (0020,0032) or Image Orientation (Patient) (0020,0037) are present. May be present otherwise.
     - C
   * - 
     - Synchronization
     - C.7.4.2
     - U
     - U
   * - Equipment
     - General Equipment
     - C.7.5.1
     - U
     - U

       See Section 7.4.1.5
   * - 
     - SC Equipment
     - C.8.6.1
     - M
     - M
   * - Acquisition
     - General Acquisition
     - C.7.10.1
     - M
     - M
   * - Image
     - General Image
     - C.7.6.1
     - M
     - M

       See Section 7.4.1.7
   * - 
     - General Reference
     - C.12.4
     - U
     - U
   * - 
     - Enhanced Patient Orientation
     - C.7.6.30
     - U
     - U
   * - 
     - Image Plane
     - C.7.6.2
     - U
     - U
   * - 
     - Image Pixel
     - C.7.6.3
     - M
     - M
   * - 
     - Device
     - C.7.6.12
     - U
     - U
   * - 
     - Specimen
     - C.7.6.22
     - U
     - U
   * - 
     - SC Image
     - C.8.6.2
     - M
     - M
   * - 
     - Overlay Plane
     - C.9.2
     - U
     - U
   * - 
     - Modality LUT
     - C.11.1
     - U
     - U
   * - 
     - VOI LUT
     - C.11.2
     - U
     - U
   * - 
     - SOP Common
     - C.12.1
     - M
     - M
   * - 
     - Common Instance Reference
     - C.12.2
     - U
     - U

7.3.6.1 Additional Encoding Requirements
++++++++++++++++++++++++++++++++++++++++

If any...to be determined...
