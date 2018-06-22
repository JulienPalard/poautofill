==========
poautofill
==========


.. image:: https://img.shields.io/pypi/v/poautofill.svg
        :target: https://pypi.python.org/pypi/poautofill


Script to automatically translate a given po file. It currently only
uses https://deepl.com but should be extended to use other sources.

It only translates empty translations, and mark them as ``fuzzy`` so
you can easily spot them for mandatory review.

This project is *not* aimed to automatically translate files for use
in production, more to give some material for translators while
translating offline, like missing vocabulary.

Usage::

  poautofill any_file.po
  # processes any_file.po

  poautofill -h
  # displays help

* Free software: MIT license
