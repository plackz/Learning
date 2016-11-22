#! /usr/bin/python3
# phoneAndEmail.py
# python program to search clipboard text

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first three digits
    (\s|-|\.)                           # separator
    (\d{4})                             # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
    )''', re.VERBOSE)

# TODO: Create email regex

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
