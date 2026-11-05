import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent.parent/'lakapdf_alpha'))
from app import self_test
class Tests(unittest.TestCase):
 def test_roundtrip(self):self_test()
