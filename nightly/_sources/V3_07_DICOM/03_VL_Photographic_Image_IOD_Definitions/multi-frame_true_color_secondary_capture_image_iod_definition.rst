:orphan:

.. _multi-frame_true_color_secondary_capture_image_iod_definition:

7.3.5 Multi-frame True Color Secondary Capture Image IOD Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This normative section contains a description of the DICOM tags which are
necessary to capture scan film, negatives, or positive photographs. 

The baseline requirements for Multi-frame True Color Secondary Capture Image IODs are defined in `DICOM PS3.3: A.8.5.3 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.8.5.3.html>`_ . In Table 7.3.5-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

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
     - RC

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
     - RC

       See Section 7.4.1.8
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
     - M See Section 7.4.1.9
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
