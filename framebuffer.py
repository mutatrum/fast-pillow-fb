from PIL import Image, ImageColor
import pyximport; pyximport.install()
import RGBtoBGR

class Framebuffer(object):
    def __init__(self, device_no: int):
        self.path = "/dev/fb%d" % device_no
        config_dir = "/sys/class/graphics/fb%d/" % device_no
        self.size = tuple(_read_config(config_dir + "virtual_size"))
        self.stride = _read_config(config_dir + "stride")[0]
        self.bits_per_pixel = _read_config(config_dir + "bits_per_pixel")[0]
        assert self.stride == self.bits_per_pixel // 8 * self.size[0]

    def __str__(self):
        args = (self.path, self.size, self.stride, self.bits_per_pixel)
        return "%s  size:%s  stride:%s  bits_per_pixel:%s" % args

    def show(self, image: Image):
        assert image.size == self.size

        raw = bytearray(image.tobytes())

        out = RGBtoBGR.rgbtobgr(raw)

        with open(self.path, "wb") as fp:
            fp.write(out)

    def on(self):
        pass

    def off(self):
        pass


def _read_config(filename):
    with open(filename, "r") as fp:
        content = fp.readline()
        tokens = content.strip().split(",")
        return [int(t) for t in tokens if t]
