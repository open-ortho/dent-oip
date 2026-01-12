.. _vl image:

7.4.x Image Modules
+++++++++++++++++++
This section contains IHE constraints on Modules that are common across multiple DICOM Composite IODs.

7.4.x.y VL Image Module
++++++++++++++++++++++

This normative section contains extensions to DICOM tags defined in the Patient module .

This normative section contains a description of the DICOM tags defined in the VL Image module which are relevant to orthodontic photography.

For orthodontic photography, we make use of the `VL Image Module <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.12.html#table_C.8-77>`__ to store the conditions of the patient during the photographic acquisition session (lips and mouth open, closed, smiling, relaxed, etc), the occlusal relationship (centric occlusion, centric relation, see :ref:`definitions`), the Image View (projection) and the Image View Modifier (direct or indirect).


**References:**

+ `DICOM PS3.3: C.7.1.1  <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.12.html#sect_C.8.12.1>`_ "VL Image Module"
+ Extensions in 7.4.x.y-1 are from ???

**Table 7.4.x.y-1 VL Image Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - View Code Sequence 
      - (0054,0220)
      - O+ (Recommended. SHOULD be specified, if known. Only one value is allowed.)
      - The projection of the anatomic region of interest on an image receptor.  Use one of the lateral projections for photographs of the buccal (cheek) region.   See Section 7.4.x.y.1.
    * - View Code Modifier Sequence 
      - (0054,0221)
      - C (Recommended. SHOULD be specified, if known. Only one value is allowed.)
      - The projection of the anatomic region of interest on an image receptor.  Use one of the lateral projections for photographs of the buccal (cheek) region.   See Section 7.4.x.y.1.

7.4.x.y.1 View Code Sequence (0054,0220)
+++++++++++++++++++++++++++++++++++++++

*Buccal projection* is not present in SNOMED-CT, but there are various lateral projections. *Buccal (intended site)* `SCT 763825005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=763825005&edition=MAIN&release=&languages=en>`__ in the anatomic region sequence is enough to specify un-ambiguosly that this photograph is a buccal view. 

Allowed values:
- `**CID 4062**: VL View <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4062.html>`__
- `**CID 4063**: VL Dental View <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4063.html>`__

.. _cid-4062:
.. list-table:: Table CID 4062. VL View
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `399033003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399033003&edition=MAIN&release=&languages=en>`__
      - frontal
      - 
    * - SCT
      - `399173006 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399173006&edition=MAIN&release=&languages=en>`__
      - left lateral 
      - For left buccal photographs
    * - SCT
      - `260421001 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260421001&edition=MAIN&release=&languages=en>`__
      - left lateral oblique
      - 
    * - SCT
      - `399198007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399198007&edition=MAIN&release=&languages=en>`__
      - right lateral projection
      - For right buccal photographs
    * - SCT
      - `260424009 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260424009&edition=MAIN&release=&languages=en>`__
      - right lateral oblique
      - 
    * - SCT
      - `399182000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399182000&edition=MAIN&release=&languages=en>`__
      - oblique projection
      - 
    * - SCT
      - `260454004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260454004&edition=MAIN&release=&languages=en>`__
      - 45 degree projection
      - 
    * - SCT
      - `260427002 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260427002&edition=MAIN&release=&languages=en>`__
      - oblique lateral
      - Mandatory for :ref:`IV24 <IV24>`, :ref:`IV25 <IV25>`, :ref:`IV26 <IV26>`, :ref:`IV27 <IV27>` 
    * - SCT
      - `399255003 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=399255003&edition=MAIN&release=&languages=en>`__
      - submentovertical
      - Mandatory for :ref:`EV36 <EV36>`
    * - SCT
      - `260461000 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260461000&edition=MAIN&release=&languages=en>`__
      - vertex 
      - Mandatory for :ref:`EV37 <EV37>`
    * - SCT
      - `410514004 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=410514004&edition=MAIN&release=&languages=en>`__
      - Unknown (qualifier value)
      - This code is used when the photograph is taken without specific attention to the projection, prioritizing image detail over projection accuracy. In cases where the :ref:ViewModifierCodeSequence is required, it must be included. Since the :ref:ViewModifierCodeSequence also requires the parent :ref:ViewCodeSequence, the sequence cannot be omitted, and the value 'Unknown' SHALL be used.

.. _cid-4063:
.. list-table:: Table CID 4063. VL Dental View
    :header-rows: 1

    * - code scheme designator
      - code value
      - code meaning
      - notes
    * - SCT
      - `260499007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260499007&edition=MAIN&release=&languages=en>`__
      - Occlusal projection (qualifier value)

.. toctree::
	:glob:
	:maxdepth: 2

	./*
