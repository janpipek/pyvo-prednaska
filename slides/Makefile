theme = physt-white
highlighttheme = github
themeoptions = --theme $(theme) --highlight-theme $(highlighttheme)

all: static  # print

static: slides.md background.png
	reveal-md slides.md --static build $(themeoptions)
	cp -r theme build
	cp *png build
	cp *html build
	cp *svg build

print: slides.md background.png
	reveal-md slides.md --print slides.pdf $(themeoptions)

present: background.png
	reveal-md slides.md --disable-auto-open $(themeoptions) -w

background.png: backgrounds.py
	python backgrounds.py
