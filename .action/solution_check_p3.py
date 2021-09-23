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
from srcutilities import solution_check_make

# Note: see https://stackoverflow.com/questions/5132749/diff-an-image-using-imagemagick


def run_p3(binary):
    """ Run part-1 """
    status = True
    values = (
        (0, 0, 0),
        (-7.5, -7, 6),
        (123.45, 123, 5, 3),
        (4.3, 4, 3, 4),
        )
    for index, val in enumerate(values):
        answer = ' '.join(map(str, val[1:]))
        logging.info('Test %d - %f %s', index + 1, val[0], answer)
        status = status and  _run(binary, val)
        if not status:
            logging.error("Did not receive expected response. Halting test.")
            break
    return status


def _run(binary, values):
    """ This is the test for the BMR program given the inputs from run_p1 """
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    #proc.logfile = sys.stdout.buffer
    values = list(map(str, values))
    try:
        proc.expect(r'(?i)\s*Enter\s+the\s+number\s+of\s+feet\s+you\s+wish\s+to\s+convert\s+to\s+feet-inch:\s*')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[0])

    try:
        if len(values) == 3:
            proc.expect(r'(?i)\s*{}\s+feet\s+is\s+{}\s+feet,\s+{}\s+inches\s*'.format(values[0], values[1], values[2]))
        else:
            proc.expect(r'(?i)\s*{}\s+feet\s+is\s+{}\s+feet,\s+{}\s+and\s+{}/8\s+inches\s*'.format(values[0], values[1], values[2], values[3]))
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status


    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status


if __name__ == '__main__':
    #solution_check_make(run=run_p3)
    print('Sorry, no built in tests for part-3.')
