.. _ViewCodeSequence:

View Code Sequence (0054,0220)
==============================

The projection of the anatomic region of interest on an image receptor.

.. note::
  Use one of the lateral projections for photographs of the buccal (cheek) region.
  
  *Buccal projection* is not present in SNOMED-CT, but there are various lateral projections. *Buccal (intended site)* `SCT 763825005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=763825005&edition=MAIN&release=&languages=en>`__ in the anatomic region sequence is enough to specify un-ambiguosly that this photograph is a buccal view. 

.. _cid-BBBB:
.. list-table:: Table CID BBBB. VL View
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `399033003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399033003&edition=MAIN&release=&languages=en>`__
      - Frontal projection (qualifier value)
      - 
    * - SCT
      - `399173006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399173006&edition=MAIN&release=&languages=en>`__
      - Left lateral projection (qualifier value)
      - For left buccal photographs
    * - SCT
      - `260421001 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260421001&edition=MAIN&release=&languages=en>`__
      - Left lateral oblique (qualifier value)
      - 
    * - SCT
      - `399198007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399198007&edition=MAIN&release=&languages=en>`__
      - Right lateral projection (qualifier value)
      - For right buccal photographs
    * - SCT
      - `260424009 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260424009&edition=MAIN&release=&languages=en>`__
      - Right lateral oblique (qualifier value)
      - 
    * - SCT
      - `399182000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399182000&edition=MAIN&release=&languages=en>`__
      - Oblique projection (qualifier value)
      - 
    * - SCT
      - `260454004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260454004&edition=MAIN&release=&languages=en>`__
      - 45 degree projection (qualifier value)
      - 
    * - SCT
      - `260427002 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260427002&edition=MAIN&release=&languages=en>`__
      - Oblique lateral (qualifier value)
      - 

.. _cid-CCCC:
.. list-table:: Table CID CCCC. VL Dental View
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `260499007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260499007&edition=MAIN&release=&languages=en>`__
      - Occlusal projection (qualifier value)
      - 

.. _ViewModifierCodeSequence:

View Modifier Code Sequence (0054,0222)
---------------------------------------

Photographs in orthodontics are not always taken directly: sometimes there is a
device between the patient and the camera lens, like a mirror, to be able to see
specific regions.

.. _cid-EEEE:
.. list-table:: Table CID EEEE. VL Dental View Modifier
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `789134001 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789134001&edition=MAIN&release=&languages=en>`__
      - Mirrored visible image uncorrected flipped horizontally
      - Light from anatomy is reflected on a mirror before reaching camera lens. Image has been flipped horizontally by image acquisition device.
    * - SCT
      - `789132002 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789132002&edition=MAIN&release=&languages=en>`__
      - Mirrored visible image uncorrected flipped horizontally and vertically
      - Light from anatomy is reflected on a mirror before reaching camera lens. Image has been flipped horizontally and vertically by image acquisition device.
    * - SCT
      - `789133007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789133007&edition=MAIN&release=&languages=en>`__
      - Mirrored visible image uncorrected flipped vertically
      - Light from anatomy is reflected on a mirror before reaching camera lens. Image has been flipped vertically by image acquisition device.
