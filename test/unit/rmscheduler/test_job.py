###
# Copyright 2009-2014 Ghent University
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
import unittest
import hod.rmscheduler.job as hrj

class HodRMSchedulerJobTestCase(unittest.TestCase):
    def test_job_init(self):
        j = hrj.Job(None)

    @unittest.expectedFailure
    def test_job_submit(self):
        j = hrj.Job(None)
        j.submit()

    @unittest.expectedFailure
    def test_job_generate_script(self):
        j = hrj.Job(None)
        j.generate_script()

    def test_job_generate_environment(self):
        j = hrj.Job(None)
        j.generate_environment()

    def test_job_generate_extra_environment(self):
        j = hrj.Job(None)
        j.generate_extra_environment()

    def test_job_generate_exe(self):
        j = hrj.Job(None)
        j.generate_exe()

    def test_job_generate_modules(self):
        j = hrj.Job(None)
        j.generate_modules()

    def test_job_get_jobs(self):
        hrj.Job.get_job(hrj.Job, None)

