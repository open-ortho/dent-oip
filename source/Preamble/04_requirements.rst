Requirements (Informative)
==========================

M: Mandatory (SHALL)
C: Conditionally Mandatory
R: Recommended (SHOULD)
O: Optional (MAY)

In ADA SCDI WP-1100, the orthodontic providers have identified the following functionality as being essential or crucial for providing maximum patient care and research capabilities: 

Capture/acquire visible light (VL) images
-----------------------------------------

- The system SHALL provide a way to capture VL still images.
- The system SHALL be able to store the captured VL still images persistently.
- The system SHALL provide the ability to capture the entire head including neck.
- The system SHALL provide the ability to capture the oral cavity.
- The system SHALL provide the ability to capture VL images with natural or artifical lighting.
- The system SHALL provide the ability to capture VL images when natural lighting is insufficient by augmenting it (e.g. flash).
- The system SHOULD provide the ability to associate the images to the subject without having to re-enter the patient information if it has been already entered in a connected system.
- The system SHOULD have a latency of capture (time between 'click' and when the system capture the images) below 500ms.
- The system SHOULD provide the ability to capture images without shadows.
- The system SHOULD provide a way to upload the images to a medical enterprise imaging network.
- The system SHOULD provide the ability to arrange the VL images in a specific layout.
- The system SHOULD assist the provider with acquiring series of VL images. Each series can be composes of any amount of any number of types of images.
- The system SHALL be able to store the layout and the images in it persistently, when applicable.
- The system MAY aid the operator during the acquisition process (e.g. by prompting the operator which image to take, showing a silhoutte of the image type, etc). The system MAY warn if the the operator was prompted to take one image type, but acquired a different one.


View the visible light images
-----------------------------

- The system SHALL have the ability to present and visualize the VL images at the same quality and resolution as the one that was used during acquisition time.
- The system SHALL be device independent: the visualizing system SHALL be able to display images taken with a the same or a different device manufactured by the same or a different vendor equally accurately.
- If known, the system SHALL inform the user if the asymmetry portrayed in the image is functional or skeletal (e.g. if it is caused by Bell's palsy, or other condition or obstruction that prevents the patient from moving the body).
- The system SHOULD inform the user if the image (resolution, compression, contrast, etc.) has been modified from the original.

Searching for VL images
-----------------------

- The system SHOULD provide a way to search by 
    - [M] First Family Name of Patient
    - [M] Patient identifier
    - [R] By appointment (Acession Number)
    - [O] Acquisition date
    - [O] By Procedure type (e.g. Cementazione (MEA) Maxillary Expander Appliance )

Image Exporting
---------------

- The system SHALL always export the images with all associated clinical and demographical data, unless specifcally chosen not to (e.g. anonymization).
- The system MAY allow exporting of images using conventional, non-medical formats (i.e. JPG, TIFF, PNG, etc.). When doing so, the system SHALL  by default include with the image the clinical and demographical data in a way that the importing system is able to interpret or present such data to the receiving provider, unless specifcally chosen not to (e.g. anonymization).
- In case the system has the capability of storing the images and their patient data, the system SHALL have the ability to export **all** data in bulk in a digital format compatible with medical enterprise imaging standards.

Sharing of images
-----------------

- The system SHOULD have the ability to share images with other parties outside of the institution in a secure way.
- The system SHOULD have the ability to share images and their viewsets with other parties outside of the institution in a secure way.


Metadata
--------

- The captured image SHALL be inequivocably associated with required clincal and demographical patient data 

- [M] Patient demographics (see DHFP)
- [M] Support for all character sets required to fully represent the patient's name and address details.
- [M] Whether or not the image is associated to other images taken during the same encounter.
- [C] The time point with respect to Orthodontic Treatment (progress). Mandatory if known.
- [C] Occlusal relationship (Centric occlusion, centric relation). Required for specific view sets only (e.g. frontal and lateral extra oral)
- [C] Skeletal or functional asymmetry. Required for specific view sets only 
- [R] Orientation of patient to the device (left, right, frontal, ...)
- [R] Anatomy being imaged (whole face, part of face, mouth)
- [R] Who acquired the image (patient, assistant, parent, robot, ...)
- [R] If the image was captured directly or indirectly (taking photo of the mirror)
- [R] Skeletal or functional asymmetry.
- [O] Device that acquired the image (iPhone X, Nikon SLR camera, ...)
- [O] Patients having a specific feature (tattoo, birthmark, ...)
- [O] Devices present (visible or invisible) in the field of view (tongue depressor, ruler  )
- [O] Responsible party (human or non-human) which ordered the image to be taken.
- [O] The coding and indexing of teeth present in the image IS NOT required, nor defined.
- [?] The reason why the VL images were taken.


This document was developed to fulfill the following requirements, setting a standard that clearly defines how orthodontic photographic images should be electronically represented:

1. **Using DICOM**: 
   - DICOM provides the industry with the ability to develop solutions that store and recall images and their metadata across different products.

2. **Improving Search Capabilities**: 
   - Using DICOM tags allows the industry to develop solutions that enhance search capabilities by searching through DICOM tags and their values.

3. **Acquisition Process**: 
   - Demonstrating or aiding the staff member during the acquisition process is part of the user experience of the software they are using and is not covered in this document. The choice of standards utilized here (DICOM and SNOMED-CT) will not impede the industry’s ability to provide such solutions.

5. **Implementation Benefits**: 
   - By implementing this standard, the industry can develop products that capture and store all necessary information, eliminating the need for custom implementations.

6. **Persistence**: 
   - Persistence is a key characteristic of DICOM and SNOMED-CT.

7. **DICOM Protocol**: 
   - DICOM has a defined protocol for exchanging images over networks and between devices. Promoting DICOM use facilitates implementation, and increased adoption by developers enhances interoperability. SNOMED-CT ensures consistent interpretation across different devices and software.

8. **DICOM Tags**: 
   - All characteristics listed in sections 9-18 can be recorded in DICOM tags and are addressed in this document.