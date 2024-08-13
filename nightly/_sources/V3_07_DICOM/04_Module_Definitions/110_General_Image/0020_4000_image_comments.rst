Image Comments (0020,4000)
==========================

According to DICOM, Image comments can be any string with a maximum length
of 10240 characters. New lines and tabs are allowed. For orthodontic purposes, any kind of clinical comments for an image
would normally go in the practice management software, or in a DICOM
structured report. 

We recommend this field to be used to store the image
view type with the following format:

``<num>^<code>^<meaning>``

where:

``num``: is the view number, for example EV01 (from ADA WP-1100)

``code``: is the view code, for example EV.RP.LR.CO (from ADA WP-1100)

``meaning``: is the code meaning, for example Extraoral, Right Profile
(subject is facing observer's right), Lips Relaxed, Centric Occlusion (from ADA WP-1100)

An example string:

``EV02^EV.RP.LR.CR^Extraoral, Right Profile (subject is facing observer's right), Lips Relaxed, Centric Relation``


The comprehensive list of orthodontic views, as defined in ADA WP-1100, is available in :ref:`view_examples`.