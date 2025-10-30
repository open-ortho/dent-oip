.. _dicom_conventions:

7.1 Conventions
===============
*<note to Toni:  I have updated this section to align with the conventions documented in the IHE RAD TF.   What was here came from the template, but RAD's content is better (more accurate), and I have submitted a CP to IHE to fix it>*

For some DICOM content described in this document, IHE has strengthened the requirements on the use of selected Type 2 and Type 3 attributes.  These situations are explicitly documented in the content specifications here in Volume 3.

IHE specifically emphasizes that DICOM Type 2 attributes (for instance, Patient Name, Patient ID) shall be transmitted with zero length if the source system does not possess valid values for
such attributes; in other words, the creator shall not assign default values to such attributes. The consumer must be able to handle zero-length values for such attributes.

IHE has defined requirements related to the support for and use of attributes by both creators and consumers of DICOM objects; IHE also defines requirements related to the support for and use of attributes in DICOM storage
transactions by both Service Class Users (SCUs) and Service Class Providers (SCPs):   

.. list-table:: **Table 7.1-1: Usage of DICOM Modules in IHE**
   :header-rows: 0
   :widths: 10 90

   * - M / C / U
     - As defined in DICOM PS 3.3
   * - R
     - The Module is defined as Conditional (C) or User Option (U) in DICOM. The Requirement is an IHE extension of the DICOM requirements, and the module shall be present.
   * - RC
     - The Module is defined as Conditional (C) or User Option (U) in DICOM. The Requirement is an IHE extension of the DICOM requirements, and the module shall be present when the specified conditions apply.

.. list-table:: **Table 7.1-2:  Usage of DICOM Attributes in IHE
   :header-rows: 0
   :widths: 10 90

    * - O
      - The attribute or its value is optional, i.e., in DICOM it is Type 2 or 3. 
    * - R
      - The attribute is required, and is not an IHE extension of the DICOM requirements; i.e., it is already Type 1 in DICOM, but additional constraints are placed by IHE, for example on the value set that may be used for the attribute. 
    * - R+
      - The Requirement is an IHE extension of the DICOM requirements, and the attribute shall be present, i.e., is Type 1, whereas the DICOM requirement may be Type 2 or 3. 
    * - RC+
      - The Requirement is an IHE extension of the DICOM requirements, and the attribute shall be present when the condition is satisfied, i.e., is Type 1C, whereas the DICOM requirement may be Type 2 or 3. If the condition is not fulfilled, the DICOM definitions apply. Note, that this means that the attribute may be present / have a value also in case the condition does not apply.


