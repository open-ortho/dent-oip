# Volume 2 - Transactions (Template Digest)

## Add Section 3.Y

3.Y <Transaction Name [DOM-#]>

- "Y" matches the DOM-#.

### 3.Y.1 Scope

- Describe what the transaction accomplishes (keep abstract for reuse).

### 3.Y.2 Actor Roles

Alternative 1 (simple table):

Table 3.Y.2-1: Actor Roles

| Actor | Role |
| --- | --- |
| <Actor name> | <Role description> |

Alternative 2 (role-based table):

Table 3.Y.2-1: Actor Roles

- Role: <Role Name> (unique within transaction)
- Description: <Role description>
- Actor(s): <Actor(s) that may play the role>

### 3.Y.3 Referenced Standards

- <List referenced standards and links>

### 3.Y.4 Messages

Figure 3.Y.4-1: Interaction Diagram

#### 3.Y.4.1 <Message 1 Name>

- One or two sentence summary (no SHALL language).
- State actor multiplicity if applicable.

##### 3.Y.4.1.1 Trigger Events

- Real-world events that cause Message 1.

##### 3.Y.4.1.2 Message Semantics

- Describe the standard and actor mapping (e.g., DICOM C-FIND, SCU/SCP).
- Profile the message: parameters, payload encoding, structure, and meaning.

##### 3.Y.4.1.3 Expected Actions

- Actions on send/receive.
- Avoid re-stating process flow sequencing.

#### 3.Y.4.2 <Message 2 Name>

- Repeat 3.Y.4.1 structure for additional messages.

### 3.Y.5 Protocol Requirements

- Describe protocol bindings (SOAP/HTTP, etc.) or "NA".

### 3.Y.6 Security Considerations

#### 3.Y.6.1 Security Audit Considerations

- Identify ATNA audit events and encoding requirements.

#### 3.Y.6.(z) <Actor> Specific Security Considerations

- Actor-specific security requirements.

## Appendices to Volume 2

- Mark each appendix as Informative or Normative.
- If none, write "Not applicable" and remove placeholders.

## Namespace Additions for Volume 2

- List new OIDs, UIDs, URNs defined for this profile (Public Comment and Trial Implementation only).
- Ensure registry entry before Trial Implementation.
- This section is removed before Final Text.

Template text:

- The <domain name> registry of OIDs is located at <link to registry>.
- Volume 2 additions to the <Domain Name> OID Registry are: <list>.
