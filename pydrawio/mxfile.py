import xml.etree.ElementTree as ET
from core import XmlObject
from typing import List

class Diagram(XmlObject):
    ''' Diagram
    Attributes:
        id (str)
        name (str)
        value (str)
    '''

    id: str
    name: str
    value: str

    def __init__(self, element: ET.Element):
        super().__init__(element)
        self.value = element.text

    def make_tree(self) -> ET.ElementTree:
        diagram = ET.Element('diagram')
        diagram = super().set_attrib(diagram)
        diagram.text = self.value

        return ET.ElementTree(diagram)

class Mxfile(XmlObject):
    ''' Mxfile
    Attributes:
        host (str)
        modified (str)
        agent (str)
        version (str)
        type (str)
        etag (str)
        diagram (List[Diagram])
    '''

    host: str
    modified: str
    agent: str
    version: str
    type: str
    etag: str
    diagram: List[Diagram]

    def __init__(self, xmlstr: str='<mxfile host="" modified="" agent="" version="" type="" etag=""></mxfile>'):
        tree = ET.ElementTree(ET.fromstring(xmlstr))
        root = tree.getroot()
        super().__init__(root)
        self.diagram = []
        diagrams = list(root)
        for diagram in diagrams:
            self.diagram.append(Diagram(diagram))

    def make_tree(self) -> ET.ElementTree:
        mxfile = ET.Element('mxfile')
        mxfile = super().set_attrib(mxfile)
        for diagram in self.diagram:
            mxfile.append(diagram.make_tree().getroot())

        return ET.ElementTree(mxfile)

    def write(self, filepath: str, encoding='utf-8'):
        ''' write
        Write Mxfile
        Args:
            filepath (str): Output filepath
            (optional) encoding (str): encode type
        '''

        self.make_tree().write(filepath, encoding=encoding)
