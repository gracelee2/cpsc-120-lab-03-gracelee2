#!/usr/bin/env python3
#
# Copyright 2021 Michael Shafae
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
""" Check student's submission; requires the main file and the
    template file from the original repository. """
# pexpect documentation
#  https://pexpect.readthedocs.io/en/stable/index.html
import logging
import pexpect
import subprocess
import difflib
from srcutilities import solution_check_make


def run_p2(binary):
    """ This is the test for the BMR program given the inputs from run_p1 """
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    cmd = binary

    expected_output = '*||||||||||||||||||||||\n-*|||||||||||||||||||||\n--*||||||||||||||||||||\n---*|||||||||||||||||||\n----*||||||||||||||||||\n-----*|||||||||||||||||\n------*||||||||||||||||\n-------*|||||||||||||||\n--------*||||||||||||||\n---------*|||||||||||||\n----------*||||||||||||\n-----------*|||||||||||\n------------*||||||||||\n-------------*|||||||||\n--------------*||||||||\n---------------*|||||||\n----------------*||||||\n-----------------*|||||\n------------------*||||\n-------------------*|||\n--------------------*||\n---------------------*|\n'.split('\n')

    proc = subprocess.run([cmd], capture_output=True, shell=True, \
        timeout=1, check=False, text=True)
    output = str(proc.stdout).split('\n')
    diff = difflib.context_diff(output, expected_output, \
        'Student Program\'s Output', 'Expected Output', n=3)
    diff = list(diff)
    if diff:
        logging.error('Output did not match expected output.\n')
        logging.error('\n'.join(diff))
    else:
        logging.info('Output matched expectations.')
        status = True
    return status


if __name__ == '__main__':
    solution_check_make(run=run_p2)
