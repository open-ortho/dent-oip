.. _definitions:
Definitions
===========

.. _centric relation:
.. _centric occlusion:
Centric relation and Centric occlusion
--------------------------------------


Centric relation and centric occlusion are terms which define the mandibular jaw position of the patient. 

In orthodontics, the doctor asks the patient to place the mandible in one of these positions when imaging the patient in order to provide better informed clinical decisions. It is important that these positions are recorded with the image as these two positions can be measured or compared.

According to Hidaka (2002), centric occlusion (CO) is *the patient's full or habitual occlusion* whereas centric relation (CR) is the position of the condyle when *it is forward and uppermost against the eminence when the joint is loaded by the elevating musculature.*

.. note::
    Both centric relation and centric occlusion define a type of dental occlusion, i.e. how teeth occlude. In other words they specify how the cusps of the opposing teeth fitting together come into contact.
    
    It is therefore not possible to have the mouth open while being in centric occlusion or centric relation. The DICOM tags for the photograph can therefore not contain both *mouth open* or *teeth apart* and *centric relation* or *centric occlusion* at the same time.

Definitions
***********

.. list-table:: 
    :header-rows: 1

    * - Term
      - Definition
    * - Centric occlusion (CO)
      - The relation of the mandibular and maxillary teeth in maximum dental intercuspation independent of condylar position.
    * - Centric relation (CR)
      - The relation of the mandible to the maxilla when the mandibular condyles are in a physiologically optimal position independent of tooth contacts.
    * - Functional shift (CR-CO shift)
      - A forward, backward or lateral deflection of the mandible from centric relation to centric occlusion due to premature contact of the teeth in centric relation.



See also :ref:`functional conditions present during acquisition`.


Overjet
-------

.. _overjet:

Quoting from Draker (1960):


    *Overjet in millimeters is recorded with the patient in the centric occlusion and measured using a ruler from the labial of the lower incisor to the labial of the upper incisor. The measurement could apply to a protruding single tooth as well as to the whole arch. The measurement is read and rounded off to the nearest millimeter.*


Overjet is a clinical diagnosis and requires clinical interpretation and therefore is not stored in the original DICOM image object. However, in order to properly measure Overjet, a measuring device such as a millimeter ruler is required in the image itself and should be recorded accordingly. See :ref:`DICOM Device Sequence <device sequence>` for details.

Occlusal cant
-------------

.. _occlusal cant:

Quoting from `Olivares et al (2013) <https://doi.org/10.4317%2Fmedoral.18335>`__:

    *Occlusal plane canting is one characteristic that must be evaluated in any assessment of smile esthetics. It describes the vertical position of the teeth when the left and right sides are different and this is defined as the rotation upwards or downwards in the transversal plane of one side over the other.*

Occlusal canting is often measured visually with a :ref:`Tongue Depressor<tongue_depressor>`.

See :ref:`EV-39 <EV39>` and :ref:`Tongue Depressor<tongue_depressor>`
