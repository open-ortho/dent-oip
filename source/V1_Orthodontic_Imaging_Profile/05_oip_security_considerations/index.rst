3.5 OIP Security Considerations
-------------------------------

OIP content modules define how dental images, video, and models are encoded
and labeled, and the Display Visible Light Images [DEN-1] transaction defines
display behavior for visible light photographs. They do not define network
transport, storage, authentication, or authorization mechanisms.
Implementations shall assess the security capabilities of the actors and
mechanisms grouped with OIP.

**Confidentiality**

OIP objects contain patient-identifying DICOM attributes. Photographs, video,
radiographs, surface scans, and 3D models may also contain identifying anatomy,
recognizable facial features, burned-in annotations, or other identifying
content after identifying metadata has been removed.

- Implementations shall protect OIP objects in transit and at rest according
  to applicable policy and regulation.
- When de-identification is required, implementations shall apply the DICOM
  Attribute Confidentiality Profile in DICOM PS3.15 Annex E and the applicable
  options, including the Clean Pixel Data Option when necessary.
- Metadata de-identification alone is not sufficient for identifiable content.
  De-identified pixel, video, and geometric data should be reviewed to confirm
  that identifying content has been addressed as required by the intended use.

**Integrity and Patient Safety**

Modification, substitution, or incorrect patient association of an OIP object
can cause a practitioner to interpret the wrong clinical information.
Modification of a Structured Display or Hanging Protocol object can cause
content to be presented in the wrong position or context.

- Implementations shall preserve the integrity of pixel and geometric data,
  patient and study identifiers, acquisition and view-identification metadata,
  Structured Display objects, and Hanging Protocol objects.
- Implementations shall maintain and validate the association between each
  object and the correct patient, study, acquisition, and view before clinical
  use or display.

**Availability**

Loss of access to OIP objects or required display information may delay care.
OIP does not define availability, backup, or recovery mechanisms. Deployments
should provide those capabilities according to their clinical risk assessment
and operational requirements.

**Authentication, Authorization, and Audit**

Implementations shall authenticate users and systems, authorize access using
an appropriate access-control policy, and record security-relevant events.
Authorization is separate from IHE Audit Trail and Node Authentication (ATNA).
When applicable to the selected transport and deployment architecture, ATNA
may be used for secure-node authentication, protected communications, and
audit logging.

3.6 OIP Cross-Profile Considerations
------------------------------------

*TO DO: This is a place to point to other profiles that can be used alongside OIP for enhanced functionality.   For example, when you have a workflow profile with DICOM MWL and Storage, you would reference that in this section.*
