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

class Skill:
    name = ""
    id = -1
    w = 0.0
    l = []

	# parameterized constructor
    def __init__(self, name, id, w, l):
        self.name = name
        self.id = id
        self.w = w
        self.l = l

    def display(self):
        print("c skill " + self.name+ ", id = " + str(self.id) + ", weight = " + str(self.w) + ", agents = " + str(self.l))

    def display(self, outputFile):
        print("c skill " + self.name+ ", id = " + str(self.id) + ", weight = " + str(self.w) + ", agents = " + str(self.l), file=outputFile)
