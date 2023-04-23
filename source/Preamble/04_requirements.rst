Requirements (Informative)
==========================

In ADA SCDI WP-1100, the orthodontic providers have identified the following functionality as being essential or crucial for providing maximum patient care and research capabilities: 

1. ability to store and recall visible light store and recall visible light images that have metadata associate to them and present them in the same way that they were acquired, whether or not the same product was used
2. find the images without requiring a lot of manual labor
3. demonstrate the staff member which image to take
4. warn if the wrong picture was taken
5. acquire the desired images and viewsets correctly
6. store these images and viewsets persistently
7. recall and share these images and viewsets persistently
8. ensure the following characteristics of the images are indexable separately:
    9. Patient demographics
    #. Device that acquired the image (iPhone X, Nikon SLR camera, ...)
    #. Orientation of patient to the device (left, right, frontal, ...)
    #. Anatomy being imaged (whole face, part of face, mouth)
    #. Occlusal relationship (Centric occlusion, centric relation)
    #. Patients having a specific feature (tattoo, birthmark, ...)
    #. Who acquired the image (patient, assistant, parent, ...)
    #. Conditions under which the image was acquired (tongue depressor, mirror, )
    #. Whether or not the image is associated to other images taken during the same encounter.
    #. Person who ordered the image to be taken.

This document was developed in order to fulfill these requirements, a standard that unambiguously defines how orthodontic photographic images should be electronically represented.

1. Using DICOM gives the industry the ability to develop solutions that are able to store and recall images and their metadata across different products.
2. Improving the search capabilities of images is not directly addressed in this document. However, using DICOM tags will provide the industry to develop solutions that can improve search capabilities by searching through the DICOM tags and their values.
3. Demonstrating or otherwise aiding the staff member during the acquisition process is part of the user experience of the software that the staff member is using, and not part of this document. However, the choice of standards used in this standards (DICOM and SNOMED-CT) will not alter or hinder in any way the ability of industry to provide such solutions.
4. Warning the staff member during the acquisition process that the wrong image is being taken or has been taken is part of the user experience of the software that the staff member is using, and not part of this document. However, the choice of standards used in this standards (DICOM and SNOMED-CT) could be leveraged by the industry to have tools to provide such solutions.
5. By implementing this standard, industry could develop products that capture and store all of the information needed for the process to be considered "correct" without having to implement something similar themselves.
6. Persistence is a characteristic of DICOM and SNOMED-CT:
7. DICOM has a defined protocol for exchanging images over the network and between devices. By promoting the use of DICOM, we facilitate the implementation of it, and the more developers implement it, the greater the level of interoperabiltiy will be. By making use of SNOMED-CT, we make sure that different devices and software don't interpret it incorrectly.
8. All of the characteristics in 9-18 can be recorded in DICOM tags, and are addressed in this document.
