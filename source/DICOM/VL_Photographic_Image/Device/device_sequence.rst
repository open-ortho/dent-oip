.. _device sequence:

Device Sequence (0050,0010)
===========================

The Device Sequence allows for an unlimited number of devices, which are defined
using SNOMED codes. The following are the codes that are most commonly used for
orthodontic views that may be visible in the image. See :ref:`device_examples` for a more detailed explanation of how these devices look like and how they are used.

.. list-table:: 
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - SCT 102304005
      - Measuring Ruler
      - When included, the ruler should be in SI units (millimeter increments). DICOM device sequence does not have a place for defining ruler units. Usually used for :ref:`Overjet <overjet>` measurements.
    * - SCT XXXXXX
      - Intraoral Photographic Mirror
      - Awaiting for SNOMED publication of new code. Use SCT 47162009 'Mirror'.
    * - SCT XXXXXX
      - Contraster
      - Awaiting for SNOMED publication of new code. 
    * - SCT XXXXXX
      - Black Mirror
      - Awaiting for SNOMED publication of new code.
    * - SCT XXXXXX
      - Coin
      - Awaiting for SNOMED publication of new code.
    * - SCT 86967005
      - Tool
      - Use when other devices are present in the field of view, such as contraster, coin or black mirror.


Additional Tags for Compliance with this Standard
-------------------------------------------------


+----------------------------+-------------+------+------------------------------------------------------+
| Attribute Name             | Tag         | Type | Attribute Description                                |
+============================+=============+======+======================================================+
| >Manufacturer              | (0008,0070) | 3    | Manufacturer of the device                           |
+----------------------------+-------------+------+------------------------------------------------------+
| >Manufacturer's Model Name | (0008,1090) | 3    | Manufacturer's model name of the device              |
+----------------------------+-------------+------+------------------------------------------------------+
| >Device Serial Number      | (0018,1000) | 3    | Manufacturer's serial number of the device           |
+----------------------------+-------------+------+------------------------------------------------------+
| >Device ID                 | (0018,1003) | 3    | User-supplied identifier for the device              |
+----------------------------+-------------+------+------------------------------------------------------+
| >Device Length             | (0050,0014) | 3    | Length in mm of device. See Section C.7.6.12.1.1.    |
+----------------------------+-------------+------+------------------------------------------------------+
| >Device Diameter           | (0050,0016) | 3    | Unit diameter of device. See Section C.7.6.12.1.1.   |
+----------------------------+-------------+------+------------------------------------------------------+
| >Device Diameter Units     | (0050,0017) | 2C   | "Required if Device Diameter (0050,0016) is present. |
+----------------------------+-------------+------+------------------------------------------------------+
