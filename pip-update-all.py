# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation; either version 3 of the License,
# or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program.
# If not, see https://www.gnu.org/licenses/.

import os

def update_psw():
    # Updating pip, setuptools, and wheel
    print("")
    print("Updating pip...")
    os.system("python3 -m pip install --upgrade pip")
    print("Updating setuptools...")
    os.system("python3 -m pip install --upgrade setuptools")
    print("Updating wheel...")
    os.system("python3 -m pip install --upgrade wheel")


def update_outdated_packages():
    print("")
    print("Querying packages to upgrade. Sit tight; this may take a long time...", end="")
    print("")

    # Querying outdated packages
    output = os.popen("pip3 list --outdated").read()
    print("")

    # There are three lines that doesn't contain package info and can be ignored
    lines_to_ignore = 3
    lines = output.split("\n")
    count = len(lines) - lines_to_ignore

    if count < 0:
        count = 0

    print("Found", count, "outdated packages.")

    i = 0
    for line in lines[2:]:
        if line == "" or line == " ":
            continue
        i += 1
        end = line.find(" ")
        package = line[:end]
        print("Updating package", i, "of", count, " " + str(package) + "...")
        os.system("pip3 install --upgrade " + str(package))


if __name__ == "__main__":
    update_psw()
    update_outdated_packages()
    print("Updating packages finished. "
      "\nIf some packages didn't update, you may want to re-run this script or update them manually.")
