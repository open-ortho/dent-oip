# Volume 1 - Profiles (Template Digest)

## Domain-specific additions

- <Include any domain-specific sections added to TF-1 Sections 1 or 2, without changing numbering. If none, write "None".>

## Add new Section #

- Reserve the next section number in the domain TF-1.
- Replace "X" with that number and keep it stable when moving to Final Text.

## X <Profile Name> (<Profile Acronym>) Profile

- Provide a brief end-user overview (1-2 paragraphs).
- Explicitly state whether this is a Workflow, Transport, Content Module, or combination profile.

## X.1 <Profile Acronym> Actors, Transactions, and Content Modules

General actor definitions: IHE TF General Introduction Appendix A.
Transactions: IHE TF General Introduction Appendix B.

### Workflow/Transport instructions

- If the profile defines workflow/transport transactions, include the actor diagram and transaction table.

Figure X.1-1: <Profile Acronym> Actor Diagram

Table X.1-1: <Profile Acronym> Profile - Actors and Transactions

| Actors | Transactions | Initiator or Responder | Optionality | Reference |
| --- | --- | --- | --- | --- |
| Actor A | Transaction 1 | <Initiator/Responder> | R | <DOM> TF-2: 3.Y1 |
| Actor A | Transaction 2 | <Initiator/Responder> | R | <DOM> TF-2: 3.Y2 |
| Actor B | Transaction 3 | <Initiator/Responder> | R/O | <DOM> TF-2: 3.Y3 |

Notes:

- Do not list dotted-line actors (from other profiles) in Table X.1-1.
- Use notes to specify conditional requirements (e.g., at least one of two transactions).

### Content Module instructions

- If the profile defines Content Modules, include the content diagram and content module table.
- Adjust figure/table numbering if both transactions and content modules are present.

Figure X.1-1: <Profile Acronym> Actor Diagram (Content)

Table X.1-1: <Profile Acronym> - Actors and Content Modules

| Actors | Content Modules | Optionality | Reference |
| --- | --- | --- | --- |
| Content Creator | Content Module 1 Name and Template ID | R | <DOM> TF-3: 6.3.1.D |
| Content Creator | Content Module 2 Name and Template ID | O (See Note) | <DOM> TF-3: 6.3.1.D |
| Content Consumer | Content Module 1 Name and Template ID | O (See Note) | <DOM> TF-3: 6.3.1.D |
| Content Consumer | Content Module 2 Name and Template ID | R | <DOM> TF-3: 6.3.1.D |

Note: Describe conditions such as "at least one of Content Module 2/3/4".

## X.1.1 Actor Descriptions and Actor Profile Requirements

Workflow profile:

- Most requirements are in TF-2 transactions.
- Add only additional requirements here, or "No additional requirements needed."

Content module profile:

- Most requirements are in TF-3 content modules.
- Add only additional requirements here, or "No additional requirements needed."

FHIR profiles:

- Systems shall provide a CapabilityStatement per ITI TF-2x Appendix Z.3 covering all actors and query parameters.

### X.1.1.1 <Actor A>

- Add profile-specific actor description if Appendix A is insufficient.

### X.1.1.2 <Actor B>

- Additional actor detail if needed.

## X.2 <Profile Acronym> Actor Options

Table X.2-1: <Profile Name> - Actors and Options

| Actor | Option Name | Reference |
| --- | --- | --- |
| Actor A | <Option 1 name> Option | Section X.2.1 |
| Actor B | No options defined | -- |
| Actor C | <Option 2 name> Option | Section X.2.2 |
| Actor D | <Option 1 name> Option | Section X.2.1 |
| Actor E | View/Import options (if applicable) | PCC TF-2: 3.1.1-3.1.4 |

Note: Options are exposed in integration statements; keep them minimal.

### X.2.1 <Option Name>

- One sentence describing the capability.
- Enumerate requirements for actors that support the option.
- If an optional transaction becomes mandatory for an option, state it here.
- If option requires grouping with another profile, state and reference Table X.3-1.

## X.3 <Profile Acronym> Required Actor Groupings

Describe required groupings with other actors/profiles. Use one of two table alternatives:

Alternative 1 (no option-specific grouping conditions):

Table X.3-1: <Profile Name> - Required Actor Groupings

| <Profile Acronym> Actor | Actor(s) to be grouped with | Reference | Content Bindings Reference |
| --- | --- | --- | --- |
| Actor A | <external DOM> <profile>/<Actor> | <TF reference> | -- |
| Actor B | None | -- | -- |

Alternative 2 (groupings depend on options):

Table X.3-1: <Profile Acronym> Profile - Required Actor Groupings

| <Profile Acronym> Actor | Grouping Condition | Actor(s) to be grouped with | Reference |
| --- | --- | --- | --- |
| Actor A | -- | None | -- |
| Actor B | Required | <external DOM> <profile>/<Actor> | <TF reference> |
| Actor C | With the <Option name> Option | <external DOM> <profile>/<Actor> | <Section where option is defined> |

Notes:

- Use notes to describe "one of several" groupings.
- Include security groupings (CT, ATNA, etc.) where required.

## X.4 <Profile Acronym> Overview

- Explain how transactions/content modules combine to address use cases.
- Use cases are informative only; no SHALL language.

### X.4.1 Concepts

- Provide background concepts or "Not applicable".

### X.4.2 Use Cases

#### X.4.2.1 Use Case #1: <Simple Name>

- Short description.

##### X.4.2.1.1 <Simple Name> Use Case Description

- Full description (<= 1 page; otherwise use appendix).

##### X.4.2.1.2 <Simple Name> Process Flow

- Describe and diagram process flow(s).
- Include external transactions/events if helpful.
- Use actor names for swimlane roles; include profile acronym for actors from other profiles.

Content module only profiles should include:

- X.4.1.2.1 Pre-conditions
- X.4.1.2.2 Main Flow
- X.4.1.2.3 Post-conditions

## X.5 <Profile Acronym> Security Considerations

- Describe profile-specific security risks and mitigations.
- Include groupings and residual risks for product/system/policy.
- For content modules, note dependence on grouped actors.

## X.6 <Profile Acronym> Cross Profile Considerations

- Informative only. Provide context with other profiles.
- If blank, write "Not applicable."

## Appendices to Volume 1

- Appendices are informational only (no SHALL language).
- If none, write "Not applicable" and remove placeholder appendices.
