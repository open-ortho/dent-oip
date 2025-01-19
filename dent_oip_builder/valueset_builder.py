""" Python module to convert FHIR value sets to sphinx documentation.

The various tables which rely on various codes which can be obtaines as FHIR ValueSets should use this code to generate the RST Sphinx source files.

"""
import requests
import csv
from pathlib import Path

urls = [
    "http://terminology.open-ortho.org/fhir/extraoral-2d-photographic-scheduled-protocol",
    "http://terminology.open-ortho.org/fhir/intraoral-2d-photographic-scheduled-protocol",
    "http://terminology.open-ortho.org/fhir/extraoral-3d-visible-light-scheduled-protocol",
    "http://terminology.open-ortho.org/fhir/intraoral-3d-visible-light-scheduled-protocol"
]


def download_fhir_codesystem_to_rst(url, output_file):
    response = requests.get(url)
    response.raise_for_status()
    codesystem = response.json()

    with open(output_file, 'a') as file:
        file.write(f".. _{codesystem['id']}:\n")
        file.write(f".. list-table:: {codesystem['title']}\n")
        file.write("    :header-rows: 1\n\n")
        file.write("    * - code scheme designator\n")
        file.write("      - code value\n")
        file.write("      - code meaning\n")
        file.write("      - notes\n")

        for concept in codesystem['concept']:
            file.write(f"    * - {codesystem['url']}\n")
            file.write(f"      - {concept['code']}\n")
            file.write(f"      - {concept['display']}\n")
            file.write("      - \n")


def download_fhir_codesystem_to_csv(url, output_file):
    response = requests.get(url)
    response.raise_for_status()
    codesystem = response.json()

    with open(output_file, 'a', newline='', encoding='utf-8') as file:
        # get code scheme designator from codesystem
        if 'identifier' in codesystem:
            codeschemedesignator = codesystem['identifier'][0]['value']
        else:
            codeschemedesignator = codesystem['url']
        writer = csv.writer(file)
        writer.writerow(["Attribute Name", "Tag", "Value"])
        for concept in codesystem['concept']:
            writer.writerow(
                [codeschemedesignator, concept['code'], concept['display']])


def main():
    for url in urls:
        output_base_path = Path('source') / 'tables' / 'generated'
        # Create the directory if it doesn't exist
        output_base_path.mkdir(parents=True, exist_ok=True)
        for url in urls:
            output_file = output_base_path / (url.split('/')[-1] + '.csv')
            download_fhir_codesystem_to_csv(url, output_file)


if __name__ == "__main__":
    main()
