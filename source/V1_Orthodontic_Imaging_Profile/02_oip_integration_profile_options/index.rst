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
      - No options defined
      - --

.. note::

   Future revisions of OIP will add Content Creator options to this table to enable support for other types of DICOM images (e.g., Video Photographic Image, Surface Scan Mesh, Secondary Capture).

.. toctree::
    :maxdepth: 1

    direct_photography_option

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
