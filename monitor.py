"""Compatibility launcher; source is maintained in Neptune Hub."""
from pathlib import Path as _CompatPath

_canonical = _CompatPath(__file__).resolve().parents[1] / "neptune-charge-hub" / "modules" / "nearby" / "monitor.py"
NEPTUNE_STATIONS_CSV = _canonical.parent / "stations_yuquan.csv"
if not _canonical.is_file():
    raise RuntimeError("The consolidated neptune-charge-hub checkout is required.")
# Retain the legacy static panel for compatibility with the original launcher.
exec(compile(_canonical.read_bytes(), str(_canonical), "exec"), globals(), globals())
