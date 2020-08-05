# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Nvtop(CMakePackage):
    """Nvtop stands for NVidia TOP, a (h)top like task monitor for NVIDIA GPUs.
    It can handle multiple GPUs and print information about them in a htop
    familiar way."""

    homepage = "https://github.com/Syllo/nvtop"
    url      = "https://github.com/Syllo/nvtop/archive/1.0.0.tar.gz"

    version('1.0.0', sha256='de3d7b6a889f886f3bc28c15c3c34cfb6fcb7cb7ebc9a0cc36c3c77d837029b1')

    depends_on('ncurses', type=('build','run'))
    depends_on('cuda', type=('build','run'))

    def cmake_args(self):
        spec = self.spec

        options = []

        options.extend([
            '-DNVML_INCLUDE_DIRS=%s' % spec['cuda'].prefix.include,
            '-DNVML_LIBRARIES=%s' % spec['cuda'].prefix.lib64
        ])
        return options
