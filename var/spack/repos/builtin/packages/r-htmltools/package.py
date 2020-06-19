# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RHtmltools(RPackage):
    """Tools for HTML generation and output."""

    homepage = "https://github.com/rstudio/htmltools"
    url      = "https://cloud.r-project.org/src/contrib/htmltools_0.3.6.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/htmltools"

    version('0.5.0', sha256='ff0a2ce3d4afd7758db1b2fae33e4f6321c6e359f4dbd6862936ead295fdd21d')
    version('0.4.0', sha256='5b18552e1183b1b90b5cca8e7f95b57e8124c9d517b22aa64783b829513b811a')
    version('0.3.6', '336419c2143f958862e01ef1bbc9c253')
    version('0.3.5', '5f001aff4a39e329f7342dcec5139724')

    depends_on('r@2.14.1:', type=('build', 'run'))
    depends_on('r-digest', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
    depends_on('r-rlang', when='@0.4.0:', type=('build', 'run'))
