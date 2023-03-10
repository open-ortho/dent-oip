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
PATH_VIEW_EXAMPLES = Path(PATH_APPENDIX, "ViewExamples","generated")

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

    PATH_TABLES_GENERATED.mkdir(parents=True, exist_ok=True)
    for dcm in PATH_IMAGES.glob("*.dcm"):
        logging.info(f"Converting {dcm} to CSV.")
        save_dataset_to_csv(dcm)

def generate_rst_pages():
    def h1(h_text):
        return h_text + f"\n{'-' * len(h_text)}"

    def generate_rst_page_from_dcm(dcm_filename):
        """Write Intraoral Views to RestructuredText file.

        This function is very similar to ev_write_rst and has been kept separate on
        purpose, to allow for customization.
        """
        ds = dcmread(dcm_filename)
        number, title = ds.ImageComments.split("^")
        file_stem = Path(dcm_filename.stem)
        image_filename = file_stem.with_suffix(".png")
        image_path = f"../../../images/{image_filename}"
        rst_filename = file_stem.with_suffix(".rst")
        rst_path = Path(PATH_VIEW_EXAMPLES,rst_filename)

        rst_string = f"""
{h1(title)}

.. _{number}:
.. image:: {image_path}
    :class: with-border
    :align: center
    :alt: Line drawing of {title}
    
    
.. csv-table:: {number}
   :file: ../../../tables/generated/{number}.csv
   :widths: 40, 10, 10, 40
   :header-rows: 1
    
    
Primary Anatomic Structure Sequence
:::::::::::::::::::::::::::::::::::
    
See section :ref:`primary anatomic structure sequence`
    
"""

        with open(rst_path, "w") as rst_out:
            rst_out.write(rst_string)
        

    # Make output directory if it doesn't exist already.
    PATH_VIEW_EXAMPLES.mkdir(parents=True, exist_ok=True)
    for dcm in PATH_IMAGES.glob("*.dcm"):
        logging.info(f"Creating RST page for {dcm}.")
        generate_rst_page_from_dcm(dcm)

def main(args):
    print("Main")
    generate_views_in_dicom()
    generate_tables_in_csv()
    generate_rst_pages()

if __name__ == "__main__":
    main(sys.argv[1:])
