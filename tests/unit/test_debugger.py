from define import STARTUPINFO
from ctypes import windll
import unittest

class TestDefines(unittest.TestCase):
	
	def setUp(self):
		self.startupinfo = STARTUPINFO()

	def test_startupInfo_structure(self):
		self.startupinfo.dwFlags = 0x1
		self.assertEqual(self.startupinfo.dwFlags, 0x1)


class TestLoadDll(unittest.TestCase):

	def setUp(self):
		self.kernel32 = windll.kernel32

	def test_kernel32_loads_ok(self):
		self.assertIsNotNone(self.kernel32)