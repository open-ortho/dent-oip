.. _viewset_display_requirements:

3.1.4.1.3.2 Viewset VS-01
*************************

As defined in ADA 1100, Section 10, "Viewset VS-01," introductory paragraphs,
VS-01 is the viewset preferred by the American Board of Orthodontics for case
submission and display. It is most commonly used by orthodontic practitioners
and orthodontic software.

The parenthetical source citations in Sections 3.1.4.1.3.2 through 3.1.4.1.3.5
use the clause numbering ADA 1100 2025 release. The normative reference remains
the published edition listed in Section 3.1.3.

Common Viewset Display Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Image Display shall apply the following requirements when displaying any
of VS-01 through VS-04. VS-02 through VS-04 inherit the common VS-01
requirements except where their respective sections specify otherwise.

- The Image Display shall display the complete viewset within one display
  area. (ADA 1100, Section 10, VS-01 requirement 5(iii).)
- The Image Display shall provide visible separation between adjacent display
  boxes. The separation shall not obscure an image, contain advertising or
  unrelated content, or interfere with comparison of adjacent images. (ADA
  1100, Section 10, VS-01 requirements 5(i), 5(ii), and 5(iv).)
- The Image Display shall assign each image to the location specified by the
  applicable image location table. Assignment shall be based on the image-view
  semantics encoded as specified in :ref:`Section 7.4.2.1.1
  <view_code_sequence>` and not on filename or retrieval order. (ADA 1100,
  Section 10, VS-01 requirement 7 and Tables 4.1 through 4.4; DENT-OIP adds
  the explicit DICOM assignment rule.)
- All displayed images shall be of the same patient and shall have been
  acquired during the same encounter or clinical time frame, before a
  clinically significant change in the patient. (ADA 1100, Section 10, VS-01
  requirements 10 and 11.)
- Images acquired in centric occlusion and images acquired in centric relation
  shall not be mixed in one viewset. (ADA 1100, Section 10, note following
  Table 4.1.)
- The Image Display shall preserve the clinical content of each image. It may
  scale and position an image within its assigned box, but shall not otherwise
  alter the image unless the alteration is documented in the DICOM instance.
  (ADA 1100, Section 10, VS-01 requirements 8 and 9.)
- Mirror-acquired images identified as corrected shall be displayed in the
  corrected anatomical orientation. (ADA 1100, Section 10, Tables 4.1 through
  4.4, entries identified as ``WM.BC``; DENT-OIP states the display behavior.)
- The Image Display shall maintain each image's pixel aspect ratio when
  scaling it to fit its assigned box. (DENT-OIP constraint supporting ADA
  1100, Section 10, VS-01 requirement 8.)
- The information box shall display the patient's initials, age in years and
  months, and the acquisition date of the photographs. (ADA 1100, Section 10,
  Tables 4.1 through 4.4, ``Text box`` or ``TEXT`` entry.)

For normalized layout coordinates, the lower-left corner of the complete
viewset is the origin ``(0,0)`` and the upper-right corner is ``(1,1)``. For a
display area with pixel width *W* and pixel height *H*, the Image Display shall
calculate pixel coordinates as ``x = normalized-x * W`` and
``y = normalized-y * H``. (ADA 1100, Section 10, VS-01 through VS-03
Construction Details, bullets 2 and 4 and steps 3 and 4.)

In the following tables, ILC means Image Location Code. ILC values number
display boxes from left to right and from top to bottom. (ADA 1100, Section 10,
notes following Table 4.1.)

VS-01 Layout
^^^^^^^^^^^^

The Image Display shall construct VS-01 as follows:

- The layout shall contain nine equal-width boxes arranged in three rows and
  three columns. (ADA 1100, Section 10, VS-01 requirements 1 through 3.)
- The height of the three boxes within each row shall be identical. (ADA 1100,
  Section 10, VS-01 requirement 6.)
- The width-to-height ratio of each top-row box shall be ``0.866``. (ADA 1100,
  Section 10, VS-01 requirement 4, Top Row.)
- The width-to-height ratio of each middle-row box shall be ``1.432``. (ADA
  1100, Section 10, VS-01 requirement 4, Middle Row.)
- The width-to-height ratio of each bottom-row box shall be ``1.794``. (ADA
  1100, Section 10, VS-01 requirement 4, Bottom Row.)
- The width-to-height ratio of the complete layout shall be ``1.000:0.829``.
  (ADA 1100, Section 10, VS-01 Construction Details, bullet 1.)
- The boxes shall contain the images or information specified in Table
  3.1.4.1.3.2-1. (ADA 1100, Section 10, VS-01 requirement 7 and Table 4.1.)

**Table 3.1.4.1.3.2-1: VS-01 Image Locations**

Source: ADA 1100, Section 10, Table 4.1, corresponding ILC row.

.. list-table::
   :header-rows: 1
   :widths: 8 22 70

   * - ILC
     - ADA 1100 term
     - Required content
   * - 01
     - EO.RP.LR.CO
     - Extraoral right profile, subject facing the observer's right, lips
       relaxed, teeth in centric occlusion
   * - 02
     - EO.FF.LR.CO
     - Extraoral full face, lips relaxed, teeth in centric occlusion
   * - 03
     - EO.FF.FS.CO
     - Extraoral full face, full smile, teeth in centric occlusion
   * - 04
     - IO.MX.MO.OV.WM.BC
     - Intraoral maxillary occlusal view, mouth open, acquired with a mirror
       and corrected
   * - 05
     - TEXT
     - Patient information box
   * - 06
     - IO.MD.MO.OV.WM.BC
     - Intraoral mandibular occlusal view, mouth open, acquired with a mirror
       and corrected
   * - 07
     - IO.RB.CO.NM or IO.RB.CO.WM.BC
     - Intraoral right buccal segment in centric occlusion, acquired directly
       or with a mirror and corrected
   * - 08
     - IO.FV.CO.NM
     - Intraoral frontal view in centric occlusion
   * - 09
     - IO.LB.CO.NM or IO.LB.CO.WM.BC
     - Intraoral left buccal segment in centric occlusion, acquired directly
       or with a mirror and corrected

Informative illustrations are provided in :ref:`Appendix B
<viewset_vs01_examples>`.

3.1.4.1.3.3 Viewset VS-02
*************************

VS-02 is a craniofacial viewset used primarily to document orthognathic and
craniofacial surgical treatment. Its profile and 45-degree views support
comparison of both sides of the face. (ADA 1100, Section 10, "Viewset VS-02,"
introductory paragraph.)

VS-02 Layout
^^^^^^^^^^^^

The Image Display shall construct VS-02 as follows:

- The layout shall contain thirteen equal-width boxes arranged as six boxes
  in the top row, four centered boxes in the middle row, and three centered
  boxes in the bottom row. (ADA 1100, Section 10, Figure A2-1.)
- The height of the boxes within each row shall be identical. (ADA 1100,
  Section 10, Figure A2-1.)
- The width-to-height ratio of each top-row box shall be ``0.370``. (Derived
  from ADA 1100, Section 10, Figure A2-1.)
- The width-to-height ratio of each middle-row box shall be ``0.611``. (Derived
  from ADA 1100, Section 10, Figure A2-1.)
- The width-to-height ratio of each bottom-row box shall be ``0.773``. (Derived
  from ADA 1100, Section 10, Figure A2-1.)
- The width-to-height ratio of the complete layout shall be ``1.000:0.544``.
  (ADA 1100, Section 10, VS-02 Construction Details, bullet 1.)
- The boxes shall contain the images or information specified in Table
  3.1.4.1.3.3-1. (ADA 1100, Section 10, Table 4.2.)

**Table 3.1.4.1.3.3-1: VS-02 Image Locations**

Source: ADA 1100, Section 10, Table 4.2, corresponding ILC row.

.. list-table::
   :header-rows: 1
   :widths: 8 22 70

   * - ILC
     - ADA 1100 term
     - Required content
   * - 01
     - EO.RP.LR.CO
     - Extraoral right profile, lips relaxed, teeth in centric occlusion
   * - 02
     - EO.RP.LR.CO.45
     - Extraoral 45-degree right profile, lips relaxed, teeth in centric
       occlusion
   * - 03
     - EO.FF.LR.CO
     - Extraoral full face, lips relaxed, teeth in centric occlusion
   * - 04
     - EO.FF.FS.CO
     - Extraoral full face, full smile, teeth in centric occlusion
   * - 05
     - EO.LP.LR.CO.45
     - Extraoral 45-degree left profile, lips relaxed, teeth in centric
       occlusion
   * - 06
     - EO.LP.LR.CO
     - Extraoral left profile, lips relaxed, teeth in centric occlusion
   * - 07
     - IO.MX.OV.MO.WM.BC
     - Intraoral maxillary occlusal view, mouth open, acquired with a mirror
       and corrected
   * - 08
     - IO.MD.OV.MO.WM.BC
     - Intraoral mandibular occlusal view, mouth open, acquired with a mirror
       and corrected
   * - 09
     - IO.FV.IV.CO.NM
     - Intraoral inferior frontal view in centric occlusion, showing the depth
       of the bite
   * - 10
     - TEXT
     - Patient information box
   * - 11
     - IO.RB.CO.NM or IO.RB.CO.WM.BC
     - Intraoral right buccal segment in centric occlusion, acquired directly
       or with a mirror and corrected
   * - 12
     - IO.FV.CO.NM or IO.FV.CO.WM.BC
     - Intraoral frontal view in centric occlusion, acquired directly or with
       a mirror and corrected
   * - 13
     - IO.LB.CO.NM or IO.LB.CO.WM.BC
     - Intraoral left buccal segment in centric occlusion, acquired directly
       or with a mirror and corrected

Informative illustrations are provided in :ref:`Appendix B
<viewset_vs02_examples>`.

3.1.4.1.3.4 Viewset VS-03
*************************

VS-03 is a supplementary patient-record viewset used to document findings such
as excessive overjet or impinging deep bite. It includes lateral dentition
views showing overjet and an inferior frontal dentition view showing bite
depth. (ADA 1100, Section 10, "Viewset VS-03," introductory paragraph.)

VS-03 Layout
^^^^^^^^^^^^

The Image Display shall apply the VS-01 display requirements except as follows.
(ADA 1100, Section 10, VS-03 compliance statement.)

- The layout shall contain thirteen equal-width boxes in an inverted-pyramid
  arrangement: five boxes in the top row, four centered boxes in the middle
  row, and four centered boxes in the bottom row. (ADA 1100, Section 10, VS-03
  requirements 1 through 3.)
- The height of the boxes within each row shall be identical. (ADA 1100,
  Section 10, VS-03 compliance statement and VS-01 requirement 6.)
- The width-to-height ratio of each top-row box shall be ``0.370``. (Derived
  from ADA 1100, Section 10, Figure A3-1.)
- The width-to-height ratio of each middle-row box shall be ``0.611``. (Derived
  from ADA 1100, Section 10, Figure A3-1.)
- The width-to-height ratio of each bottom-row box shall be ``0.773``. (Derived
  from ADA 1100, Section 10, Figure A3-1.)
- The width-to-height ratio of the complete layout shall be ``1.000:0.544``.
  (ADA 1100, Section 10, VS-03 Construction Details, bullet 1.)
- The boxes shall contain the images or information specified in Table
  3.1.4.1.3.4-1. (ADA 1100, Section 10, Table 4.3.)

**Table 3.1.4.1.3.4-1: VS-03 Image Locations**

Source: ADA 1100, Section 10, Table 4.3, corresponding ILC row.

.. list-table::
   :header-rows: 1
   :widths: 8 22 70

   * - ILC
     - ADA 1100 term
     - Required content
   * - 01
     - EO.FF.LR.CO
     - Extraoral full face, lips closed, teeth in centric occlusion
   * - 02
     - EO.FF.FS.CO
     - Extraoral full face, full smile, teeth in centric occlusion
   * - 03
     - EO.RP.LR.CO
     - Extraoral right profile, subject facing the observer's right, lips
       relaxed, teeth in centric occlusion
   * - 04
     - EO.RP.FS.CO
     - Extraoral right profile, subject facing the observer's right, full
       smile, teeth in centric occlusion
   * - 05
     - EO.LP.LR.CO
     - Extraoral left profile, subject facing the observer's left, lips
       relaxed, teeth in centric occlusion
   * - 06
     - IO.MX.MO.OV.WM.BC
     - Intraoral maxillary occlusal view, mouth open, acquired with a mirror
       and corrected
   * - 07
     - IO.MD.MO.OV.WM.BC
     - Intraoral mandibular occlusal view, mouth open, acquired with a mirror
       and corrected
   * - 08
     - IO.FV.IV.CO.NM
     - Intraoral inferior frontal view in centric occlusion, showing bite depth
   * - 09
     - IO.RL.CO.OJ.NM
     - Intraoral right lateral view in centric occlusion, showing overjet
   * - 10
     - IO.RB.CO.NM or IO.RB.CO.WM.BC
     - Intraoral right buccal segment in centric occlusion, acquired directly
       or with a mirror and corrected
   * - 11
     - IO.FV.CO.NM
     - Intraoral frontal view in centric occlusion
   * - 12
     - IO.LB.CO.NM or IO.LB.CO.WM.BC
     - Intraoral left buccal segment in centric occlusion, acquired directly
       or with a mirror and corrected
   * - 13
     - TEXT
     - Patient information box

Informative illustrations are provided in :ref:`Appendix B
<viewset_vs03_examples>`.

3.1.4.1.3.5 Viewset VS-04
*************************

VS-04 is a supplementary patient-record viewset intended to support assessment
of craniofacial asymmetry. It includes superior and inferior views of the face
and views of both sides of the face. (ADA 1100, Section 10, "Viewset VS-04,"
introductory paragraph.)

VS-04 Layout
^^^^^^^^^^^^

The Image Display shall apply the VS-01 display requirements except as follows.
(ADA 1100, Section 10, VS-04 compliance statement.)

- The layout shall contain twelve equal-width boxes arranged as four columns
  and three rows. (ADA 1100, Section 10, VS-04 requirements 1 through 3.)
- The height of the four boxes within each row shall be identical. (ADA 1100,
  Section 10, VS-04 compliance statement and VS-01 requirement 6.)
- The width-to-height ratio of each top- and middle-row box shall be ``0.635``.
  (DENT-OIP constraint derived from the ADA 1100 working-layout diagram; not
  specified in the May 2025 ballot.)
- The width-to-height ratio of each bottom-row box shall be ``1.315``.
  (DENT-OIP constraint derived from the ADA 1100 working-layout diagram; not
  specified in the May 2025 ballot.)
- The width-to-height ratio of the complete layout shall be ``1.000:0.733``.
  (DENT-OIP constraint from the ADA 1100 working-layout Construction Details;
  not specified in the May 2025 ballot.)
- The boxes shall contain the images or information specified in Table
  3.1.4.1.3.5-1. (ADA 1100, Section 10, Table 4.4.)

**Table 3.1.4.1.3.5-1: VS-04 Image Locations**

Source: ADA 1100, Section 10, Table 4.4, corresponding ILC row.

.. list-table::
   :header-rows: 1
   :widths: 8 22 70

   * - ILC
     - ADA 1100 term
     - Required content
   * - 01
     - EO.RP.LR.CO
     - Extraoral right profile, subject facing the observer's right, lips
       relaxed, teeth in centric occlusion
   * - 02
     - EO.RP.LR.CO.45
     - Extraoral 45-degree right profile, lips relaxed, teeth in centric
       occlusion
   * - 03
     - EO.FF.LR.CO
     - Extraoral full face, lips closed, teeth in centric occlusion
   * - 04
     - EO.FF.FS.CO
     - Extraoral full face, full smile, teeth in centric occlusion
   * - 05
     - EO.OF.SV
     - Extraoral superior face view showing forehead, infraorbital-rim
       contours, nasal dorsum, upper lip, and chin
   * - 06
     - EO.OF.IV
     - Extraoral inferior face view showing mandibular lower border, nares,
       infraorbital-rim contours, and forehead contours
   * - 07
     - EO.LP.LR.CO.45
     - Extraoral 45-degree left profile, lips relaxed, teeth in centric
       occlusion
   * - 08
     - EO.LP.LR.CO
     - Extraoral left profile, subject facing the observer's left, lips
       relaxed, teeth in centric occlusion
   * - 09
     - IO.RB.CO.NM or IO.RB.CO.WM.BC
     - Intraoral right buccal segment in centric occlusion, acquired directly
       or with a mirror and corrected
   * - 10
     - IO.FV.CO.NM
     - Intraoral frontal view in centric occlusion
   * - 11
     - IO.LB.CO.NM or IO.LB.CO.WM.BC
     - Intraoral left buccal segment in centric occlusion, acquired directly
       or with a mirror and corrected
   * - 12
     - TEXT
     - Patient information box

Informative illustrations are provided in :ref:`Appendix B
<viewset_vs04_examples>`.
