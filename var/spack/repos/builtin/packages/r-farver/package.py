# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RFarver(RPackage):
    """The encoding of colour can be handled in many different ways, using
    different colour spaces. As different colour spaces have different uses,
    efficient conversion between these representations are important. The
    'farver' package provides a set of functions that gives access to very
    fast colour space conversion and comparisons implemented in C++, and
    offers speed improvements over the 'convertColor' function in the
    'grDevices' package."""

    homepage = "https://cloud.r-project.org/package=farver"
    url      = "https://cran.r-project.org/src/contrib/farver_2.0.3.tar.gz"

    version('2.0.3', sha256='0e1590df79ec6078f10426411b96216b70568a4eaf3ffd84ca723add0ed8e5cc')

    depends_on('r-testthat@2.1.0:', type=('build', 'run'))
    depends_on('r-covr', type=('build', 'run'))
