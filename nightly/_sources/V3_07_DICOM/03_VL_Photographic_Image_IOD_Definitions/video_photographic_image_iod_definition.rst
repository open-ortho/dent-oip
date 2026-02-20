.. _video_photographic_image_iod_definition:

7.3.2 Video Photograpic Image IOD Definition 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This normative section contains a description of the DICOM tags which are
necessary to capture motion picture, movies, and/or video in orthodontics.

The baseline requirements for Video Photographic Image IODs are defined in `DICOM PS3.3: A.32.7.3 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.32.7.3.html>`_ . In Table 7.3.2-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

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

       See Section 7.4.1.6
   * - 
     - Device
     - C.7.6.12
     - U
     - RC

       See Section 7.4.1.8
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

       See :ref:`Section 7.4.2.1 <vl_image_module>`
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
