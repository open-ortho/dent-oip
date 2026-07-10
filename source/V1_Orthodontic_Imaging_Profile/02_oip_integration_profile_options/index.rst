.. _oip_integration_profile_options:

3.2 OIP Profile Options
-----------------------

Options that may be selected for each actor in this profile, if any, are listed in the Table 3.2-1. Dependencies between options, when applicable, are specified in notes.

**Table 3.2-1: OIP Profile Actors and Options**

.. list-table::
    :header-rows: 1

    * - **Actor**
      - **Option Name**
      - **Reference**
    * - Content Creator
      - Direct Photography Option
      - Section 3.2.1
    * - Content Consumer
      - No options defined
      - --
    * - Image Display
      - Structured Display Option
      - Section 3.2.2
    * -
      - Hanging Protocol Option
      - Section 3.2.3

.. note::

   Future revisions of OIP will add Content Creator options to this table to enable support for other types of DICOM images (e.g., Video Photographic Image, Surface Scan Mesh, Secondary Capture).

.. toctree::
    :maxdepth: 1

    direct_photography_option

3.2.2 Structured Display Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Structured Display Option enables an Image Display actor to retrieve and render a Structured Display IOD that defines a standardized layout for presenting a set of orthodontic images. An Image Display actor that supports this option shall implement the requirements in DEN TF-2: 3.1.4.1.3.6 and shall support the Structured Display IOD Definition in DEN TF-3: 7.3.2.

3.2.3 Hanging Protocol Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Hanging Protocol Option enables an Image Display actor to apply a Hanging Protocol IOD to automatically arrange and configure the display of a set of orthodontic images. An Image Display actor that supports this option shall implement the requirements in DEN TF-2: 3.1.4.1.3.6 and shall support the Hanging Protocol IOD Definition in DEN TF-3: 7.3.3.

3.3 OIP Required Actor Groupings
--------------------------------
An actor from this profile (Column 1) shall implement all of the required transactions and/or content modules in this profile in addition to all of the requirements for the grouped actor (Column 2).

.. list-table::
    :header-rows: 1

    * - **OIP Actor**
      - **Profile/Actor(s) to be Grouped With**
      - **Reference**
    * - Content Creator
      - None
      - 
    * - Content Consumer
      - None
      - 
    * - Image Display
      - OIP / Content Consumer
      - Section 3.1.1.2

Section 3.6 describes some optional groupings in other related profiles.
