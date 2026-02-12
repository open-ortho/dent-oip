# Template: DICOM Message Semantics

This transaction utilizes the C-STORE DIMSE Service for transmitting DICOM SOP Instances.

## SOP Class Definitions

The system should be capable of transmitting the following SOP Classes:

| SOP Class Name                   | SOP Class UID                       |
| :------------------------------- | :---------------------------------- |
| Key Object Selection Document    | 1.2.840.10008.5.1.4.1.1.88.59       |
| Grayscale Softcopy Presentation State | 1.2.840.10008.5.1.4.1.1.11.1 |

## DICOM Information Object Definition (IOD)

This section outlines the requirements for the DICOM object (e.g., Key Object Selection Document) created during this transaction.

### IOD Module Table:

| IE       | Module                   | Reference                | Usage                      |
| :------- | :----------------------- | :----------------------- | :------------------------- |
| Patient  | Patient                  | DICOM PS3.3 C.7.1.1      | U - Required if known      |
| Study    | General Study            | DICOM PS3.3 C.7.2.1      | R                          |
| Series   | Key Object Doc Series    | DICOM PS3.3 C.17.4       | R                          |
| Document | Document                 | DICOM PS3.3 C.17.6       | R                          |

### Module Attributes:

This table specifies the attributes for the Module:

| Attribute Name               | Tag         | Type | Req Type | Notes / Value Set Constraints          |
| :--------------------------- | :---------- | :--- | :------- | :------------------------------------- |
| Patient's Name               | (0010,0010) | 2    | U        | Required if known by the actor.        |
| Patient ID                   | (0010,0020) | 2    | U        |                                         |
| Issuer of Patient ID         | (0010,0021) | 3    | C        | Required if Patient ID is present.     |
| Content Date                 | (0008,0023) | 1    | R        |                                         |
| Content Time                 | (0008,0033) | 1    | R        |                                         |
| Referenced Request Sequence  | (0040,A370) | 1    | R        | Shall contain one item.                |
| Requested Procedure ID       | (0040,1001) | 1    | R        |                                         |