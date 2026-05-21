import os

shutdown_after_minutes = 1

wake_after_minutes = 2

print(f"System will shutdown/sleep after {shutdown_after_minutes} minute(s)")

os.system(f"sleep {shutdown_after_minutes * 60}")

print(f"System sleeping now...")

print(f"System will wake after {wake_after_minutes} minute(s)")

os.system(f"sudo rtcwake -m mem -s {wake_after_minutes * 60}")
