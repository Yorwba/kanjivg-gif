#!/usr/bin/env python

from __future__ import division

import lxml.etree
import math
from PIL import Image, ImageDraw
import subprocess
import svg.path

STROKE_WIDTH = 4
STROKE_SPEED = 20
FRAME_RATE = 20

def complex_to_tuple(complex):
    return (complex.real, complex.imag)

def create_frames(path_data, frame_size):
    path = svg.path.parse_path(path_data)
    length = path.length()
    duration = math.sqrt(length)/STROKE_SPEED
    num_frames = int(math.ceil(duration*FRAME_RATE))
    frames = []
    previous_point = complex_to_tuple(path.point(0))

    for frame in range(1, num_frames+1):
        next_point = complex_to_tuple(path.point(frame/num_frames))
        image = Image.new('P', frame_size)
        image.putpalette([0]*(3*256))
        ImageDraw.Draw(image).line(previous_point + next_point, fill=1, width=STROKE_WIDTH)
        image.info['transparency'] = 0
        image.info['loop'] = 0
        image.info['duration'] = int(duration/num_frames*1000)

        frames.append(image)
        previous_point = next_point

    return frames

def create_gif(svg):
    assert svg.endswith('.svg')

    doc = lxml.etree.parse(svg)
    root = doc.getroot()
    frame_size = (int(root.get('width')), int(root.get('height')))
    frames = []
    for path in doc.iterfind('.//{http://www.w3.org/2000/svg}path'):
        frames.extend(create_frames(path.get('d'), frame_size))

    gif = svg[:-4]+'.gif'
    frames[0].save(gif, save_all=True, optimize=True, append_images=frames[1:])

    try:
        subprocess.Popen(['gifsicle', '--batch', '--optimize=3', gif])
    except OSError:
        pass  # optimization is optional

def main(argv):
    svgs = argv[1:]

    for svg in svgs:
        create_gif(svg)


if __name__ == '__main__':
    import sys
    main(sys.argv)
