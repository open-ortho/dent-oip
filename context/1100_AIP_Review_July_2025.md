# Proposed ANSI/ADA Standard No. 1100
## AIP Review: July 2025

Title: Dentistry - 2D and 3D Orthodontic/Craniofacial/Forensic Photographic Views and Viewsets
Status: Draft
Copyright: (c) 2025 American Dental Association. All rights reserved.

Note: This markdown is a text-only digest of the PDF. Figures and images are referenced but not reproduced.

## Administrative Overview

- ADA is an ANSI-accredited standards developing organization.
- ADA Consensus Body 11 on Dental Data Structure and Exchange approved the draft.
- Working Group 11.6 (Integration of Orthodontic Standards) formulated the document.
- This standard cancels and replaces ADA White Paper No. 1100:2021.
- This is the first edition of ANSI/ADA Standard No. 1100.

Working Group 11.6 members (at time of development):

- Carlotta Evans (Co-Chair), Individual Representative, Chicago, IL
- Antonio Magni (Co-Chair), Case Western Reserve University Department of Orthodontics, Cleveland, OH
- Anil Ardeshna, Rutgers University School of Health Related Professions, Highland Park, NJ
- Clifton Carey, University of Colorado; Pittsburgh, PA
- Andrew Casertano, Consultant, MD
- William Harrell, Harrell Orthodontics, Alexander City, AL
- Vicente Hernandez-Soler, Valencia University, Spain
- Peter Mah, Individual Representative, San Antonio, TX
- Shivam Mehta, Texas A&M University College of Dentistry, Irving, TX
- Holly Moon, American Association of Orthodontists, La Habra, CA
- Suliman Salman, Rodeo Dental and Orthodontics, McAllen, TX
- Kirt Simmons, American Association of Orthodontists, Roland, AR
- Justin Sorg, Smile Doctors, Greene, OH
- Callan White, Asheville Family Dentistry, Asheville, NC
- Tingxi Wu, ADA Forsyth Institute, Cambridge, MA

## Background (Summary)

The standard defines an open architecture for interoperability and transmission of visible light intraoral and extraoral images. It provides enumerated terms, view definitions, and viewsets (templates) to support automated labeling, metadata assignment, and consistent placement of images. It includes VS-01 from DICOM CP1571 plus three additional viewsets. A separate implementation standard (ADA 1107, in development) is intended to cover coding details for SNOMED CT, SNODENT, and DICOM.

## Introduction (Summary)

Standardized photographic views support diagnosis, treatment planning, research, publication, teaching, medico-legal, and forensic activities. Consistent coding and view definitions improve interoperability and reduce errors when images are exchanged among providers.

## Scope

Provides:

- A list of intraoral and extraoral visible light image views used by orthodontic/craniofacial/forensic providers
- Explanations and attributes for each view
- Terminology for encoding views and viewsets

Suitable for use in tags, fields, and information for visible light image views in implementation guides and profiles.

## Use Cases

1. Routine photo set: software prompts each photo, labels images, and assembles viewset from uploads (camera or phone).
2. Referral: sender labels photos per the standard; receiver maps them into preferred viewset without manual sorting.

## Views (Definition)

A view is a well-defined type of photograph. Examples:

- Extraoral, Full Face, Lips Closed, Centric Occlusion
- Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected
- Extraoral, Right Profile (subject facing observer's right), Full Smile, Centric Occlusion

## Viewsets (Definition)

A viewset is a structured layout (template) with placeholders for specific views. It defines image count, types, positions, and dimensions for display.

## From Use Cases to Viewsets (Summary)

Images are labeled using enumerated terms and placed into viewsets (such as VS-01). Viewsets should include a text box for timing metadata (e.g., initial, progress, final, follow-up) and acquisition date.

## Orthodontic Progress

At acquisition time, identify if the patient:

- Was undergoing treatment (progress photos)
- Had never undergone treatment before (observation/pretreatment photos)
- Had completed treatment (posttreatment photos)

## Table 1 - Enumerated Terms (Acronyms and Definitions) (Normative)

These terms are used to identify orthodontic views and viewsets.

| Term | Definition | Notes |
| --- | --- | --- |
| IO | IntraOral | IV = intraoral view |
| EO | ExtraOral | EV = extraoral view |
| MD | ManDibular |  |
| MX | MaXillary |  |
| MO | Mouth Open |  |
| MC | Mouth Closed | Teeth together. Do not use; use LC, CO, or CR. |
| TA | Teeth Apart |  |
| CO | Centric Occlusion | Maximum intercuspation of teeth |
| CR | Centric Relation | Joint-determined position of mandible |
| OJ | showing OverJet | Horizontal distance between maxillary and mandibular incisors |
| RP | Right Profile | Extraoral photo of subject's right profile |
| LP | Left Profile | Extraoral photo of subject's left profile |
| FF | Full Face |  |
| LR | Lips Relaxed |  |
| LC | Lips Closed |  |
| FS | Full Smile |  |
| PF | Mandible Postured Forward |  |
| OF | Other Face | Other view of face (e.g., tipped back or from above) |
| NM | No Mirror | Image acquired directly without mirror |
| WM | With Mirror | Intraoral only; not for extraoral photographs |
| WM.BC | With Mirror, But Corrected | Flipped/rotated to appear direct; intraoral only |
| RB | Right Buccal | Posterior dental occlusion, patient's right |
| LB | Left Buccal | Posterior dental occlusion, patient's left |
| RL | Right Lateral | Occlusion from patient's right side |
| LL | Left Lateral | Occlusion from patient's left side |
| FV | Frontal View |  |
| IV | Inferior View | Use IO.IV to show depth of bite and overjet from below |
| SV | Superior View |  |
| 45 | 45 degree view |  |
| OV | Occlusal View |  |
| CS | Close-up Smile |  |
| Frown | Frown | Functional condition for video or still images |
| Pucker | Pucker | Functional condition for video or still images |
| Close Eyes | Close Eyes | Functional condition for video or still images |
| Raise Eyebrows | Raise Eyebrows | Functional condition for video or still images |
| Track Jaw Movements | Track Jaw Movements | Functional condition for video or still images |
| Document Speech | Document Speech | Functional condition for video or still images |
| WH | Whole Head | Used for 3D photographic image |
| OC | Occlusal Cant |  |
| FI | Forensic Interest |  |
| NW | Nerve Weakness |  |
| AN | Anomalies |  |
| FR | Frenum |  |
| PA | Using Photo Accessory | Contraster or black mirror; can be appended to any IO view |
| TT | Tongue Thrust |  |
| FTO | First Time Observation | Newly registered; no treatment yet |
| OBS | Observation | Regular visits; observation records |
| PRT | Pretreatment | Acquired before treatment starts; treat as Observation |
| IN | Initial | Baseline after agreeing to start treatment |
| P | Progress | Images during treatment |
| F | Final | End of active treatment; no sequence number required |
| FU | Follow-Up | Post-treatment changes over time |
| PST | Posttreatment | Image acquired after treatment |

## Table 2.1 - Extraoral 2D Views (EV) (Normative)

| Image ID | Enumerated Terms | Meaning |
| --- | --- | --- |
| EV-01 | EO.RP.LR.CO | Extraoral, right profile, lips relaxed, centric occlusion |
| EV-02 | EO.RP.LR.CR | Extraoral, right profile, lips relaxed, centric relation |
| EV-03 | EO.RP.LC.CO | Extraoral, right profile, lips closed, centric occlusion |
| EV-04 | EO.RP.LC.CR | Extraoral, right profile, lips closed, centric relation |
| EV-05 | EO.RP.FS.CO | Extraoral, right profile, full smile, centric occlusion |
| EV-06 | EO.RP.FS.CR | Extraoral, right profile, full smile, centric relation |
| EV-07 | EO.RP.MD.PF | Extraoral, right profile, mandible postured forward |
| EV-08 | EO.RP.LR.CO.45 | Extraoral, 45 degree right profile, lips relaxed, centric occlusion |
| EV-09 | EO.RP.LR.CR.45 | Extraoral, 45 degree right profile, lips relaxed, centric relation |
| EV-10 | EO.RP.LC.CO.45 | Extraoral, 45 degree right profile, lips closed, centric occlusion |
| EV-11 | EO.RP.LC.CR.45 | Extraoral, 45 degree right profile, lips closed, centric relation |
| EV-12 | EO.RP.FS.CO.45 | Extraoral, 45 degree right profile, full smile, centric occlusion |
| EV-13 | EO.RP.FS.CR.45 | Extraoral, 45 degree right profile, full smile, centric relation |
| EV-14 | EO.RP.MD.PF.45 | Extraoral, 45 degree right profile, mandible postured forward |
| EV-15 | EO.FF.LR.CO | Extraoral, full face, lips relaxed, centric occlusion |
| EV-16 | EO.FF.LR.CR | Extraoral, full face, lips relaxed, centric relation |
| EV-17 | EO.FF.LC.CO | Extraoral, full face, lips closed, centric occlusion |
| EV-18 | EO.FF.LC.CR | Extraoral, full face, lips closed, centric relation |
| EV-19 | EO.FF.FS.CO | Extraoral, full face, full smile, centric occlusion |
| EV-20 | EO.FF.FS.CR | Extraoral, full face, full smile, centric relation |
| EV-21 | EO.FF.MD.PF | Extraoral, full face, mandible postured forward |
| EV-22 | EO.LP.LR.CO | Extraoral, left profile, lips relaxed, centric occlusion |
| EV-23 | EO.LP.LR.CR | Extraoral, left profile, lips relaxed, centric relation |
| EV-24 | EO.LP.LC.CO | Extraoral, left profile, lips closed, centric occlusion |
| EV-25 | EO.LP.LC.CR | Extraoral, left profile, lips closed, centric relation |
| EV-26 | EO.LP.FS.CO | Extraoral, left profile, full smile, centric occlusion |
| EV-27 | EO.LP.FS.CR | Extraoral, left profile, full smile, centric relation |
| EV-28 | EO.LP.MD.PF | Extraoral, left profile, mandible postured forward |
| EV-29 | EO.LP.LR.CO.45 | Extraoral, 45 degree left profile, lips relaxed, centric occlusion |
| EV-30 | EO.LP.LR.CR.45 | Extraoral, 45 degree left profile, lips relaxed, centric relation |
| EV-31 | EO.LP.LC.CO.45 | Extraoral, 45 degree left profile, lips closed, centric occlusion |
| EV-32 | EO.LP.LC.CR.45 | Extraoral, 45 degree left profile, lips closed, centric relation |
| EV-33 | EO.LP.FS.CO.45 | Extraoral, 45 degree left profile, full smile, centric occlusion |
| EV-34 | EO.LP.FS.CR.45 | Extraoral, 45 degree left profile, full smile, centric relation |
| EV-35 | EO.LP.MD.PF.45 | Extraoral, 45 degree left profile, mandible postured forward |
| EV-36 | EO.OF.IV | Extraoral, other face, inferior view (head tipped back) |
| EV-37 | EO.OF.SV | Extraoral, other face, superior view (viewed from above) |
| EV-38 | EO.OF.CS | Extraoral, other face, close-up smile (with lips) |
| EV-39 | EO.OF.OC | Extraoral, other face, occlusal cant |
| EV-40 | EO.OF.FI | Extraoral, other face, forensic interest |
| EV-41 | EO.OF.AN | Extraoral, other face, anomalies |
| EV-42 | EO.FF.MO | Extraoral, full face, mouth open |
| EV-43 | EO.FF.NW | Extraoral, full face, demonstrating nerve weakness |

Notes on Extraoral Views (Informative):

- Use proper depth of field so nose-to-ear contours are in focus.
- For facial views, rotate camera for vertical acquisition.
- Remove glasses and jewelry for treatment planning; remove removable appliances; pull hair back.
- Standardize magnification across time points; ideally include a fiducial.

## Table 2.2 - Extraoral 3D Views (EV3D) (Normative)

| Image ID | Enumerated Terms | Meaning |
| --- | --- | --- |
| EV3D-01 | EO.WH.LC.CO | Whole head - lips closed, CO |
| EV3D-02 | EO.WH.LC.CR | Whole head - lips closed, CR |
| EV3D-03 | EO.WH.LR.CO | Whole head - lips relaxed, CO |
| EV3D-04 | EO.WH.LR.CR | Whole head - lips relaxed, CR |
| EV3D-05 | EO.WH.FS.CO | Whole head - smile, CO |
| EV3D-06 | EO.WH.FS.CR | Whole head - smile, CR |

Note: Any EV3D view may be tagged with functional conditions such as frown (FR), jaw tracking (JT), or speech (SP).

## Table 2.3 - Intraoral 2D Views (IV) (Normative)

| ID | Enumerated Values | Meaning |
| --- | --- | --- |
| IV-01 | IO.RB.CO.NM | Intraoral, right buccal segment, centric occlusion, no mirror (direct) |
| IV-02 | IO.RB.CO.WM | Intraoral, right buccal segment, centric occlusion, with mirror |
| IV-03 | IO.RB.CO.WM.BC | Intraoral, right buccal segment, centric occlusion, with mirror, but corrected |
| IV-04 | IO.RB.CR.NM | Intraoral, right buccal segment, centric relation, no mirror (direct) |
| IV-05 | IO.RB.CR.WM | Intraoral, right buccal segment, centric relation, with mirror |
| IV-06 | IO.RB.CR.WM.BC | Intraoral, right buccal segment, centric relation, with mirror, but corrected |
| IV-07 | IO.FV.CO.NM | Intraoral, frontal view, centric occlusion, no mirror (direct) |
| IV-08 | IO.FV.CR.NM | Intraoral, frontal view, centric relation, no mirror (direct) |
| IV-09 | IO.FV.TA.NM | Intraoral, frontal view, teeth apart, no mirror (direct) |
| IV-10 | IO.FV.MO.NM | Intraoral, frontal view, mouth open, no mirror (direct) |
| IV-11 | IO.FV.IV.CO.NM | Intraoral, frontal inferior view, centric occlusion, no mirror (direct) |
| IV-12 | IO.FV.IV.CR.NM | Intraoral, frontal inferior view, centric relation, no mirror (direct) |
| IV-13 | IO.FV.TT.NM | Intraoral, frontal view, tongue thrust, no mirror (direct) |
| IV-14 | IO.RL.CO.OJ.NM | Intraoral, right lateral view, centric occlusion, overjet, no mirror (direct) |
| IV-15 | IO.RL.CR.OJ.NM | Intraoral, right lateral view, centric relation, overjet, no mirror (direct) |
| IV-16 | IO.LL.CO.OJ.NM | Intraoral, left lateral view, centric occlusion, overjet, no mirror (direct) |
| IV-17 | IO.LL.CR.OJ.NM | Intraoral, left lateral view, centric relation, overjet, no mirror (direct) |
| IV-18 | IO.LB.CO.NM | Intraoral, left buccal segment, centric occlusion, no mirror (direct) |
| IV-19 | IO.LB.CO.WM | Intraoral, left buccal segment, centric occlusion, with mirror |
| IV-20 | IO.LB.CO.WM.BC | Intraoral, left buccal segment, centric occlusion, with mirror, but corrected |
| IV-21 | IO.LB.CR.NM | Intraoral, left buccal segment, centric relation, no mirror (direct) |
| IV-22 | IO.LB.CR.WM | Intraoral, left buccal segment, centric relation, with mirror |
| IV-23 | IO.LB.CR.WM.BC | Intraoral, left buccal segment, centric relation, with mirror, but corrected |
| IV-24 | IO.MX.MO.OV.WM | Intraoral, maxillary, mouth open, occlusal view, with mirror |
| IV-25 | IO.MX.MO.OV.WM.BC | Intraoral, maxillary, mouth open, occlusal view, with mirror, but corrected |
| IV-26 | IO.MD.MO.OV.WM | Intraoral, mandibular, mouth open, occlusal view, with mirror |
| IV-27 | IO.MD.MO.OV.WM.BC | Intraoral, mandibular, mouth open, occlusal view, with mirror, but corrected |
| IV-28 | IO.GR.[tooth number] | Intraoral, gingival recession; may include ISO tooth numbers |
| IV-29 | IO.FR.[tooth number] | Intraoral, frenum; may include ISO tooth numbers |
| IV-30 | IO.[modifier].PA | Intraoral view using photo accessory (contraster/black mirror) |

Notes on correction of mirrored 2D images (Normative):

- Mirror-acquired intraoral images must be corrected before placement in viewsets.
- Occlusal mirror images are reversed and must be flipped on the vertical axis.
- If photographer is in front of patient, images may be inverted and must be rotated 180 degrees along the horizontal axis.
- If photographer is superior and behind patient, image is not upside down but still must be flipped on the vertical axis.
- Frontal view should fill frame with maxillary and mandibular arches; center using facial midline.
- Buccal view: use retractors; avoid direct image of teeth; place mirror with narrow end buccal to last molar, not touching it.
- Occlusal view: mirror at 45 degrees; capture distal of second molars to slightly anterior to central incisors; center midline.

## Table 2.4 - Intraoral 3D Views (IV3D) (Normative)

| Image ID | Enumerated Terms | Type | Meaning |
| --- | --- | --- | --- |
| IV3D-01 | IO.MX | 1 | Intraoral 3D surface of maxillary dentition |
| IV3D-02 | IO.MD | 1 | Intraoral 3D surface of mandibular dentition |
| IV3D-03 | IO.CO | 1 | Intraoral 3D centric occlusion |
| IV3D-04 | IO.CR | 1 | Intraoral 3D centric relation |

## Table 3 - Information to be Captured (Normative)

| Information | Type | Description |
| --- | --- | --- |
| Patient identifiers | 1 | Patient name and unique number; use DICOM since cameras cannot embed this |
| Date | 1 | Date of image |
| Patient Age | 1 | Age at photo acquisition |
| Camera Information | 2 | Camera type, file capture type, exposure data (aperture, f-stop), aspect ratio, photographer |
| Fiducials | 3 | Include scale for size/magnification; place near area of interest without obscuring details |
| Mirror Correction | 1 | Mirror-acquired intraoral images must be corrected before placement in viewsets |
| Head Orientation | 1 | Use consistent natural head position; no head tipping in frontal view |
| Camera to Subject Distance | 2 | Maintain uniform distance to keep magnification consistent |

## Types of Visible Light Images Not Requiring Viewsets

- Video images, 3D extraoral images, and 3D intraoral images do not require viewsets.
- 3D images can be rotated on screen as desired; 2D images derived from 3D may be placed in viewsets.
- Fiducials are not required for 3D systems because dimensions are recorded and 1:1 size is determinable.

## Viewsets

Figures referenced in the PDF: Figure 1 (VS-01 layout), Figure 2 (summary of views), Figures A1-1 to A4-1 (viewset layouts and examples).

### Viewset VS-01 (Normative)

VS-01 (from DICOM CP1571) is the template preferred by the ABO for case submission/display. It has 8 images and 1 text box.

Table 4.1 - VS-01 Image Metadata

| ILC | Enumerated Terms | Meaning |
| --- | --- | --- |
| 01 | EO.RP.LR.CO | Extraoral, right profile, lips relaxed, centric occlusion |
| 02 | EO.FF.LR.CO | Extraoral, full face, lips relaxed, centric occlusion |
| 03 | EO.FF.FS.CO | Extraoral, full face, full smile, centric occlusion |
| 04 | IO.MX.MO.OV.WM.BC | Intraoral, maxillary, mouth open, occlusal, with mirror, but corrected |
| 05 | Text box | Patient initials, age (years-months), date acquired, etc. |
| 06 | IO.MD.MO.OV.WM.BC | Intraoral, mandibular, mouth open, occlusal, with mirror, but corrected |
| 07 | IO.RB.CO.NM or IO.RB.CO.WM.BC | Intraoral, right buccal, centric occlusion, direct or corrected mirror |
| 08 | IO.FV.CO.NM | Intraoral, frontal view, centric occlusion, direct |
| 09 | IO.LB.CO.NM or IO.LB.CO.WM.BC | Intraoral, left buccal, centric occlusion, direct or corrected mirror |

VS-01 requirements:

1. 9 image boxes in a 3x3 grid.
2. All image boxes have identical widths.
3. Image proportions (width/height):
   - Top row (facial/extraoral): 0.866
   - Middle row (occlusal/intraoral): 1.432
   - Bottom row (frontal/buccal/intraoral): 1.794
4. Padding between images must be visible but not distracting and allow all images on one screen.
5. Height is identical within each row.
6. Content must follow the VS-01 metadata table.
7. Images should not be altered other than positioning; modifications must be documented per underlying format (e.g., DICOM).
8. All images are from the same person and acquired in the same encounter/time frame.

Construction details (normalized dimensions):

- Horizontal to vertical ratio for entire template: 1.000 : 0.829
- Coordinates are normalized (DICOM standard); origin (0,0) is lower left
- Example: if width is 1024 px, height is 1024 x 0.829 = 849 px

### Viewset VS-02 (Normative)

Custom craniofacial viewset for documentation of orthognathic and craniofacial surgery treatment.

Table 4.2 - VS-02 Image Metadata

| ILC | Enumerated Terms | Meaning |
| --- | --- | --- |
| 1 | EO.RP.LR.CO | Right profile, lips relaxed, centric occlusion |
| 2 | EO.RP.LR.CO.45 | 45 degree right profile, lips relaxed, centric occlusion |
| 3 | EO.FF.LR.CO | Full face, lips relaxed, centric occlusion |
| 4 | EO.FF.FS.CO | Full face, full smile, centric occlusion |
| 5 | EO.LP.LR.CO.45 | 45 degree left profile, lips relaxed, centric occlusion |
| 6 | EO.LP.LR.CO | Left profile, lips relaxed, centric occlusion |
| 7 | IO.MX.OV.MO.WM.BC | Intraoral maxillary occlusal, mouth open, mirror corrected |
| 8 | IO.MD.OV.MO.WM.BC | Intraoral mandibular occlusal, mouth open, mirror corrected |
| 9 | IO.FV.IV.CO.NM | Intraoral frontal inferior view, centric occlusion, direct |
| 10 | Text box | Patient initials, age (years-months), date acquired, etc. |
| 11 | IO.RB.CO.NM or IO.RB.CO.WM.BC | Intraoral right buccal, CO, direct or corrected mirror |
| 12 | IO.FV.CO.NM or IO.FV.CO.WM.BC | Intraoral frontal view, CO, direct or corrected mirror |
| 13 | IO.LB.CO.NM or IO.LB.CO.WM.BC | Intraoral left buccal, CO, direct or corrected mirror |

Construction details:

- Horizontal to vertical ratio: 1.000 : 0.544
- Coordinates normalized; origin lower left

### Viewset VS-03 (Normative)

Supplementary viewset for insurance documentation (e.g., excessive overjet or deep bite).

Table 4.3 - VS-03 Image Metadata

| ILC | Enumerated Terms | Meaning |
| --- | --- | --- |
| 01 | EO.FF.LR.CO | Extraoral, full face, lips closed, centric occlusion |
| 02 | EO.FF.FS.CO | Extraoral, full face, full smile, centric occlusion |
| 03 | EO.RP.LR.CO | Extraoral, right profile, lips relaxed, centric occlusion |
| 04 | EO.RP.FS.CO | Extraoral, right profile, full smile, centric occlusion |
| 05 | EO.LP.LR.CO | Extraoral, left profile, lips relaxed, centric occlusion |
| 06 | IO.MX.MO.OV.WM.BC | Intraoral maxillary occlusal, mouth open, mirror corrected |
| 07 | IO.MD.MO.OV.WM.BC | Intraoral mandibular occlusal, mouth open, mirror corrected |
| 08 | IO.FV.IV.CO.NM | Inferior frontal view showing depth of bite, direct |
| 09 | IO.RL.CO.OJ.NM | Right lateral view, CO, overjet, direct |
| 10 | IO.RB.CO.NM or IO.RB.CO.WM.BC | Intraoral right buccal, CO, direct or corrected mirror |
| 11 | IO.FV.CO.NM | Intraoral frontal view, CO, direct |
| 12 | IO.LB.CO.NM or IO.LB.CO.WM.BC | Intraoral left buccal, CO, direct or corrected mirror |
| 13 | TEXT | Patient initials, age (years-months), date acquired |

VS-03 requirements (differences from VS-01):

- 13 image boxes in inverted pyramid layout (top row 5, middle row 4, bottom row 4)
- All boxes have identical width
- Horizontal to vertical ratio: 1.000 : 0.544

### Viewset VS-04 (Normative)

Supplementary viewset for craniofacial asymmetry assessment.

Table 4.4 - VS-04 Image Metadata

| ILC | Enumerated Terms | Meaning |
| --- | --- | --- |
| 01 | EO.RP.LR.CO | Extraoral, right profile, lips relaxed, centric occlusion |
| 02 | EO.RP.LR.CO.45 | Extraoral, 45 degree right profile, lips relaxed, centric occlusion |
| 03 | EO.FF.LR.CO | Extraoral, full face, lips closed, centric occlusion |
| 04 | EO.FF.FS.CO | Extraoral, full face, full smile, centric occlusion |
| 05 | EO.OF.SV | Extraoral, other face, superior view |
| 06 | EO.OF.IV | Extraoral, other face, inferior view |
| 07 | EO.LP.LR.CO.45 | Extraoral, 45 degree left profile, lips relaxed, centric occlusion |
| 08 | EO.LP.LR.CO | Extraoral, left profile, lips relaxed, centric occlusion |
| 09 | IO.RB.CO.NM or IO.RB.CO.WM.BC | Intraoral right buccal, CO, direct or corrected mirror |
| 10 | IO.FV.CO.NM | Intraoral frontal view, CO, direct |
| 11 | IO.LB.CO.NM or IO.LB.CO.WM.BC | Intraoral left buccal, CO, direct or corrected mirror |
| 12 | TEXT | Patient initials, age (years-months), date acquired |

VS-04 requirements (differences from VS-01):

- 12 image boxes in a 4x3 grid (3 rows, 4 per row)
- All boxes have identical width

## Bibliography

- ADA Technical Report No. 1029, Guide to Digital Dental Photography and Imaging
- ADA Technical Report No. 1051, DICOM Requirements for Digital Imaging in Institutional Dentistry
- ADA Technical Report No. 1065, Use Cases of the Orthodontic Electronic Health Record
- ANSI/NIST-ITL, Special Publication 500-280v2.1, Mobile ID Device Best Practice Recommendation, Version 2.1, 2015
- DICOM correction package CP1570, Dental Acquisition Context Module, 2019
- DICOM correction package CP1571, Structured Display for Orthodontics and Forensic Odontology Viewsets, 2019
- NIST Special Publication 500-290 Edition 3, Data Format for the Interchange of Fingerprint, Facial and Other Biometric Information, 2015
- SNODENT: https://www.ada.org/resources/practice/dental-standards/snodent
- SNOMED CT browser: https://browser.ihtsdotools.org/
- DICOM standard 2025 release: http://www.dicomstandard.org/current/

## Other Recommended Reading

- Ahmad I. Digital and Conventional Dental Photography. Quintessence Publishing Co, Inc. 2004.
- American Academy of Cosmetic Dentistry. A guide to accreditation photography, 2013: https://aacd.com/proxy/files/Students%20and%20Faculty/AACD_2013_Photo_Guide(1).pdf
- American Board of Orthodontics: https://americanboardortho.com/media/1177/example-photo-montage.pdf
- American Board of Orthodontics: https://americanboardortho.com/media/1206/example-photos-radiographs.pdf
- ASTM International E3115-17, Standard Guide for Capturing Facial Images for Use with Facial Recognition Systems, 2019: https://www.astm.org/Standards/E3115.htm
- Badano A, Revie C, Casertano A, Cheng W-C, Green P, Kimpe T, Krupinski E, Sisson C, Skrovseth S, Treanor D, Boynton P, Clunie D, Flynn MJ, Heki T, Hewitt S, Homa H, Masia A, Matsui T, Nagy B, Nishibori M, Penczek J, Schopf T, Yagi Y, Yokoi H. Consistency and standardization of color in medical imaging: a consensus report. J Digit Imaging 18:41-52, 2015.
- Bengel W. Mastering Dental Photography. Quintessence Verlags - GMBH, pp. 59 and 71, 2002.
- Heike CL, Upson K, Stuhaug E, Weinberg SM. 3D digital stereophotogrammetry: A practical guide to facial image acquisition. Head Face Med 6:18, 2010.
- Institute of Medical Illustrators, IMI National Guidelines: A Guide to Good Practice Cleft Lip and Palate, 2018.
- Institute of Medical Illustrators, IMI National Guidelines Orthodontic Photography, 2008.
- International Civil Aviation Organization, Machine Readable Travel Documents Doc 9303, 2015: https://www.icao.int/publications/Documents/9303_p12_cons_en.pdf
- Sandler J, Gutierrez RJ, Murray A. Clinical photographs: the gold standard, an update. Prog Orthod 13:296-303, 2012.
- Samawi SS. A Short Guide to Clinical Digital Photography in Orthodontics, 2008: https://www.free-ebooks.net/health/A-Short-Guide-to-Clinical-Digital-Photography-in-Orthodontics/pdf?dl&preview
- Virginia Department of Commerce, Forensic Photography Section Procedures Manual, DFS Document 241-D500 Revision 3, 2013.

All links current as of May 29, 2025.
