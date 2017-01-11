#!/bin/env /home/eisamar/.virtualenvs/pandoc-shortcaption/bin/python

from pandocfilters import toJSONFilter, RawInline
import logging
FORMAT = "%(asctime)s %(levelname)-8s%(module)-10s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

# \begin{figure}[htbp]
# \centering
# \includegraphics{Image Source}
# \caption{Image Title}
# \end{figure}

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever

def shortcap(key, value, format, meta):

    if key == 'Image' and format == "latex":
        logging.debug(value)

        label = value[0][0]
        src = value[2][0]
        alt = remove_prefix(value[2][1], "fig:")

        if (alt != ""):

            caption = " ".join([c['c'] for c in value[1] if c['t'] == "Str"])

            raw = r'\begin{figure}[htbp]' + '\n'
            raw += r'\centering' + '\n'
            raw += '\\includegraphics{{{}}}'.format(src, alt) + '\n'
            raw += '\\caption[{}]{{{}}}'.format(alt, caption)
            if (label != ''):
                raw += '\label{{{}}}'.format(label)
            raw += '\n' + r'\end{figure}' + '\n'

            return RawInline('tex', raw)


def main():
    toJSONFilter(shortcap)


if __name__ == "__main__":
    main()
