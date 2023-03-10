.. _primary anatomic structure sequence:

Primary Anatomic Structure Sequence (0008,2228)
===============================================

Primary Anatomic Structure Sequence contains a list of visible teeth using ISO
tooth numbering system (represented as SNOMED CT codes) in a specific view.

Allowed Values
--------------


Primary Anatomic Structure for Intraoral Photography
::::::::::::::::::::::::::::::::::::::::::::::::::::

This tag is used to define which teeth are represented in the image. Refer to DICOM `CID-4018 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4018.html>`_ and `CID-4019 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4019.html>`_ for a list of permissible values.

You can find examples of usage in the Appendix :ref:`View Examples <view_examples>`

Primary Anatomic Structure for Extraoral Photography
::::::::::::::::::::::::::::::::::::::::::::::::::::

+-----------------+------------+-----------------+-----------------+
| Code Scheme     | Code Value | Code Meaning    | when to use     |
| Designator      |            |                 |                 |
+=================+============+=================+=================+
| SCT             | 362627000  | Entire left     | For all left    |
|                 |            | side of face    | profile         |
|                 |            |                 | photographs.    |
+-----------------+------------+-----------------+-----------------+
| SCT             | 362626009  | Entire right    | For all right   |
|                 |            | side of face    | profile         |
|                 |            |                 | photographs.    |
+-----------------+------------+-----------------+-----------------+
| SCT             | 368761004  | Entire center   | For all frontal |
|                 |            | of face         | photographs.    |
+-----------------+------------+-----------------+-----------------+

Choosing the Correct Primary Anatomic Structure
-----------------------------------------------

Intraoral Photography
:::::::::::::::::::::

-  When one tooth is visible, this sequence will contain a single SNOMED
   CT code representing the visible tooth.

-  When more teeth are visible, this sequence will contain a list of
   SNOMED CT codes representing all visible teeth.

-  When the region of the mouth imaged is not expected to show any teeth, omit this
   sequence completely.

Extraoral Photography
:::::::::::::::::::::

.. TODO: Do we have to put something here?

