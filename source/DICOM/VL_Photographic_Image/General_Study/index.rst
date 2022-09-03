.. _general_study:

General Study
=============

This normative section contains a description of the DICOM tags relevant to
orthodontic photography pertaining to the General Study module.

Each DICOM Study is associated to a specific orthodontic progress and not necessarily to an orthodontic visit.

When two progresses are collected during the same orthodontic visit (for example when a patient is removing braces, the practice might acquire a set of images just before removing braces, and another set just after removing braces), the software shall create two separate DICOM Studies, one for each progress. Each progress is distnguished by making use of the :ref:`Acquisition Context Module <acquisition_context>`

This part was compiled using the various values allowed in the DICOM CID
(Content IDs) tables, highlighting those values which are relevant to the
orthodontic domain.

.. toctree::
	:glob:
	:maxdepth: 2

	./*