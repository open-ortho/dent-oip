.. _scroll-bookmark-7:

Patient Orientation (0020,0020)
===============================

Patient direction of the rows and columns of the image. Required
because:

1. This IOD VL Photographic Image does not require Image Orientation
   (Patient) (0020,0037) or Image Position (Patient) (0020,0032)

2. This IOD VL Photographic Image does not require Image Orientation
   (Slide) (0048,0102).

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
