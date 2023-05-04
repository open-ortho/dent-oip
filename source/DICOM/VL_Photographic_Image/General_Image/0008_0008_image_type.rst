Image Type (0008,0008)
======================

When acquiring orthodontic photographs, the photographs can usually be archived in two forms:

.. list-table::
    :header-rows: 1

    * - Code
      - Use Case
    * - ['ORIGINAL','PRIMARY']
      - The photographic acquisition device (camera or software) will upload the photograph as is.
    * - ['ORIGINAL','PRIMARY']
      - The photographic acquisition device (camera or software) will perform basic operations like rotation and cropping, and save the image as rotated or cropped and discard the uncropped, unrotated image.
    * - ['ORIGINAL','PRIMARY'] and ['DERIVED','PRIMARY']
      - The photographic acquisition device (camera or software) will perform basic operations like rotation and cropping, and save the image as rotated or cropped as ['DERIVED'] and save the uncropped, unrotated image as well as ['ORIGINAL'].

When saving both the original and the derived image, the derived image will have to reference the original image making use of the `General Reference Module <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.12.4.html#table_C.12-10>`__.