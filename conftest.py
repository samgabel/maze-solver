import sys
from pathlib import Path

# Assuming conftest.py is in the project root directory
# Adjust the path if your conftest.py is located elsewhere
base_dir = Path(__file__).parent
src_path = f"{base_dir}/src"

if src_path not in sys.path:
    sys.path.append(src_path)
