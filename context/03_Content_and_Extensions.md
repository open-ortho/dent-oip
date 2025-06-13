# IHE Profile: Volume 3/4 - Content, Bindings, and Extensions

## Content Modules

<This section is used if the profile defines specific content structures, like a CDA document template or a FHIR Composition.>

### 1. <Content Module Name>

#### 1.1 Conformance

<Specifies the rules for conforming to this content module.>

#### 1.2 Content Definition

<The detailed structure of the content.>

---

## National Extensions

<This section is for country-specific adaptations of the profile.>

### 1. National Extensions for <Country Name or IHE Organization>

#### 1.1 <Profile Acronym> <Type of Change>

<Details of the national extension.>

---

## Appendices to Volume 4

### 1. Glossary

<Definitions of terms specific to this profile.>

| Term       | Definition |
|------------|------------|
| <Term>     | <Definition> |

### 2. Value Set Bindings

<This section binds abstract concepts from the profile to specific value sets (collections of codes).>

**Example:**
- **Concept Domain:** `UV_CardiacProcedureDrugClasses`
- **Binding:** `US_CardiacProcedureDrugClasses`
- **Value Set OID:** `1.3.6.1.4.1.19376.1.4.1.5.15`

### 3. Value Set Definitions

<This section defines the content of the value sets.>

**Example: `US_CardiacProcedureDrugClasses`**

| Coding Scheme | Concept                 | SNOMED CT | NDF-RT      |
|---------------|-------------------------|-----------|-------------|
| SNOMED CT     | Calcium channel blockers| 48698004  | N0000029119 |
| SNOMED CT     | Beta-blockers           | 33252009  | N0000029118 |