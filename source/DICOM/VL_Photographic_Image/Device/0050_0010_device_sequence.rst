.. _device sequence:

Device Sequence (0050,0010)
===========================

.. warning:: 
  Missing SNOMED codes.


The Device Sequence allows for an unlimited number of devices, which are defined
using SNOMED codes. The following are the codes that are most commonly used for
orthodontic views that may be visible in the image. See :ref:`device_examples` for a more detailed explanation of how these devices look like and how they are used.

.. list-table:: 
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - `SCT 462735007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=462735007&edition=MAIN&release=&languages=en>`__
      - Periodontal probe (physical object)
      - Frequently included in photographs to document gengival health (See :ref:`[IV28] <IV28>`). May be included in photographs for other purposes as well.
    * - `SCT 102304005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=102304005&edition=MAIN&release=&languages=en>`__
      - Measuring Ruler
      - When included, the ruler should be in SI units (millimeter increments). DICOM device sequence does not have a place for defining ruler units. Usually used for :ref:`Overjet <overjet>` measurements.
    * - SCT XXXXXX
      - Intraoral Photographic Mirror
      - Awaiting for SNOMED publication of new code. Use SCT 47162009 'Mirror'.
    * - SCT XXXXXX
      - Contraster/Black Mirror
      - Awaiting for SNOMED publication of new code. 

It is not required to codify each object present in the field of view of the image, except for those listed above. The implementer may, however, add additional entries making uses of codes which are childre of `SCT 260787004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260787004&edition=MAIN&release=&languages=en>`__ physical object.

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
