.. _dental image view:

CID xxx2 Dental Image View
**************************

.. warning:: 
  The table :ref:`cid-xxx2` below is missing definitions.

.. list-table:: 
    :header-rows: 1

    * - Attribute Name
      - Tag
      - Value
      - Meaning
    * - > Acquisition Context Sequence Attribute
      - (0040,0555) 
      - 
      - 
    * - >> Concept Name Code Sequence Attribute
      - (0040,A043)
      - DCM-111031
      - Image View
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID xxx3 values. 
      - See :ref:`notes <cid-xxx2>` below.

Concept Name Code Sequence Attribute (0040,A043)
------------------------------------------------

The Concept Name "`Image View <https://dicom.nema.org/medical/dicom/current/output/html/part16.html#DCM_111031>`__" already exists in DICOM and can be found througout `DICOM Part 16 <https://dicom.nema.org/medical/dicom/current/output/html/part16.html>`__ 

Concept Code Sequence Attribute (0040,A168)
-------------------------------------------

Photographs in orthodontics are not always taken directly: sometimes there is a
device between the patient and the camera lens, like a mirror, to be able to see
specific regions.


.. _cid-xxx2:
.. list-table:: CID-xxx2
    :header-rows: 1

    * - Code
      - Meaning
      - Notes
    * - SCT 255589003
      - Direct
      - traditional photograph, nothing between lens and anatomy.
    * - SCT 255541007
      - Indirect
      - ?? Needs Explanation TODO: Explain *Indirect*
    * - SCT 47162009
      - Mirror
      - light from anatomy is reflected on a mirror before reaching camera lens.
    * - SCT 
      - Indirect and mirrored
      - ?? Needs Explanation TODO: Explain *Indirect and mirrored*
