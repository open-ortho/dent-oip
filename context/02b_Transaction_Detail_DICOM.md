# Template: DICOM Message Semantics



[cite_start]This transaction utilizes the C-STORE DIMSE Service for transmitting DICOM SOP Instances[cite: 1].

## SOP Class Definitions

[cite_start]The system should be capable of transmitting the following SOP Classes[cite: 2]:

| SOP Class Name                   | SOP Class UID               |
| :------------------------------- | :-------------------------- |
| Key Object Selection Document    | [cite_start]1.2.840.10008.5.1.4.1.1.88.59 [cite: 3] |
| Grayscale Softcopy Presentation State | [cite_start]1.2.840.10008.5.1.4.1.1.11.1 [cite: 3] |

## DICOM Information Object Definition (IOD)

[cite_start]This section outlines the requirements for the DICOM object (e.g., Key Object Selection Document) created during this transaction[cite: 4].

### IOD Module Table:

| IE       | Module                   | Reference           | Usage             |
| :------- | :----------------------- | :------------------ | :---------------- |
| Patient  | Patient                  | [cite_start]DICOM PS3.3 C.7.1.1 [cite: 5] | [cite_start]U - Required if known [cite: 6] |
| Study    | General Study            | [cite_start]DICOM PS3.3 C.7.2.1 [cite: 6] | R                 |
| Series   | Key Object Doc Series    | [cite_start]DICOM PS3.3 C.17.4 [cite: 7] | R                 |
| Document | Document                 | [cite_start]DICOM PS3.3 C.17.6 [cite: 8] | R                 |

### Module Attributes:
[cite_start]This table specifies the attributes for the Module[cite: 8].

| Attribute Name              | Tag         | Type | Req Type | Notes / Value Set Constraints         |
| :-------------------------- | :---------- | :--- | :------- | :------------------------------------ |
| Patient's Name              | (0010,0010) | 2    | U        | [cite_start]Required if known by the actor. [cite: 10] |
| Patient ID                  | (0010,0020) | 2    | [cite_start]U        | [cite: 11]                            |
| Issuer of Patient ID        | (0010,0021) | 3    | C        | [cite_start]Required if Patient ID is present. [cite: 12] |
| Content Date                | (0008,0023) | 1    | [cite_start]R        | [cite: 13]                            |
| Content Time                | (0008,0033) | 1    | [cite_start]R        | [cite: 13]                            |
| >Referenced Request Sequence | (0040,A370) | 1    | R        | [cite_start]Shall contain one item. [cite: 14]    |
| >>Requested Procedure ID    | (0040,1001) | 1    | [cite_start]R        | [cite: 15]                            |