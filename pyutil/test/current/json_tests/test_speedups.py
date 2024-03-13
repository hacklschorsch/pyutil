# -*- coding: utf-8; fill-column: 77 -*-
# -*- indent-tabs-mode: nil -*-
from twisted.trial.unittest import SkipTest, TestCase

from pyutil.jsonutil import decoder
from pyutil.jsonutil import encoder

class TestSpeedups(TestCase):
    def test_scanstring(self):
        if not encoder.c_encode_basestring_ascii:
            raise SkipTest("no C extension speedups available to test")
        self.assertEqual(decoder.scanstring.__module__, "simplejson._speedups")
        self.assertIs(decoder.scanstring, decoder.c_scanstring)

    def test_encode_basestring_ascii(self):
        if not encoder.c_encode_basestring_ascii:
            raise SkipTest("no C extension speedups available to test")
        self.assertEqual(encoder.encode_basestring_ascii.__module__, "simplejson._speedups")
        self.assertIs(encoder.encode_basestring_ascii,
                          encoder.c_encode_basestring_ascii)
