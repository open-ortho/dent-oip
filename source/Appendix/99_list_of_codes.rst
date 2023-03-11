.. _list_of_codes:

List of Codes used for ADA/ANSI-1107
--------------------------------------------------------

* The *keyword* column contains codes used internally to simplify the maintenance of ADA-1107. It is used to reference rows between ``views.csv`` and ``codes.csv``.
* The *codeset* column contains the abbreviation for the codeset used, i.e. ``SCT`` for SNOMED-CT, ``DCM`` for DICOM.
* The codes which are not part of a real codeset and are considered CS (Coded String) in DICOM, have ``CS`` in the *codeset* column.
* The special keyword ``__version__`` is used to store the version of this table.

.. csv-table::
	:file:	../tables/codes.csv
	:delim:	,
	:header-rows: 1




