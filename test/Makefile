PANDOC=pandoc

all: tex

tex: test.tex

test.tex: test.md
	$(PANDOC) $< --filter pandoc-shortcaption -o $@

clean:
	rm -rf test.tex