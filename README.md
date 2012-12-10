# PSRD Parser
This program parses the text from the [Paizo Pathfinder Reference Document](http://paizo.com/pathfinderRPG/prd/) website and turns the data into a series of JSON files.  It then can transform those JSON files into an SQLite3 database intended for use with the [Pathfinder Open Reference](https://github.com/devonjones/PathfinderOpenReference) project.

## Configuration

Any third-party libraries that need to be installed are listed in ```conf/requirements.txt```.

You need to ensure you have a ```src/dir.conf``` file, that sets up certain environment variables and is sourced by the shell scripts. A template file is provided: ```src/dir.conf.template```.

Check ```docs``` for known issues and notes on the database, among other things.

## License
PSRD Parser is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

PSRD Parser is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with PSRD Parser. If not, see <http://www.gnu.org/licenses/>.
