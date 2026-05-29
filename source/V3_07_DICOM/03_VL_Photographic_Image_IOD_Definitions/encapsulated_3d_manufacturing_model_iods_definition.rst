:orphan:

.. _encapsulated_3d_manufacturing_model_iods_definition:

7.3.3 Encapsulated 3D Manufacturing Models IODs Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The baseline requirements for Encapsulated 3D Manufacturing Model IODs are defined in `DICOM PS3.3: A.85 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.85.html>`_ , specifially:

+ **Encapsulated STL IOD** in `DICOM PS3.3: A.85.1 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.85.html#sect_A.85.1>`_ - The Encapsulated STL IOD describes a 3D model in Stereolithography (STL) format that has been encapsulated within a DICOM Information Object.
+ **Encapsulated OBJ IOD** in `DICOM PS3.3: A.85.2 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.85.html#sect_A.85.2>`_ - The Encapsulated OBJ IOD describes a 3D model in OBJ format. *(Note:  Any supporting material library file (MTL) and supporting 2D texture map image files are addressed in other DICOM IODs..)*
+ **Encapsulated MTL IOD** in `DICOM PS3.3: A.85.3 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.85.html#sect_A.85.3>`_ . The Encapsulated MTL IOD describes in MTL format a materials library used by an Encapsulated OBJ 3D model (see `DICOM PS3.3: A.85.2.1 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.85.2.html#sect_A.85.2.1>`_).

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
     - RC

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
     - M

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
     - M See Section 7.4.1.9
   * - 
     - Common Instance Reference
     - C.12.1
     - C - Required if other Instances are referenced
     - C
   * - Acquisition *<note:  currently not in DICOM; needed before including this IOD in the profile>*
     - Acquisition Context 
     - C.7.6.14
     - X
     - M  -  See Section 7.4.1.6


7.3.3.1 Additional Encoding Requirements
+++++++++++++++++++++++++++++++++++++++

If any...to be determined...
