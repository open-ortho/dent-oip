.. _lossy_image_compression:

Lossy Image Compression (0028,2110)
===================================

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
| 4 | was modified and         |             | compression | IMage       |
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

Lossy Image Compression Attribute (0028,2110)
---------------------------------------------

Set to the string ``"00"`` if image is not compressed. Otherwise set to
the string ``"01"``.

In order to determine if an image is to be considered compressed or not,
one needs to be familiar with the algorithm used to store the image. As
an example, all forms of JPEG images are considered lossy compression
and should thus be tagged as ``"01"``.

Lossy Image Compression Ratio (0028,2112)
-----------------------------------------

.. _compression_method:

Lossy Image Compression Method (0028,2114)
------------------------------------------

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
