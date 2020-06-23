# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RMicrobenchmark(RPackage):
    """Provides infrastructure to accurately measure and compare the
    execution time of R expressions."""

    homepage = "https://github.com/joshuaulrich/microbenchmark/"
    url      = "https://cloud.r-project.org/src/contrib/microbenchmark_1.4-7.tar.gz"

    version('1.4-7', sha256='268f13c6323dd28cc2dff7e991bb78b814a8873b4a73f4a3645f40423da984f6')
