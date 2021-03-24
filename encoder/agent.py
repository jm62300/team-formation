# Copyright (C) 2021  Lagniez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/python3

class Agent:
    name = ""
    id = -1
    w1 = 0.0
    w2 = 0.0
    l = []

	# parameterized constructor
    def __init__(self, name, id, w1, w2, l):
        self.name = name
        self.id = id
        self.w1 = w1
        self.w2 = w2
        self.l = l

    def display(self):
        print("c agent " + str(self.name) + ", id =  " + str(self.id) + ", weight phase 1 = " + str(self.w1) +
              ", weight phase 2 = " + str(self.w2) + ", skills = " + str(self.l))

    def display(self, outputFile):
        print("c agent " + str(self.name) + ", id =  " + str(self.id) + ", weight phase 1 = " + str(self.w1) +
              ", weight phase 2 = " + str(self.w2) + ", skills = " + str(self.l), file=outputFile)
