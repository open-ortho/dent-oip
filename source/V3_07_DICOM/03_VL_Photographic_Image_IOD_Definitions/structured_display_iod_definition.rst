.. _structured_display_iod_definition:

7.3.7 Structured Display IOD Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This normative section describes the Basic Structured Display IOD which specifies an Instance of a single screen structured display that has been created for a Patient. It references specific image or other composite SOP Instances from one or more Studies for that Patient, or for other Patients for comparison, arranged in a specific presentation layout. 

The baseline requirements for Structured Display IODs are defined in `DICOM PS3.3: A.33.5.3 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.33.5.3.html>`_ . In Table 7.3.7-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

.. list-table:: **Table 7.3.7-1 Usage of DICOM Modules in Basic Structured Display IOD**
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - IHE Usage
   * - Patient
     - Patient
     - C.7.1.1
     - M
     - M See Section 7.4.1.1
   * - 
     - Clinical Trial Subject
     - C.7.1.3
     - U
     - U
   * - Study
     - General Study
     - C.7.2.1
     - M
     - M See Section 7.4.1.2
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - RC See Section 7.4.1.3
   * - 
     - Clinical Trial Study
     - C.7.2.3
     - U
     - U
   * - Series
     - General Series
     - C.7.3.1
     - M
     - M See Section 7.4.1.4
   * -  
     - Clinical Trial Series
     - C.7.3.2
     - U
     - U
   * - 
     - Presentation Series
     - C.11.9
     - M
     - M
   * - Equipment
     - General Equipment
     - C.7.5.1
     - M
     - M  See Section 7.4.1.5
   * - 
     - Enhanced General Equipment
     - C.7.5.2
     - U
     - U
   * - Presentation State
     - Structured Display
     - C.11.16
     - M
     - M
   * - 
     - Structured Display Image Box
     - C.11.17
     - M
     - M
   * - 
     - Structured Display Annotation
     - C.11.18
     - U
     - U
   * - 
     - Common Instance Reference
     - C.12.2
     - M
     - M
   * - 
     - Specimen
     - C.7.6.22
     - U
     - U
   * - SOP Common
     - SOP Common
     - C.12.1
     - M
     - M See Section 7.4.1.9
