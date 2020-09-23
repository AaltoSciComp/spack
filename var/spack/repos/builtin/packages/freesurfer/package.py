# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.util.environment import EnvironmentModifications
from distutils.dir_util import copy_tree
import os
from glob import glob


class Freesurfer(Package):
    """FreeSurfer Software Suite - An open source software suite for
    processing and analyzing (human) brain MRI images."""

    homepage = "https://surfer.nmr.mgh.harvard.edu/"
    url      = "ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz"

    version('7.1.0', sha256='1b8f26fe5c712433ddb74c47fe1895ed1d9fbff46cfae8aaae2697cb65ae8840')
    version('6.0.0', sha256='9e68ee3fbdb80ab73d097b9c8e99f82bf4674397a1e59593f42bb78f1c1ad449')

    depends_on('libpng@1.2.0:1.2.99', type=('run'), when='@6.0.0')
    depends_on('mesa+opengl', type=('run'))
    depends_on('libxscrnsaver', type=('run'))

    license_required = True
    license_files    = ['license.txt']

    def url_for_version(self, version):

        if version >= Version('7.0.0'):
            url = "https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/{0}/freesurfer-linux-centos7_x86_64-{0}.tar.gz"
        else:
            url = "ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/{0}/freesurfer-Linux-centos6_x86_64-stable-pub-v{0}.tar.gz"
        return url.format(str(version))

    def install(self, spec, prefix):
        copy_tree(".", prefix)
        if self.spec.version >= Version('7.0.0'):
            with working_dir(prefix):
                os.symlink('license.txt', '.license')


    def setup_environment(self, spack_env, run_env):
        run_env.set('FREESURFER_HOME', self.prefix)
        freesurfer_sh = os.path.join(
            self.prefix,
            'SetUpFreeSurfer.sh'
        )
        if os.path.isfile(freesurfer_sh):
            os.environ['FREESURFER_HOME'] = self.prefix
            run_env.extend(EnvironmentModifications.from_sourcing_file(
                freesurfer_sh))
        libs = ['KWWidgets', 'cuda', 'petsc', 'qt', 'tcltktixblt', 'vtk/lib/vtk-5.6']
        for lib in libs:
            run_env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix.lib, lib))
        run_env.prepend_path('LD_LIBRARY_PATH', self.prefix.mni.lib)
        if self.spec.satisfies('%gcc'):
            compiler_path = os.path.dirname(os.path.dirname(self.compiler.cc))
            libpath = join_path(compiler_path, 'lib', 'gcc')
            libc_paths = glob(join_path(libpath, 'x86_64*', self.compiler.version))
            libc_paths.append(join_path(compiler_path, 'lib64'))
            for libc_path in libc_paths:
                run_env.prepend_path('LD_LIBRARY_PATH', libc_path)
