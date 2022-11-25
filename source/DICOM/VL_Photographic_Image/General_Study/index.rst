.. _general_study:

General Study
=============

This normative section contains a description of the DICOM tags relevant to
orthodontic photography pertaining to the General Study module.

#. Each DICOM Study is associated to a specific orthodontic progress and not necessarily to an orthodontic visit.

#. Each DICOM Series is associate to a specific photographic capturing session. In a conventional orthodontic visit (one during which photographs are captured), a set of intra-oral and extra-oral photographs are usually taken in a single session, which the orthodontic provider considers a unit. Such unit is best represented in a DICOM Series.

#. If during the orthodontic visit the photograph acquisition session is split between intra-oral and extra-oral, it would be reasonable to portray the intra-oral session as a DICOM Series and the extra-oral as another DICOM Series, as long as they are both part of the same DICOM Study.

#. When two progresses are collected during the same orthodontic visit (for example when a patient is removing braces, the practice might acquire a set of images just before removing braces, and another set just after removing braces), the software shall create two separate DICOM Studies, one for each progress. Each progress is distnguished by making use of the :ref:`Acquisition Context Module <acquisition_context>`

This part was compiled using the various values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

.. toctree::
	:glob:
	:maxdepth: 2

	./*