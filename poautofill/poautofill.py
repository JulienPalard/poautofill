#!/usr/bin/env python3

"""Fill given .po files with deepl.com results.
"""

import argparse
import time

import requests
import polib


def deepl(english_sentence, target_lang='FR'):
    """Query deepl via their jsonrpc to translate the given
    english_sentence to the given target language.

    May return an empty string on failure.
    """
    response = requests.post(
        'https://www.deepl.com/jsonrpc',
        json={"jsonrpc": "2.0",
              "method": "LMT_handle_jobs",
              "params": {
                  "jobs": [
                      {"kind": "default",
                       "raw_en_sentence": english_sentence}],
                  "lang": {
                      "user_preferred_langs": ["EN"],
                      "source_lang_user_selected": "EN",
                      "target_lang": target_lang},
                  "priority": -1},
              "id": 36}).json()
    try:
        return response['result']['translations'][0]['beams'][0][
            'postprocessed_sentence']
    except (IndexError, KeyError):
        return ''


def fill_po(po_file):
    """Fill given po files with deepl translations.
    """
    entries = polib.pofile(po_file)
    for entry in entries:
        if entry.msgstr:
            continue
        entry.msgstr = deepl(entry.msgid)
        entry.flags.append('fuzzy')
        time.sleep(1)  # Hey deepl.com, hope it's nice enough, love your work!
    entries.save()


def fill_pos(po_files):
    """Fill given po files with deepl translations.
    """
    for po_file in po_files:
        fill_po(po_file)


def parse_args():
    """Parses command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Fill a .po file with deepl translations")
    parser.add_argument("po_files", nargs="+")
    return parser.parse_args()


def main():
    """Module entry point.
    """
    args = parse_args()
    fill_pos(args.po_files)


if __name__ == '__main__':
    main()
