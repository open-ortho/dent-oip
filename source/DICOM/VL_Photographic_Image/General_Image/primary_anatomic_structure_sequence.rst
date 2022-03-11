.. _primary anatomic structure sequence:

Primary Anatomic Structure Sequence (0008,2228)
===============================================

Primary Anatomic Structure Sequence contains a list of visible teeth using ISO
tooth numbering system (represented as SNOMED CT codes) in a specific view.

Allowed Values
--------------

Refer to the tables below for a list of permissible values.

Primary Anatomic Structure for Intraoral Photography
::::::::::::::::::::::::::::::::::::::::::::::::::::


+------------------+-------------+---------------+------------------+
| Code Scheme      | Code Value  | Code Meaning  | when to use      |
| Designator       |             |               |                  |
+==================+=============+===============+==================+
| SCT              |             | "Not Visible" | not seen in this |
|                  |             |               | image            |
+------------------+-------------+---------------+------------------+
| SCT              | 278650002   | "Edentulous"  | if in the view,  |
|                  |             |               | one expects to   |
|                  |             |               | see teeth but    |
|                  |             |               | sees none. The   |
|                  |             |               | subcategories of |
|                  |             |               | this SNOMED code |
|                  |             |               | are of limited   |
|                  |             |               | interest for the |
|                  |             |               | orthodontic      |
|                  |             |               | domain, however  |
|                  |             |               | they may be used |
|                  |             |               | within a Primary |
|                  |             |               | Anatomic         |
|                  |             |               | Structure        |
|                  |             |               | Modifier         |
|                  |             |               | Sequence         |
|                  |             |               | (0008,2230).     |
+------------------+-------------+---------------+------------------+
| SCT              | *245575001* | "11"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245574002* | "12"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245572003* | "13"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245571005* | "14"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245570006* | "15"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245568002* | "16"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245567007* | "17"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245566003* | "18"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245587008* | "21"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245586004* | "22"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245584001* | "23"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245583007* | "24"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245582002* | "25"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245579007* | "26"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245578004* | "27"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245577009* | "28"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245611006* | "31"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245610007* | "32"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245608005* | "33"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245607000* | "34"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245606009* | "35"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245604007* | "36"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245603001* | "37"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245602006* | "38"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245600003* | "41"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245599001* | "42"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245597004* | "43"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245596008* | "44"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245595007* | "45"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245592005* | "46"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245591003* | "47"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245590002* | "48"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245620002* | "51"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245619008* | "52"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245617005* | "53"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245616001* | "54"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245615002* | "55"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245627004* | "61"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245626008* | "62"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245624006* | "63"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245623000* | "64"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245622005* | "65"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245642001* | "71"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245641008* | "72"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245639007* | "73"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245638004* | "74"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245637009* | "75"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245635001* | "81"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245634002* | "82"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245632003* | "83"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245631005* | "84"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the view         |
+------------------+-------------+---------------+------------------+
| SCT              | *245630006* | "85"          | if this          |
|                  |             |               | particular tooth |
|                  |             |               | is visible in    |
|                  |             |               | the              |
+------------------+-------------+---------------+------------------+

Primary Anatomic Structure for Extraoral Photography
::::::::::::::::::::::::::::::::::::::::::::::::::::

+-----------------+------------+-----------------+-----------------+
| Code Scheme     | Code Value | Code Meaning    | when to use     |
| Designator      |            |                 |                 |
+=================+============+=================+=================+
| SCT             | 362627000  | Entire left     | For all left    |
|                 |            | side of face    | profile         |
|                 |            |                 | photographs.    |
+-----------------+------------+-----------------+-----------------+
| SCT             | 362626009  | Entire right    | For all right   |
|                 |            | side of face    | profile         |
|                 |            |                 | photographs.    |
+-----------------+------------+-----------------+-----------------+
| SCT             | 368761004  | Entire center   | For all frontal |
|                 |            | of face         | photographs.    |
+-----------------+------------+-----------------+-----------------+

Choosing the Correct Primary Anatomic Structure
-----------------------------------------------

Intraoral Photography
:::::::::::::::::::::

-  When one tooth is visible, this sequence will contain a single SNOMED
   CT code representing the visible tooth.

-  When more teeth are visible, this sequence will contain a list of
   SNOMED CT codes representing all visible teeth.

-  When the region of the mouth imaged is not expected to show any teeth, omit this
   sequence completely.

-  Use Edentulous when one would normally expect to see teeth in that region,
   however the field of view is of an are of the mouth that no longer has (or
   was always missing) teeth. An edentulous patient may have only one or two
   missing teeth, either in one spot or throughout the mouth.

Extraoral Photography
:::::::::::::::::::::

.. TODO: Do we have to put something here?

