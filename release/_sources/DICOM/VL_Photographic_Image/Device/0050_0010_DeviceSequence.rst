.. _DeviceSequence:

Device Sequence (0050,0010)
===========================

Recommended. This sequence SHOULD be used whenever a known device was purposely used during the acquisition process.

The Device Sequence allows for an unlimited number of devices, which are defined using SNOMED codes. The following are the codes that are most commonly used for orthodontic views that may be visible in the image. See :ref:`device_examples` for a more detailed explanation of how these devices look like and how they are used.

.. list-table:: 
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - `SCT 462735007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=462735007&edition=MAIN&release=&languages=en>`__
      - Periodontal probe (physical object)
      - Frequently included in photographs to document gingival health (See :ref:`[IV28] <IV28>`). May be included in photographs for other purposes as well.
    * - `SCT 102304005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=102304005&edition=MAIN&release=&languages=en>`__
      - Measuring Ruler
      - When included, the ruler should be in SI units (millimeter increments). DICOM DeviceSequence does not have a place for defining ruler units. Usually used for :ref:`Overjet <overjet>` measurements.
    * - `SCT 39802000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=39802000&edition=MAIN&release=&languages=en>`__
      - Tongue blade, device
      -
    * - `SCT 53535004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=53535004&edition=MAIN&release=&languages=en>`__
      -  Retractor, device
      -
    * - `SCT 1332162007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1332162007&edition=MAIN&release=&languages=en>`__
      - Intraoral photography mirror
      - SHOULD be used for 
    * - `SCT 1332163002 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1332163002&edition=MAIN&release=&languages=en>`__
      - Dental photography black contraster
      - 
    * - `SCT 1332164008 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=1332164008&edition=MAIN&release=&languages=en>`__
      - Photographic image fiducial marker
      - 

It is not required to codify each object present in the field of view of the image, except for those listed above. 

Additional entries making uses of codes which are children of `SCT 260787004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260787004&edition=MAIN&release=&languages=en>`__ physical object MAY be used.

Other tags of the Device Sequence
-------------------------------------------------

The device sequence is extensive and includes many tags. The following table lists those that are recommended and *SHOULD* be used where applicable. All other tags are optional and *MAY* be used.


.. list-table::
   :header-rows: 1

   * - Attribute Name
     - Tag
     - Attribute Description
   * - Manufacturer
     - (0008,0070)
     - Manufacturer of the device
   * - Manufacturer's Model Name
     - (0008,1090)
     - Manufacturer's model name of the device
   * - Device Serial Number
     - (0018,1000)
     - Manufacturer's serial number of the device
   * - Device ID
     - (0018,1003)
     - User-supplied identifier for the device
   * - Device Length
     - (0050,0014)
     - Length in mm of device. See `DICOM Section C.7.6.12.1.1 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.12.html#sect_C.7.6.12.1.1>`__.
   * - Device Diameter
     - (0050,0016)
     - Unit diameter of device. See `DICOM Section C.7.6.12.1.1 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.12.html#sect_C.7.6.12.1.1>`__.
   * - Device Diameter Units
     - (0050,0017)
     - Required if Device Diameter (0050,0016) is present.
