.. _scroll-bookmark-14:

Progress
========

During an orthodontic treatment, it is common for the provider to keep
track of treatment progress by regularly collecting records (such as
photographs or intra-oral surface scans) [provide reference]. It is
therefore useful to identify when, relative to an orthodontic treatment,
the records were taken. Examples could be:


.. list-table:: 
    :header-rows: 1
    * - type
      - short
      - description
      - code
    * - Observation
      - OBSER
      - Images used for general documentation. Not part of regular treatment records. Sequence number is not required.
      - ?
    * - Pre-treatment
      - PRETX
      - Images acquired before treatment starts. Only used when the patient and doctor have agreed to start a treatment. Initial would be the last "pretreatment" image acquired before treatment starts.
      - ?
    * - Progress
      - PROGR
      - Images taken during treatment.
      - ?
    * - Final
      - FINAL
      - Image taken at the end of active treatment (after appliance removal, if applicable).
      - ?
    * - Post-treatment
      - POSTX
      - Image acquired after treatment.
      - ?

The lack of a row for "Initial" is intentional. All Pre-treatment images are essentially initials because treatment is expected. There is no need for coding Initial in the image. The last pretreatment image acquired before treatment starts would be the initial.

When a provider only has a single image, or a set of images of a single Pre-treatment time point, 

1. Check if this patient has an progress, final or Post-treatment photograph.
2. If the patient does, then last image with the date closest the the first image of treatment would be considered in treatment.

Note that there is no "Initial"

Where *n* is a serial number or letter indicating the sequence order.
For example, "Pre-treatment 1" would refer to records taken temporally
before "Pre-treatment 3". And the existence of "Pre-treatment 3"
indicates that other two sets of records where take for this patient.

.. list-table:: 
    :header-rows: 1

    * - Attribute Name
      - Tag
      - Value
      - Meaning
    * - > Acquisition Context Sequence Attribute
      - (0040,0555) 
      - 
      - 
    * - >> Concept Name Code Sequence Attribute
      - (0040,A043)
      - DCM-126072
      - Time Point Type
    * - >> Concept Code Sequence Attribute
      - (0040,A168)
      - One of CID6146 values. 
      - See Notes below.
    * - > Acquisition Context Sequence Attribute
      - (0040,0555) 
      - 
      - This sequence is omitted for "Initial" and "Final", as there are no progresses.
    * - >> Concept Name Code Sequence Attribute
      - (0040,A043)
      - DCM-126073
      - Time Point Order
    * - >> Numeric Value Attribute 
      - (0040,A30A)
      - 1,2,3,...
      - An integer representing the sequence number of the progress.
    * - Study Description
      - (0008,1030)
      - X
      - See notes below.

Concept Code Sequence Attribute
-------------------------------

Allowed values for this tag are taken from DICOM Table CID6146. 


Study Description
-----------------

This field is used 

1.
For Pretreatment and Postreatment, the VL object would include (along with all other tags):

> Acquisition Context Sequence Attribute (0040,0555)
>> Concept Name Code Sequence Attribute (0040,A043): (126072, DCM, "Time Point Type")
>> Concept Code Sequence Attribute (0040,A168): One of CID6146 values. Pretreatment and posttreatment.
> Acquisition Context Sequence Attribute (0040,0555)
>> Concept Name Code Sequence Attribute (0040,A043): (126073, DCM, "Time Point Order") = code
>> Numeric Value Attribute (0040,A30A): Integer number of Progress
> Study Description (0008,1030): "Pretreatment <n>" or "Posttreatment <n>"

2.
For Initial, Final the VL object would include (along with all other tags):

> Acquisition Context Sequence Attribute (0040,0555)
>> Concept Name Code Sequence Attribute (0040,A043): (126072, DCM, "Time Point Type")
>> Concept Code Sequence Attribute (0040,A168): Initial|Final. We would need to request addition in a correction package to extend CID6146 to include Initial and Final
> Study Description (0008,1030): "Initial", or "Final"

3.
For Progresses the VL objects would include (along with other necessary tags):

> Acquisition Context Sequence Attribute (0040,0555)
>> Concept Name Code Sequence Attribute (0040,A043): (126072, DCM, "Time Point Type")
>> Concept Code Sequence Attribute (0040,A168): Progress. We would need to request addition in a correction package to extend CID6146 to include Initial and Final
> Acquisition Context Sequence Attribute (0040,0555)
>> Concept Name Code Sequence Attribute (0040,A043): (126073, DCM, "Time Point Order") = code
>> Numeric Value Attribute (0040,A30A): Integer number of Progress
> Study Description (0008,1030): "Progress <n>" 


.. _scroll-bookmark-15:

Proposed DICOM tags to keep record of progress
----------------------------------------------

.. _scroll-bookmark-16:

Study Description (0008,1030)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is an optional DICOM tag, which can contain a Long String (64
character max), part of the General Study module. Because each
orthodontic visit would fall under a DICOM Study, this location could be
appropriate.

.. _scroll-bookmark-17:

Pros
^^^^

-  Study Description is often visible from many PACS search results. The
   provider can therefore quickly identify which progress the entry
   refers to. This is a weak pro, because nothing prevents orthodontic
   specific software to show this information, were it stored elsewhere.

.. _scroll-bookmark-18:

Cons
^^^^

-  Text limited to 64 characters. Taking up ca 16 characters for
   progress, would leave only 48 characters for other study
   descriptions.

-  Cannot be coded. Study Description does not allow code sets and could
   contain other data, as implementation might vary.

.. _scroll-bookmark-19:

Reason For Performed Procedure Code Sequence Attribute (0040,1012)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This is an optional DICOM tag, which can contain a Long String (64
character max), part of the General Study module. Because each
orthodontic visit would fall under a DICOM Study, this location could be
appropriate.*

.. _scroll-bookmark-20:

Pros
^^^^

-  This is a code sequence, hence SNOMED CT codes could be used here.

-  This attribute allow for multiple instances codes. This means that
   using one to indicate progress, would not limit the provider for
   adding others.

.. _scroll-bookmark-21:

Cons
^^^^

-  Existing PACS software does not look at this tag, and would not show
   it by default. This is a weak con, because nothing prevents
   orthodontic specific software to show these fields. Actually, this
   could be an incentive for vendors to develop more orthodontic
   specific DICOM software, and for orthodontic providers to support and
   request them.
