from setuptools import setup

setup(
    name='kanjivg-gif',
    version='0.1',
    description='Turns an SVG into an animated GIF, intended for KanjiVG data.',
    author='Yorwba',
    author_email='yorwb4@gmail.com',
    scripts=[
        'kanjivg-gif.py'
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    install_requires=[
        'lxml',
        'pillow',
        'svg.path',
    ],
)
