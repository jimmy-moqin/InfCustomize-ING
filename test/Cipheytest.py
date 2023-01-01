import base64
import zlib

cobj = zlib.compressobj(wbits=-zlib.MAX_WBITS)
dobj = zlib.decompressobj(wbits=-zlib.MAX_WBITS)

with open("base64str", "r") as f:
    b = f.read()

lenth = len(b)
d = base64.b64decode(b)
data_string = dobj.decompress(d)
data_string += dobj.flush()

with open('data_string', 'wb') as f:
    f.write(data_string)


# with open('data_string', 'rb') as f:
#     data_string = f.read()

# data1 = cobj.compress(data_string)
# data1 += cobj.flush()
# data2 = base64.b64encode(data1)

# with open('data2', 'wb') as f:
#     f.write(data2)





