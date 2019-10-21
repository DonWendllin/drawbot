# -*- coding: utf-8 -*-
#
# DrawBot documentation build configuration file, created by
# sphinx-quickstart on Wed Sep 11 22:57:28 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shutil
import time


# some hacking
# support read the docs and the missing packages

class MetaMock(type):

    __slots__ = []

    def __getattr__(self, name):
        return self


class Mock(object, metaclass=MetaMock):

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        else:
            return Mock


MOCK_MODULES = ['py2app',
        'AppKit', 'Quartz', 'CoreText', 'QTKit',
        'fontTools',
        'fontTools.ttLib',
        'fontTools.ttLib.ttCollection',
        'fontTools.misc',
        'fontTools.misc.transform',
        'fontTools.misc.xmlWriter',
        'fontTools.misc.py23',
        'fontTools.misc.macCreatorType',
        'fontTools.misc.macRes',
        'fontTools.pens',
        'fontTools.pens.basePen',
        'fontTools.pens.areaPen',
        'ufoLib',
        'ufoLib.pointPen',
        'booleanOperations',
        'vanilla',
        'vanilla.vanillaBase']

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()

print(sys.version_info)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../'))


import drawBot.drawBotSettings as drawBotSettings

appName = "DrawBot"

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = appName
copyright = u'%s, Just van Rossum, Erik van Blokland, Frederik Berlaen' % (time.strftime('%Y'))

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = drawBotSettings.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "autumn"

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'drawBotTheme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "%s %s" % (appName, release)

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = appName

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'DrawBotdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'DrawBot.tex', u'DrawBot',
   u'Just van Rossum, Erik van Blokland, Frederik Berlaen', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'DrawBot', u'Draw With Python',
     [u'Just van Rossum, Erik van Blokland, Frederik Berlaen'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'DrawBot', u'DrawBot',
   u'Just van Rossum, Erik van Blokland, Frederik Berlaen',
   'DrawBot',
   'Drawing With Python.',
   ),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# auto doc

add_module_names = False
autodoc_member_order = 'bysource'

# sphinx hacking

import posixpath

import inspect

from sphinx import addnodes
from sphinx.directives.code import LiteralInclude, CodeBlock
from sphinx.util.inspect import getargspec
from sphinx.ext import autodoc
from sphinx.writers.html import HTMLTranslator
from sphinx.util import DownloadFiles


def add_file_overwrite(self, docname, filename):
    # type: (str, str) -> None
    if filename not in self:
        dest = os.path.basename(filename)
        self[filename] = (set(), dest)

    self[filename][0].add(docname)
    return self[filename][1]

DownloadFiles.add_file = add_file_overwrite

downloadCodeRoot = os.path.join(os.path.dirname(__file__), "downloads")
if os.path.exists(downloadCodeRoot):
    shutil.rmtree(downloadCodeRoot)

os.mkdir(downloadCodeRoot)

imageSourceRoot = os.path.join(os.path.dirname(__file__), "..", "tests", "data")


def visit_download_reference(self, node):
    if node.hasattr('filename'):
        if not node.get("dontShowThisNode"):
            data = dict(
                urlPath=posixpath.join(self.builder.dlpath, node['filename']),
                fileName=node['filename']
            )
            self.body.append('<div class="downloadlink"><a class="reference internal drawbotlink" href="%(urlPath)s">Open in DrawBot: %(fileName)s</a>' % data)
            self.body.append('<a class="reference internal" href="%(urlPath)s">Download: %(fileName)s</a></div>' % data)

            if node.get('imageFileName'):
                imageUrl = posixpath.join(self.builder.dlpath, node['imageFileName'])
                self.body.append('<div class="example-image"><image src="%s"/></div>' % imageUrl)
        node.clear()


def depart_download_reference(self, node):
    pass


HTMLTranslator.visit_download_reference = visit_download_reference
HTMLTranslator.depart_download_reference = depart_download_reference


class ShowCode(LiteralInclude):

    has_content = False
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        nodes = super(ShowCode, self).run()
        node = addnodes.download_reference()
        node['reftarget'] = self.arguments[0]
        nodes.append(node)
        return nodes


class DownloadCode(CodeBlock):

    def run(self):
        # get the argument
        fileName = self.arguments[0]
        # set the required language argument back
        self.arguments[0] = os.path.splitext(fileName)[1][1:]
        # set it as filename
        self.options['filename'] = fileName
        # encode the whole content
        self.content = [line for line in self.content]
        # call parent class
        nodes = super(DownloadCode, self).run()
        # get the content and encode
        code = u'\n'.join(self.content)
        # get the path
        path = os.path.join(downloadCodeRoot, fileName)
        # check the path on duplicates
        path = self.checkPath(path)
        # the filename could be changed
        fileName = os.path.basename(path)
        self.options["filename"] = fileName
        # write to disk
        f = open(path, "w")
        f.write(code)
        f.close()
        # add example image if present
        imageBaseName, _ = os.path.splitext(fileName)
        imageFileName = "example_%s.png" % imageBaseName
        imagePath = os.path.join(imageSourceRoot, imageFileName)
        if os.path.exists(imagePath):
            imageDestPath = os.path.join(downloadCodeRoot, imageFileName)
            shutil.copy(imagePath, imageDestPath)
        else:
            imageFileName = ""
        # add download links
        node = addnodes.download_reference()
        node['reftarget'] = "/downloads/" + fileName
        node['imageFileName'] = imageFileName
        nodes.append(node)
        if imageFileName:
            node = addnodes.download_reference()
            node['reftarget'] = "/downloads/" + imageFileName
            node['dontShowThisNode'] = True
            nodes.append(node)
        return nodes

    def checkPath(self, path, sourcePath=None, add=1):
        if sourcePath is None:
            sourcePath = path
        if os.path.exists(path):
            fileName, ext = os.path.splitext(sourcePath)
            path = fileName + str(add) + ext
            return self.checkPath(path, sourcePath=sourcePath, add=add+1)
        return path


class DrawBotDocumenter(autodoc.FunctionDocumenter):

    objtype = "function"

    def format_args(self):
        if inspect.isbuiltin(self.object) or \
               inspect.ismethoddescriptor(self.object):
            # cannot introspect arguments of a C function or method
            return None
        try:
            argspec = getargspec(self.object)
        except TypeError:
            # if a class should be documented as function (yay duck
            # typing) we try to use the constructor signature as function
            # signature without the first argument.
            try:
                argspec = getargspec(self.object.__new__)
            except TypeError:
                argspec = getargspec(self.object.__init__)
                if argspec[0]:
                    del argspec[0][0]
        if "self" in argspec.args:
            argspec.args.remove("self")
        args = inspect.formatargspec(*argspec)
        # escape backslashes for reST
        args = args.replace('\\', '\\\\')
        return args


def setup(app):
    app.add_directive('showcode', ShowCode)
    app.add_directive('downloadcode', DownloadCode)
    app.add_autodocumenter(DrawBotDocumenter)
