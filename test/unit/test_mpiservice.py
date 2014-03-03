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
import hod.mpiservice as hm

class MPIServiceTestCase(unittest.TestCase):
    def test_mpiservice_init(self):
        ms = hm.MpiService(False)
        self.assertEqual(ms.size, -1)
        self.assertEqual(ms.rank, -1)

    def test_mpiservice_init_init_com(self):
        ms = hm.MpiService()
        self.assertTrue(ms.comm is not None)
        self.assertTrue(ms.size is not None)
        self.assertTrue(ms.rank is not None)

    def test_mpiservice_barrier(self):
        ms = hm.MpiService()
        ms.barrier('Wibble')

    def test_mpiservice_collectnodes(self):
        ms = hm.MpiService()
        ms.collect_nodes()

    def test_mpiservice_make_topoplogy_comm(self):
        ms = hm.MpiService()
        ms.make_topology_comm()

    def test_mpiservice_who_is_out_there(self):
        ms = hm.MpiService()
        ms.init_comm()
        others = ms.who_is_out_there(ms.comm)
        print others

    def test_mpiservice_stop_comm(self):
        ms = hm.MpiService()
        ms.init_comm()
        ms.stop_comm(ms.comm)

    def test_mpiservice_stop_service(self):
        ms = hm.MpiService()
        ms.stop_service()

    def test_mpiservice_check_group(self):
        ms = hm.MpiService()
        ms.init_comm()
        ms.check_group(ms.comm.Get_group())

    def test_mpiservice_check_comm(self):
        ms = hm.MpiService()
        ms.init_comm()
        ms.check_comm(ms.comm)

    def test_mpiservice_make_comm_group(self):
        ms = hm.MpiService()
        ms.make_comm_group(range(1))

    def test_mpiservice_distribution(self):
        ms = hm.MpiService()
        ms.distribution() # TODO:  Does nothing. If it's an interface, make abstract.

    def test_mpiservice_spread(self):
        ms = hm.MpiService()
        ms.spread()

    @unittest.expectedFailure
    def test_mpiservice_run_dist(self):
        ms = hm.MpiService()
        ms.distribution()
        ms. run_dist()
