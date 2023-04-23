.. _view_examples:

View Examples
=============

Examples of DICOM implementations of the 77 views defined in ADA SCDI White Paper 1100. Each view contains a sample DICOM image, a rendered table with DICOM tags and a comment section explaining tags which are less intuitive.


.. _view keywords:

View keywords
-------------

In ADA-1107, every orthodontic view is identified with a keyword, like `IV01` or `EV20`. View keywords allow software and standard developers to have a standardized way of dealing with the view name, when required, without needing to use SNOMED-CT codes. This would be the analogous of DICOM Keywords, where, for example, the attribute Patient's Name has keyword "PatientName" defined in DICOM.

Here we define how to use keywords for views. The regular expressione for the keyword is: ``^[I,E]VP?[0-9]+$``. In plain English, this translates to:

- Each keyword is composed of intially a sequnce of capital letters, followed a sequence of digits. 
- The character part defines the type, like intraoral or extroral.
- Allowed types currently are ``IV``, ``EV``, ``IVP``, ``EVP``. However more views can be added following the scheme defined here.
- The digit part define view number.
- Private views are views that do not exist in ADA-1107 and that the developer has needed to add as requested by the medical provider.
- Private views have a P preceding to the digits. So ``EVP01`` would be private view.
- Zero padding is not defined. Can be used or not used. Valid examples are therefore ``EV1``, ``EV01``, ``EV001``.
- No dashes between charachter part and digit part are allowed.

General notes regarding the examples
------------------------------------

* SOP Instance UID (0008,0018), Study Instance UID (0020,000d) and Series Instance UID(0020,000e) have been purposely left blank to avoid inadvertently copying them from this table when implementing the standard, instead of generating these randomly or pseudo-randomly. Here is an example in Python:

.. code-block:: 

    import uuid
    def generate_dicom_uid():
        new_uuid = uuid.uuid4().bytes # Generate a 128bit UUID Type 4
        dicom_uid = ''
        for i in range(len(new_uuid)):
            dicom_uid += '.' + str(new_uuid[i])
        return dicom_uid[1:]


* The actual image that was encoded in DICOM was a 1 bit black and white (not grayscale) image, which is not what a realistic color orthodontic photograph would be like.

List of view examples
---------------------

.. toctree::
	:glob:
	:maxdepth: 2

	./generated/*
