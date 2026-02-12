.. _device:

7.4.1.8 Device
++++++++++++++

This normative section contains extensions to DICOM tags defined in the Device module which are relevant to orthodontic image acquisition.

**References:**

+ `DICOM PS3.3: C.7.6.12 <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.7.6.12>`_
+ Extensions in Table 7.4.1.7-1 are from ADA Standard No. 1114 Rev. ??. Section 6.1

In Table 6.4.1.7-1, attributes with Type O+ are recommended and SHOULD be used where applicable.

.. list-table:: **Table 7.4.1.7-1 Device Module Attribute Requirements**
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Notes**
    * - Device Sequence
      - (0050,0010)
      - 
      - This sequence SHOULD be used whenever a known device was purposely used during the acquisition process.

	The Device Sequence allows for an unlimited number of devices, which are defined using SNOMED codes. 
	
	It is not required to codify each object present in the field of view of the image, except for those in Section 7.4.1.8.1. 
    * - > 
      - include `Code Sequence Macro Attributes <https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_8.8-1>`_
      - R+ 
      - See Section 7.4.1.8.1 for codes for devices most commonly used for orthodontic views that may be visible in the image. 

	Additional sequence entries making uses of codes which are children of `SCT 260787004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260787004&edition=MAIN&release=&languages=en>`__ physical object MAY be used.	
    * - > Manufacturer
      - (0008,0070)
      - O+
      - 
    * - > Manufacturer's Model Name
      - (0008,1090)
      - O+
      - 
    * - > Device Serial Number
      - (0018,1000)
      - O+
      - 
    * - > Device ID
      - (0018,1003)
      - O+
      - 
    * - > Device Length
      - (0050,0014)
      - O+
      - Length in mm of device. See `DICOM Section C.7.6.12.1.1 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.12.html#sect_C.7.6.12.1.1>`__.
    * - > Device Diameter
      - (0050,0016)
      - O+
      - Unit diameter of device. See `DICOM Section C.7.6.12.1.1 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.12.html#sect_C.7.6.12.1.1>`__.
    * - > Device Diameter Units
      - (0050,0017)
      - RC
      - Required if Device Diameter (0050,0016) is present.

7.4.1.8.1 Device Code Values 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`device_examples` for a more detailed explanation of what these devices look like and how they are used.

.. list-table:: 
    :header-rows: 1

    * - **Code**
      - **Meaning**
      - **Notes**
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

