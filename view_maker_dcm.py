import dicom4ortho.controller

def generate_views_in_dicom():
    ''' Take the png files in images, extract the image type from the file name and generate the dcm files.'''
    for png in list_of_pngs:
        c = dicom4ortho.controller.SimpleController()
        c.convert_image_to_dicom4orthograph(metadata=dicom_metadata(png))
        

def dicom_metadata():
    ''' Generate metadata that is to be used from all the images produced.
    
    Patient Demographics
    Doctor
    ...
    '''
    pass