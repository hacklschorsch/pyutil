# -*- coding: utf-8; fill-column: 77 -*-
# -*- indent-tabs-mode: nil -*-
import decimal
from unittest import TestCase

from pyutil import jsonutil as json

class TestDecode(TestCase):
    def test_decimal(self):
        rval = json.loads('1.1', parse_float=decimal.Decimal)
        self.assertIsInstance(rval, decimal.Decimal)
        self.assertEqual(rval, decimal.Decimal('1.1'))

    def test_float(self):
        rval = json.loads('1', parse_int=float)
        self.assertIsInstance(rval, float)
        self.assertEqual(rval, 1.0)
