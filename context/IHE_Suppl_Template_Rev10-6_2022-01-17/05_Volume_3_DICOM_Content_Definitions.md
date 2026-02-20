# Volume 3 - DICOM Content Definitions (Section 7)

## 7 <Domain Name> DICOM Content Definitions

Purpose:

- Constrain DICOM IOD instances used in the profile.
- Apply requirements to creators, and sometimes receivers/users.

Common IHE constraints:

- Make optional DICOM modules required/conditional.
- Make optional attributes required/conditional or absent.
- Constrain attribute values, sources, and encoding.
- Require attributes be displayed to operators.

Implementers must still conform to DICOM PS 3.3 and related DICOM requirements.

### 7.1 Conventions

See General Introduction Appendix E for DICOM conventions.

Table 7.1.2-1: Usage of DICOM Modules in IHE

| Code | Meaning |
| --- | --- |
| M / C / U | As defined in DICOM PS 3.3 |
| R | IHE elevates a DICOM C/U module to required |
| RC | IHE elevates a DICOM C/U module to required when condition applies |

Table 7.1.2-2: Usage of DICOM Attributes in IHE

| Code | Meaning |
| --- | --- |
| O | Optional (Type 2 or 3) |
| O+* | Optional with added constraints (does not force Type 1) |
| R | Required by DICOM (Type 1) with added IHE constraints |
| R+ | IHE elevates to required (Type 1) |
| RC+ | IHE elevates to required when condition applies (Type 1C) |
| D | DICOM applies unchanged; attribute must be displayed |
| - | No IHE extension; listed for readability |
| X+ | Attribute must be absent (Type 2 present with no value; Type 3 absent) |

### 7.1.1 DICOM Structured Report

- Conventions for SR constraints are not fully defined; in many cases requiring a specific SR template is sufficient.

### 7.1.2 Display Requirements

- If a requirement lists "*", the attribute is not required to be displayed.

### 7.2 General Definitions

- Add domain-wide DICOM protocol requirements (character sets, storage, etc.).

### 7.3 IOD Definitions

#### 7.3.1 <IOD Group Name> IODs

##### 7.3.1.1 <DICOM IOD Name> IOD

###### 7.3.1.1.1 <DICOM IOD Name> IOD <Use Case Context>

- An IOD may have different requirements in different contexts.

###### 7.3.1.1.1.1 Referenced Standards

- <e.g., DICOM PS 3.3: A.35.8 X-Ray Radiation Dose SR IOD>

###### 7.3.1.1.1.2 IOD Definition

Table 7.3.1.1.1.2-1: Usage of DICOM Modules in IHE

| IE | Module | Reference | DICOM Usage | IHE-<DOM> Usage |
| --- | --- | --- | --- | --- |
| <IE> | <Module> | <Module ref> | M/C/U | M/C/U/R/RC/Absent + references to 7.4 sections |

### 7.4 Module Definitions

#### 7.4.1 <Module Group Name> Modules

##### 7.4.1.1 <Module Name> Module

###### 7.4.1.1.1 <Module Name> Module <Use Case Context>

###### 7.4.1.1.1.1 Referenced Standards

- <e.g., DICOM PS 3.3: A.35.8 X-Ray Radiation Dose SR IOD>

###### 7.4.1.1.1.2 Module Definition

Table 7.4.1.1.1.2-1: Usage of DICOM Attributes in IHE

| Attribute | Tag | IHE Usage | Attribute Requirements |
| --- | --- | --- | --- |
| <DICOM Attribute Name> | <Tag> | <O/R/R+ etc.> | <Constraints> |

## Appendices to Volume 3

- Add as needed. If none, write "Not applicable" and remove placeholder appendices.
