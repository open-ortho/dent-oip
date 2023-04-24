.. _code selection:

SNOMED Codes selection
======================

This section describes the criteria followed when selecting SNOMED-CT codes. This section should be followed when making any kind of modification to this document which affects the selection of SNOMED-CT codes.

SNOMED codes can be very granular and what appears to be the same concept can be represented by different codes. In reality, each code has a different meaning, and one must pay attention when selecting codes in order to maintain consistency within this standard and within the entire DICOM standard.

Use "structure of"
------------------

In SNOMED-CT it is frequent to find "Structure of... " and "Entire..." concepts. For example:

* `302549007 |Entire face (body structure) <https://browser.ihtsdotools.org/?perspective=full&conceptId1=302549007&edition=MAIN&release=&languages=en>`__
* `89545001 |Face structure (body structure) <https://browser.ihtsdotools.org/?perspective=full&conceptId1=89545001&edition=MAIN&release=&languages=en>`__

In this situation, David Clunie recommends maintaining the consistency with the rest of DICOM and picking the parent "Face Structure".

Prefer post-coordination
------------------------

https://michaelstearns.net/post-coordination-pre-coordination-codified-concepts/ provides a good explanation for post-coordination:

    Post-coordination refers to using two codes to represent a clinical expression such as “severe headache.”    For example a code exists for the symptom “headache” (e.g., SNOMED CT code 25064002) and a separate code exists for the modifier “severe” (e.g., SNOMED CT code 24484000).  These two are then placed together in combination as 24484000 (severe) + 25064002 (headache), allowing the information system to identify when a patient presents with a severe headache vs. just a headache alone or a mild headache. 

