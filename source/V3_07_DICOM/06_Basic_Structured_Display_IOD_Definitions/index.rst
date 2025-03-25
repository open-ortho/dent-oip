.. _basic_structured_display_iod_definitions:

IOD Definitions
===============

Introduction
-----------

The Basic Structured Display IOD is a DICOM Information Object Definition that specifies a fixed, deterministic layout of images and related content that must be presented to the viewer exactly as defined. It provides a mechanism to create reproducible presentations of images, graphics, text and other renderable content.

In orthodontics, Basic Structured Displays can be used to exchange images with other medical providers, software systems or patients while ensuring they are displayed in the same way. This can be achieved by attaching, along with the actual image data (like the :ref:`VL Photographic Image IOD <vl_photographic_image_iod_definitions>`), a Structured Display IOD that defines which of the VL Image IODs should go in which image box, how they should be arranged, and what annotations should be displayed.

Basic Structured Displays may be constructed from a :ref:`Hanging Protocol IOD <hanging_protocol_iod_definitions>`, which acts as a "template", as it defines generically, which type of image should go in which box, the size of the boxes, and the layout of the boxes. 

Basic Structured Displays are particularly valuable:

* for saving a specific layout and ensuring that layout persists. Every time the user asks the system to show the images, they will be shown in the same way;
* for exchanging images with other systems or providers, ensuring that the images are displayed in the same way on the receiving end;



.. list-table:: Usage of DICOM Modules in Basic Structured Display
   :header-rows: 1
   :widths: 15 25 15 40 15

   * - IE
     - Module
     - Reference
     - Usage
     - IHE Usage
   * - Patient
     - Patient
     - C.7.1.1
     - M
     - M
   * - 
     - Clinical Trial Subject
     - C.7.1.3
     - U
     - U
   * - Study
     - General Study
     - C.7.2.1
     - M
     - M
   * - 
     - Patient Study
     - C.7.2.2
     - U
     - U
   * - 
     - Clinical Trial Study
     - C.7.2.3
     - U
     - U
   * - Series
     - General Series
     - C.7.3.1
     - M
     - M
   * - 
     - Clinical Trial Series
     - C.7.3.2
     - U
     - U
   * - 
     - Presentation Series
     - C.11.9
     - M
     - M
   * - Equipment
     - General Equipment
     - C.7.5.1
     - M
     - M
   * - 
     - Enhanced General Equipment
     - C.7.5.2
     - U
     - U
   * - Presentation State
     - Structured Display
     - C.11.16
     - M
     - M
   * - 
     - Structured Display Image Box
     - C.11.17
     - M
     - M
   * - 
     - Structured Display Annotation
     - C.11.18
     - U
     - U
   * - 
     - Common Instance Reference
     - C.12.2
     - M
     - M
   * - 
     - Specimen
     - C.7.6.22
     - U
     - U
   * - SOP Common
     - SOP Common
     - C.12.1
     - M
     - M
