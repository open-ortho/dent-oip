import logging
logging.basicConfig(level=logging.INFO)

import sys
import dicom4ortho.controller
from  pathlib import Path
from pydicom import dcmread

# Files and paths
PATH_TABLES = Path(".", "source", "tables")
PATH_APPENDIX = Path(".", "source", "Appendix")
PATH_IMAGES = Path(".", "source", "images")
PATH_TABLES_GENERATED = Path(PATH_TABLES, "generated")
RST_INTRAORAL_VIEWS = Path(PATH_APPENDIX, "01_intraoral_views.rst")
RST_EXTRAORAL_VIEWS = Path(PATH_APPENDIX, "02_extraoral_views.rst")
CSV_SNOMED = Path(PATH_TABLES, "codes_snomed.csv")
CSV_DICOM = Path(PATH_TABLES, "codes_dicom.csv")
CSV_DICOM_TAGS = Path(PATH_TABLES, "tags_dicom.csv")
CSV_VIEWS = Path(PATH_TABLES, "views.csv")
CSV_CID4018 = Path(PATH_TABLES, "CID-4018.csv")
CSV_CID4019 = Path(PATH_TABLES, "CID-4019.csv")
DBFILE = "views.db"

def generate_views_in_dicom():
    ''' Take the png files in images, extract the image type from the file name and generate the dcm files.'''
    def make_photo_metadata(input_image_filename):
        metadata = {
            "image_type": input_image_filename.stem.split("_")[0].replace("-",""),
            "patient_firstname": "Michael",
            "patient_lastname": "Jackson",
            "patient_id": "X1",
            "patient_sex": "M",
            "patient_birthdate": "1958-08-29",
            "dental_provider_firstname": "Conrad",
            "dental_provider_lastname": "Murray",
            "study_instance_uid": "generate_dicom_uid()",
            "series_instance_uid": "generate_dicom_uid()",
            "series_description": "UnitTest make_photo_metadata",
            "input_image_filename": input_image_filename,
        }
        return metadata

    for png in PATH_IMAGES.glob("*.png"):
        logging.info(f"Converting {png} to DICOM.")
        c = dicom4ortho.controller.SimpleController()
        c.convert_image_to_dicom4orthograph(metadata=make_photo_metadata(png))
        
def generate_tables_in_csv():
    ''' Generate the CSV tables which contain all DICOM tags.
    
    These should then be used to generate the RST pages for each view.
    '''
    ignore_values_of = [
        "(0008,0018)",
        "(0020,000d)",
        "(0020,000e)",
    ]
    def show_dataset(ds, indent):
        csv_row = ""
        for elem in ds:
            tag = str(elem.tag).replace(" ","")
            if elem.keyword != "PixelData":
                if elem.VR == "SQ" or tag in ignore_values_of:
                    value = ""
                else:
                    value = elem.value
                attr_name = f"{indent} {elem.name}".strip()
                csv_row += f'"{attr_name}","{tag}","{value}",""\n'
            if elem.VR == "SQ":
                indent += ">"
                for item in elem:
                    csv_row += show_dataset(item, indent)
                indent = indent[1:]
        return csv_row

    def save_dataset_to_csv(file_name):
        logging.info(f"Creating CSV File from {file_name}")
        ds = dcmread(file_name)
        csv_header = '"Attribute Name","Tag","Value","Meaning"\n'
        csv_body = show_dataset(ds, indent="")
        csv_file_name = Path(PATH_TABLES_GENERATED,file_name.stem).with_suffix(".csv")

        with open(csv_file_name,'w') as csvfile:
            csvfile.write(f"{csv_header}{csv_body}")

    for dcm in PATH_IMAGES.glob("*.dcm"):
        logging.info(f"Converting {dcm} to CSV.")
        save_dataset_to_csv(dcm)


def main(args):
    print("Main")
    # generate_views_in_dicom()
    generate_tables_in_csv()

if __name__ == "__main__":
    main(sys.argv[1:])
