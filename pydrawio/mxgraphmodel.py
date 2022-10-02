import base64
import zlib
import urllib.parse
import keyword
import xml.etree.ElementTree as ET
from typing import Dict, List
from abc import ABCMeta, abstractmethod
from core import XmlObject

class MxPoint(XmlObject):
    ''' MxPoint
    Attributes:
        x (str)
        y (str)
        as_ (str)
    '''

    x: str
    y: str
    as_: str

    def __init__(self, element: ET.Element):
        super().__init__(element)

    def make_tree(self) -> ET.ElementTree:
        mxpoint = ET.Element('mxPoint')

        return ET.ElementTree(self.set_attrib(mxpoint))

class MxGeometry(XmlObject):
    ''' MxGeometry
    Attributes:
        x (str)
        y (str)
        width (str)
        height (str)
        as_ (str)
        relative (str)
        mxPoint (MxPoint)
    '''

    x: str
    y: str
    width: str
    height: str
    as_: str
    relative: str
    mxPoint: MxPoint

    def __init__(self, element: ET.Element):
        super().__init__(element)
        mxpoint = element.find('mxPoint')
        self.mxPoint = MxPoint(mxpoint) if mxpoint else None

    def make_tree(self) -> ET.ElementTree:
        mxgeometry = ET.Element('mxGeometry')
        mxgeometry = self.set_attrib(mxgeometry)
        if self.mxPoint is not None:
            mxgeometry.append(self.mxPoint.make_tree().getroot())

        return ET.ElementTree(mxgeometry)

class IContent(XmlObject):
    ''' IContent
    Superclasses MxCell and Object
    Attributes:
        id (str)
    '''

    id: str
    def __init__(self, element: ET.Element):
        super().__init__(element)

    @abstractmethod
    def make_tree(self) -> ET.ElementTree:
        raise NotImplementedError

class MxCell(IContent):
    ''' MxCell
    Attributes:
        value (str)
        style (str)
        parent (str)
        source (str)
        target (str)
        edge (str)
        vertex (str)
        mxGeometry (MxGeometry)
    '''

    value: str
    style: str
    parent: str
    source: str
    target: str
    edge: str
    vertex: str
    mxGeometry: MxGeometry

    def __init__(self, element: ET.Element):
        super().__init__(element)
        self.mxGeometry = element.find('mxGeometry')

    def make_tree(self) -> ET.ElementTree:
        mxcell = ET.Element('mxCell')
        mxcell = self.set_attrib(mxcell)
        if self.mxGeometry is not None:
            mxcell.append(self.mxGeometry.make_tree().getroot())

        return ET.ElementTree(mxcell)

class Object(IContent):
    ''' Object
    Attributes:
        label (str)
        mxCell (MxCell)
    '''

    label: str
    mxCell: MxCell

    def __init__(self, element: ET.Element):
        super().__init__(element)
        self.mxCell = element.find('mxCell')

    def make_tree(self) -> ET.ElementTree:
        object_ = ET.Element('object')
        object_ = self.set_attrib(object_)
        if self.mxCell is not None:
            object_.append(self.mxCell.make_tree().getroot())

        return ET.ElementTree(object_)

class Root(XmlObject):
    ''' Root
    Attributes:
        items (List[IContent])
    '''

    items: List[IContent]

    def __init__(self, element: ET.Element):
        super().__init__(element)
        self.items = []
        contents = list(element)
        for content in contents:
            self.items.append(Object(content)) if content.find('mxCell') else self.items.append(MxCell(content))

    def make_tree(self) -> ET.ElementTree:
        root = ET.Element('root')
        for item in self.items:
            root.append(item.make_tree().getroot())

        return ET.ElementTree(root)

class MxGraphModel(XmlObject):
    ''' MxGraphModel
    Attributes:
        content (Root)
        dx (str)
        dy (str)
        grid (str)
        gridSize (str)
        guides (str)
        tooltips (str)
        connect (str)
        arrows (str)
        fold (str)
        page (str)
        pageScale (str)
        pageWidth (str)
        pageHeight (str)
        math (str)
        shadow (str)
    '''

    content: Root
    dx: str
    dy: str
    grid: str
    gridSize: str
    guides: str
    tooltips: str
    connect: str
    arrows: str
    fold: str
    page: str
    pageScale: str
    pageWidth: str
    pageHeight: str
    math: str
    shadow: str

    def __init__(self, xmlstr: str):
        tree = ET.ElementTree(ET.fromstring(xmlstr))
        root = tree.getroot()
        super().__init__(root)
        content = root.find('root')
        self.content = Root(content) if content else None

    def make_tree(self) -> ET.ElementTree:
        mxGraphModel = ET.Element('mxGraphModel')
        mxGraphModel = super().set_attrib(mxGraphModel)
        if self.content is not None:
            mxGraphModel.append(self.content.make_tree().getroot())

        return ET.ElementTree(mxGraphModel)

    def compress(self) -> str:
        ''' compress
        Compress MxGraphModel xml string
        Returns:
            str: Compressed string
        '''

        tree = self.make_tree()
        quoted = urllib.parse.quote(ET.tostring(tree.getroot()), safe='~()*!.\'')
        compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15, memLevel=8, strategy=zlib.Z_DEFAULT_STRATEGY)
        compressed_b = compress.compress(quoted.encode())
        compressed_b += compress.flush()
        return base64.b64encode(compressed_b).decode()

    def get_ids(self) -> List[str]:
        ''' get_ids
        Get IContent ID list from MxGraphModel
        Returns:
            List[str]: IContent ID list
        '''

        return [ item.id for item in self.content.items ]

    def find_content(self, id_: str) -> IContent:
        ''' find_content
        Find IContent from MxGraphModel
        Args:
            id_ (str): Target IContent id
        Returns:
            IContent: First match IContent
        '''

        founds = list(filter(lambda item: item.id == id_, self.content.items))
        if len(founds) < 1:
            return None

        return founds[0]


def decompress(compressed_str: str) -> MxGraphModel:
    ''' decompress
    Decompress compressed MxGraphModel xml string
    Args:
        compressed_str (str): Compressed string
    Returns:
        MxGraphModel: Source MxGraphmOdel
    '''

    compressed_b = base64.b64decode(compressed_str.encode())
    compressed_b = zlib.decompress(compressed_b, wbits=-15)
    xmlstr = urllib.parse.unquote(compressed_b.decode())
    return MxGraphModel(xmlstr)
