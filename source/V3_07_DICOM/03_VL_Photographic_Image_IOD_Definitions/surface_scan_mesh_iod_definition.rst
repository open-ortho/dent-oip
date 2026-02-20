.. _surface_scan_mesh_iod_definition:

7.3.4 Surface Scan Mesh IOD Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This normative section contains a description of the DICOM tags which are
necessary to capture 3D intraoral or extraoral surface scans directly from a patient.

The baseline requirements for Surface Scan Mesh IODs are defined in `DICOM PS3.3: A.68.3 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.68.3.html>`_ . In Table 7.3.4-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

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
     - M See Section 7.4.1.9

7.3.4.1 Additional Encoding Requirements
+++++++++++++++++++++++++++++++++++++++

If any...to be determined...
