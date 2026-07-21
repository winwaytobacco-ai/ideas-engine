#!/bin/zsh
# macOS double-click launcher for the weekend run
cd "$(dirname "$0")"
# Terminal.app's default login shell caps open files at 256, which the
# batch OHLCV downloads + yfinance's own sqlite cache blow through
# ("Too many open files" / "unable to open database file"). Raise it
# for this process only.
ulimit -n 4096
python3 main.py
# Publish fresh output to GitHub Pages; harmless to skip when offline
# or when the run produced no changes.
if git add -A && git commit -m "Weekend run $(date +%F)" >/dev/null 2>&1; then
    # the daily cloud run also commits — sync its history before pushing
    git pull --rebase origin main >/dev/null 2>&1
    if git push >/dev/null 2>&1; then
        echo "Published: https://winwaytobacco-ai.github.io/ideas-engine/"
    else
        echo "(commit saved locally — push failed, will publish next time you're online)"
    fi
else
    echo "(nothing new to publish)"
fi
echo
read "?Run complete. Press Enter to close…"
