.. _secondary_capture_image_iod_definition:

7.3.6 Secondary Capture Image IOD Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This normative section contains a description of the DICOM tags which are necessary to capture scanned study models or other body parts (i.e. face)

The baseline requirements for Secondary Capture Image IODs are defined in `DICOM PS3.3: A.8.1.3 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.8.html#sect_A.8.1.3>`_ . In Table 7.3.6-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

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
     - RC See Section 7.4.1.8
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
     - M See Section 7.4.1.9
   * - 
     - Common Instance Reference
     - C.12.2
     - U
     - U

7.3.6.1 Additional Encoding Requirements
+++++++++++++++++++++++++++++++++++++++

If any...to be determined...
