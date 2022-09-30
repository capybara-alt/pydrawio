# Pydrawio
## Quick Start
```
~$ pip install pydrawio
```
## Usage
### MxGraphModel
```
        # get compressed string from Mxfile or Mxlibrary
        compressed = 'lJI9b8MgGIR/DWMlA1WaDl5i5WNIl2ZIOyLz1iDxJUJip7++ChCMoizdfA9nOO4F0U5PW8+c+LAcFCINn1pECMbNAhFy09ebXuJlkoOXPBpmeZC/EFGT2VlyOFWmYK0K0tWot8ZAHyrCvLdjbfmxqj7JsQEe5KFn6pEdJQ8iJiZvM92BHEQ6DS/eE9csGXPqk2DcjgXQNaKdtzakLz11oG71pNvPFkQ2ee2ZrwTzYMJ/foRud/naD+bTuOG4N99yp8lL3u3C1DleOwcP19SCt2fDgbcNoqtRyAAHx3poR88coisRtGoxoqvHSPddwQeYCsihtmA1BH9FpIlrZcjxVeDXrMZ76/hepyiNLzJhcbhD2bDuoRzzrBpENvMgkn1+sHT9BwAA//8BAAD//w=='
        mxgraphmodel = decompress(compressed)
        # processing mxgraphmodel
        mxgraphmodel.compress()
```
### Mxlibrary
```
        # create Mxlibrary instance
        mxlibrary = Mxlibrary() # or Mxlibrary(Mxlibrary_file_contents)
        # make mxlibobject
        mxlibobj1 = mxlibrary.make_mxlibobject(mxgraphmodel, 'test_lib_1',  25, 25)
        mxlibobj2 = mxlibrary.make_mxlibobject(mxgraphmodel, 'test_lib_2',  25, 25)
        # set Mxlibobject
        mxlibrary.set_mxlibobject([ mxlibobj1, mxlibobj2 ])
        # write mxlibrary file
        mxlibrary.write(filepath)
        
        # get Mxlibobject
        mxlibobj = json.loads(mxlibrary.value)
        for mxlibobj in mxlibobjs:
            mxlibobj = Mxlibobject(**mxlibobj)
```
### Mxfile
```
        mxfile = Mxfile() # or Mxfile(Mxfile_file_contents)
        # get MxGraphModel from Mxfile
        compressed = mxfile.diagram[0].value
        mxgraphmodel = decompress(compressed)

        # processing MxGraphModel

        # write mxfile file
        mxfile.write(filepath)
```