import unittest
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
