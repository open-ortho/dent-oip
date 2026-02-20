# Volume 3 - Content Modules (CDA) and Vocabularies

## Overview

- Template covers HL7 v3 CDA Content Modules and DICOM Content Definitions.
- CDA content modules are in Section 6 of Volume 3.
- DICOM Content Definitions are in Section 7 (see separate digest file).

## 5 IHE Namespaces, Concept Domains and Vocabularies

### 5.1 IHE <Domain Name> Namespaces

Public Comment and Trial Implementation require listing new OIDs, UIDs, URNs.

- Registry location: http://wiki.ihe.net/index.php/OID_Registration#IHE_Domain_Namespaces

Table template:

| codeSystem | codeSystemName | Description |
| --- | --- | --- |
| <oid or uid> | <code system name> | <short description> |

### 5.2 IHE <Domain Name> Concept Domains

- Concept domains define categories where value sets vary by locale/context.

Table template:

| conceptDomain | conceptDomainName | Description |
| --- | --- | --- |
| <oid or uid> | <concept domain name> | <short description> |

### 5.3 IHE <Domain Name> Format Codes and Vocabularies

#### 5.3.1 IHE Format Codes

List new format codes (also update IHE Format Codes wiki).

| Profile | Format Code | Media Type | Template ID |
| --- | --- | --- | --- |
| <Profile Name> (<Profile Acronym>) | <urn:ihe:...> | <media type> | <oid> |

#### 5.3.2 IHEActCode Vocabulary

List new codes (also update IHEActCode vocabulary wiki).

| Code | Description |
| --- | --- |
| <code> | <short description> |

#### 5.3.3 IHERoleCode Vocabulary

List new role codes (also update IHERoleCode vocabulary wiki).

| Code | Description |
| --- | --- |
| <role> | <short description> |

## 6 <Domain Name> HL7 V3 CDA Content Modules

### 6.1 Conventions

- CDA conventions are in General Introduction Appendix E.

### 6.2 Folder Modules

- Placeholder. Use "NA" if the domain does not use folders.

### 6.3 Content Modules

This section defines CDA content modules. The template is divided into four module types:

1. Document (D)
2. Header (H)
3. Section (S)
4. Entry (E)

Choose one representation format for constraints and use it consistently:

- Tabular format
- Discrete conformance format

### 6.3.1 CDA Document Content Modules

Replicate for each CDA document (6.3.1.D1, D2, etc.).

#### 6.3.1.D <Content Module Name (Acronym)> Document Content Module

##### 6.3.1.D.1 Format Code

- XDSDocumentEntry format code: urn:ihe:dom:name:year

##### 6.3.1.D.2 Parent Template

- List parent templates (if any) and notes on inherited requirements.

##### 6.3.1.D.3 Referenced Standards

Table 6.3.1.D.3-1: <Document Name> - Referenced Standards

| Abbreviation | Title | URL |
| --- | --- | --- |
| <abbr> | <standard name> | <link> |

##### 6.3.1.D.4 Data Element Requirement Mappings to CDA

- Map data elements from referenced standards to CDA.
- If large, move to Volume 2 appendix.

##### 6.3.1.D.5 Document Content Module Specification

Tabular format template:

- Template Name, Template ID, Parent Template(s), General Description, Document Code
- Header Elements and Sections with Opt/Card, condition, Template ID, spec reference, vocabulary constraint

Discrete conformance format template:

- Numbered SHALL/SHOULD/MAY statements with cardinality and constraints.

##### 6.3.1.D.6 Conformance and Example

- Describe inheritance from parent templates (include OIDs).
- Provide example XML on IHE Google Drive using naming convention <DOM>_<Profile Acronym>_CDA-sample_<version>.xml
- Note example is informative only.

### 6.3.2 CDA Header Content Modules

Replicate for each header module (6.3.2.H1, H2, etc.).

Tabular format template includes:

- Template Name/ID
- Parent Template or Header Element (not both)
- Opt/Card, participation/act relationship, description, template ID, spec doc, vocabulary constraint

Discrete conformance format template includes numbered SHALL/SHOULD/MAY statements.

### 6.3.3 CDA Section Content Modules

Replicate for each section module (6.3.3.10.S1, S2, etc.).

Tabular format template includes:

- Template name/ID, parent template, general description, section code
- Author/Informant/Subject
- Subsections and Entries with Opt/Card, condition, template ID, spec doc, vocabulary constraint

Discrete conformance format template includes numbered constraints and optional XML example.

### 6.3.4 CDA Entry Content Modules

Replicate for each entry module (6.3.4.E1, E2, etc.).

Tabular format template includes:

- Template name/ID, parent template, general description
- Class/Mood code, value constraints, Opt/Card, entryRelationship, description, template ID, spec doc, vocabulary constraint

Discrete conformance format template includes numbered constraints and optional XML example.

### 6.4 Section not applicable

- This heading is reserved for numbering integrity; do not remove.

### 6.5 <Domain Name> Value Sets and Concept Domains

Replicate 6.5.x for each value set/concept domain.

Tabular format recommended. Include coding scheme and concept list, or concept domain with concept names.

## Appendices to Volume 3

- Add as needed. If none, write "Not applicable" and remove placeholder appendices.
