.. _vl_photographic_image_module_constraints:

7.4.2 VL Photographic Image IOD - Module Constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This section contains IHE constraints on Modules that are specific to the VL Phtotgraphic Image IOD.

.. _vl_image_module:

7.4.2.1 VL Image Module
+++++++++++++++++++++++

This normative section contains a description of the DICOM tags defined in the VL Image module which are relevant to orthodontic photography.  This section describes the requirements for storing the image type of an orthodontic photograph as a code in a DICOM Visible Light (VL) object. While the orthodontic image can be fully represented using a combination of various DICOM attributes, there exist many situations where it is more convenient to encode the image type in a single code.

For orthodontic photography, we make use of the VL Image Module  to store the conditions of the patient during the photographic acquisition session (lips and mouth open, closed, smiling, relaxed, etc), the occlusal relationship (centric occlusion, centric relation, see :ref:`definitions`), the Image View (projection) and the Image View Modifier (direct or indirect).

**References:**

+ `DICOM PS3.3: C.8.12.1  <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.12.html#sect_C.8.12.1>`_ "VL Image Module"
+ `DICOM PS3.16: CID 4062 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4062.html>`_ "VL View"
+ `DICOM PS3.16: CID 4063 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4063.html>`_ "VL Dental View"
+ `DICOM PS3.16: CID 4065 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4065.html>`_  "VL Dental View Modifier"
+ Extensions in Table 7.4.2.1-1 are from ???

**Table 7.4.2.1-1 VL Image Module Attribute Requirements**

.. list-table::
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - View Code Sequence 
      - (0054,0220)
      - O+ (Recommended. SHOULD be specified, if known. Only one value is allowed.)
      - The projection of the anatomic region of interest on an image receptor.  Use one of the lateral projections for photographs of the buccal (cheek) region.   See Section 7.4.2.1.1.
    * - > View Code Modifier Sequence 
      - (0054,0221)
      - C (Recommended. SHOULD be specified, if known. Only one value is allowed.)
      - Sequence that provides modifiers for the view of the anatomic region of interest in the image.   See `CID 4065 <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4065.html>`_ "VL Dental View Modifier".

7.4.2.1.1 View Code Sequence (0054,0220)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Buccal projection* is not present in SNOMED-CT, but there are various lateral projections. *Buccal (intended site)* `SCT 763825005 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=763825005&edition=MAIN&release=&languages=en>`__ in the anatomic region sequence is enough to specify un-ambiguosly that this photograph is a buccal view. 

Allowed values:

- `CID 4062: VL View <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4062.html>`__

- `CID 4063: VL Dental View <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_4063.html>`__

**Table CID 4062. VL View**

.. list-table:: 
    :header-rows: 1

    * - Code Scheme Designator
      - Code Value
      - Code Meaning
      - Notes
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

**Table CID 4063. VL Dental View**

.. list-table:: 
    :header-rows: 1

    * - Code Scheme Designator
      - Code Value
      - Code Meaning
      - Notes
    * - SCT
      - `260499007 <https://browser.ihtsdotools.org/?perspective=full&conceptId1=260499007&edition=MAIN&release=&languages=en>`__
      - Occlusal projection (qualifier value)
      - 

.. _vl_photographic_acquisition:

7.4.2.2 VL Photographic Acquisition
+++++++++++++++++++++++++++++++++++

This normative section contains extensions to  DICOM tags defined in the VL Photographic Acquisition Module which are necessary to fully describe orthodontic views (photographs).

Most of the tags of this module have a direct mapping to EXIF tags that come from digital cameras. 

Any EXIF tag which comes from the camera, should be mapped and stored in the VL Photographic Acquisition Module, making use of the table specified in `DICOM PS3.17: Section NNNN <https://dicom.nema.org/medical/dicom/current/output/html/part17.html#chapter_NNNN>`__ "Mapping of Visible Light Photography Related Attributes to EXIF and TIFF/EP Tags".

**References:**

+ `DICOM PS3.3: C.8.12.11 <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.12.11.html>`_
+ Extensions in Table 7.4.2.2-1 are from ???

.. list-table:: **Table 7.4.2.2-1 VL Photographic Acquisition Module Attribute Requirements**
    :header-rows: 1

    * - **Attribute**
      - **Tag**
      - **Type**
      - **Attribute Description**
    * - File Source
      - (0016,003A)
      - RC+ (confirm this)
      - Indicates the type of scene. In orthodontic photography, digital still cameras record the image and this tag value shall be set to 3, indicating that the image was taken with a digital still camera (DSC).
    * - Scene Type
      - (0016,003B)
      - R+ (confirm this)
      - Indicates the type of scene. In orthodontic photography, digital still cameras record the image and this tag value must shall be set to 1, indicating that the image was directly photographed.
    * - TBD
      - TBD
      - TBD
      - TBD

**Requirements**

1. **ViewCodeSequence Usage**

   - The DICOM attribute ``ViewCodeSequence`` (Tag: (0054,0220)) SHALL be used to encode the image type for orthodontic photographs.
   - Only a single Item SHALL be present in the ``ViewCodeSequence`` for each image type code.

2. **Context Identifier (CID) and Private Extension**

   - The ``ContextIdentifier`` (Tag: (0008,010F)) of the code item in ``ViewCodeSequence`` SHALL be set to the value ``4063`` (CID 4063, "VL Dental View") for standard codes.
   - For private or proprietary codes, the ``ContextIdentifier`` SHALL be set to ``4063`` with extension attributes as described below.

3. **Context Group Extension Attributes**

   - If a code is not part of the standard CID 4063, the following attributes SHALL be present in the code item:
   
     - ``ContextGroupExtensionFlag`` (Tag: (0008,010B)) = ``'Y'``
     - ``ContextGroupLocalVersion`` (Tag: (0008,0107)) = the current date in ``YYYYMMDD`` format
     - ``ContextGroupExtensionCreatorUID`` (Tag: (0008,010D)) = a UID identifying the entity responsible for the code (see below)
   
   - The ``ContextGroupExtensionCreatorUID``:
     - SHALL be set by the application or site generating the code.

4. **Code Triplet**

   - Each code item in ``ViewCodeSequence`` SHALL include:
     - ``CodeValue`` (Tag: (0008,0100)): The code identifier (max 16 chars, or use Long/URN Code Value as appropriate)
     - ``CodingSchemeDesignator`` (Tag: (0008,0102)): The coding scheme (e.g., ``99ORG`` for private codes)
     - ``CodeMeaning`` (Tag: (0008,0104)): Human-readable meaning of the code

5. **Setting and Retrieving the Code**

   - When setting the image type code, the implementation SHALL:
     - Set or update the code item in ``ViewCodeSequence`` matching both ``ContextIdentifier`` and ``ContextGroupExtensionFlag``.
     - If no such item exists, append a new item.
   - When retrieving the image type code, the implementation SHALL:
     - Return the first item in ``ViewCodeSequence`` where ``ContextIdentifier`` and ``ContextGroupExtensionFlag`` match the expected values.

6. **Interoperability**

   - Receivers of the DICOM object SHOULD recognize and preserve private extension codes, including all extension attributes.
   - Receivers MAY ignore codes with unknown ``ContextGroupExtensionCreatorUID``, but SHALL keep them.

7. **Example**

.. code-block:: python

   code = Dataset()
   code.CodeValue = 'EV20'
   code.CodingSchemeDesignator = '99OPOR'
   code.CodeMeaning = 'Extraoral, Full Face, Full Smile, Centric Relation'
   code.ContextIdentifier = '4063'
   code.ContextGroupExtensionFlag = 'Y'
   code.ContextGroupLocalVersion = '20240625'
   code.ContextGroupExtensionCreatorUID = '1.2.826.0.1.3680043.10.1234'

   ds.ViewCodeSequence = Sequence([code])

8. **Compliance**

   - Implementations SHALL follow this specification for all orthodontic photographs requiring non-standard image type codes.
   - Implementations SHOULD provide a mechanism for the application to specify the ``ContextGroupExtensionCreatorUID``.
   - Implementations MAY provide a fallback UID for development or testing, but SHALL warn the user.

.. _vl_photographic_acquisition_module:

7.4.2.2 VL Photographic Acquisition Module
++++++++++++++++++++++++++++++++++++++++++

This normative section contains a description of the DICOM tags defined in the VL Photographic Acquisition module which are relevant to orthodontic photography.

<*OPEN ISSUE: Are there any constraints in this module*>

**References:**

+ `DICOM PS3.3: C.8.12.11  <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.12.11.html>`_ "VL Photographic Acquisition Module"
