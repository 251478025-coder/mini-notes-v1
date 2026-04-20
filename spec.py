PROJECT: mini-notes
AUTHOR: Pelin Kışlak (251478025)
VERSION: v0
DATE: 2026-04-05

========================================
OVERVIEW
========================================
mini-notes is a simple command-line note-taking tool.
It allows users to store, list, and search text notes in a local file.
All data is stored in a directory called .mininotes/

========================================
COMMANDS
========================================

--- init ---
Usage: python mininotes.py init
Creates a .mininotes/ directory and an empty notes.dat file.
If directory exists, print "Already initialized" and exit.

--- add ---
Usage: python mininotes.py add "Meeting at 5pm"
Appends a new note to notes.dat.
Format: id|content|date
Prints "Note saved with ID: <id>"

--- list ---
Usage: python mininotes.py list
(To be fully implemented in v1. In v0, shows raw file content.)

--- search ---
Usage: python mininotes.py search "keyword"
(To be implemented in v2.)

========================================
DATA FORMAT
========================================
File: .mininotes/notes.dat
Example:
1|Buy groceries|2026-04-05
2|Finish homework|2026-04-05

========================================
ERROR HANDLING
========================================
- Command without init: "Error: Not initialized. Run 'init' first."
- Missing arguments: "Usage: python mininotes.py <command> [args]"