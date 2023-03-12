.. _vl_photographic_acquisition:

VL Photographic Acquisition
===========================

This normative section contains a description of the DICOM tags present in the VL Photographic Acquisition Module which are
necessary to fully describe orthodontic views (photographs).

Most of the tags of this module have a direct mapping to EXIF tags that come from digital cameras. Any EXIF tag which comes from the camera, should be mapped and stored here making use of the table specified in DICOM `NNNN Mapping of Visible Light Photography Related Attributes to EXIF and TIFF/EP Tags <https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_NNNN.html>`__ .

Of particular interest for orthodontic photography are the following tags.

.. list-table:: 
    :header-rows: 1

    * - Tag
      - Meaning
      - Value
      - Notes
    * - (0016,003A)
      - File Source
      - ``3``
      - Indicates the type of scene. In orthodontic photography, digital still cameras record the image and this tag value must always be set to 3, indicating that the image was taken with a digital still camera (DSC).
    * - (0016,003B)
      - Scene Type
      - ``1``
      - Indicates the type of scene. In orthodontic photography, digital still cameras record the image and this tag value must always be set to 1, indicating that the image was directly photographed.
