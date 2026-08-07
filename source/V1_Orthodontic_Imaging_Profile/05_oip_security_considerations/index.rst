3.5 OIP Security Considerations
-------------------------------

OIP content modules and the Display Visible Light Images [DEN-1] transaction
define how orthodontic photographs are encoded, labeled, and displayed. They
do not define network transport, storage, authentication, or authorization
mechanisms. Implementations shall assess the security capabilities of the
actors and mechanisms grouped with OIP.

**Confidentiality**

OIP objects contain patient-identifying DICOM attributes. Facial and intraoral
photographs may also identify a patient from the pixel data itself, even after
identifying metadata has been removed.

- Implementations shall protect OIP objects in transit and at rest according
  to applicable policy and regulation.
- When de-identification is required, implementations shall apply the DICOM
  Attribute Confidentiality Profile in DICOM PS3.15 Annex E and the applicable
  options, including the Clean Pixel Data Option when necessary.
- Metadata de-identification alone is not sufficient for identifiable
  photographs. De-identified pixel data should be reviewed to confirm that
  recognizable facial features, burned-in annotations, and other identifying
  content have been addressed as required by the intended use.

**Integrity and Patient Safety**

Modification, substitution, or incorrect patient association of an image can
cause a practitioner to interpret the wrong clinical information. Modification
of a Structured Display or Hanging Protocol object can cause photographs to be
presented in the wrong position or context.

- Implementations shall preserve the integrity of image pixel data, patient
  and study identifiers, view-identification metadata, Structured Display
  objects, and Hanging Protocol objects.
- Implementations shall maintain and validate the association between each
  image and the correct patient, study, and view before clinical display.

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

Cross-profile actor groupings are outside the scope of this revision of OIP.
No cross-profile groupings are defined.
