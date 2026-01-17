.. _vl_photographic_acquisition:

VL Photographic Acquisition
===========================

This normative section contains extensions to  DICOM tags defined in the VL Photographic Acquisition Module which are necessary to fully describe orthodontic views (photographs).

Most of the tags of this module have a direct mapping to EXIF tags that come from digital cameras. 

Any EXIF tag which comes from the camera, should be mapped and stored in the VL Photographic Acquisition Module, making use of the table specified in `DICOM PS3.17: Section NNNN <https://dicom.nema.org/medical/dicom/current/output/html/part17.html#chapter_NNNN>`__ "Mapping of Visible Light Photography Related Attributes to EXIF and TIFF/EP Tags".

**References:**

+ `DICOM PS3.3: C.8.12.11 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.8.12.11>`_
+ Extensions in Table X.y z-1 are from ???

**Table X.y.z-1 VL Photographic Acquisition Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - File Source
      - (0016,003A)
      - RC+ (confirm this)
      - Indicates the type of scene. In orthodontic photography, digital still cameras record the image and this tag value shall be set to 3, indicating that the image was taken with a digital still camera (DSC).
    * - Scene Type
      - (0016,003B)
      - R+ (confirm this)
      - Indicates the type of scene. In orthodontic photography, digital still cameras record the image and this tag value must shall be set to 1, indicating that the image was directly photographed.




