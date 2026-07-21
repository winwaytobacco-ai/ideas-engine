#!/bin/zsh
# macOS double-click launcher for the weekend run
cd "$(dirname "$0")"
# Terminal.app's default login shell caps open files at 256, which the
# batch OHLCV downloads + yfinance's own sqlite cache blow through
# ("Too many open files" / "unable to open database file"). Raise it
# for this process only.
ulimit -n 4096
python3 main.py
echo
read "?Run complete. Press Enter to close…"
