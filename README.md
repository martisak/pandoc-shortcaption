# pandoc-shortcaption filter

[![Build Status](https://travis-ci.org/martisak/pandoc-shortcaption.svg?branch=master)](https://travis-ci.org/martisak/pandoc-shortcaption)

`pandoc-shortcaption` is a [pandoc](http://pandoc.org/) filter for adding short captions to images in LaTeX output, i.e. `\caption[Short caption]{Long caption}`.

## Installation

~~~
pip install pandoc-shortcaption
~~~

or

~~~
python setup.py install
~~~

## Basic usage

~~~
![This is a long image caption](img.png "Image Short Caption")
~~~

Compile with
~~~
pandoc -f markdown -t latex --filter pandoc-shortcaption test.md
~~~

If you would like to use with [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref), then add that filter afterwards.

~~~
![long caption again](img.png "short caption"){#fig:myfig2}

Here is a reference to @fig:myfig2.
~~~

You can also add a width in percent (no other units supported as of now).

~~~
![long caption again](img.png "short caption"){#fig:myfig2 width=60%}
~~~


Compile with

~~~
pandoc -f markdown -t latex --filter pandoc-shortcaption --filter pandoc-crossref test.md
~~~


## Acknowledgments and references

Inspired by [Template for writing a PhD thesis in Markdown](https://github.com/tompollard/phd_thesis_markdown).

* [Python Apps the Right Way: entry points and scripts](https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/)
*  [pandocfilters](https://github.com/jgm/pandocfilters)

