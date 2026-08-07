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

OIP focuses on the content encoding of visible light orthodontic images. Implementations will typically pair OIP with one or more workflow or transport profiles:

- **Modality Worklist**: To obtain patient demographics and order information prior to image acquisition, a Content Creator may be grouped with an actor that supports DICOM Modality Worklist (e.g., the IHE RAD Acquisition Modality). This grouping is deferred to a future revision of OIP.
- **DICOM Storage (C-STORE)**: To send OIP-compliant images from a Content Creator to a Content Consumer, implementers may use DICOM C-STORE. Formal transaction requirements for storage are deferred to a future revision of OIP or a separate profile.
- **Query/Retrieve**: To retrieve OIP-compliant images from an archive for display, an Image Display may be grouped with a DICOM Query/Retrieve SCU. This is deferred to a future revision of OIP.
