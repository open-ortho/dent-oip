""" Python module to convert FHIR value sets to sphinx documentation.

The various tables which rely on various codes which can be obtaines as FHIR ValueSets should use this code to generate the RST Sphinx source files.

"""
import requests

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

def main():

    for url in urls:
        output_file = url.split('/')[-1] + '.rst'
        download_fhir_codesystem_to_rst(url, output_file)

if __name__ == "__main__":
    main()

