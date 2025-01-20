.. _ScheduledProcedureStepSequence:

Scheduled Procedure Step Sequence (0040,0100)
=============================================



Modality (0008,0060)
---------------------

- Modality SHALL be ``XC``.

Scheduled Station AE Title (0040,0001)
--------------------------------------

TODO


Scheduled Procedure Step Start Time (0040,0003)
--------------------------------------------------

TODO

Scheduled Procedure Step ID (0040,0009)
----------------------------------------

TODO

.. _scheduled_protocol_code_sequence:
Scheduled Protocol Code Sequence (0040,0008)
--------------------------------------------

Define the types of images, also known as "Image Views" in ADA-1100. ADA-1100 refers to these as views from the perspective of defining the photograph. In DICOM, we consider them as a requested procedure, which encompasses a more functional approach. This protocol outlines the methods used to acquire these images, such as instructing the patient to smile and capturing a photograph of their face while smiling...

.. Include values from: 
    http://terminology.open-ortho.org/fhir/extraoral-2d-photographic-scheduled-protocol
    http://terminology.open-ortho.org/fhir/intraoral-2d-photographic-scheduled-protocol
    http://terminology.open-ortho.org/fhir/extraoral-3d-visible-light-scheduled-protocol
    http://terminology.open-ortho.org/fhir/intraoral-3d-visible-light-scheduled-protocol

.. _extraoral-2d-photographic-scheduled-protocol:
.. csv-table:: Extraoral 2D Photographic Scheduled Protocol
    :header-rows: 1
    :file: ../../../tables/generated/extraoral-2d-photographic-scheduled-protocol.csv

.. _intraoral-2d-photographic-scheduled-protocol:
.. csv-table:: Intraoral 2D Photographic Scheduled Protocol
    :header-rows: 1
    :file: ../../../tables/generated/intraoral-2d-photographic-scheduled-protocol.csv

.. _extraoral-3d-visible-light-scheduled-protocol:
.. csv-table:: Extraoral 3D Visible Light Scheduled Protocol
    :header-rows: 1
    :file: ../../../tables/generated/extraoral-3d-visible-light-scheduled-protocol.csv

.. _intraoral-3d-visible-light-scheduled-protocol:
.. csv-table:: Intraoral 3D Visible Light Scheduled Protocol
    :header-rows: 1
    :file: ../../../tables/generated/intraoral-3d-visible-light-scheduled-protocol.csv
