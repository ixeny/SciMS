# -*- coding: utf-8 -*-
import re

def toHTML(str):
	section = re.compile(r"^\\(section)\{([a-zA-Z0-9_ ]*)\}", re.MULTILINE)
	subsection = re.compile(r"^\\(subsection)\{([a-zA-Z0-9_ ]*)\}", re.MULTILINE)
	mathform =re.compile(r"(\[.*\])", re.MULTILINE)
	tofcontents =re.compile(r"\\(tableofcontents)", re.MULTILINE)
	image =re.compile(r"\{%(.*)%\}", re.MULTILINE)

	sect = "<h2 class=\"section\">\\2</h2>"
	subsect = "<h3 class=\"subsection\">\\2</h3>"
	math = "<math class=\"formule\" display=\"block\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><mrow><mi>d</mi><mo>=</mo>2</mrow></math>"
	contents = "<div id=\"tofcontents\"><h4>Table des matières</h4></div>"
	img="<img src=\"\\1\">"

	str = section.sub(sect, str)
	str = subsection.sub(subsect, str)
	str = mathform.sub(math, str)
	str = image.sub(img, str)
	return tofcontents.sub(contents,str)
