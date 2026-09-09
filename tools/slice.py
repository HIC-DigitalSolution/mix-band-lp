import sys
from PIL import Image
out, out_dir, name, slices = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
im = Image.open(out)
w, h = im.size
sh = h // slices
for i in range(slices):
    top = i * sh
    bottom = h if i == slices - 1 else top + sh
    path = "%s/%s-%d.png" % (out_dir, name, i + 1)
    im.crop((0, top, w, bottom)).save(path)
    print(path)
