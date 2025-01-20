.. _instance_number:

Instance Number (0020,0013)
============================

See also :ref:`scheduled_protocol_code_sequence`.

- The Instance Number (0020,0013) is a unique integer for each image in the series. If present, it SHOULD be used to place the different views in the series in the order intended by the acquisition operator or modality.
- If :ref:`scheduled_protocol_code_sequence` in the :ref:`scheduledprocedurestepsequence` are present, the Instance Number SHALL be considered as a pointer to refer to the index position of the Scheduled Protocol Code Sequence. This means that with the combination of the Scheduled Protocol Code Sequence and the Instance Number, the type of image can be identified.

