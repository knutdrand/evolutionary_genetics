from evolutionary_genetics.hardy_weinberg import HardyWeinberg
import pytest
from numpy.testing import assert_almost_equal


@pytest.fixture
def hw():
    return HardyWeinberg(0.3)


@pytest.fixture
def hw2():
    return HardyWeinberg(0.33)


@pytest.fixture
def hw3():
    return HardyWeinberg(0.25)


def test_expected_genotype(hw):
    assert_almost_equal(hw.expected_genotype(0, 0), 0.09)
    assert_almost_equal(hw.expected_genotype(0, 1), 0.42)
    assert_almost_equal(hw.expected_genotype(1, 1), 0.49)


def test_chi_square(hw2):
    assert_almost_equal(hw2.chi_square(12, 42, 46), 0.252, decimal=3)


def test_F_IS(hw3):
    assert_almost_equal(hw3.F_IS(0.5, 0.5, 0), -0.333, decimal=3)
