Anatomic Region Sequence (0008,2218)
====================================

The use of the Anatomic Region Sequence, populated with standard values, enables seamless interoperability of imaging data regardless of whether images are used within a site or across different sites and systems.

According to DICOM, this sequence identifies the anatomic region of interest, i.e., external anatomy, surface anatomy, or general region of the body. Only a single Item is permitted in this Sequence.

When applied to orthodontic photographs, the anatomic region is either Face for extraoral photographs, or Jaw for intraoral photographs. Refer to the :ref:`View Examples <view_examples>` in the Appendix for the correct SNOMED codes to use.


Anatomic Region Modifier Sequence (0008,2220)
---------------------------------------------

DICOM allows this sequence to be used for anything that is necessary to further define the anatomical region represented in the image. There is no restriction on the amount of region "modifications" that can be used.

When applied to orthodontic photographs, the following "modifications" are used. Refer to the :ref:`View Examples <view_examples>` in the Appendix for the correct SNOMED codes to use.

* Buccal
* Left
* Right
* Left and Right
* Closeup
