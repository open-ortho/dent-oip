.. _hanging_protocol_iod_definition:

7.3.8 Hanging Protocol IOD Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This normative section describes a Hanging Protocol entity that specifies the viewing preferences of a specific user or group, for a specific type of Study (Modality, Anatomy, Laterality combination, and optionally Procedure, and/or Reason).

The baseline requirements for Hanging Protocol IODs are defined in `DICOM PS3.3: A.44.3 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.44.3.html>`_ . In Table 7.3.8-1, Column 5 identifies modules where the OIP profile defines additional constraints on the baseline DICOM requirements. 

.. list-table:: **Table 7.3.8-1 Usage of DICOM Modules in Hanging Protocol IODs**
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - OIP Profile Usage
   * - Hanging Protocol
     - SOP Common
     - C.12.1
     - M
     - M See Section 7.4.1.9
   * - 
     - Hanging Protocol Definition
     - C.23.1
     - M
     - M 
   * - 
     - Hanging Protocol Environment
     - C.23.2
     - M
     - M 
   * - 
     - Hanging Protocol Display
     - C.23.3
     - M
     - M 
