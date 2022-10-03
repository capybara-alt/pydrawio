import unittest
import xml.etree.ElementTree as ET
from pydrawio.mxgraphmodel import decompress, MxGraphModel

class TestMxGraphModel(unittest.TestCase):
    def test_decompress(self):
        tests = 'lJI9b8MgGIR/DWMlA1WaDl5i5WNIl2ZIOyLz1iDxJUJip7++ChCMoizdfA9nOO4F0U5PW8+c+LAcFCINn1pECMbNAhFy09ebXuJlkoOXPBpmeZC/EFGT2VlyOFWmYK0K0tWot8ZAHyrCvLdjbfmxqj7JsQEe5KFn6pEdJQ8iJiZvM92BHEQ6DS/eE9csGXPqk2DcjgXQNaKdtzakLz11oG71pNvPFkQ2ee2ZrwTzYMJ/foRud/naD+bTuOG4N99yp8lL3u3C1DleOwcP19SCt2fDgbcNoqtRyAAHx3poR88coisRtGoxoqvHSPddwQeYCsihtmA1BH9FpIlrZcjxVeDXrMZ76/hepyiNLzJhcbhD2bDuoRzzrBpENvMgkn1+sHT9BwAA//8BAAD//w=='
        mxgraphmodel = decompress(tests)
        self.assertEqual('0', mxgraphmodel.content.items[0].id)
        self.assertEqual('1', mxgraphmodel.content.items[1].id)
        self.assertEqual('eCHvXLgnRnpgWLnYiHm2-1', mxgraphmodel.content.items[2].id)

    def test_compress(self):
        tests = 'lJI9b8MgGIR/DWMlA1WaDl5i5WNIl2ZIOyLz1iDxJUJip7++ChCMoizdfA9nOO4F0U5PW8+c+LAcFCINn1pECMbNAhFy09ebXuJlkoOXPBpmeZC/EFGT2VlyOFWmYK0K0tWot8ZAHyrCvLdjbfmxqj7JsQEe5KFn6pEdJQ8iJiZvM92BHEQ6DS/eE9csGXPqk2DcjgXQNaKdtzakLz11oG71pNvPFkQ2ee2ZrwTzYMJ/foRud/naD+bTuOG4N99yp8lL3u3C1DleOwcP19SCt2fDgbcNoqtRyAAHx3poR88coisRtGoxoqvHSPddwQeYCsihtmA1BH9FpIlrZcjxVeDXrMZ76/hepyiNLzJhcbhD2bDuoRzzrBpENvMgkn1+sHT9BwAA//8BAAD//w=='
        mxgraphmodel = decompress(tests)
        mxgraphmodel = decompress(mxgraphmodel.compress())

    def test_get_ids(self):
        tests = 'lJI9b8MgGIR/DWMlA1WaDl5i5WNIl2ZIOyLz1iDxJUJip7++ChCMoizdfA9nOO4F0U5PW8+c+LAcFCINn1pECMbNAhFy09ebXuJlkoOXPBpmeZC/EFGT2VlyOFWmYK0K0tWot8ZAHyrCvLdjbfmxqj7JsQEe5KFn6pEdJQ8iJiZvM92BHEQ6DS/eE9csGXPqk2DcjgXQNaKdtzakLz11oG71pNvPFkQ2ee2ZrwTzYMJ/foRud/naD+bTuOG4N99yp8lL3u3C1DleOwcP19SCt2fDgbcNoqtRyAAHx3poR88coisRtGoxoqvHSPddwQeYCsihtmA1BH9FpIlrZcjxVeDXrMZ76/hepyiNLzJhcbhD2bDuoRzzrBpENvMgkn1+sHT9BwAA//8BAAD//w=='
        mxgraphmodel = decompress(tests)
        ids = mxgraphmodel.get_ids()
        self.assertEqual('0', ids[0])
        self.assertEqual('1', ids[1])
        self.assertEqual('eCHvXLgnRnpgWLnYiHm2-1', ids[2])

    def test_find_content(self):
        tests = 'lJI9b8MgGIR/DWMlA1WaDl5i5WNIl2ZIOyLz1iDxJUJip7++ChCMoizdfA9nOO4F0U5PW8+c+LAcFCINn1pECMbNAhFy09ebXuJlkoOXPBpmeZC/EFGT2VlyOFWmYK0K0tWot8ZAHyrCvLdjbfmxqj7JsQEe5KFn6pEdJQ8iJiZvM92BHEQ6DS/eE9csGXPqk2DcjgXQNaKdtzakLz11oG71pNvPFkQ2ee2ZrwTzYMJ/foRud/naD+bTuOG4N99yp8lL3u3C1DleOwcP19SCt2fDgbcNoqtRyAAHx3poR88coisRtGoxoqvHSPddwQeYCsihtmA1BH9FpIlrZcjxVeDXrMZ76/hepyiNLzJhcbhD2bDuoRzzrBpENvMgkn1+sHT9BwAA//8BAAD//w=='
        mxgraphmodel = decompress(tests)
        content = mxgraphmodel.find_content('eCHvXLgnRnpgWLnYiHm2-1')
        self.assertEqual('eCHvXLgnRnpgWLnYiHm2-1', content.id)

    def test_find_content_not_found(self):
        tests = 'lJI9b8MgGIR/DWMlA1WaDl5i5WNIl2ZIOyLz1iDxJUJip7++ChCMoizdfA9nOO4F0U5PW8+c+LAcFCINn1pECMbNAhFy09ebXuJlkoOXPBpmeZC/EFGT2VlyOFWmYK0K0tWot8ZAHyrCvLdjbfmxqj7JsQEe5KFn6pEdJQ8iJiZvM92BHEQ6DS/eE9csGXPqk2DcjgXQNaKdtzakLz11oG71pNvPFkQ2ee2ZrwTzYMJ/foRud/naD+bTuOG4N99yp8lL3u3C1DleOwcP19SCt2fDgbcNoqtRyAAHx3poR88coisRtGoxoqvHSPddwQeYCsihtmA1BH9FpIlrZcjxVeDXrMZ76/hepyiNLzJhcbhD2bDuoRzzrBpENvMgkn1+sHT9BwAA//8BAAD//w=='
        mxgraphmodel = decompress(tests)
        content = mxgraphmodel.find_content('aaaa')
        self.assertEqual(None, content)

    def test_make_tree_1(self):
        tests = 'rZTJbsIwEEC/JsdKwW6r5FqgFKmVKnFA6s3EQ+LKiS1jSNKvr03G4Ai6ST3F82a8PY+S0GndLQzT1YviIBOS8i6hs4SQCckz9/GkH0hG0gGURnAsOoOV+ACEoWwvOOxGhVYpaYUew0I1DRR2xJgxqh2XbZUc76pZCRdgVTB5SdeC2wppHq7hE08gyipsTVLM1CxUI9hVjKs2QnSe0KlRyg6jupuC9PaCmGHe4xfZ08kMNPY3E1p50Hq2XN7O88Pzuqtf33J5g6scmNzjjfGwtg8KjNo3HPwiaUIf2kpYWGlW+GzrHt2xytbSRRM3vDxU2AGMhS5CeMgFqBqs6V0JZu+CQWwZmmPcRg8QpFaR+3tkDN+8PC19tuIGKOYYqs277xqSSrYBGQuwvcb7F8IUzsWRfuuSRNdC95FGB1zTws8K2U4PnbwVndf+L07J2Cm54jS7ojT7u1IXotUQnlv8WBr9Kej8Ew=='
        mxgraphmodel = decompress(tests)
        xml_str = ET.tostring(mxgraphmodel.make_tree().getroot())
        self.assertEqual('<mxGraphModel dx="1298" dy="820" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1920" pageHeight="1200" math="0" shadow="0"><root><mxCell id="0" /><mxCell id="1" parent="0" /><mxCell id="wlvppDII4E9vLWxmPZ9l-1" value="" style="rounded=0;whiteSpace=wrap;html=1;" parent="1" vertex="1"><mxGeometry x="500" y="390" width="120" height="60" as="geometry" /></mxCell><object label="" type="circle" id="wlvppDII4E9vLWxmPZ9l-2"><mxCell style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;" parent="1" vertex="1"><mxGeometry x="520" y="290" width="80" height="80" as="geometry" /></mxCell></object></root></mxGraphModel>',
        xml_str.decode())

    def test_make_tree_2(self):
        tests = '<mxGraphModel dx="1298" dy="820" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1920" pageHeight="1200" math="0" shadow="0"><root><mxCell id="0" /><mxCell id="1" parent="0" /><mxCell id="wlvppDII4E9vLWxmPZ9l-1" value="" style="rounded=0;whiteSpace=wrap;html=1;" parent="1" vertex="1"><mxGeometry x="500" y="390" width="120" height="60" as="geometry"><mxPoint x="0" y="0" /><mxPoint x="1" y="1" /></mxGeometry></mxCell><object label="" type="circle" id="wlvppDII4E9vLWxmPZ9l-2"><mxCell style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;" parent="1" vertex="1"><mxGeometry x="520" y="290" width="80" height="80" as="geometry" /></mxCell></object></root></mxGraphModel>'
        mxgraphmodel = MxGraphModel(tests)
        xml_str = ET.tostring(mxgraphmodel.make_tree().getroot())
        self.assertEqual(tests, xml_str.decode())
