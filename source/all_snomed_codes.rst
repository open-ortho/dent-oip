.. _scroll-bookmark-2:

Summary of DICOM tags for orthodontic/craniofacial views
========================================================

It was compiled from the various DICOM CID (Content IDs) tables. Only
the domain relevant values of each table are included here.The table
below contains all DICOM tags used to uniquely identify and encode each
orthodontic view.

It was compiled from the various DICOM CID (Content IDs) tables. Only
the domain relevant values of each table are included here.

.. csv-table :: testtable
	:file:	all_snomed_codes.csv
	:delim:	tab
	:header: "Image Laterality (0020,0062)","Patient Orientation (0020,0020)","Anatomic Region Sequence (0008,2218)","Anatomic Region Modifier Sequence (0008,2220)","Primary Anatomic Structure Sequence (0008,2228)","Acquisition View (xxxx,xxxx)","Image View (xxxx,xxxx)","Functional Condition Present During Acquisition (CID 91) (xxxx,xxxx)","Occlusal Relationship (xxxx,xxxx)"

+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| Image | Pa    | Ana   | *Ana  | Pr    | A     | Image | Funct | Occ   |
| Later | tient | tomic | tomic | imary | cquis | View  | ional | lusal |
| ality | O     | R     | R     | Ana   | ition |       | Cond  | Re    |
| (     | rient | egion | egion | tomic | View  | *(x   | ition | latio |
| 0020, | ation | Seq   | Mod   | Stru  |       | xxx,x | Pr    | nship |
| 0062) | (     | uence | ifier | cture | *(x   | xxx)* | esent |       |
|       | 0020, |       | Sequ  | Seq   | xxx,x |       | D     | *(x   |
|       | 0020) | *(0   | ence* | uence | xxx)* |       | uring | xxx,x |
|       |       | 008,2 |       |       |       |       | A     | xxx)* |
|       |       | 218)* | *(0   | (     |       |       | cquis |       |
|       |       |       | 008,2 | 0008, |       |       | ition |       |
|       |       |       | 220)* | 2228) |       |       | (CID  |       |
|       |       |       |       |       |       |       | 91)   |       |
|       |       |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       | *(x   |       |
|       |       |       |       |       |       |       | xxx,x |       |
|       |       |       |       |       |       |       | xxx)* |       |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| "U"   | "A    | "     | "Bu   | (See  | "Sa   | "Di   | "Lip  | "Ce   |
|       | ","F" | Face" | ccal" | se    | gitta | rect" | rel   | ntric |
|       |       | SCT:  | SCT:  | ction | l/Lat | SCT:  | axed" | occl  |
|       |       | *     | *     | *Pr   | eral" | *     | SCT:  | usion |
|       |       | 30254 | 26106 | imary | SCT:  | 25558 | *     | of    |
|       |       | 9007* | 2005* | Ana   | *3073 | 9003* | 78931 | t     |
|       |       |       |       | tomic | 0003* |       | 4008* | eeth" |
|       |       |       |       | Stru  |       |       |       | SCT:  |
|       |       |       |       | cture |       |       |       | *     |
|       |       |       |       | Seque |       |       |       | 11032 |
|       |       |       |       | nce*) |       |       |       | 0000* |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| "L"   | "P    | "Max  | "Clos |       | "45°  | "Mir  | "Lips | "Ce   |
|       | ","F" | illa" | e-up" |       | d     | rored | cl    | ntric |
|       |       | SCT:  | SCT:  |       | egree | view  | osed" | rel   |
|       |       | *     | *     |       | view  | un    | SCT:  | ation |
|       |       | 18181 | 78913 |       | (f    | corre | *     | of    |
|       |       | 3003* | 1009* |       | ace)" | cted" | 78760 | t     |
|       |       |       |       |       | SCT:  | SCT:  | 7005* | eeth" |
|       |       |       |       |       | *     | 7891  |       | SCT:  |
|       |       |       |       |       | 78761 | 35000 |       | *     |
|       |       |       |       |       | 2006* |       |       | 73678 |
|       |       |       |       |       |       |       |       | 3005* |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| "R"   | "R    | "Mand | "     |       | "Co   | "M    | "S    | "Cant |
|       | ","F" | ible" | Null" |       | ronal | irror | mile" | of    |
|       |       | SCT:  | SCT:  |       | /Fro  | corre | SCT:  | occ   |
|       |       | *     | *     |       | ntal" | cted" | *     | lusal |
|       |       | 18181 | 27672 |       | SCT:  | SCT:  | 22558 | p     |
|       |       | 2008* | 7009* |       | 816   | *     | 3004* | lane" |
|       |       |       |       |       | 54009 | 78761 |       | SCT:  |
|       |       |       |       |       |       | 0003* |       | *     |
|       |       |       |       |       |       |       |       | 71079 |
|       |       |       |       |       |       |       |       | 3000* |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| "B"   |       | "Jaw  | "R    |       | "Occl | "Phy  | "Open | "     |
|       |       | re    | ight" |       | usal" | sical | m     | Null" |
|       |       | gion" | *SCT: |       | SCT:  | ob    | outh" | SCT:  |
|       |       | SCT:  | 2402  |       | *     | ject" | SCT:  | *     |
|       |       | *     | 8007* |       | 71009 | SCT:  | *     | 27672 |
|       |       | 18181 |       |       | 8004* | *     | 26201 | 7009* |
|       |       | 1001* |       |       |       | 27237 | 6004* |       |
|       |       |       |       |       |       | 8003* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       | "Oral | "Bila |       |       |       | "     |       |
|       |       | re    | teral |       |       |       | Mouth |       |
|       |       | gion" | (     |       |       |       | cl    |       |
|       |       | SCT:  | Right |       |       |       | osed" |       |
|       |       | *     | and   |       |       |       | SCT:  |       |
|       |       | 36262 | Left) |       |       |       | *     |       |
|       |       | 8005* | "SCT: |       |       |       | 28686 |       |
|       |       |       | 514   |       |       |       | 6000* |       |
|       |       |       | 40002 |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       | "Ant  | "Left |       |       |       | "Man  |       |
|       |       | erior | "SCT: |       |       |       | dible |       |
|       |       | t     | 77    |       |       |       | pos   |       |
|       |       | eeth" | 71000 |       |       |       | tured |       |
|       |       | SCT:  |       |       |       |       | for   |       |
|       |       | *     |       |       |       |       | ward" |       |
|       |       | 78931 |       |       |       |       | SCT:  |       |
|       |       | 3002* |       |       |       |       | *     |       |
|       |       |       |       |       |       |       | 78761 |       |
|       |       |       |       |       |       |       | 1004* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |       |       | "Man  |       |
|       |       |       |       |       |       |       | dible |       |
|       |       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       |       | artly |       |
|       |       |       |       |       |       |       | open, |       |
|       |       |       |       |       |       |       | mouth |       |
|       |       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       |       | artly |       |
|       |       |       |       |       |       |       | open" |       |
|       |       |       |       |       |       |       | SCT:  |       |
|       |       |       |       |       |       |       | *     |       |
|       |       |       |       |       |       |       | 78913 |       |
|       |       |       |       |       |       |       | 0005* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |       |       | "Infe |       |
|       |       |       |       |       |       |       | rior" |       |
|       |       |       |       |       |       |       | SCT:  |       |
|       |       |       |       |       |       |       | *     |       |
|       |       |       |       |       |       |       | 26108 |       |
|       |       |       |       |       |       |       | 9000* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |       |       | "Supe |       |
|       |       |       |       |       |       |       | rior" |       |
|       |       |       |       |       |       |       | SRT:  |       |
|       |       |       |       |       |       |       | *     |       |
|       |       |       |       |       |       |       | 26421 |       |
|       |       |       |       |       |       |       | 7000* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |       | "     | "T    |       |
|       |       |       |       |       |       |       | ongue |       |
|       |       |       |       |       |       |       | th    |       |
|       |       |       |       |       |       |       | rust" |       |
|       |       |       |       |       |       |       | SCT:  |       |
|       |       |       |       |       |       |       | *     |       |
|       |       |       |       |       |       |       | 11034 |       |
|       |       |       |       |       |       |       | 3009* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |       |       | "Gin  |       |
|       |       |       |       |       |       |       | gival |       |
|       |       |       |       |       |       |       | Reces |       |
|       |       |       |       |       |       |       | sion" |       |
|       |       |       |       |       |       |       | SCT:  |       |
|       |       |       |       |       |       |       | *435  |       |
|       |       |       |       |       |       |       | 6008* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |       |       | "Fr   |       |
|       |       |       |       |       |       |       | enum" |       |
|       |       |       |       |       |       |       | SCT:  |       |
|       |       |       |       |       |       |       | 4182  |       |
|       |       |       |       |       |       |       | 32001 |       |
|       |       |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       | *The  |       |
|       |       |       |       |       |       |       | sub   |       |
|       |       |       |       |       |       |       | categ |       |
|       |       |       |       |       |       |       | ories |       |
|       |       |       |       |       |       |       | of    |       |
|       |       |       |       |       |       |       | this  |       |
|       |       |       |       |       |       |       | S     |       |
|       |       |       |       |       |       |       | NOMED |       |
|       |       |       |       |       |       |       | code  |       |
|       |       |       |       |       |       |       | are   |       |
|       |       |       |       |       |       |       | of    |       |
|       |       |       |       |       |       |       | li    |       |
|       |       |       |       |       |       |       | mited |       |
|       |       |       |       |       |       |       | int   |       |
|       |       |       |       |       |       |       | erest |       |
|       |       |       |       |       |       |       | for   |       |
|       |       |       |       |       |       |       | the   |       |
|       |       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       |       | rthod |       |
|       |       |       |       |       |       |       | ontic |       |
|       |       |       |       |       |       |       | do    |       |
|       |       |       |       |       |       |       | main, |       |
|       |       |       |       |       |       |       | ho    |       |
|       |       |       |       |       |       |       | wever |       |
|       |       |       |       |       |       |       | they  |       |
|       |       |       |       |       |       |       | may   |       |
|       |       |       |       |       |       |       | be    |       |
|       |       |       |       |       |       |       | used  |       |
|       |       |       |       |       |       |       | w     |       |
|       |       |       |       |       |       |       | ithin |       |
|       |       |       |       |       |       |       | a     |       |
|       |       |       |       |       |       |       | Pr    |       |
|       |       |       |       |       |       |       | imary |       |
|       |       |       |       |       |       |       | Ana   |       |
|       |       |       |       |       |       |       | tomic |       |
|       |       |       |       |       |       |       | Stru  |       |
|       |       |       |       |       |       |       | cture |       |
|       |       |       |       |       |       |       | Mod   |       |
|       |       |       |       |       |       |       | ifier |       |
|       |       |       |       |       |       |       | Seq   |       |
|       |       |       |       |       |       |       | uence |       |
|       |       |       |       |       |       |       | (00   |       |
|       |       |       |       |       |       |       | 08,22 |       |
|       |       |       |       |       |       |       | 30).* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |       |       | *"F   |       |
|       |       |       |       |       |       |       | acial |       |
|       |       |       |       |       |       |       | pa    |       |
|       |       |       |       |       |       |       | lsy/B |       |
|       |       |       |       |       |       |       | ell's |       |
|       |       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       |       | alsy" |       |
|       |       |       |       |       |       |       | SCT:* |       |
|       |       |       |       |       |       |       | *     |       |
|       |       |       |       |       |       |       | 19309 |       |
|       |       |       |       |       |       |       | 3009* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |       |       | Null" |       |
|       |       |       |       |       |       |       | SCT:  |       |
|       |       |       |       |       |       |       | *     |       |
|       |       |       |       |       |       |       | 27672 |       |
|       |       |       |       |       |       |       | 7009* |       |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+
