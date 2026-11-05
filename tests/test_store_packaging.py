import importlib.util
import pathlib
import tempfile
import unittest
import xml.etree.ElementTree as ET

root=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("storepack",root/"store"/"prepare_msix.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class StorePackageTests(unittest.TestCase):
    def test_manifest(self):
        mod.validate("LarxVo.LakaPDF","CN=10000000-0000-0000-0000-000000000001","0.3.1.0")
        root=ET.fromstring(mod.manifest("LarxVo.LakaPDF","CN=10000000-0000-0000-0000-000000000001","Larx Vo","0.3.1.0"))
        self.assertEqual(root.find("{http://schemas.microsoft.com/appx/manifest/foundation/windows10}Identity").attrib["Version"],"0.3.1.0")
    def test_reject_placeholder(self):
        with self.assertRaises(ValueError): mod.validate("placeholder.app","CN=123","0.3.1.0")
        with self.assertRaises(ValueError): mod.validate("LarxVo.LakaPDF","CN=Larx Vo","0.3.1.0")
        with self.assertRaises(ValueError): mod.validate("LarxVo.LakaPDF","CN=123","0.3.1")
    def test_icons(self):
        with tempfile.TemporaryDirectory() as d:
            path=pathlib.Path(d)
            mod.icons(path)
            self.assertTrue((path/"Square150x150Logo.png").is_file())
if __name__=="__main__":unittest.main()
