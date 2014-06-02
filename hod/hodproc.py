# #
# Copyright 2009-2013 Ghent University
#
# This file is part of hanythingondemand
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/hanythingondemand
#
# hanythingondemand is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# hanythingondemand is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hanythingondemand. If not, see <http://www.gnu.org/licenses/>.
# #
"""

@author: Stijn De Weirdt
"""
import os
import logging as log
from os.path import join as mkpath, basename

from hod.mpiservice import MpiService, Task, MASTERRANK

from hod.config.config import (PreServiceConfigOpts, ConfigOpts,
        manifest_config_path, service_config_paths, resolve_config_str)
from hod.work.config_service import ConfiguredService

from hod.rmscheduler.hodjob import Job

from hod.config.hodoption import HodOption


class Slave(MpiService):
    """Basic Slave"""
    def __init__(self, options):
        MpiService.__init__(self)
        self.options


def _ignore_oserror(fn):
    '''
    Given a function, ignore OSError. 
    >>> def fn(x,y):
    ...    raise OSError
    >>> _ignore_oserror(lambda: fn(1,2))
    >>>
    '''
    try:
        fn()
    except OSError, e:
        pass


def _copy_config(src_file, dest_dir):
    cfg = open(src_file, 'r').read()
    cfg = resolve_config_str(cfg)
    dest_file = mkpath(dest_dir, basename(src_file))
    open(dest_file, 'w').write(cfg)
 

class ConfiguredMaster(MpiService):
    """
    Use config to setup services.
    """
    def __init__(self, options):
        MpiService.__init__(self)
        self.options = options


    def distribution(self):
        """Master makes the distribution"""
        self.dists = []
       
        config_dir = self.options.options.config_dir

        m_config_filename = manifest_config_path(config_dir)
        self.log.info('Loading "%s" manifest config'  % m_config_filename)
        m_config = PreServiceConfigOpts(open(m_config_filename, 'r'))

        _ignore_oserror(lambda: os.makedirs(m_config.basedir))
        _ignore_oserror(lambda: os.makedirs(m_config.configdir))

        for cfg in m_config.config_files:
            self.log.info("Copying config %s file to '%s'" % (cfg, config_dir))
            _copy_config(cfg, config_dir)

        svc_cfgs = service_config_paths(config_dir)
        self.log.info('Loading %d service configs.'  % len(svc_cfgs))
        for config_filename in svc_cfgs:
            self.log.info('Loading "%s" service config'  % config_filename)
            config = ConfigOpts(open(config_filename, 'r'))
            slaves = filter(lambda x: x != MASTERRANK, range(self.size))
            rank_to_run = [MASTERRANK] if config.runs_on_master else slaves
            self.dists.append(Task(ConfiguredService, rank_to_run, config, None))
