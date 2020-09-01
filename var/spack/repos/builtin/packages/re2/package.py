# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Re2(MakefilePackage):
    """RE2 is a regular expression library."""

    homepage = "https://github.com/google/re2/"
    url      = "https://github.com/google/re2/archive/2020-08-01.tar.gz"

    version('2020-08-01', sha256='6f4c8514249cd65b9e85d3e6f4c35595809a63ad71c5d93083e4d1dcdf9e0cd6')

    def patch(self):
        filter_file(r'/usr/local',
                    self.spec.prefix,
                    'Makefile')
