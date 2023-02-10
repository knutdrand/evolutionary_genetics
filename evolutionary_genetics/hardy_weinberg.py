from scipy.stats import chi2_contingency


class HardyWeinberg:
    def __init__(self, p):
        self._p = p
        self._q = 1-p

    def expected_genotype(self, i, j):
        assert (i, j) in [(0, 0), (0, 1), (1, 1)]
        if i == 0 and j == 0:
            return self._p ** 2
        if i == 1 and j == 1:
            return self._q ** 2
        return 2 * self._p * self._q

    def chi_square(self, observed_g11, observed_g12, observed_g22):
        N = sum((observed_g11, observed_g12, observed_g22))
        expected = (self.expected_genotype(*g)*N for g in ((0, 0), (0, 1), (1, 1)))
        observed = (observed_g11, observed_g12, observed_g22)
        return sum((e-o)**2/e for e, o in zip(expected, observed))

    @property
    def H_S(self):
        return self.expected_genotype(0, 1)

    def F_IS(self, g11, g12, g22):
        return (self.H_S-g12)/self.H_S

