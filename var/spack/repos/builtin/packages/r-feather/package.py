# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RFeather(RPackage):
    """Read and write feather files, a lightweight binary columnar data
    store designed for maximum speed."""

    homepage = "https://github.com/wesm/feather"
    url      = "https://cran.r-project.org/src/contrib/feather_0.3.5.tar.gz"

    version('0.3.5', sha256='50ff06d5e24d38b5d5d62f84582861bd353b82363e37623f95529b520504adbf')

    depends_on('r-rcpp', type=('build', 'run'))
    depends_on('r-hms', type=('build', 'run'))
    depends_on('r-tibble@2.0.0:', type=('build', 'run'))
