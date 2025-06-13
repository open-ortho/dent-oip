# Template: FHIR Message Semantics

This transaction is implemented using the FHIR RESTful API.

### 1. Scope

This transaction involves a `POST` of a FHIR `Bundle` from the <Source Actor> to the <Destination Actor>.

### 2. Interaction Summary

| Actor             | FHIR Interaction | Resource Type(s) |
|-------------------|------------------|------------------|
| <Source Actor>    | `POST [base]/`   | `Bundle`         |
| <Destination Actor>| `transaction`    | `Bundle`         |

### 3. Message Definition

The message is a FHIR `transaction` Bundle that conforms to the [<Profile Name> Bundle Profile](StructureDefinition-<profile-name>-bundle.html).

The Bundle shall contain a set of resources. The first resource in the bundle SHALL be a `<Primary Resource, e.g., Composition>` resource.

#### Resource Profiles

The resources included in the Bundle shall conform to the following FHIR profiles:

| Resource    | Profile Name                                | Cardinality |
|-------------|---------------------------------------------|-------------|
| Composition | [<Profile Name> Composition](StructureDefinition-...) | [1..1]      |
| Patient     | [IHE PDQm Patient](StructureDefinition-IHE.PDQm.Patient.html) | [1..1]      |
| Encounter   | [<Profile Name> Encounter](StructureDefinition-...) | [0..1]      |
| Practitioner| [<Profile Name> Practitioner](StructureDefinition-...) | [0..*]      |
| ...         | ...                                         | ...         |

#### Bundle Structure

```xml
<Bundle>
    <id value="[UUID]"/>
    <meta>
        <profile value="http://ihe.net/fhir/StructureDefinition/<profile-name>-bundle"/>
    </meta>
    <type value="transaction"/>
    <entry>
        <!-- The Composition Resource -->
        <fullUrl value="urn:uuid:[UUID]"/>
        <resource>
            <Composition>
                <!-- Conforms to the Composition Profile -->
            </Composition>
        </resource>
        <request>
            <method value="POST"/>
            <url value="Composition"/>
        </request>
    </entry>
    <entry>
        <!-- The Patient Resource -->
        <fullUrl value="urn:uuid:[UUID]"/>
        <resource>
            <Patient>
                <!-- Conforms to the PDQm Patient Profile -->
            </Patient>
        </resource>
        <request>
            <method value="POST"/>
            <url value="Patient"/>
        </request>
    </entry>
    <!-- Other entries... -->
</Bundle>
```

#### Expected Actions: FHIR Server

The <Destination Actor> shall:
1.  Support the `transaction` interaction at the server's base URL `[base]`.
2.  Validate that the incoming Bundle and its contained resources conform to the required IHE profiles.
3.  Process the resources within the transaction Bundle atomically. Either all resources are created successfully, or none are.
4.  Return an `HTTP 200 OK` status on success.
5.  Return an `OperationOutcome` resource with an appropriate `HTTP 4xx` or `5xx` error code on failure.
