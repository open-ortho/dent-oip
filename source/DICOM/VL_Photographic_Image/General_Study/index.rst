.. _general_study:

General Study
=============

This normative section contains a description of the DICOM tags relevant to
orthodontic photography pertaining to the General Study module.

#. Each DICOM *Study* is associated with a specific orthodontic progress and not necessarily with an orthodontic visit.

#. Each DICOM *Series* is associated with a specific photographic capturing session. In an orthodontic visit (one during which photographs are captured), a set of intra-oral and extra-oral photographs are usually taken in a single session, considered as a unit. Such unit is best represented as a DICOM Series.

#. If during the orthodontic visit the photograph acquisition session is split between intra-oral and extra-oral, the intra-oral session shall be portrayed as one DICOM Series and the extra-oral as another DICOM Series, as long as they are both part of the same DICOM Study (i.e. visit).

#. When two progresses are collected during the same orthodontic visit (the practice might acquire a set of images just before removing braces, and another set just after removing braces during the same patient encounter), the software shall create two separate DICOM Studies, one for each progress. Each progress is distinguished by making use of the :ref:`Acquisition Context Module <acquisition_context>`

This part was compiled using the values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

.. toctree::
	:glob:
	:maxdepth: 2

	./*