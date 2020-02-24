# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RHtmltools(RPackage):
    """Tools for HTML generation and output."""

    homepage = "https://github.com/rstudio/htmltools"
    url      = "https://cloud.r-project.org/src/contrib/htmltools_0.3.6.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/htmltools"

    version('0.4.0', sha256='5b18552e1183b1b90b5cca8e7f95b57e8124c9d517b22aa64783b829513b811a')
    version('0.3.6', sha256='44affb82f9c2fd76c9e2b58f9229adb003217932b68c3fdbf1327c8d74c868a2')
    version('0.3.5', sha256='29fb7e075744bbffdff8ba4fce3860076de66f39a59a100ee4cfb4fc00722b49')

    depends_on('r@2.14.1:', type=('build', 'run'))
    depends_on('r-digest', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
    depends_on('r-rlang', when='@0.4.0:', type=('build', 'run'))
