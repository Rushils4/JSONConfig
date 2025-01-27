import os
import sys

# Dynamically add the parent directory to sys.path
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
# print()
# print(parent_path)
# print()
# print(sys.path)
# print()
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)