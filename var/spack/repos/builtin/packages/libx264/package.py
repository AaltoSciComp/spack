# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Libx264(AutotoolsPackage):
    """x264 is a free software library and application for encoding video
    streams into the H.264/MPEG-4 AVC compression format.
    """

    homepage = "https://www.videolan.org/developers/x264.html"
    url      = "https://code.videolan.org/videolan/x264.git"
    git      = "https://code.videolan.org/videolan/x264.git"

    version('develop', branch='master')

    variant('shared', default=True,
            description='Build shared version of the library')
    variant('pic', default=True,
            description='Produce position-independent code (for shared libs)')

    depends_on('nasm@2.13.0:')

    def configure_args(self):
        args = []
        if '+pic' in self.spec:
            args += ['--enable-pic']
        if '+shared' in self.spec:
            args += ['--enable-shared']
        return args
