from __future__ import print_function

import sys, os.path, codecs

robot_useragents = set()

def is_robot(user_agent):
    if not isinstance(user_agent, basestring):
        raise TypeError
    if len(user_agent) == 0:
        raise ValueError

    return any(robot_ua in user_agent for robot_ua in robot_useragents)


def _parse_db_export(filename):
    assert os.path.isfile(filename)

    lines = codecs.open(filename, encoding="latin1").readlines()

    exclude_ua = set()
    for line in lines:
        if line.startswith("robot-exclusion-useragent:"):
            line = line.strip()
            dont_care, ua = line.split(":", 1)
            ua = ua.strip()
            if ' or ' in ua:
                uas = ua.split(" or ")
                # remove quotes
                uas = [x[1:-1] if (x[0] in ['"', "'"] and x[-1] in ['"', "'"]) else x for x in uas]
            else:
                uas = [ua]
            for ua in uas:
                # don't include nonsense stuff
                if ua.lower() not in ['', '*', 'n/a', 'none', 'yes', 'no', "due to a deficiency in java it's not currently possible to set the user-agent."]:
                    exclude_ua.add(ua)

    if robot_useragents != exclude_ua:
        print(exclude_ua)


if __name__ == '__main__' and len(sys.argv) == 2:
    _parse_db_export(sys.argv[1])

