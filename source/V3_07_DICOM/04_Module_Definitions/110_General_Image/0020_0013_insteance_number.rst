.. _instance_number:

Instance Number (0020,0013)
============================

See also :ref:`scheduled_protocol_code_sequence`.

The below defined schema allows for proper definition, even if different instances of the same image type are required in the same series.

- The Instance Number (0020,0013) is a unique integer for each image in the series. If present, it SHOULD be used to place the different views in the series in the order intended by the acquisition operator or modality.
- If :ref:`scheduled_protocol_code_sequence` in the :ref:`scheduledprocedurestepsequence` are present, the Instance Number SHALL be considered as a pointer to refer to the index position of the Scheduled Protocol Code Sequence. This means that with the combination of the Scheduled Protocol Code Sequence and the Instance Number, the type of image can be identified.
- The actual position/index SHALL be InstanceNumber//100 (integer division, dropping remainder). 100-199:1, 200-299:2, etc. 
- Is a String Integer and SHALL thus be zero padded to a total of five digits. Ex: "00100" refers to first instance of the type defined by the first scheduled protocol code in the sequence. "00203" would be the fourth instance of the second scheduled protocol code in the sequence.

