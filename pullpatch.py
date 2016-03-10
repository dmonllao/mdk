##
# Usage:
#   pullpatch.py MDL-12345 MOODLE_XY_STABLE
#
# Args:
#   $1 => Issue number
#   $2 => Major branch name
##

import logging
import os
import sys
from mdk.moodle import Moodle
from mdk.fetch import FetchTracker

logging.basicConfig(format='%(message)s', level=logging.INFO)

# This script should run from a moodle site's dirroot.
cwd = os.getcwd()
M = Moodle(cwd, cwd)

f = FetchTracker(M)
f.setFromTracker(sys.argv[1], sys.argv[2])
f.pull()
