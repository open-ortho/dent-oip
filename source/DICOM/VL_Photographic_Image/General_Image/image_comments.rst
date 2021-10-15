Image Comments (0020,4000)
==========================

According to DICOM, Image comments can be any string with maximum length
of 10240 characters. New lines and tabs are allowed.

For orthodontic purposes, any kind of clinical comments for an image
would normally go in the practice management software, or in a DICOM
structured report. This field can therefore be used to store the image
view type with the following format:

``<num>^<code>^<meaning>``

where:

``num``: is the view number, for example EV01

``code``: is the view code, for example EO.RP.LR.CO

``meaning``: is the code meaning, for example Extraoral, Right Profile
(subject is facing observer's right), Lips Relaxed, Centric Occlusion

An example:

``EV02^EO.RP.LR.CR^Extraoral, Right Profile (subject is facing observer's right), Lips Relaxed, Centric Relation``
