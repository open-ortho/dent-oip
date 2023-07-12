.. _study_description:

Study Description (0008,1030)
=============================

This is an optional DICOM tag, which can contain a Long String (64
character max), part of the General Study module. For the application of orthodontic photographs, Study Description is used to replicate the treatment progress, as defined in :ref:`orthodontic treatment progress`.

The *Study Description* is shown by most PACS system in the search results when listing studies after a query. It is therefore recommended to repeat the information contained in the Concept Codes described in :ref:`orthodontic treatment progress` also here. 

It would be acceptable to choose a *Study Description* with the progress name as defined by the main practice management system in use by the practice who was responsible for initially acquiring the photographs. For example:

- Pre-treatment 1
- Initial
- Progress 12
- Final


.. note::
    - The Study Description is usually used by the medical provider which is treating the patient and has acquired the images.
    - Other software might also use *Study Description* and only 64 characters are allowed. We therefore recommend keeping it less than 16 characters.
    - When importing images acquired by other institutions, it may happen for the *Study Description* to not be relevant to the receiving practice.
    - *Study Description* is *not* a good tag to be relied upon for interoperability across systems and institutions.
    - For reliable interoperability,  you can rely on the *Acquisition Context* codes as defined in :ref:`orthodontic treatment progress`.
