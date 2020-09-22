# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RGgplot2movies(RPackage):
    """A dataset about movies. This was previously contained in ggplot2,
    but has been moved its own package to reduce the download size of ggplot2."""

    homepage = "https://cloud.r-project.org/package=ggplot2movies"
    url      = "https://cran.r-project.org/src/contrib/ggplot2movies_0.0.1.tar.gz"

    version('0.0.1', sha256='186da1d21c3ac58699eb7bf5602bdf19944fee0d4c647076a4ebb22e9b69f418')
