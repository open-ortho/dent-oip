3.1 Display Visible Light Images [DEN-1]
----------------------------------------
3.1.1 Scope
~~~~~~~~~~~
This transaction is used to present DICOM Visual Light Photographic Images to a dental professional interpreting a study.  This includes 2-dimensional radiographic images such as intraoral and panoramic image, cone beam computed tomography (CBCT) data); as well as visible light images, such as photographs in an organized and structured manner for all aspect of oral healthcare, including those in private practice settings.  The images rendered in this transaction are produced by a OIP Content Creator actor supporting the Direct Photography Option; see DEN TF-1: X.2.1.

*<NOTE to Toni:  The above list comes from the ADA spec, Introduction section pg 7>*

This transaction is not a typical network-based transaction between two devices; instead, the primary focus of the requirements is on the behavior of the display applction rather than messaging between two actors. This can be thought
of as an “informational transaction” between a display device and a user.

The display may have behaviors in addition to those required by this transaction.  

Methods for selecting and obtaining the data to be displayed are outside the scope of this transaction.

3.1.2 Actor Roles
~~~~~~~~~~~~~~~~~
The roles in this transaction are defined in the following table and may be played by the actors shown here:

**Table 3.1.2-1: Actor Roles**

.. list-table::
    :header-rows: 0

    * - **Role**
      - Display:  
           Presents results visually to a user.

    * - **Actor(s)**
      - The following actors may play the role of Display:   
           Image Display

3.1.3 Referenced Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~
+ ANSI/ADA Standard No. 1100, Rev. ??, "Dentistry - 2D and 3D Orthodontic/Cranial/Forensic Photographic Views and View Sets
+ TO DO: Add list of standards here...

3.1.4 Messages
~~~~~~~~~~~~~~

.. figure:: ../../images-static/Figure_3.1.4-1_InteractionDiagram.jpg
    :class: with-border with-shadow float-left
    :align: center

**Figure  3.1.4-1 Interaction Diagram**

3.1.4.1 Display Results
+++++++++++++++++++++++
The Display presents one or more DICOM studies to the user.

3.1.4.1.1 Trigger Events
^^^^^^^^^^^^^^^^^^^^^^^^
A user or an automated function determines that one or more studies should be presented.

3.1.4.1.2 Message Semantics
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The DICOM images are encoded as described in DEN TF-3: 7.3.1.

This transaction does not depend on how the DICOM images were transferred to the Display. If the Display
receives results by a profiled mechanism such as DICOM C-STORE, the messaging protocol is specified in that corresponding transaction. If results are accessed by being grouped with another actor such as a Content Consumer or an Image Manager / Image Archive, there is no messaging protocol involved.

3.1.4.1.3 Expected Actions (i.e., Display Requirements)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The behaviors in this section are specified as baseline capabilities.  Displays may have additional or alternate capabilities that may be invoked or configured.

Displays shall support the capabilities described in this section for DICOM images encoded in instances of the following:

* VL Photographic Image IOD as defined in DEN TF-3: 7.3.1.

3.1.4.1.3.1 General Display Requirements
****************************************
The Display shall:

+ <TO DO:  enumerate here requirements that apply to all IODs, or that are independent of an IOD type

<TO DO:  Next, add logical subsections.   There are examples of how this is done for NM display in RAD TF-2: 4.16.4.2.2.3, for mammo in RAD TF-2: 4.16.4.2.2.1, and for basic image review in RAD TF-2: 4.16.4.2.2.6.

3.1.4.1.3.2 Viewset VS-01
*************************
VS-01 (from DICOM correction package 1571) is the template preferred by the ABO for Case Submission and Display. It is the viewset most commonly used by orthodontic practitioners and vendors of orthodontic software.

The Display shall be able to display for the user Viewset VS-01, with eight images and one text box, as defined in **ANSI/ADA Standard No. 1100**, Section 10.

3.1.4.1.3.3 Viewset VS-02
*************************
VS-02 is a custom craniofacial viewset has greatest use for documentation of orthognathic and craniofacial surgery treatment.

The Display shall be able to display for the user Viewset VS-01, with 13 views as defined in **ANSI/ADA Standard No. 1100**, Section 10.

3.1.4.1.3.4 Viewset VS-03
*************************
VS-03 is a custom supplementary patient record display, presents specific views commonly requested by insurance companies for documentation of automatic qualifiers (such as excessive overjet or impinging deep bite).

The Display shall be able to display for the user Viewset VS-03, with 13 image boxes as defined in **ANSI/ADA Standard No. 1100**, Section 10.

3.1.4.1.3.5 Viewset VS-04
*************************
VS-04 is a custom supplementary patient record display, was designed to facilitate assessment of craniofacial asymmetries. 

The Display shall be able to display for the user Viewset VS-04, with 12 image boxes as defined in **ANSI/ADA Standard No. 1100**, Section 10.
