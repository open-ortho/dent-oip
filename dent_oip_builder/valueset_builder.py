""" Python module to convert FHIR value sets to sphinx documentation.

The various tables which rely on various codes which can be obtaines as FHIR ValueSets should use this code to generate the RST Sphinx source files.

"""
import requests
import ftplib
import tempfile
import csv
import json
from urllib.parse import urlparse
from pathlib import Path
from fhir.resources.codesystem import CodeSystem
from fhir.resources.valueset import ValueSet

import logging
# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


SYSTEM_TO_CODESCHEMEDESIGNATOR_MAP = {
    "http://dicom.nema.org/resources/ontology/DCM": "DCM",
    "http://snomed.info/srt": "SRT",
    "http://snomed.info/sct": "SCT",
    "http://loinc.org": "LOINC",
    "http://​www.snomed.org/": "SRT",
    "http://sig.biostr.washington.edu/projects/fm/AboutFM.html": "FMA",
}


urls = [
    "http://terminology.open-ortho.org/fhir/extraoral-2d-photographic-scheduled-protocol",
    "http://terminology.open-ortho.org/fhir/intraoral-2d-photographic-scheduled-protocol",
    "http://terminology.open-ortho.org/fhir/extraoral-3d-visible-light-scheduled-protocol",
    "http://terminology.open-ortho.org/fhir/intraoral-3d-visible-light-scheduled-protocol",
    "ftp://medical.nema.org/medical/dicom/resources/valuesets/fhir/json/ValueSet-dicom-cid-2-AnatomicModifier.json",
    "ftp://medical.nema.org/medical/dicom/resources/valuesets/fhir/json/ValueSet-dicom-cid-7201-ReferencedImagePurposeOfReference.json",
    "ftp://medical.nema.org/medical/dicom/resources/valuesets/fhir/json/ValueSet-dicom-cid-247-LateralityLeftRightOnly.json"
]


def download_fhir_codesystem_to_csv(url, output_file):
    logger.info(f"Downloading {url} to {output_file}")
    parsed_url = urlparse(url)
    if parsed_url.scheme in ['http', 'https']:
        response = requests.get(url)
        response.raise_for_status()
        codesystem = response.json()
    elif parsed_url.scheme == 'ftp':
        ftp = ftplib.FTP(parsed_url.hostname)
        ftp.login()
        ftp.cwd(parsed_url.path.rsplit('/', 1)[0])
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            ftp.retrbinary(f"RETR {parsed_url.path.rsplit('/', 1)[1]}", temp_file.write)
            temp_file.seek(0)  # Go back to the beginning of the file
            codesystem = json.load(temp_file)

    else:
        raise ValueError("Unsupported URL scheme")

    if 'resourceType' in codesystem and codesystem['resourceType'] == 'CodeSystem':
        codesystem = CodeSystem.model_validate(codesystem)
        write_codesystem_to_csv(codesystem, output_file)
    elif 'resourceType' in codesystem and codesystem['resourceType'] == 'ValueSet':
        valueset = ValueSet.model_validate(codesystem)
        write_valueset_to_csv(valueset, output_file)


def write_valueset_to_csv(valueset, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Coding Scheme Designator",
                        "Code Value", "Code Meaning"])
        for system in valueset.compose.include:
            codeschemedesignator = SYSTEM_TO_CODESCHEMEDESIGNATOR_MAP.get(system.system)
            if not codeschemedesignator:
                logger.warning(
                    f"Unknown system {system.system}, skipping")
                continue

            for concept in system.concept:
                writer.writerow(
                    [codeschemedesignator, concept.code, concept.display])


def write_codesystem_to_csv(codesystem, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        if hasattr(codesystem, 'identifier') and codesystem.identifier:
            codeschemedesignator = codesystem.identifier[0].value
        else:
            codeschemedesignator = codesystem.url
        writer = csv.writer(file)
        writer.writerow(["Coding Scheme Designator",
                        "Code Value", "Code Meaning"])
        for concept in codesystem.concept:
            writer.writerow(
                [codeschemedesignator, concept.code, concept.display])


def main():
    for url in urls:
        output_base_path = Path('source') / 'tables' / 'generated'
        # Create the directory if it doesn't exist
        output_base_path.mkdir(parents=True, exist_ok=True)
        output_file = output_base_path / (url.split('/')[-1] + '.csv')
        download_fhir_codesystem_to_csv(url, output_file)


if __name__ == "__main__":
    main()
