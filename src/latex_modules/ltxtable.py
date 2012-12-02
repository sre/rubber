# This file is part of Rubber and thus covered by the GPL
# (c) Sebastian Reichel, 2012
"""
Dependency analysis for package 'ltxtable' in Rubber.
"""

def setup (document, context):
	global doc
	doc = document
	doc.hook_macro('LTXtable', 'aa', hook_ltxtable)

def hook_ltxtable (loc, width, file):
	# If the file name looks like it contains a control sequence or a macro
	# argument, forget about this \LTXtable.
	if file.find('\\') < 0 and file.find('#') < 0:
		doc.add_source(file)
