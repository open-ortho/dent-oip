.. _vl_photographic_image_iod_definitions:

7.3 IOD Definitions
===================
This section contains DICOM IOD specifications referenced in profiles of the IHE Dental domain, specifying the parts of the DICOM Standard used and the extended IHE requirements.

This normative section contains a description of the DICOM tags which are
necessary to fully describe orthodontic views (photographs) and to request for these photographs to be taken (acquired).

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

The baseline requirements for the VL Photographic Image IOD is defined in DICOM `PS3.3: A.32.4 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.32.4>`_ .  In Table 7.3.1-1, Column 4 identifies modules where the IOP profile defines additional constraints on the baseline DICOM requirements. 

*<Discuss with Toni:   How to interpret blank cells in Column 4>>*

7.3.1 VL Photographic Image IOD Definition
+++++++++++++++++++++++++++++++++++++++++++

.. list-table:: Table 7.3.1-1 - IHE constraints DICOM Modules for VL Photographic Image IODs
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
