# fast-pillow-fb
Fast Python/PILLOW rendering to framebuffer on Raspberry Pi

# Description

Python library to enable fast-ish framebuffer rendering from PILLOW to the Raspberry Pi framebuffer.

The Raspberry Pi framebuffer has a reversed pixel format, BGR instead of RGB. For slow Raspberry Pi versions and larger displays, this is not feasible to do in pure python.

The demo running on a Raspberry Pi Zero and a [Waveshare 2.8inch Display HAT](https://www.waveshare.com/wiki/2.8inch_DPI_LCD):

| Pixel format conversion code | fps |
|---|---|
| python | 1 fps |
| numpy | 7 fps |
| cython | 17 fps |
| no conversion (wrong colors) | 25 fps |

The code is also tested on a [Waveshare 1.3inch LCD Hat](https://www.waveshare.com/wiki/1.3inch_LCD_HAT).

## Requirements

cython
