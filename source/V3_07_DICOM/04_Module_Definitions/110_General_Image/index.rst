.. _general_image:

General Image
=============

This normative section contains a description of the DICOM tags relevant to
orthodontic photography pertaining to the General Image module.

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.


7.4.1.x General Image
=====================

This normative section contains extensions to DICOM tags defined in the General Image module DICOM tags which are relevant to orthodontic image acquisition.

**References:**

+ `DICOM PS3.3: C.7.6.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.1>`_
+ Extensions in Table 7.4.1.x-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

**Table 7.4.1.x-1 General Image Module Attribute Requirements**

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
    * - Image Type
      - (0008,0008)
      - R+
      - See 


.. toctree::
	:glob:
	:maxdepth: 1

	./*


