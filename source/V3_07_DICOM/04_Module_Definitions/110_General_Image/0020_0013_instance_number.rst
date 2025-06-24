.. _instance_number:

Instance Number (0020,0013)
============================

To ensure images are presented in a specific sequence, set the Instance Number
(0020,0013) for each image according to the desired order. 

Examples 
----------------------

For example, if you have a series of intraoral photographs, assign Instance
Numbers incrementally:

.. code-block:: none

   (0020,0013) Instance Number: 1   # Frontal view
   (0020,0013) Instance Number: 2   # Right lateral view
   (0020,0013) Instance Number: 3   # Left lateral view
   (0020,0013) Instance Number: 4   # Maxillary occlusal view
   (0020,0013) Instance Number: 5   # Mandibular occlusal view

When generating DICOM files programmatically, set the Instance Number attribute for each image object:

.. code-block:: python

   # Example using pydicom
   import pydicom
   ds = pydicom.Dataset()
   ds.InstanceNumber = 1  # Set according to the image order
   # ... set other attributes ...
   ds.save_as('image1.dcm')

Repeat for each image, incrementing the Instance Number as needed. This ensures that DICOM viewers and systems can display the images in the intended sequence.

Non-Sequential Instance Numbers
--------------------------------

Instance Numbers do not have to be strictly sequential. For example, you may
assign non-consecutive values to allow for future insertion of images or to
match an external numbering scheme:

.. code-block:: none

   (0020,0013) Instance Number: 10   # Frontal view
   (0020,0013) Instance Number: 20   # Right lateral view
   (0020,0013) Instance Number: 30   # Left lateral view

DICOM viewers will still use the Instance Number to determine display order,
regardless of whether the numbers are consecutive.