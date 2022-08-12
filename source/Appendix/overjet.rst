.. _overjet:

Overjet
========

Quoting from Draker, 1960:

    Overjet in millimeters is recorded with the patient in the centric occlusion and measured using a ruler from the labial of the lower incisor to the labial of the upper incisor. The measurement could apply to a protruding single tooth as well as to the whole arch. The measurement is read and rounded off to the nearest millimeter. 


Overjet in DICOM
****************

Overjet is a clinical diagnosis and is therefore not reccommended to store in DICOM. However, in order to properly measure Overjet, a measuring device such as a ruler is required in the image itself and should be recorded accordingly. See :ref:`DICOM Device Sequence <device sequence>` for details.

Why are we not storing Overjet as a SNOMED code somewhere in DICOM?
*******************************************************************

HLD/OJ measurement is a clinical issue. 1107 shouldn't be clinical in nature, but more technical.

