import base64
import zlib
import urllib.parse
import keyword
import xml.etree.ElementTree as ET
from typing import Dict, List
from abc import ABCMeta, abstractmethod

class XmlObject(metaclass=ABCMeta):
    ''' XmlObject
    XmlObject class is a superclass of classes mapping from xml 
    '''
    def __init__(self, element: ET.Element):
        str_fields = filter(lambda key : type(element.attrib[key]) is str, element.attrib)
        for key in str_fields:
            if keyword.iskeyword(key):
                self.__dict__['{}_'.format(key)] = element.attrib[key]
            else:
                self.__dict__['{}'.format(key)] = element.attrib[key]

    def set_attrib(self, element: ET.Element) -> ET.Element:
        ''' set_attrib
        Set public field of implemented class to element attributes
        Args:
            element (xml.etree.ElementTree.Element): Target element
        Returns:
            xml.etree.ElementTree.Element: Input element with attributes
        '''

        str_fields = filter(lambda key : type(self.__dict__[key]) is str, self.__dict__)
        for key in str_fields:
            if keyword.iskeyword(key.removesuffix('_')):
                element.attrib[key.removesuffix('_')] = self.__dict__[key]
            else:
                element.attrib[key] = self.__dict__[key]

        return element
    
    @abstractmethod
    def make_tree(self) -> ET.ElementTree:
        ''' make_tree
        Abstract method to make ElementTree from XmlObject
        Raises:
            NoImplementedError: Subclass does not implement this method
        '''

        raise NotImplementedError
