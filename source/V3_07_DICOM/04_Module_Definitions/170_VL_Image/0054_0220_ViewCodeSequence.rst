.. _ViewCodeSequence:

View Code Sequence (0054,0220)
==============================

Recommended. SHOULD be specified, if known. Only one value is allowed.

The projection of the anatomic region of interest on an image receptor.

.. note::
  Use one of the lateral projections for photographs of the buccal (cheek) region.
  
  *Buccal projection* is not present in SNOMED-CT, but there are various lateral projections. *Buccal (intended site)* `SCT 763825005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=763825005&edition=MAIN&release=&languages=en>`__ in the anatomic region sequence is enough to specify un-ambiguosly that this photograph is a buccal view. 

Allowed values:
- `**CID 4062**: VL View <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4062.html>`__
- `**CID 4063**: VL Dental View <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4063.html>`__

.. _cid-4062:
.. list-table:: Table CID 4062. VL View
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `399033003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399033003&edition=MAIN&release=&languages=en>`__
      - frontal
      - 
    * - SCT
      - `399173006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399173006&edition=MAIN&release=&languages=en>`__
      - left lateral 
      - For left buccal photographs
    * - SCT
      - `260421001 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260421001&edition=MAIN&release=&languages=en>`__
      - left lateral oblique
      - 
    * - SCT
      - `399198007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399198007&edition=MAIN&release=&languages=en>`__
      - right lateral projection
      - For right buccal photographs
    * - SCT
      - `260424009 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260424009&edition=MAIN&release=&languages=en>`__
      - right lateral oblique
      - 
    * - SCT
      - `399182000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399182000&edition=MAIN&release=&languages=en>`__
      - oblique projection
      - 
    * - SCT
      - `260454004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260454004&edition=MAIN&release=&languages=en>`__
      - 45 degree projection
      - 
    * - SCT
      - `260427002 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260427002&edition=MAIN&release=&languages=en>`__
      - oblique lateral
      - Mandatory for :ref:`IV24 <IV24>`, :ref:`IV25 <IV25>`, :ref:`IV26 <IV26>`, :ref:`IV27 <IV27>` 
    * - SCT
      - `399255003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399255003&edition=MAIN&release=&languages=en>`__
      - submentovertical
      - Mandatory for :ref:`EV36 <EV36>`
    * - SCT
      - `260461000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260461000&edition=MAIN&release=&languages=en>`__
      - vertex 
      - Mandatory for :ref:`EV37 <EV37>`
    * - SCT
      - `410514004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=410514004&edition=MAIN&release=&languages=en>`__
      - Unknown (qualifier value)
      - This code is used when the photograph is taken without specific attention to the projection, prioritizing image detail over projection accuracy. In cases where the :ref:ViewModifierCodeSequence is required, it must be included. Since the :ref:ViewModifierCodeSequence also requires the parent :ref:ViewCodeSequence, the sequence cannot be omitted, and the value 'Unknown' SHALL be used.

.. _cid-4063:
.. list-table:: Table CID 4063. VL Dental View
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
=======================================



Photographs in orthodontics are not always taken directly: sometimes there is a device between the patient and the camera lens, like a mirror, to be able to see specific regions.

.. _cid-4064:
.. list-table:: Table CID 4064. VL View Modifier
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `789135000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789135000&edition=MAIN&release=&languages=en>`__
      - Mirrored visible image uncorrected
      - 
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

.. _cid-4065:
.. list-table:: Table CID 4065. VL Dental View Modifier
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `789131009 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789131009&edition=MAIN&release=&languages=en>`__
      - Close up photographic view of teeth with no set magnification or distance
      - 
    * - SCT
      - `787610003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=787610003&edition=MAIN&release=&languages=en>`__
      - Photographic image corrected intraoral mirrored visible record
      - 
    * - SCT
      - `789310004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789310004&edition=MAIN&release=&languages=en>`__
      - Mirrored photographic image of teeth corrected flipped horizontally
      - 
    * - SCT
      - `789311000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789311000&edition=MAIN&release=&languages=en>`__
      - Mirrored photographic image of teeth corrected flipped vertically
      - 
    * - SCT
      - `789312007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789312007&edition=MAIN&release=&languages=en>`__
      - Mirrored photographic image of teeth corrected flipped vertically and horizontally
      - 
    * - SCT
      - `787612006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=787612006&edition=MAIN&release=&languages=en>`__
      - Photographic image extraoral with 45 degree view
      - 
    * - SCT
      - `787611004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=787611004&edition=MAIN&release=&languages=en>`__
      - Photographic image extraoral with mandible postured forward
      - 
    * - SCT
      - `789313002 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789313002&edition=MAIN&release=&languages=en>`__
      - Photographic image of anterior teeth
      - 
    * - SCT
      - `789314008 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789314008&edition=MAIN&release=&languages=en>`__
      - Photographic image of face with lips in relaxed position
      - 
    * - SCT
      - `787607005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=787607005&edition=MAIN&release=&languages=en>`__
      - Photographic image with lips closed
      - 
    * - SCT
      - `789130005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=789130005&edition=MAIN&release=&languages=en>`__
      - Photographic image with mouth partially opened position and teeth apart
      - 
