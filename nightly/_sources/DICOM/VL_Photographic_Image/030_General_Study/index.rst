.. _general_study:

General Study
=============

This normative section contains a description of the DICOM tags relevant to
orthodontic photography pertaining to the General Study module.

#. Each DICOM *Study* SHALL represent a specific orthodontic progress (rather than necessarily an orthodontic visit). The same *Study* SHALL NOT span across multiple visits, or multiple progresses.

#. Each DICOM *Series* SHALL represent a specific photographic capturing session. In an orthodontic visit (one during which photographs are captured), a set of intra-oral and extra-oral photographs are usually taken in a single session, considered as a unit. Such unit is best represented as a DICOM Series.

#. If during the orthodontic visit the photograph acquisition session is split between intra-oral and extra-oral, the intra-oral session SHALL Be portrayed as one DICOM Series and the extra-oral as another DICOM Series, as long as they are both part of the same DICOM Study (i.e. visit), 

#. Intra-oral and extra-oral photographs MAY be part of the same Series, as long as they represent the same clinical context. DICOM Series SHALL portray a single clinical context. 

#. When two separate acquisition devices (cameras) are used (as could easily happen, since EVs are usually captured with the patient standing and a special background to prevent shadows, while the IVs are often taken with the patient on the chair), the Series SHOULD be part of the same Study (Study with the same Study Instance UID). The camera SHOULD get the Study Instance UID from the Modality Work List (coming from the practice management software), and both series would therefore be part of the same Study. 

#. In the case in which Modality Worklists are not impleented, each camera MAY produce a new Study Instance UID, as long as it is properly tagged with the *Orthodontic Progress*, date and Acession Number.

#. When two progresses are collected during the same orthodontic visit (the practice might acquire a set of images just before removing braces, and another set just after removing braces during the same patient encounter), the software shall create two separate DICOM Studies, one for each progress. Each progress is distinguished by making use of the :ref:`Acquisition Context Module <acquisition_context>`

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

.. toctree::
	:glob:
	:maxdepth: 2

	./*