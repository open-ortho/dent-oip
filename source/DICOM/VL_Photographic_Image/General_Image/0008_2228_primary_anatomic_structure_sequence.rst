.. _primary anatomic structure sequence:

Primary Anatomic Structure Sequence (0008,2228)
===============================================

When applied to orthodontic photographs, for intraoral views the anatomic region is always

* *Oral cavity structure (body structure)*

Refer to the :ref:`List of Codes <list_of_codes>` in the Appendix for the correct SNOMED codes to use.

This tag is omitted entirely for extraoral views, because of the less detailed nature of these views.

Primary Anatomic Structure Modifier Sequence (0008,2230)
--------------------------------------------------------

This tag is used to further specify the area of the oral cavity being imaged, and is used for intraoral views only.

* *Buccal*
* *Entire frenulum labii (body structure)*
* *Entire lower dental arch (body structure)*
* *Entire upper dental arch (body structure)*


Primary Anatomic Structure for including teeth
----------------------------------------------

.. warning::
   The entire tooth section needs work. I think we have considered removing it from v1.

Primary Anatomic Structure Sequence contains a list of visible teeth using ISO
tooth numbering system (represented as SNOMED CT codes) in a specific view.

This tag is used to define which teeth are represented in the image. Refer to DICOM `CID-4018 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4018.html>`_ and `CID-4019 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4019.html>`_ for a list of permissible values.

You can find examples of usage in the Appendix :ref:`View Examples <view_examples>`

-  When one tooth is visible, this sequence will contain a single SNOMED
   CT code representing the visible tooth.

-  When more teeth are visible, this sequence will contain a list of
   SNOMED CT codes representing all visible teeth.

-  When the region of the mouth imaged is not expected to show any teeth, omit this
   sequence completely.
