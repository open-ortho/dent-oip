Anatomic Region Sequence (0008,2218)
====================================

The use of the Anatomic Region Sequence, populated with standard values, enables seamless interoperability of imaging data regardless of whether images are used within a site or across different sites and systems.

According to DICOM, this sequence identifies the anatomic region of interest, i.e., external anatomy, surface anatomy, or general region of the body. Only a single Item is permitted in this Sequence.

When applied to orthodontic photographs, the anatomic region is either Face for extraoral photographs, or Jaw for intraoral photographs. See :ref:`Intraoral Views <intraoral views>` and :ref:`Extraoral Views <extraoral views>` in Appendix for the correct SNOMED codes to use.


Anatomic Region Modifier Sequence (0008,2220)
---------------------------------------------

.. table:: Anatomic Region Modifier for Extra-oral Photography

   +----------+----------+----------+----------+----------+----------+
   | Coding   | Code     | Code     | SNODENT  | S        | UMSL     |
   | Scheme   | Value    | Meaning  | Code     | NOMED-RT | Concept  |
   | De       |          |          |          | ID       | Unique   |
   | signator |          |          |          |          | ID       |
   +==========+==========+==========+==========+==========+==========+
   |          |          |          |          |          |          |
   +----------+----------+----------+----------+----------+----------+

.. table:: Anatomic Region Modifier for Intra-oral Photography

   +----------+----------+----------+----------+----------+----------+
   | Coding   | Code     | Code     | SNODENT  | S        | UMSL     |
   | Scheme   | Value    | Meaning  | Code     | NOMED-RT | Concept  |
   | De       |          |          |          | ID       | Unique   |
   | signator |          |          |          |          | ID       |
   +==========+==========+==========+==========+==========+==========+
   |          |          |          |          |          |          |
   +----------+----------+----------+----------+----------+----------+

