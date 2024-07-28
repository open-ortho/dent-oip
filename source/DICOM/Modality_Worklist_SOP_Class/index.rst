.. _modality_worklist_sop_class:

.. toctree::
	:glob:
	:maxdepth: 2

	*/index


Modality Worklist SOP Class
===========================

This normative section contains a description of the DICOM tags which are
necessary to request for orthodontic photographs to be taken (acquired).

The Modality Worklist is designed to streamline the exchange of clinical information between devices, minimizing the need for manual data entry across multiple systems. Proper implementation of Modality Worklists can reduce staff burnout and human errors, ultimately enhancing patient care.

This section aims to promote the widespread adoption of the Modality Worklist workflow by simplifying its implementation and reducing associated costs to a minimum.

Modality Worklist Workflow
--------------------------

1. **Request Generation by Practice Management System (PMS)**
   The Practice Management System (PMS) is responsible for generating requests for acquiring photographs or radiographs. 

2. **Determination of Image Type**
   The PMS uses information from the appointment type or the procedure associated with the appointment to determine the specific images required, such as panoramic (PX), CBCT (CT), Digital Radiographs (DX) or intraoral photographs taken with an External Camera (XC).

3. **Image Acquisition Request**
   Upon patient check-in, the PMS generates a request for the required images to be acquired via the DICOM network.

4. **Modality Query**
   When a staff member operates an imaging device (referred to as a Modality in DICOM terminology), the device queries the PMS using DICOM language to understand the imaging requirements.

5. **PMS Response with Modality Worklist**
   The PMS responds with a Modality Worklist DICOM object, which includes specific information such as patient demographics, type of image to be acquired (e.g., CT, PX, DX, XC), and the required protocol.

6. **Pre-Population of Fields**
   The imaging device pre-populates all necessary fields based on the Modality Worklist and presents only the relevant options required for the image acquisition.

7. **Image Acquisition**
   The staff member proceeds to acquire the images as specified.

8. **Image Formatting and Transmission**
   The imaging device uses information from the Modality Worklist to create properly tagged and formatted medical images in DICOM format, which are then sent to the imaging server (PACS).


Relationship between elements
-----------------------------

Modality Worklist Building Blocks in Orthodontics

There are three main building blocks of a modality worklist. This explanation will describe how these components apply to the orthodontic domain, specifically for orthodontic photographs. For further details, refer to `DICOM Part 3.4, Section K.6 <https://dicom.nema.org/medical/dicom/current/output/chtml/part04/sect_K.6.html>`_ and the `IHE RAD-5 Profile <https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol2.pdf>`_.

1. **Requested Procedure** <_requested_procedure>

   This represents a high-level procedure associated with an appointment, such as an Initial Visit or Initial Records. During such appointments, the patient may need to collect various types of images, including Digital X-rays (DX), Panoramic X-rays (PX), Computed Tomography (CT), and Extraoral Photographs (XC).

2. **Scheduled Procedure Step** <_scheduled_procedure_step>

   Each requested procedure can have multiple procedure steps, which are modality-specific. For instance, for an Initial Visit, the following steps might be required:
   
   - One PX
   - Two DX (PA and lateral)
   - Eight XC (intraoral and extraoral)

3. **Scheduled Protocol Code** <_scheduled_protocol_code>

   Each procedure step can include one or more scheduled protocol codes. For example, the PX scheduled procedure step might use the code `89846007 | Orthopantogram (procedure)`, while the XC scheduled procedure step may include codes such as:
   
   - `1306665006 | Photographic extraoral image of full face with full smile and jaws in centric relation (record artifact)`
   - `1306651009 | Photographic extraoral image of left half of face with full smile and teeth in centric occlusion (record artifact)`
   - ...
