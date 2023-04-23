.. _patient orientation:

Patient Orientation (0020,0020)
===============================

Patient direction of the rows and columns of the image. Required because:

1. This IOD VL Photographic Image does not require Image Orientation
   (Patient) (0020,0037) or Image Position (Patient) (0020,0032)

2. This IOD VL Photographic Image does not require Image Orientation
   (Slide) (0048,0102).


Allowed Values
--------------

.. list-table::
   :header-rows: 1

   * - Meaning
     - DICOM Enumerated Value
     - SNOMED Code
   * - Anterior
     - A
     - `(255549009, SCT, "Anterior") <http://snomed.info/id/255549009>`__
   * - Posterior
     - P
     - `(255551008, SCT, "Posterior") <http://snomed.info/id/255551008>`__
   * - Left
     - L
     - `(7771000, SCT, "Left") <http://snomed.info/id/7771000>`__
   * - Right
     - R
     - `(24028007, SCT, "Right") <http://snomed.info/id/24028007>`__
.. See TROSD-65
   * - Top (towards the head)
     - H
     - `(421812003, SCT, "Top") <http://snomed.info/id/421812003>`__
.. See TROSD-65
   * - Bottom (towards the lower limbs)
     - F
     - `(421610009, SCT, "Bottom") <http://snomed.info/id/421610009>`__

Choosing the Correct Patient Orientation
----------------------------------------

Patient Orientation (0020,0020) relative to the image plane shall be
specified by two values that designate the anatomical direction of the
positive row axis (left to right) and the positive column axis (top to
bottom).

-  The first entry is the direction of the rows, given by the direction
   of the last pixel in the first row from the first pixel in that row.

-  The second entry is the direction of the columns, given by the
   direction of the last pixel in the first column from the first pixel
   in that column.

Since Anatomical Orientation Type (0010,2210) is absent (or has a value
of BIPED), anatomical direction shall be designated by abbreviations
using the capital letters:

= =========
A anterior
P posterior
R right
L left
H head
F foot
= =========

Example: a Right Profile photograph of the face, would have Patient
Orientation set to ['A','F']
