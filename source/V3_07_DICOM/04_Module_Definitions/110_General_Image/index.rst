.. _general_image:

7.4.1.7 General Image
+++++++++++++++++++++

This normative section contains extensions to DICOM tags defined in the General Image module which are relevant to orthodontic image acquisition.

**References:**

+ `DICOM PS3.3: C.7.6.1 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.1>`_
+ Extensions in Table 7.4.1.7-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

.. list-table:: **Table 7.4.1.7-1 General Image Module Attribute Requirements**
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

	See Section 7.2.1 for coded values taken from DICOM CID 4028 Craniofacial Anatomic Region :ref:`cid_4028`
    * - >Anatomic Region Modifier Sequence
      - (0008,2220)
      - O+
      - This modifier is used to clarify which side of the region is contained in the image.  

	See Section 7.2.2 for coded values taken from DICOM CID 247 Laterality
    * - >>Primary Anatomic Structure Sequence 
      - (0008,2228)
      - O+
      - For orthodontic photographs, the primary anatomic structure for extraoral views is designated as Face Structure (body structure). In contrast, intraoral views exhibit a broader range of variations.

	See Section 7.2.4 for coded values taken from CID 4061 :ref:`cid_4061`. Head and/or Neck Primary Anatomic Structure
    * - >>>Anatomic Region Modifier Sequence
      - (0008,2220)
      - O+
      - This modifier is used to clarify which side of the structure is contained in the image. 

		See Section 7.2.2 for coded values taken from DICOM CID 247 Laterality Left-Right Only :ref:`cid_247`
    * - Instance Number
      - (0020,0014)
      - R+
      - To ensure images are presented in a specific sequence, set the Instance Number (0020,0013) for each image in a series according to the desired order.   See Section 7.4.1.7.1 :ref:`instance_number` for guidance and examples.
    * - Patient Orientation
      - (0020,0020)
      - R+
      - Patient direction of the rows and columns of the image. 

	Required because the IOD VL Photographic Image does not require Image Orientation (Patient) (0020,0037) or Image Position (Patient) (0020,0032), and the IOD VL Photographic Image does not require Image Orientation (Slide) (0048,0102).

	See Section 7.2.5 :ref:`patient_orientation` for guidance and allowed values.
    * - Image Laterality
      - (0020,0062)
      - R+
      - See Section 7.2.3 :ref:`cid_144` for guidance and allowed values.
    * - Image Comments
      - (0020,4000)
      - O+
      - According to DICOM, Image comments can be any string with a maximum lengthof 10240 characters. N ew lines and tabs are allowed. For orthodontic purposes, any kind of clinical comments for an image would normally go in the practice management software, or in a DICOM  structured report. 

	We recommend this field to be used to store the image view type with the following format: ``<num>^<code>^<meaning>``

	where:

	``num``: is the view number, for example EV01 (from ADA WP-1100)

	``code``: is the view code, for example EV.RP.LR.CO (from ADA WP-1100)
	``meaning``: is the code meaning, for example Extraoral, Right Profile (subject is facing observer's right), Lips Relaxed, Centric Occlusion (from ADA WP-1100)

	An example string: ``EV02^EV.RP.LR.CR^Extraoral, Right Profile (subject is facing observer's right), Lips Relaxed, Centric Relation``
    * - Quality Control Image
      - (0028,0300)
      - O+
      - Indicates whether or not this image is a quality control or phantom image. 

	In the orthodontic practice, a quality control image is usually an image that the staff acquires to ensure that the equipment is functioning as desired, or to test new settings (flash, exposure, ...) on the camera. Under these circumstances, set the value to ``YES``.

	For regular production use, this value should always be set to ``NO``.
    * - Burned in Annotation 
      - (0028,0301)
      - O+
      - According to DICOM, burned in annotation indicates whether or not an image  contains sufficient burned in annotation to identify the patient and date the image was acquired. If this Attribute is absent, then the image may or may not contain burned in annotation.

	For orthodontic purposes, conventionally photographs do not contain any burned in annotations. If this were the case for your software, thisvalue could always be present and set to ``NO``.
    * - Lossy Image Compression 
      - (0028,2110)
      - O+
      - Because of the varied nature of photographic capture equipment used for orthodontic purposes, this tag should be used. E.g, some cameras are configured to store images in raw and uncompressed format, others will save a compressed JPEG image. 

	See Section 7.4.1.7.2 :ref:`lossy_compression` for guidance on encoding this attribute.

.. _instance_number:

7.4.1.7.1 Instance Number (0020,0013) Examples
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

.. _lossy_compression:

7.4.1.7.2 Lossy Image Compression (0028,2110) - Guidance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
7.4.1.7.2.1 Compression Use Cases
*********************************
Compression, in general, aims to reduce file size, with or without decreasing data quality of the original file. DICOM is a medical imaging file standard used to store multiple information such as information of the image itself (resolution, pixel data, bit allocation, compression type, etc.) . With the rising usage of imaging in clinical diagnosis, there is a need for a fast and secure method to share a large number of  images between  practitioners, and compression is used to facilitate interoperability.

The main purpose of compression techniques is memory efficiency, fast compression, and the generation of the best output. It can be divided into two types, lossless compression and lossy compression. Lossless compression is a type of data compression which does not remove any information from the initial data, while the lossy compression removes some of the information from the initial data. 

Compression of image may compromise the diagnostic value of photographs and is therefore not the preferred method of storage. The main reasons to utilize compression in the past were related to storage costs and bandwidth speed, which, over time, have increased by orders of magnitude. In addition, each image is composed of single relatively small file (less then 20MB).

According to
`DICOM <http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.html#sect_C.7.6.1.1.5>`__
:

   The Attribute Lossy Image Compression (0028,2110) conveys that the
   Image has undergone lossy compression. It provides a means to record
   that the Image has been compressed (at a point in its lifetime) with
   a lossy algorithm and changes have been introduced into the pixel
   data. Once the value has been set to "01", it shall not be reset.

   Note

   If an image is compressed with a lossy algorithm, the Attribute Lossy
   Image Compression (0028,2110) is set to "01". Subsequently, if the
   image is decompressed and transferred in uncompressed format, this
   Attribute value remains "01". The value of Lossy Image Compression
   (0028,2110) in SOP Instances containing multiple frames in which one
   or more of the frames have undergone lossy compression shall be "01".

For orthodontic purposes, this tag should be used, because of the varied
nature of photographic capture equipment. Some cameras are configured to
store images in raw and uncompressed format, others will save a
compressed JPEG image. In order to correctly encode this information,
the following three DICOM tags should be used.

In an orthodontic setting, the following use cases are to be considered:

+---+--------------------------+-------------+-------------+-------------+
|   | Use Case                 | (0028,2110) | (0028,2112) | (0028,2114) |
+---+--------------------------+-------------+-------------+-------------+
| 0 | Photograph was acquired  | 00          | not present | not present |
| 1 | with a camera which      |             |             |             |
|   | saves the images in RAW  |             |             |             |
|   | uncompressed format, or  |             |             |             |
|   | a lossless compression   |             |             |             |
|   | method. For example:     |             |             |             |
|   | TIFF, RAW or PNG.        |             |             |             |
+---+--------------------------+-------------+-------------+-------------+
| 0 | Photograph was acquired  | 01          | For a 30:1  | See `Lossy  |
| 2 | with a camera which      |             | compression | IMage       |
|   | saved the image using a  |             | ratio, set  | Compression |
|   | lossy compression        |             | to 30. If   | Method <#   |
|   | scheme, for example      |             | unknown, do | compression |
|   | JPEG.                    |             | not add     | _method>`__ |
|   |                          |             | this tag.   | below.      |
+---+--------------------------+-------------+-------------+-------------+
| 0 | Photograph was acquired  | If image is | If image is | If image is |
| 3 | with a camera using an   | in a lossy  | in a lossy  | in a lossy  |
|   | unknown type of image    | compression | compression | compression |
|   | format, and then         | format like | format like | format like |
|   | converted into DICOM.    | JPEG, use   | JPEG,       | JPEG,       |
|   |                          | 01 here and | follow same | follow same |
|   |                          | follow same | indications | indications |
|   |                          | indications | as above    | as above    |
|   |                          | as above    | use case    | use case    |
|   |                          | use case    | 02.         | 02.         |
|   |                          | 02.         | Otherwise   | Otherwise   |
|   |                          | Otherwise   | don't       | don't       |
|   |                          | don't       | specify     | specify     |
|   |                          | specify     | this tag at | this tag at |
|   |                          | this tag at | all.        | all.        |
|   |                          | all.        |             |             |
+---+--------------------------+-------------+-------------+-------------+
| 0 | An existing DICOM image  | 01          | For a 30:1  | See `Lossy  |
| 4 | was modified and         |             | compression | Image       |
|   | compressed with a lossy  |             | ratio, set  | Compression |
|   | algorithm.               |             | to 30. If   | Method <#   |
|   |                          |             | unknown, do | compression |
|   |                          |             | not add     | _method>`__ |
|   |                          |             | this tag.   | below.      |
+---+--------------------------+-------------+-------------+-------------+
| 0 | Photograph was taken     | Use SC      | Use SC      | Use SC      |
| 5 | using an analog camera,  | `Secondary  | `Secondary  | `Secondary  |
|   | and image was then       | Capture     | Capture     | Capture     |
|   | converted into digital   | IOD <http:/ | IOD <http:/ | IOD <http:/ |
|   | using a scanner.         | /dicom.nema | /dicom.nema | /dicom.nema |
|   |                          | .org/medica | .org/medica | .org/medica |
|   |                          | l/dicom/cur | l/dicom/cur | l/dicom/cur |
|   |                          | rent/output | rent/output | rent/output |
|   |                          | /chtml/part | /chtml/part | /chtml/part |
|   |                          | 03/sect_A.8 | 03/sect_A.8 | 03/sect_A.8 |
|   |                          | .html#table | .html#table | .html#table |
|   |                          | _A.8-1>`__. | _A.8-1>`__. | _A.8-1>`__. |
|   |                          | Then set    | Then set    | Then set    |
|   |                          | this tag    | this tag    | this tag    |
|   |                          | following   | following   | following   |
|   |                          | the same    | the same    | the same    |
|   |                          | guidelines  | guidelines  | guidelines  |
|   |                          | as use case | as use case | as use case |
|   |                          | 01 or 02    | 01 or 02    | 01 or 02    |
|   |                          | above,      | above,      | above,      |
|   |                          | s           | s           | s           |
|   |                          | ubstituting | ubstituting | ubstituting |
|   |                          | the camera  | the camera  | the camera  |
|   |                          | with        | with        | with        |
|   |                          | whatever    | whatever    | whatever    |
|   |                          | imaging     | imaging     | imaging     |
|   |                          | device was  | device was  | device was  |
|   |                          | used to     | used to     | used to     |
|   |                          | acquire or  | acquire or  | acquire or  |
|   |                          | scan the    | scan the    | scan the    |
|   |                          | analog      | analog      | analog      |
|   |                          | photograph  | photograph  | photograph  |
|   |                          | or slide.   | or slide.   | or slide.   |
+---+--------------------------+-------------+-------------+-------------+

7.4.1.7.2.2 Lossy Image Compression(0028,2110) - Attribute Values
*****************************************************************

Set to the string ``"00"`` if image is not compressed. Otherwise set to
the string ``"01"``.

In order to determine if an image is to be considered compressed or not,
one needs to be familiar with the algorithm used to store the image. As
an example, all forms of JPEG images are considered lossy compression
and should thus be tagged as ``"01"``.

7.4.1.7.2.3. Lossy Image Compression Ratio (0028,2112) - Attribute Values
*************************************************************************

.. _compression_method:

7.4.1.7.2.4. Lossy Image Compression Method (0028,2114) - Attribute Values
**************************************************************************

Check `DICOM
Standard <http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.html#sect_C.7.6.1.1.5.1>`__
for most current defined terms.

At time of writing, allowed terms were:

-  ``ISO_10918_1`` for JPEG Lossy Compression [ISO/IEC 10918-1],

-  ``ISO_14495_1`` for JPEG-LS Near-lossless Compression [ISO/IEC
   14495-1]

-  ``ISO_15444_1`` JPEG 2000 Irreversible Compression [ISO/IEC 15444-1]

All of the above terms are to be stored in this tag as a simple string
(CS Codes String DICOM value representation allows only 16 uppercase
characters or numbers here).


.. toctree::
	:glob:
	:maxdepth: 1

	./*


