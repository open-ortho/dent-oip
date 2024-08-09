Anatomic Region Sequence (0008,2218)
====================================

According to DICOM, this sequence identifies the anatomic region of interest, i.e., external anatomy, surface anatomy, or general region of the body. Only a single Item is permitted in this Sequence.

When applied to orthodontic photographs, the anatomic region is *Mouth* for intraoral views, and *Head/Neck* for extraoral views.

.. _cid-4028a:
.. list-table:: Table CID 4028. Craniofacial Anatomic Region
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - 123851003
      - Mouth region structure (body structure)
      - Used for IV-* intraoral views. 
    * - SCT
      - 774007
      - Structure of head and/or neck (body structure)
      - Used for EV-* extraoral views. This code was selected, because it is the most detailed code that includes the ear as well since the ear is present in both frontal and lateral extra oral views.


Anatomic Region Modifier Sequence (0008,2220)
---------------------------------------------

This modifier is used to clarify which side of the region is contained in the image.

.. _cid-247a:
.. list-table:: Table CID 247. Laterality Left-Right Only 
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - 24028007
      - Right (qualifier value)
      - 
    * - SCT
      - 7771000
      - Left (qualifier value)
      - 
