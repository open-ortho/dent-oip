.. _vl_photographic_image_iod_definitions:

7.3 IOD Definitions
===================
This section contains DICOM IOD specifications referenced in profiles of the IHE Dental domain, specifying the parts of the DICOM Standard used and the extended IHE requirements.

This normative section contains a description of the DICOM tags which are
necessary to fully describe orthodontic views (photographs) and to request for these photographs to be taken (acquired).

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

The baseline requirements for the VL Photographic Image IOD is defined in DICOM `PS3.3: A.32.4.3 <hhttps://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.32.4.3>`_ .  In Table 7.3.1-1, Column 4 identifies modules where the IOP profile defines additional constraints on the baseline DICOM requirements. 

*<Discuss with Toni:   How to interpret blank cells in Column 4>>*

*<Discuss:  This profile defines many constraints on the modules listed in this table.   In Col 4, add a reference to the section containing those constraints (otherwise, a quick glance at this table implies, for example, that there is no difference between DICOM and OIP for the General Study, Patient, Acquisition Context, etc modules, which is not the case)>* 

7.3.1 VL Photographic Image IOD Definition
+++++++++++++++++++++++++++++++++++++++++++

.. list-table:: **Table 7.3.1-1 - IHE constraints DICOM Modules for VL Photographic Image IODs**
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
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - U
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
   * - 
     - Clinical Trial Series
     - C.7.3.2
     - U
     - 
   * - Equipment
     - General Equipment
     - C.7.5.1
     - M
     - 
   * - 
     - VL Photographic Equipment
     - C.8.12.10
     - U
     - 
   * - Acquisition
     - General Acquisition
     - C.7.10.1
     - M
     - M
   * - Image
     - General Image
     - C.7.6.1
     - M
     - M See Section :ref:`general_image`
   * - 
     - General Reference
     - C.12.4
     - U
     - U
   * - 
     - Image Pixel
     - C.7.6.3
     - M
     - 
   * - 
     - Acquisition Context
     - C.7.6.14
     - M
     - 
   * - 
     - Device
     - C.7.6.12
     - U
     - 
   * - 
     - Specimen
     - C.7.6.22
     - C - Required if Imaging Subject is a specimen
     - 
   * - 
     - VL Image
     - C.8.12.1
     - M
     - 
   * - 
     - VL Photographic Acquisition
     - C.8.12.11
     - U
     - 
   * - 
     - VL Photographic Geolocation
     - C.8.12.12
     - U
     - 

7.3.1.1 VL Photographic Image IOD Acquisition Requirements
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Each DICOM *Study* SHALL represent a specific orthodontic progress (rather than necessarily an orthodontic visit). The same *Study* SHALL NOT span across multiple visits, or multiple progresses.

#. Each DICOM *Series* SHALL represent a specific photographic capturing session. In an orthodontic visit (one during which photographs are captured), a set of intra-oral and extra-oral photographs are usually taken in a single session, considered as a unit. Such unit is best represented as a DICOM Series.

#. If during the orthodontic visit the photograph acquisition session is split between intra-oral and extra-oral, the intra-oral session SHALL Be portrayed as one DICOM Series and the extra-oral as another DICOM Series, as long as they are both part of the same DICOM Study (i.e. visit), 

#. Intra-oral and extra-oral photographs MAY be part of the same Series, as long as they represent the same clinical context. DICOM Series SHALL portray a single clinical context. 

#. When two separate acquisition devices (cameras) are used (as could easily happen, since EVs are usually captured with the patient standing and a special background to prevent shadows, while the IVs are often taken with the patient on the chair), the Series SHOULD be part of the same Study (Study with the same Study Instance UID). The camera SHOULD get the Study Instance UID from the Modality Work List (coming from the practice management software), and both series would therefore be part of the same Study. 

#. In the case in which Modality Worklists are not impleented, each camera MAY produce a new Study Instance UID, as long as it is properly tagged with the *Orthodontic Progress*, date and Acession Number.

#. When two progresses are collected during the same orthodontic visit (the practice might acquire a set of images just before removing braces, and another set just after removing braces during the same patient encounter), the software shall create two separate DICOM Studies, one for each progress. Each progress is distinguished by making use of the :ref:`Acquisition Context Module <acquisition_context>`

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.
