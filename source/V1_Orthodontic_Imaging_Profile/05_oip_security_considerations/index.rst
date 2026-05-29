3.5 OIP Security Considerations
-------------------------------

OIP content modules define how orthodontic images are encoded and labeled; they do not define network transactions or storage protocols. Security requirements therefore depend on the transport and storage mechanisms used by grouped actors.

Implementers shall ensure that DICOM objects produced or consumed by OIP actors are protected in accordance with applicable regulations (e.g., HIPAA in the United States) and applicable IHE security profiles. In particular:

- Patient-identifying information in DICOM tags (e.g., Patient Name, Patient ID, Date of Birth) shall be protected in transit and at rest.
- If images are to be de-identified or anonymized, implementers shall follow the DICOM Attribute Confidentiality Profiles defined in DICOM PS3.15 Annex E.
- Access control to DICOM archives containing OIP-compliant objects should be managed through established mechanisms such as role-based access control or IHE ATNA (Audit Trail and Node Authentication).

3.6 OIP Cross-Profile Considerations
------------------------------------

OIP focuses on the content encoding of visible light orthodontic images. Implementations will typically pair OIP with one or more workflow or transport profiles:

- **Modality Worklist**: To obtain patient demographics and order information prior to image acquisition, a Content Creator may be grouped with an actor that supports DICOM Modality Worklist (e.g., the IHE RAD Acquisition Modality). This grouping is deferred to a future revision of OIP.
- **DICOM Storage (C-STORE)**: To send OIP-compliant images from a Content Creator to a Content Consumer, implementers may use DICOM C-STORE. Formal transaction requirements for storage are deferred to a future revision of OIP or a separate profile.
- **Query/Retrieve**: To retrieve OIP-compliant images from an archive for display, an Image Display may be grouped with a DICOM Query/Retrieve SCU. This is deferred to a future revision of OIP.
