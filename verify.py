#!/usr/bin/env python3
"""line-report: five kinds of chart on one screen, every value fed from state; three of them point at the same hour."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools"))
from appplayer import AppPlayer  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CAP = os.path.join(HERE, "captures")
BUNDLE = os.path.join(HERE, "line_report.mbd")

ap = AppPlayer()
bid = ap.install_bundle(BUNDLE)
ap.restart()
ap.open_bundle(bid)
ap.wait_text("Shift handover report")
ap.wait_text("6.2")                         # the P-4 · 11:00 cell, from state
ap.expect_text("84%")
ap.shot(f"{CAP}/01_shift_report.png")
print("line-report: gauge, bars, heatmap, line and process tree drawn from state")
