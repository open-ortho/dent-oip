.. _dicom_conventions:

Conventions
=============

DICOM Conventions are defined in Appendix E to the IHE Technical Frameworks General Introduction. 


.. list-table:: Usage of DICOM Modules in IHE
   :header-rows: 0
   :widths: 10 90

   * - M / C / U
     - As defined in DICOM PS 3.3
   * - R
     - The Module is defined as Conditional (C) or User Option (U) in DICOM. The Requirement is an IHE extension of the DICOM requirements, and the module shall be present.
   * - RC
     - The Module is defined as Conditional (C) or User Option (U) in DICOM. The Requirement is an IHE extension of the DICOM requirements, and the module shall be present when the specified conditions apply.


.. list-table:: Usage of DICOM Attributes in IHE
   :header-rows: 0
   :widths: 10 90

   * - O
     - The attribute or its value is optional, i.e., in DICOM it is Type 2 or 3.
   * - O+*
     - The attribute is optional, but additional constraints have been added. Note: The specification approach does not force a Type 2 or Type 3 value to become a Type 1 by stating O+.
   * - R
     - The attribute is required, and is not an IHE extension of the DICOM requirements; i.e., it is already Type 1 in DICOM, but additional constraints are placed by IHE, for example on the value set that may be used for the attribute.
   * - R+
     - The Requirement is an IHE extension of the DICOM requirements, and the attribute shall be present, i.e., is Type 1, whereas the DICOM requirement may be Type 2 or 3.
   * - RC+
     - The Requirement is an IHE extension of the DICOM requirements, and the attribute shall be present when the condition is satisfied, i.e., is Type 1C, whereas the DICOM requirement may be Type 2 or 3. If the condition is not fulfilled, the DICOM definitions apply. Note, that this means that the attribute may be present/have a value also in case the condition does not apply.
   * - D
     - The requirements of DICOM apply unchanged, but the attribute needs to be displayed.
   * - -
     - No IHE extension of the DICOM requirements is defined. The attribute is listed for better readability or similar purpose.
   * - X+
     - The attribute information is required to be absent. DICOM Type 2 attributes shall be present with no value. DICOM Type 3 attributes shall be absent.
