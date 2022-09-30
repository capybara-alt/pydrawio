import json
import xml.etree.ElementTree as ET
from typing import List
from core import XmlObject
from .mxgraphmodel import MxGraphModel

class Mxlibobject:
    ''' Mxlibobject
    Mxlibobject manage object of Mxlibrary value (list of json)
    Attributes:
        w (str): Width of chart
        h (str): Height of chart
        title (str): Title of chart
        xml (str): Compressed MxGraphModel xml string
    '''

    w: str
    h: str
    title: str
    xml: str

    def __init__(self, **entries):
        self.__dict__.update(entries)

class Mxlibrary(XmlObject):
    ''' Mxlibrary
    Mxlibrary manage Mxlibrary file
    Attributes:
        value (str): Mxlibrary value (json string)
        __mxlibobjects (List[Mxlibobject]): List of Mxlibobject
    '''

    value: str
    __mxlibobjects: List[Mxlibobject]

    def __init__(self, xmlstr: str ='<mxlibrary></mxlibrary>'):
        tree = ET.ElementTree(ET.fromstring(xmlstr))
        root = tree.getroot()
        self.value = root.text
        self.__mxlibobjects = []

    def make_tree(self) -> ET.ElementTree:
        mxlibrary = ET.Element('mxlibrary')
        mxlibrary.text = json.dumps(self.__mxlibobjects)

        return ET.ElementTree(mxlibrary)

    def set_mxlibobject(self, mxlibobjects: List[Mxlibobject]):
        ''' set_mxlibobject
        Set Mxlibobject to class variable of Mxlibrary
        Args:
            mxlibobjects (List[Mxlibobject]): List of Mxlibobject
        Examples:
            >>> mxlibrary.set_mxlibobject([ Mxlibobject({ value: '', 'w': 24, 'h': 24, 'title': 'test' }), ... ])
        '''

        self.__mxlibobjects = mxlibobjects

    def make_mxlibobject(self, mxgraphmodel: MxGraphModel, title: str, height: int, width: int) -> Mxlibobject:
        ''' make_mxlibobejct
        Make Mxlibobject from Mxgraphmodel and title, height, width
        Args:
            mxgraphmodel: Mxgraphmodel of chart
            title: title string
            height: Library object height
            width: Library object width
        Returns:
            Mxlibobject: Mxlibobject made from MxGraphmodel, title, height, width
        '''

        mxlibobj = {}
        mxlibobj['xml'] = mxgraphmodel.compress()
        mxlibobj['h'] = height
        mxlibobj['w'] = width
        mxlibobj['title'] = title

        return Mxlibobject(**mxlibobj)
    
    def write(self, filepath: str):
        ''' write
        Write Mxlibrary to specific filepath
        Args: filepath: output filepath string
        '''

        self.make_tree().write(filepath)
