.. _general_image:

7.4.1.5 General Image
+++++++++++++++++++++

This normative section contains extensions to DICOM tags defined in the General Image module which are relevant to orthodontic image acquisition.

**References:**

+ `DICOM PS3.3: C.7.6.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.1>`_
+ Extensions in Table 7.4.1.5-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

.. list-table:: **Table 7.4.1.5-1 General Image Module Attribute Requirements**
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
    * - Instance Number
      - (0020,0014)
      - R+
      - To ensure images are presented in a specific sequence, set the Instance Number (0020,0013) for each image in a series according to the desired order.   See Section 7.4.1.5.1 for guidance and examples.
    * - Patient Orientation
      - (0020,0020)
      - R+
      - Patient direction of the rows and columns of the image. 

	Required because the IOD VL Photographic Image does not require Image Orientation (Patient) (0020,0037) or Image Position (Patient) (0020,0032), and the IOD VL Photographic Image does not require Image Orientation (Slide) (0048,0102).

	See Section 7.2.4 for allowed values.


7.4.1.5.1 Instance Number (0020,0013) Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To ensure images are presented in a specific sequence, set the Instance Number
(0020,0013) for each image according to the desired order. 

**Examples:**

For example, if you have a series of intraoral photographs, assign Instance
Numbers incrementally:

.. code-block:: none

   (0020,0013) Instance Number: 1   # Frontal view
   (0020,0013) Instance Number: 2   # Right lateral view
   (0020,0013) Instance Number: 3   # Left lateral view
   (0020,0013) Instance Number: 4   # Maxillary occlusal view
   (0020,0013) Instance Number: 5   # Mandibular occlusal view

When generating DICOM files programmatically, set the Instance Number attribute for each image object:

.. code-block:: python

   # Example using pydicom
   import pydicom
   ds = pydicom.Dataset()
   ds.InstanceNumber = 1  # Set according to the image order
   # ... set other attributes ...
   ds.save_as('image1.dcm')

Repeat for each image, incrementing the Instance Number as needed. This ensures that DICOM viewers and systems can display the images in the intended sequence.

**Non-Sequential Instance Numbers**

Instance Numbers do not have to be strictly sequential. For example, you may
assign non-consecutive values to allow for future insertion of images or to
match an external numbering scheme:

.. code-block:: none

   (0020,0013) Instance Number: 10   # Frontal view
   (0020,0013) Instance Number: 20   # Right lateral view
   (0020,0013) Instance Number: 30   # Left lateral view

DICOM viewers will still use the Instance Number to determine display order,
regardless of whether the numbers are consecutive.

.. toctree::
	:glob:
	:maxdepth: 1

	./*


