# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RFarver(RPackage):
    """farver: High Performance Colour Space Manipulation"""

    homepage = "https://github.com/thomasp85/farver"
    url      = "https://cloud.r-project.org/src/contrib/farver_2.0.1.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/farver"

    version('2.0.3', sha256='0e1590df79ec6078f10426411b96216b70568a4eaf3ffd84ca723add0ed8e5cc')
    version('2.0.1', sha256='1642ca1519ef80616ab044ae7f6eaf464118356f2a7875e9d0e3df60ca84012b')

    depends_on('r-testthat@2.1.0:', type=('build', 'run'))
    depends_on('r-covr', type=('build', 'run'))
