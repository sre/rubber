# -*- coding: utf8 -*-
# This file is part of Rubber and thus covered by the GPL
# (c) Sebastian Reichel <sre@ring0.de>, 2012
"""
Support for the package 'xmpmulti', part of Beamer distribution.
"""

from rubber.util import parse_keyval

def setup (document, context):
	global hook_includegraphics
	document.do_module('graphics')
	_, hook_includegraphics = document.hooks['includegraphics']
	document.hook_macro("multiinclude", "ooa", hook_multiinclude);

def hook_multiinclude(loc, options_a, options_b, file):
	options = parse_keyval(options_b) if options_b is not None else parse_keyval(options_a)
	fileformat     = "." + options["format"] if options.has_key("format") else ""
	graphicoptions = options["graphics"] if options.has_key("graphics") else None
	start          = int(options["start"]) if options.has_key("start") else 0
	stop           = int(options["end"]) if options.has_key("end") else 1000000
	seperator      = "." if fileformat == "" else "-"

	for i in range(start, stop):
		number  = "%d" % i
		ok = hook_includegraphics(loc, graphicoptions, file+seperator+number+fileformat, False)
		if not ok:
			break
