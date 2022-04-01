-- SQLite
CREATE TEMP TABLE iv_03 (
    id text,
    attribute_name text,
    tag text,
    code_value text,
    meaning text
);
--
INSERT INTO iv_03 (id, attribute_name, tag)
SELECT id,
    attribute_name,
    tag
FROM tags_dicom;
-- Patient Orientation
UPDATE iv_03
SET code_value = patient_orientation.code,
    meaning = patient_orientation.meaning
FROM (
        SELECT codes_dicom.code,
            codes_dicom.meaning
        FROM ortho_views
            INNER JOIN codes_dicom ON codes_dicom.id = ortho_views.patient_orientation
        WHERE ortho_views.view_name LIKE 'IV-03'
    ) as patient_orientation
WHERE id = 'patient_orientation';
-- Laterality
UPDATE iv_03
SET code_value = laterality.code,
    meaning = laterality.meaning
FROM (
        SELECT codes_dicom.code,
            codes_dicom.meaning
        FROM ortho_views
            INNER JOIN codes_dicom ON codes_dicom.id = ortho_views.laterality
        WHERE ortho_views.view_name LIKE 'IV-03'
    ) as laterality
WHERE id = 'laterality';
-- Anatomic Region Sequence
UPDATE iv_03
SET code_value = 'SCT-' || anatomic_region_sequence.code,
    meaning = anatomic_region_sequence.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.anatomic_region_sequence
        WHERE ortho_views.view_name LIKE 'IV-03'
    ) as anatomic_region_sequence
WHERE id = 'anatomic_region_sequence';
-- Anatomic Region Modifier Sequence
UPDATE iv_03
SET code_value = 'SCT-' || anatomic_region_modifier_sequnce.code,
    meaning = anatomic_region_modifier_sequnce.meaning
FROM (
        SELECT codes_snomed.code,
            codes_snomed.meaning
        FROM ortho_views
            INNER JOIN codes_snomed ON codes_snomed.id = ortho_views.anatomic_region_modifier_sequnce
        WHERE ortho_views.view_name LIKE 'IV-03'
    ) as anatomic_region_modifier_sequnce
WHERE id = 'anatomic_region_modifier_sequnce';
-- show results
SELECT id,
    attribute_name AS "Attribute Name",
    tag AS 'Tag',
    code_value AS 'Value',
    meaning AS 'Meaning'
FROM iv_03;