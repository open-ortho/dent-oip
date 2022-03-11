Device Sequence (0050,0010)
===========================

The Device Sequence allows for an unlimited number of devices, which are defined
using SNOMED codes. The folloing are the codes that are used for orthodontic
views.

+---------------+-----------------+
|     Code      |     Meaning     |
+===============+=================+
| SCT 102304005 | Measuring Ruler |
| SCT 47162009  | Mirror          |
| SCT 468670005 | Dental Mirror   |
+---------------+-----------------+


Optional Tags
-------------

The following optional DICOM tags can be optionally used, if known, for any device used.

+----------------------------+-------------+---------------+------------------------------------------------------+
| Attribute Name             | Tag         | Value         | Meaning                                              |
+============================+=============+===============+======================================================+
| >Manufacturer              | (0008,0070) | 3             | Manufacturer of the device                           |
| >Manufacturer's Model Name | (0008,1090) | 3             | Manufacturer's model name of the device              |
| >Device Serial Number      | (0018,1000) | 3             | Manufacturer's serial number of the device           |
| >Device ID                 | (0018,1003) | 3             | User-supplied identifier for the device              |
| >Device Length             | (0050,0014) | 3             | Length in mm of device. See Section C.7.6.12.1.1.    |
| >Device Diameter           | (0050,0016) | 3             | Unit diameter of device. See Section C.7.6.12.1.1.   |
| >Device Diameter Units     | (0050,0017) | 2C            | "Required if Device Diameter (0050,0016) is present. |
+----------------------------+-------------+---------------+------------------------------------------------------+
