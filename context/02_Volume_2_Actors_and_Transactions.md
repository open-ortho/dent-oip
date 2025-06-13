# IHE Profile: Volume 2 - Actors and Transactions

## <Transaction Number> <Transaction Name>

<e.g., ITI-8: Patient Identity Feed>
<This section defines a single transaction.>

### 1. Scope

<A brief description of the purpose of this transaction.>

### 2. Actor Roles

<A diagram showing the actors involved in this specific transaction.>

| Actor        | Role                               |
|--------------|------------------------------------|
| <Actor 1>    | Initiates the transaction (Source) |
| <Actor 2>    | Responds to the transaction (Destination) |

### 3. Referenced Standards

<List of standards used, e.g., HL7 v2.5.1, DICOM PS3.18, RFC2616 (HTTP/1.1).>

### 4. Messages

<A diagram showing the message exchange.>

#### 4.1 <Trigger Event Name> Message

<e.g., A04: Register Patient>

##### 4.1.1 Trigger Events

<What causes this message to be sent?>

##### 4.1.2 Message Semantics

<For HL7v2, see the template in 02a_Transaction_Detail_HL7v2.md and insert here.>
<For DICOM, see the template in 02b_Transaction_Detail_DICOM.md and insert here.>
<For FHIR, see the template in 02c_Transaction_Detail_FHIR.md and insert here.>

<The specification must be detailed enough for an implementer to create a valid message. It should not simply repeat the base standard, but should specify all required segments/attributes, optionality (R/O/C), cardinality, and value sets.>

##### 4.1.3 Expected Actions

<What the receiving actor must do upon receiving the message.>

##### 4.1.4 Security Requirements

<Any specific security requirements for this transaction.>