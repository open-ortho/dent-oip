Scope
=====

The intended audience of this document is the medical imaging software developers or medical imaging device manufacturer who deals with visible light digital photography.

The scope of this document is to alleviate the work of the imaging software developer or device manufacturer, allowing him or her to spend more time focussing on their idea, and less time designing and implementing novel and proprietary ways for connecting with other products. That work is alreay done and defined. All that needs to be done is implement it in your product.

The document, along with its accompanying CSV files and DICOM sample files, 
provide a detailed implementation guide for encoding orthodontic/craniofacial
views using DICOM with SNOMED CT terminology. 

.. note::

    The :ref:`list of views presented in the Appendix <view_examples>` of this standard serve as example for encoding a virtually unlimited number of view types. As long as the implementer follows the guidelines of this standard, the implementation will comply to this standard, even if the view represented in such implementation is not included as one of the views in the Appendix.

This guide depends on ADA SCDI White Paper 1100 -
Orthodontic/Craniofacial/Forensic Photographic Views and Viewsets available online on the ADA Catalog.
