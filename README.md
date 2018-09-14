# KanjiVG-GIF

This is a simple script to turn SVGs (e.g. from the
[KanjiVG](http://kanjivg.tagaini.net/) project) into animated GIFs displaying
the strokes being added incrementally.

If you want the result to look beautiful, you might prefer
[Kanimaji](https://github.com/aehlke/kanimaji), which uses an actual SVG
renderer and can also create animated SVGs.

Unfortunately, the GIFs created by Kanimaji are somewhat large. By compromising
on the optics, KanjiVG-GIF creates much smaller files.

## Comparison

![Kanimaji 襲](http://maurimo.github.io/kanimaji/samples/08972_anim.gif)
![KanjiVG-GIF 襲](08972.gif)

The Kanimaji image (left) has 30'559 bytes at 150 × 150 pixels, while
KanjiVG-GIF's output (right) is uglier, but has only 3300 bytes at 109 × 109
pixels (the KanjiVG default). Both images were optimized using
[Gifsicle](https://www.lcdf.org/gifsicle/), which KanjiVG does automatically
if Gifsicle is installed.

## Usage

```
./kanjivg-gif.py 08972.svg
```
creates `08972.gif` with the animation.

## License

KanjiVG-GIF is licensed under the GPL version 3 or any later version, at your
option. See [`LICENSE.txt`](LICENSE.txt) for the full license text.
