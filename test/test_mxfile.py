import unittest
from pydrawio.mxfile import Mxfile
from pydrawio.mxgraphmodel import decompress

class TestMxfile(unittest.TestCase):
    def test_mxfile(self):
        tests = '<mxfile host="Electron" modified="2022-09-07T15:50:09.872Z" agent="5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/20.2.8 Chrome/102.0.5005.167 Electron/19.0.15 Safari/537.36" etag="gzH0kVSIBYVuorkLmoRh" version="20.2.8" type="device"><diagram id="f0Od_lqmHJlGkMBThjxj" name="ページ1">jZJLT4QwEMc/DUcTCgbXq7i7HNaLHFaPDR1pkz5Ityzgp7fIlEeIiadOfzOdx38apbnqz5Y2/M0wkFESsz5KX6MkISTO/DGSYSIHcphAbQXDoAWU4hsQxkhbweC2CXTGSCeaLayM1lC5DaPWmm4b9mXktmpDa9iBsqJyT6+COY5TJE8LL0DUPFQm2fPkUTQE4yQ3TpnpVig9RmlujXGTpfoc5Che0GV6d/rDOzdmQbv/PIC8uH9cav2um/p60Z+iUMkDZrlT2eLA2KwbggLWtJrBmCSO0peOCwdlQ6vR2/mde8adkv5GvLlvKlQA66BfIWzyDEaBs4MPQe+8evwx5BHv3aI/CaLylfYZMoorr+fUiyreQGHCdVnAr2/1jdPjDw==</diagram></mxfile>'
        mxfile = Mxfile(tests)
        self.assertEqual('Electron', mxfile.host)
        self.assertEqual('2022-09-07T15:50:09.872Z', mxfile.modified)
        self.assertEqual('5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/20.2.8 Chrome/102.0.5005.167 Electron/19.0.15 Safari/537.36', mxfile.agent)
        self.assertEqual('gzH0kVSIBYVuorkLmoRh', mxfile.etag)
        self.assertEqual('20.2.8', mxfile.version)
        self.assertEqual('device', mxfile.type)
        self.assertEqual('f0Od_lqmHJlGkMBThjxj', mxfile.diagram[0].id)

    def test_decompress_mxgraphmodel(self):
        tests = '<mxfile host="Electron" modified="2022-09-07T15:50:09.872Z" agent="5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/20.2.8 Chrome/102.0.5005.167 Electron/19.0.15 Safari/537.36" etag="gzH0kVSIBYVuorkLmoRh" version="20.2.8" type="device"><diagram id="f0Od_lqmHJlGkMBThjxj" name="ページ1">jZJLT4QwEMc/DUcTCgbXq7i7HNaLHFaPDR1pkz5Ityzgp7fIlEeIiadOfzOdx38apbnqz5Y2/M0wkFESsz5KX6MkISTO/DGSYSIHcphAbQXDoAWU4hsQxkhbweC2CXTGSCeaLayM1lC5DaPWmm4b9mXktmpDa9iBsqJyT6+COY5TJE8LL0DUPFQm2fPkUTQE4yQ3TpnpVig9RmlujXGTpfoc5Che0GV6d/rDOzdmQbv/PIC8uH9cav2um/p60Z+iUMkDZrlT2eLA2KwbggLWtJrBmCSO0peOCwdlQ6vR2/mde8adkv5GvLlvKlQA66BfIWzyDEaBs4MPQe+8evwx5BHv3aI/CaLylfYZMoorr+fUiyreQGHCdVnAr2/1jdPjDw==</diagram></mxfile>'
        mxfile = Mxfile(tests)
        compressed = mxfile.diagram[0].value
        mxgraphmodel = decompress(compressed)
        self.assertEqual('0', mxgraphmodel.content.items[0].id)
        self.assertEqual('1', mxgraphmodel.content.items[1].id)

    def test_write(self):
        tests = '<mxfile host="Electron" modified="2022-09-07T15:50:09.872Z" agent="5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/20.2.8 Chrome/102.0.5005.167 Electron/19.0.15 Safari/537.36" etag="gzH0kVSIBYVuorkLmoRh" version="20.2.8" type="device"><diagram id="f0Od_lqmHJlGkMBThjxj" name="ページ1">jZJLT4QwEMc/DUcTCgbXq7i7HNaLHFaPDR1pkz5Ityzgp7fIlEeIiadOfzOdx38apbnqz5Y2/M0wkFESsz5KX6MkISTO/DGSYSIHcphAbQXDoAWU4hsQxkhbweC2CXTGSCeaLayM1lC5DaPWmm4b9mXktmpDa9iBsqJyT6+COY5TJE8LL0DUPFQm2fPkUTQE4yQ3TpnpVig9RmlujXGTpfoc5Che0GV6d/rDOzdmQbv/PIC8uH9cav2um/p60Z+iUMkDZrlT2eLA2KwbggLWtJrBmCSO0peOCwdlQ6vR2/mde8adkv5GvLlvKlQA66BfIWzyDEaBs4MPQe+8evwx5BHv3aI/CaLylfYZMoorr+fUiyreQGHCdVnAr2/1jdPjDw==</diagram></mxfile>'
        mxfile = Mxfile(tests)
        mxfile.write('/dev/null')
