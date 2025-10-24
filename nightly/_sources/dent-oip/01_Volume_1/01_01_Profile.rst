X Orthodontic Imaging (OIP) Profile
========================================

<Provide an end-user friendly overview of what the profile does for them. Keep it brief (a paragraph or two, up to a page). If extensive detail is needed, it should be included in Section X.4- Use Cases.>

<Explicitly state whether this is a Workflow, Transport, or Content Module (or combination) profile. See the IHE Technical Frameworks General Introduction for definitions of these profile types.>


X.1 OIP Actors, Transactions, and Content Modules
--------------------------------------------------

The archival of high quality photographic documentation in a open standard is central to big data research, reduction in errors, data loss, staff and doctor burnout. This standard defines how to save orthodontic medical visible light images (aka photographs) making use of the most widely used standard for medical images: DICOM.

.. _volume_1_oip_actors_transactions:

.. list-table:: OIP Actors, Transactions, and Content Modules
    :header-rows: 1

    * - Actor
      - Description
      - Transactions
    * - Acquisition Modality
      - A system that acquires and creates medical images while a patient is present. Examples include still visible light photography, visible light motion picture with audio, radiographs, etc.
      - RAD-8, RAD-11, RAD-14, RAD-16, RAD-18
    * - Acquisition Modality Importer
      - A system that interfaces to a non-DICOM ready modality to integrate it into dental care workflows.
      - RAD-8
    * - Department System Scheduler/Order Filler
      - A department-based system that manages orders received from external systems or through the department system's user interface.
      - RAD-8

RAD-8	Modality Images Stored	
An Acquisition Modality sends acquired or generated images to the Image Archive.
                            
RAD-11	Images Availability Query	
Queries the Image Manager if a particular image or image series is available.
                            
RAD-14	Query Images	
An Image Display queries the Image Archive for a list of entries representing images by patient, study, series, or instance.
                            
RAD-16	Retrieve Images	
An Image Display or an Imaging Document Consumer requests and retrieves a particular image or set of images from the Image Archive or an Imaging Document Source, respectively.

RAD-18	Creator Images Stored	
An Image Creator sends new images to the Image Archive.

RAD-106	Invoke Image Display	
Invokes the display of DICOM image studies.

RAD-131	Store Encounter Images
Send images that were acquired in the course of a patient encounter (in contrast to those acquired for an ordered procedure).

Reference: take a look at these for inspiration:

How about this one? Is this about displaying images everywhere, like on mobile devices?
CARD-15	Invoke Image Display Service	
In the Invoke Image Display Service, the Image Manager/Image Archive provides a web interface to access stored DICOM images and evidence.

Maybe we can use some parts of this one for the MWLs?

CARD-13	Query Cardiology Images/Evidence	
Query Cardiology Images/Evidence – An enhanced version of the “Query Images” and “Query Evidence Documents” queries that requires the “Performed Protocol Code Sequence” to be returned so resting ECGs can be distinguished from other ECG tests, like stress, and Holter.


Maybe this for the cephalograms?
EYECARE-18	Modality Images - Evidence Key Objects Stored	
Requires acquisitions systems to select and send key image/measurement objects to a storage/display system (i.e., not an image archive). Also enables Image Manager/Image Archive actors to send selected key images/measurements.