Requirements
============

In ADA SCDI WP-1100, the orthodontic providers have identified the following functionality as being essential or crucial for providing maximum patient care and research capabilities: 

- ability to store and recall visible light store and recall visible light images that have metadata associate to them and present them in the same way that they were acquired
- pull the images without requiring a lot of manual labor
- demonstrate the staff member which image to take
- warn if the wrong picture was taken
- acquire the desired images correctly
- store these images persistently
- recall and share these images persistently

this functionality should include viewsets. 

- Ensure the following characteristics of the images are indexable separately:
    - Patient demographics
    - Device that acquired the image (iPhone X, Nikon SLR camera, ...)
    - Orientation of patient to the device (left, right, frontal, ...)
    - Anatomy being imaged (whole face, part of face, mouth)
    - Occlusal relationship (Centric occlusion, centric relation)
    - Patients having a specific feature (tattoo, birthmark, ...)
    - Who acquired the image (patient, assistant, parent, ...)
    - Conditions under which the image was acquired (tongue depressor, mirror, )
    - Whether or not the image is associated to other images taken during the same encounter.
    - Who ordered the image to be taken.

In order to fulfill these requirements, a standard that unambiguously defines how orthodontic photographic images should be electronically represented has been written. 

- The standard makes use of DICOM, allowing any developer to implement it.
- The standard defines a way to tag the image with all required elements.
- The tagging of the images is done making use of a standardized code set (SNOMED-CT), to ensure no ambiguity exists. 

