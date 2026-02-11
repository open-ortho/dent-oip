Introduction to this Supplement
===============================
The intended audience of this document is the medical imaging software developers or medical imaging device manufacturer who deals with visible light digital photography.

*<TO DO: First, briefly describe the current landscape in dental imaging, presumably with many proprietary implementations.  Then describe how the OIP profile addresses this problem.>*

The document, along with its accompanying CSV files and DICOM sample files found in the Volume 3 Appendices, provides a detailed implementation guide for encoding orthodontic/craniofacial
views using DICOM with SNOMED CT terminology. 

Using the Orthodontic Imaging Profile to implement a standard encoding of Visual Light Photographic Images ensures interoperability between vendors and enables the imaging software developer or device manufacturer to spend less time designing and implementing novel and proprietary ways for connecting with other products.  That work is alreay done and defined. All that needs to be done is implement it in your product.


.. note::

    The :ref:`list of views presented in the Appendix <view_examples>` of this standard serve as example for encoding a virtually unlimited number of view types. As long as the implementer follows the guidelines of this standard, the implementation will comply to this standard, even if the view represented in such implementation is not included as one of the views in the Appendix.

This guide depends on ADA SCDI White Paper 1100 -
Orthodontic/Craniofacial/Forensic Photographic Views and Viewsets available online on the ADA Catalog.

Open Issues and Questions
=========================
This section identifies open issues/questions that need to be addressed prior to publishing OIP for Trial Implementation. We are specifically soliciting public comments for these items:

#. :ref:`Vol 1 Sec 3.2 <oip_integration_profile_options>` -- In this draft of OIP, we defined options for the Content Creator to enable it to declare which type(s) of DICOM objects it is able to produce.  Should the Content Consumer that is compliant with this profile shall be able to 'process' all of the types of DICOM images in 6 options (a common pattern in IHE to enhance interoperability; e.g., a Consumer that is a DICOM archive is able to store many types of DICOM objects), or is it more appropriate to have the same options for the Consumer as we have for the Creator, enabling a Consumer that supports storing/displaying/processing a subset of the DICOM objects defined to be compliant with OIP?

#. :ref:`Vol 1 Sec 3.2 <oip_integration_profile_options>` -- This revision of the table proposes Options on the Image Display for support of Structured Display and Hanging Protocol.  Should this remain in OIP, be deferred to a future revision of the profile (or made mandatory, if that is appropriate)?

#. :ref:`Vol 1 Sec 3.2.7 and 3.2.8 <structured_display_option>` -- For the Structured Display and Hanging Protocol Options, the Image Display that supports either of the options must be able to both create the associated IOD based on the charactstics and content of a given rendering **and also** be able to consume/interpret a hanging protocol or structured display (and the associated study) created by a different system and render the study accordingly.

#. :ref:`Vol 1 Sec 3.1.1.1 <content_creator_actor>` - In IHE, a system that creates DICOM images has requirements for Study and Series UIDs, in particular conditions for when a new Series shall be created.   See `IHE RAD TF-2 <https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol2.pdf>`_: 4.8.4.1.1.1.   Should we pull these requirements into OIP?

#. Vol 2 Sec 3.1.4.1.3.1 - Regarding display of VL Photographic Images, should we include some general display requirements in addition to those specific to the Viewsets, e.g. associated with display of annotation? There are examples of how this is done for NM display in RAD TF-2: 4.16.4.2.2.3, for mammo in RAD TF-2: 4.16.4.2.2.1, and for basic image review in RAD TF-2: 4.16.4.2.2.6.

#. Vol 2 Sec 3.1.4.1.3.1 - Regarding display of VL Photographic Images, should we include some general display requirements in addition to those specific to the Viewsets, e.g. associated with display of annotation?  There are examples of how this is done for NM display in RAD TF-2: 4.16.4.2.2.3, for mammo in RAD TF-2: 4.16.4.2.2.1, and for basic image review in RAD TF-2: 4.16.4.2.2.6.

#. In Proposed 1114 AIP, Section 6.1.5 Common Requirements says, all image types "... SHOULD include the prescribing provider’s name".  Is ‘prescribing provider’ the same as Referring Physician Name (008,0090) in the General Study Module?   If “no”, then what is the DICOM attribute you want for prescribing provider??

#. Vol 3 Sec 7.4.2.2 Are there any additional OIP constraints on attributes in the VL Photographic Acquisition module?

#. Proposed 1114 AIP, Sections 7.1-7.4 contain requirements for acquiring Intra-Oral Radiographs.  Should those requirements be incorporated into OIP?   If so, they would become functional requirements added to Vol 1 Sec 3.2.1 for a Content Creator that supports the Direct Photography Option (creating VL Photographic Images).



#. Proposed 1114 AIP, Section 11.2 'DICOM Requirements for 2D Orthodontic/Craniofacial/Forensic Visible Light Images' contains requirements requirements labeled with SHOULD.  Should any of these requirements be promoted to a "SHALL" for OIP?

Closed Issues 
=============
#. This first revision of OIP does does not include transactions that specify how DICOM images and associated data is exchanged between actors.  Transactions such as DICOM C-STORE, Modality Worklist, or Query/Retrieve are deferred to a future version of OIP, or to a separate profile.

#. 

#. 

IHE Technical Frameworks General Introduction
=============================================
The `IHE Technical Frameworks General Introduction <https://profiles.ihe.net/GeneralIntro>`_ is shared by all of the IHE domain technical frameworks. Each technical framework volume contains links to this document where appropriate.

Copyright Licenses
==================
IHE technical documents refer to, and make use of, a number of standards developed and published by several standards development organizations. Please refer to the IHE Technical Frameworks General Introduction, `Section 9 - Copyright Licenses <https://profiles.ihe.net/GeneralIntro/ch-9.html>`_ for copyright license information for frequently referenced base standards. Information pertaining to the use of IHE International copyrighted materials is also available there.

Trademark
=========
IHE® and the IHE logo are trademarks of the Healthcare Information Management Systems Society in the United States and trademarks of IHE Europe in the European Community. Please refer to the IHE Technical Frameworks General Introduction, `Section 10 - Trademark <https://profiles.ihe.net/GeneralIntro/ch-10.html>`_ for information on their use.

IHE Technical Frameworks General Introduction Appendices
========================================================
The `IHE Technical Framework General Introduction Appendices <https://profiles.ihe.net/GeneralIntro/index.html>`_ are components shared by all of the IHE domain technical frameworks. Each technical framework volume contains links to these documents where appropriate.

`Appendix A <https://profiles.ihe.net/GeneralIntro/ch-A.html>`_ - **Actors**
-----------------------------------------------------------------------------

The table below lists existing actors that are utilized in this profile.

.. list-table::
    :header-rows: 1

    * - **Existing Actor Name**
      - **Definition**
    * - Content Creator
      - The Content Creator Actor creates content and transmits to a Content Consumer.   Note:  In OIP, 'content' is DICOM objects.  See :ref:`Volume 1 Section 3.1.1.1 <content_creator_actor>` for examples of products that could be a Content Creator in OIP.
    * - Content Consumer
      - The Content Consumer Actor views, imports, or performs other processing of content created by a Content Creator Actor.  Note:  In OIP, 'content' is DICOM objects.  See :ref:`Volume 1 Section 3.1.1.2 <content_consumer_actor> for examples of products that could be a Content Consumer in OIP.
    * - Image Display
      - The Image Display Actor presents medical images and associated imaging data.


