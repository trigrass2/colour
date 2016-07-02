#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour.models.rgb.common` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.models import XYZ_to_sRGB, sRGB_to_XYZ

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestXYZ_to_sRGB', 'TestsRGB_to_XYZ']


class TestXYZ_to_sRGB(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.common.XYZ_to_sRGB` definition unit tests
    methods.
    """

    def test_XYZ_to_sRGB(self):
        """
        Tests :func:`colour.models.rgb.common.XYZ_to_sRGB` definition.
        """

        np.testing.assert_almost_equal(
            XYZ_to_sRGB(np.array([0.07049534, 0.10080000, 0.09558313])),
            np.array([0.17498172, 0.38818743, 0.32159978]),
            decimal=7)

        np.testing.assert_almost_equal(
            XYZ_to_sRGB(np.array([0.47097710, 0.34950000, 0.11301649])),
            np.array([0.96979222, 0.48891569, 0.30231574]),
            decimal=7)

        np.testing.assert_almost_equal(
            XYZ_to_sRGB(np.array([0.00000000, 0.00000000, 0.00000000]),
                        np.array([0.44757, 0.40745])),
            np.array([0., 0., 0.]),
            decimal=7)

        np.testing.assert_almost_equal(
            XYZ_to_sRGB(np.array([0.1180583421, 0.10340000, 0.0515089229]),
                        np.array([0.31270, 0.32900])),
            np.array([0.48222001, 0.31654775, 0.22070353]),
            decimal=7)

        np.testing.assert_almost_equal(
            XYZ_to_sRGB(np.array([0.07049534, 0.10080000, 0.09558313]),
                        chromatic_adaptation_transform='Bradford'),
            np.array([0.17498172, 0.38818743, 0.32159978]),
            decimal=7)

        np.testing.assert_almost_equal(
            XYZ_to_sRGB(np.array([0.07049534, 0.10080000, 0.09558313]),
                        apply_encoding_cctf=False),
            np.array([0.02583795, 0.12473949, 0.08439296]),
            decimal=7)


class TestsRGB_to_XYZ(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.common.sRGB_to_XYZ` definition unit tests
    methods.
    """

    def test_sRGB_to_XYZ(self):
        """
        Tests :func:`colour.models.rgb.common.sRGB_to_XYZ` definition.
        """

        np.testing.assert_almost_equal(
            sRGB_to_XYZ(np.array([0.17498172, 0.38818743, 0.32159978])),
            np.array([0.07049534, 0.10080000, 0.09558313]),
            decimal=7)

        np.testing.assert_almost_equal(
            sRGB_to_XYZ(np.array([0.96979222, 0.48891569, 0.30231574])),
            np.array([0.47097710, 0.34950000, 0.11301649]),
            decimal=7)

        np.testing.assert_almost_equal(
            sRGB_to_XYZ(np.array([0.00000000, 0.00000000, 0.00000000]),
                        np.array([0.44757, 0.40745])),
            np.array([0., 0., 0.]),
            decimal=7)

        np.testing.assert_almost_equal(
            sRGB_to_XYZ(np.array([0.48222001, 0.31654775, 0.22070353]),
                        np.array([0.31270, 0.32900])),
            np.array([0.1180583421, 0.10340000, 0.0515089229]),
            decimal=7)

        np.testing.assert_almost_equal(
            sRGB_to_XYZ(np.array([0.17498172, 0.38818743, 0.32159978]),
                        chromatic_adaptation_method='Bradford'),
            np.array([0.07049534, 0.10080000, 0.09558313]),
            decimal=7)

        np.testing.assert_almost_equal(
            sRGB_to_XYZ(np.array([0.02583795, 0.12473949, 0.084392960]),
                        apply_decoding_cctf=False),
            np.array([0.07049534, 0.10080000, 0.09558313]),
            decimal=7)


if __name__ == '__main__':
    unittest.main()