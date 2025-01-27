import sys
import os

# Dynamically add the parent directory to sys.path
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
# print()
# print(parent_path)
# print()
# print(sys.path)
# print()
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

from DataInterface.JSONConfig import JSONConfig as jsc

if __name__ == "__main__":
    test : jsc.JSONConfig = jsc.JSONConfig(path_to_json="agent_configs/data_collection_agent_config.json")
    test.create_directories()