.. _ViewCodeSequence:

View Code Sequence (0054,0220)
==============================

The projection of the anatomic region of interest on an image receptor.

.. note::
  Use one of the lateral projections for photographs of the buccal (cheek) region.
  
  *Buccal projection* is not present in SNOMED-CT, but there are various lateral projections. *Buccal (intended site)* `SCT 763825005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=763825005&edition=MAIN&release=&languages=en>`__ in the anatomic region sequence is enough to specify un-ambiguosly that this photograph is a buccal view. 

.. list-table:: Table CID 4010. DX View
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `260454004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260454004&edition=MAIN&release=&languages=en>`__
      - 45 degree projection (qualifier value)
      - 
    * - SCT
      - `260499007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260499007&edition=MAIN&release=&languages=en>`__
      - Occlusal projection (qualifier value)
      - 
    * - SCT
      - `399033003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399033003&edition=MAIN&release=&languages=en>`__
      - Frontal projection (qualifier value)
      - 
    * - SCT
      - `399173006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399173006&edition=MAIN&release=&languages=en>`__
      - Left lateral projection (qualifier value)
      - For left buccal photographs
    * - SCT
      - `399198007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399198007&edition=MAIN&release=&languages=en>`__
      - Right lateral projection (qualifier value)
      - For right buccal photographs

.. _ViewModifierCodeSequence:

View Modifier Code Sequence (0054,0222)
---------------------------------------

Photographs in orthodontics are not always taken directly: sometimes there is a
device between the patient and the camera lens, like a mirror, to be able to see
specific regions.

.. list-table:: Table CID 4011. DX View Modifier
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `787610003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=787610003&edition=MAIN&release=&languages=en>`__
      - Photographic image corrected intraoral mirrored visible record (record artifact)
      - Light from anatomy is reflected on a mirror before reaching camera lens. Image has been flipped (either horizontally or vertically) by image acquisition device.
    * - SCT
      - `789135000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789135000&edition=MAIN&release=&languages=en>`__
      - Mirrored visible image uncorrected (record artifact)
      - Light from anatomy is reflected on a mirror before reaching camera lens.
    * - SCT
      - `XXXXXXXXX <https://browser.ihtsdotools.org/?perspective=full&conceptId1=XXXXXXXXX&edition=MAIN&release=&languages=en>`__
      - Close up 
      - Still waiting for SNOMED-CT code. Should be qualifier value. Used for a specific kind of close up of the oral cavity or face. (See :ref:`[IV28] <IV28>`, :ref:`[IV29] <IV29>`, :ref:`[EV38] <EV38>`) 
