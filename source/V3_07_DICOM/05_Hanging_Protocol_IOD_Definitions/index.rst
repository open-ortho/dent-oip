.. _hanging_protocol_iod_definitions:

IOD Definitions
===============

Introduction
-----------

A Hanging Protocol is a specialized DICOM Information Object Definition (IOD) that defines the initial display arrangement of medical images on one or more display systems. It allows for the specification of how images should be positioned, sized, annotated, and organized when initially displayed to a user.

Unlike the :ref:`Basic Structured Display IOD <basic_structured_display_iod_definitions>`, which defines a static presentation that contains references to specific image instances, Hanging Protocols provide instructions for the initial layout and the generic types of images that should be placed in the specific areas or boxes. 

Basic Structured Display, which defines a static presentation that must be shown exactly as specified, Hanging Protocols provide instructions for the initial layout while allowing users to subsequently manipulate and interact with the images. Hanging Protocols are particularly useful in clinical workflows where specific viewing configurations are preferred for different examination types or specialties.

Hanging Protocols are particularly valuable:

* when a system allows the user to customize the display of images, this customization can be saved as a Hanging Protocol, exported and re-imported in different systems, allowing the clinicians to preserve their preferred display settings, without having to re-configure the display on the new system;
* when a practice is using more than one system that requires the visualization of images and allows the user to customize the display, the Hanging Protocol can be used transferred and synchronized between the systems to ensure that the images are displayed in the same way on all systems, without requiring the user to re-configure the display on each system.

The Hanging Protocol IOD works in conjunction with display systems to streamline image interpretation and enhance workflow efficiency, providing a standardized presentation that can be applied to any image set.

.. list-table:: Usage of DICOM Modules in Hanging Protocol
   :header-rows: 1
   :widths: 15 25 15 15

   * - IE
     - Module
     - Reference
     - Usage
   * - Hanging Protocol
     - SOP Common
     - C.12.1
     - M
   * - 
     - Hanging Protocol Definition
     - C.23.1
     - M
   * - 
     - Hanging Protocol Environment
     - C.23.2
     - M
   * - 
     - Hanging Protocol Display
     - C.23.3
     - M
