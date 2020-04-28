# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.environment import EnvironmentModifications
from distutils.dir_util import copy_tree
import os


class Freesurfer(Package):
    """FreeSurfer Software Suite - An open source software suite for
    processing and analyzing (human) brain MRI images."""

    homepage = "https://surfer.nmr.mgh.harvard.edu/"
    url      = "ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz"

    version('6.0.0', 'd49e9dd61d6467f65b9582bddec653a4')

    depends_on('libpng@1.2.0:1.2.99', type=('run'))
    depends_on('mesa+opengl', type=('run'))
    depends_on('libxscrnsaver', type=('run'))
    depends_on('gcc', type=('run'))

    license_required = True
    license_files    = ['license.txt']

    def install(self, spec, prefix):
        copy_tree(".", prefix)

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
