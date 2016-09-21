# -*- coding: utf-8 -*-

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys

from oslotest import output

from six.moves import mock
import testtools


class CaptureOutputTest(testtools.TestCase):

    @mock.patch('os.environ')
    def test_disabled(self, mock_env):
        mock_env.get.return_value = ''
        f = output.CaptureOutput()
        f.setUp()
        self.assertIs(None, f.stdout)
        self.assertIs(None, f.stderr)
        self.assertIsNot(sys.stdout, f.stdout)
        self.assertIsNot(sys.stderr, f.stderr)

    @mock.patch('os.environ')
    def test_enabled(self, mock_env):
        mock_env.get.return_value = 'True'
        f = output.CaptureOutput()
        f.setUp()
        self.assertIsNot(None, f.stdout)
        self.assertIsNot(None, f.stderr)
        self.assertIs(sys.stdout, f.stdout)
        self.assertIs(sys.stderr, f.stderr)
