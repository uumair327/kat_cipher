import unittest

class TestImports(unittest.TestCase):
    """Test that required packages can be imported."""
    
    def test_import_opencv(self):
        """Test that OpenCV can be imported."""
        import cv2
        self.assertIsNotNone(cv2.__version__)
    
    def test_import_pyqt6(self):
        """Test that PyQt6 can be imported."""
        from PyQt6 import QtWidgets
        self.assertIsNotNone(QtWidgets.QApplication.instance() or True)

if __name__ == '__main__':
    unittest.main()
