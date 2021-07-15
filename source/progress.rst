.. _scroll-bookmark-14:

Progress
========

During an orthodontic treatment, it is common for the provider to keep
track of treatment progress by regularly collecting records (such as
photographs or intra-oral surface scans) [provide reference]. It is
therefore useful to identify when, relative to an orthodontic treatment,
the records were taken. Examples could be:

+--------------------+-------------------------------+---------------+
| type               | description                   | relevant code |
+====================+===============================+===============+
| Pre-treatment *n*  | Records taken before          |               |
|                    | treatment was begun.          |               |
+--------------------+-------------------------------+---------------+
| Initial            | Records taken the moment      | SCTID: 884001 |
|                    | treatment was begun.          |               |
+--------------------+-------------------------------+---------------+
| Progress *n*       | Records taken during          |               |
|                    | treatment.                    |               |
+--------------------+-------------------------------+---------------+
| Final              | Records taken the moment      |               |
|                    | treatment was completed.      |               |
+--------------------+-------------------------------+---------------+
| Post-treatment *n* | Records taken after treatment |               |
|                    | was completed.                |               |
+--------------------+-------------------------------+---------------+

Where *n* is a serial number or letter indicating the sequence order.
For example, "Pre-treatment 1" would refer to records taken temporally
before "Pre-treatment 3". And the existence of "Pre-treatment 3"
indicates that other two sets of records where take for this patient.

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
