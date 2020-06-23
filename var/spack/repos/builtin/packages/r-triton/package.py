# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RTriton(Package):
    """Metapackage for R installation on Aalto Triton cluster."""

    homepage = "https://scicomp.aalto.fi/triton/apps/r/"
    url      = "https://users.aalto.fi/~tuomiss1/r-triton/v1.0.0.tar.gz"

    version('1.0.0', sha256='56094654d3380f9b6522a9de7eb9edca9ad1743c63fa69982fe0b20a2a492cd3')

    depends_on('r-irkernel')
    depends_on('r-tidyverse')
    depends_on('r-feather')
    depends_on('r-ggplot2movies')
    depends_on('r-microbenchmark')
    depends_on('r-pryr')

    def install(self, spec, prefix):
        copy_tree(".", prefix)
