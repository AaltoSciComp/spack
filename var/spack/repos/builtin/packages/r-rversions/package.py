# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RRversions(RPackage):
    """Query the main 'R' 'SVN' repository to find the versions 'r-release' and
    'r-oldrel' refer to, and also all previous 'R' versions and their release
    dates."""

    homepage = "https://github.com/r-hub/rversions"
    url      = "https://cran.r-project.org/src/contrib/rversions_2.0.1.tar.gz"

    version('2.0.1', sha256='51ec1f64e7d628e88d716a020d5d521eba71d472e3c9ae7b694428ef6dd786c5')

    depends_on('r-curl', type=('build', 'run'))
    depends_on('r-xml2', type=('build', 'run'))
