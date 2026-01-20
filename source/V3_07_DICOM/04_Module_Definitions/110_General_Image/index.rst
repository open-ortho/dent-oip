.. _general_image:

7.4.1.5 General Image
=====================

This normative section contains extensions to DICOM tags defined in the General Image module which are relevant to orthodontic image acquisition.

**References:**

+ `DICOM PS3.3: C.7.6.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.1>`_
+ Extensions in Table 7.4.1.5-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

**Table 7.4.1.5-1 General Image Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - Image Type
      - (0008,0008)
      - R+
      - See `DICOM PS3.3: Section C.7.6.1.1.2 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.1.1.2>`_.  This is a multi-valued attribute; one of these value pairs shall be used:

	:code:`['ORIGINAL','PRIMARY']` - Use when the photographic acquisition device (camera or software) will upload the photograph as is.

	:code:`['ORIGINAL','PRIMARY']` - Use when the photographic acquisition device (camera or software) will perform basic operations like rotation and cropping, and save the image as rotated or cropped and discard the uncropped, unrotated image.

	:code:`['ORIGINAL','PRIMARY']` and :code:`['DERIVED','PRIMARY']` - Use when the photographic acquisition device (camera or software) will perform basic operations like rotation and cropping, and save the image as rotated or cropped as :code:`'DERIVED'` and save the uncropped, unrotated image as well as :code:`'ORIGINAL'`.

	(Note: When saving both the original and the derived image, the derived image will have to reference the original image making use of the `General Reference Module <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.12.4.html#table_C.12-10>`__.)
    * - Anatomic Region Sequence
      - (0008,2208)
      - O+
      - When applied to orthodontic photographs, the anatomic region is Mouth for intraoral views, and Head/Neck for extraoral views.  

	See Section 7.2.1 for coded values taken from DICOM CID 4028. Craniofacial Anatomic Region 
    * - >Anatomic Region Modifier Sequence
      - (0008,2208)
      - O+
      - This modifier is used to clarify which side of the region is contained in the image.  

	See Section 7.2.2 for coded values taken from DICOM CID 247 Laterality Left-Right Only 
 41
42
43
44
45
46
47
48
49
50
51
52
53
54

**References:**

+ `DICOM PS3.3: C.7.6.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.1>`_
+ Extensions in Table 7.4.1.5-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

**Table 7.4.1.5-1 General Image Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - Image Type
      - (0008,0008)
      - R+
      - See `DICOM PS3.3: Section C.7.6.1.1.2 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.1.1.2>`_.  This is a multi-valued attribute; one of these value pairs shall be used:

	:code:`['ORIGINAL','PRIMARY']` - Use when the photographic acquisition device (camera or software) will upload the photograph as is.

	:code:`['ORIGINAL','PRIMARY']` - Use when the photographic acquisition device (camera or software) will perform basic operations like rotation and cropping, and save the image as rotated or cropped and discard the uncropped, unrotated image.

	:code:`['ORIGINAL','PRIMARY']` and :code:`['DERIVED','PRIMARY']` - Use when the photographic acquisition device (camera or software) will perform basic operations like rotation and cropping, and save the image as rotated or cropped as :code:`'DERIVED'` and save the uncropped, unrotated image as well as :code:`'ORIGINAL'`.

	(Note: When saving both the original and the derived image, the derived image will have to reference the original image making use of the `General Reference Module <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.12.4.html#table_C.12-10>`__.)
    * - Anatomic Region Sequence
      - (0008,2208)
      - O+
      - When applied to orthodontic photographs, the anatomic region is Mouth for intraoral views, and Head/Neck for extraoral views.  

	See Section 7.2.1 for coded values taken from DICOM CID 4028 Craniofacial Anatomic Region 
    * - >Anatomic Region Modifier Sequence
      - (0008,2220)
      - O+
      - This modifier is used to clarify which side of the region is contained in the image.  

	See Section 7.2.2 for coded values taken from DICOM CID 247 Laterality
    * - >>Primary Anatomic Structure Sequence 
      - (0008,2228)
      - O+
      - For orthodontic photographs, the primary anatomic structure for extraoral views is designated as Face Structure (body structure). In contrast, intraoral views exhibit a broader range of variations.

	See Section 7.2.3 for coded values taken from CID 4061. Head and/or Neck Primary Anatomic Structure
    * - >>>Anatomic Region Modifier Sequence
      - (0008,2220)
      - O+
      - This modifier is used to clarify which side of the structure is contained in the image. 

		See Section 7.2.2 for coded values taken from DICOM CID 247 Laterality





.. toctree::
	:glob:
	:maxdepth: 1

	./*


