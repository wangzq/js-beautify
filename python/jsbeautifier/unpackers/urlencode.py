#
# Trivial bookmarklet/escaped script detector for the javascript beautifier
#     written by Einar Lielmanis <einar@jsbeautifier.org>
#     rewritten in Python by Stefano Sanfilippo <a.little.coder@gmail.com>
#
# Will always return valid javascript: if `detect()` is false, `code` is
# returned, unmodified.
#
# usage:
#
# some_string = urlencode.unpack(some_string)
#

"""Bookmarklet/escaped script unpacker."""

# Python 2 retrocompatibility
# pylint: disable=F0401
# pylint: disable=E0611
try:
    from urllib import unquote_plus, unquote
except ImportError:
    from urllib.parse import unquote_plus, unquote

PRIORITY = 0

def detect(code):
    """Detects if a scriptlet is urlencoded."""
    # the fact that script doesn't contain any space, but has %20 instead
    # should be sufficient check for now.
    return ' ' not in code and ('%20' in code or code.count('%') > 3)

def unpack(code):
    """URL decode `code` source string."""
    return unquote_plus(code) if detect(code) else code

def unpack2(code):
	"""some bookmarklet cannot be decoded using unquote_plus, example:
	javascript:(function(){%20function%20htmlEscape(s){s=s.replace(/&/g,'&amp;');s=s.replace(/>/g,'&gt;');s=s.replace(/</g,'&lt;');return%20s;}%20x=window.open();%20x.document.write('<pre>'%20+%20htmlEscape('<html>\n'%20+%20document.documentElement.innerHTML%20+%20'\n</html>'));%20x.document.close();%20})();
	"""
	return unquote(code) if detect(code) else code
