#!/usr/bin/env python3

"""Fill given .po files with deepl.com results.
"""

import time
import sys
import os

import click
import requests
import polib


def deepl(english_sentence, target_lang="FR"):
    """Query deepl via their jsonrpc to translate the given
    english_sentence to the given target language.

    May return an empty string on failure.
    """
    response = requests.post(
        "https://www2.deepl.com/jsonrpc",
        json={
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs": [{"kind": "default", "raw_en_sentence": english_sentence}],
                "lang": {
                    "user_preferred_langs": ["EN"],
                    "source_lang_user_selected": "EN",
                    "target_lang": target_lang,
                },
                "priority": -1,
            },
            "id": 36,
        },
    ).json()
    try:
        return response["result"]["translations"][0]["beams"][0][
            "postprocessed_sentence"
        ]
    except (IndexError, KeyError):
        return ""


def fill_po(po_file, verbose, target_lang):
    """Fill given po file with deepl translations.
    """
    entries = polib.pofile(po_file)
    output = sys.stdout if verbose else open(os.devnull, "w")
    with click.progressbar(entries, label=po_file, file=output) as pbar:
        for entry in pbar:
            if entry.msgstr:
                continue
            entry.msgstr = deepl(entry.msgid, target_lang)
            entry.flags.append("fuzzy")
            time.sleep(1)  # Hey deepl.com, hope it's nice enough, love your work!
    entries.save()


@click.command()
@click.argument("po-files", type=click.Path(), nargs=-1)
@click.option(
    "--verbose", "-v", is_flag=True, default=False, help="display progress bar"
)
@click.option("--target-lang", "-t", default="FR", help="target language")
def fill_pos(po_files, verbose, target_lang):
    """Fill given po files with deepl translations.
    """
    for po_file in po_files:
        fill_po(po_file, verbose, target_lang)


if __name__ == "__main__":
    fill_pos()  # pylint: disable=no-value-for-parameter
