# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RIsoband(RPackage):
    """A fast C++ implementation to generate contour lines (isolines) and
    contour polygons (isobands) from regularly spaced grids containing
    elevation data."""

    homepage = "https://github.com/wilkelab/isoband"
    url      = "https://cran.rstudio.com/bin/windows/contrib/4.1/isoband_0.2.1.zip"

    version('0.2.1', sha256='42983c22c404f107de3ef21010fc950e69b42d1cdfe23a6fc4d0d9fab5ebff77')

    depends_on('r-rcpp', type=('build', 'run'))
