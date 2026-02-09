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
*<TO DO: List the open issues/questions that need to be addressed. These are particularly useful for highlighting problematic issues and/or specifically soliciting public comments.>*

#. 

#. 

#. 

Closed Issues 
=============
#. This first revision of OIP does does not include transactions that specify how DICOM images and associated data is exchanged between actors; i.e., transactions such as DICOM C-STORE or Modality Worklist are deferred to a future version of OIP, or to a separate profile.

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
      - The Content Creator Actor creates content and transmits to a Content Consumer.
    * - Content Consumer
      - The Content Consumer Actor views, imports, or performs other processing of content created by a Content Creator Actor.
    * - Image Display
      - The Image Display Actor presents medical images and associated imaging data.


