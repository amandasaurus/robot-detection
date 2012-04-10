from __future__ import print_function

import sys, os.path, codecs

robot_useragents= set([u'ATN_Worldwide',
     u'AlkalineBOT', u'AraybOt', u'Ask Jeeves', u'Atomz',
     u'Bjaaland', u'BotLink', u'CMC/0.01', u'CoolBot',
     u'DIIbot', u'DragonBot', u'ESI', u'FDSE',
     u'FELIX IDE', u'Freecrawl', u'Getterrobo-Plus', u'Gromit',
     u'H\xe4m\xe4h\xe4kki', u'INGRID/0.1', u'InfoSpiders', u'Informant',
     u'Internet Cruiser Robot', u'Iron33', u'JBot', u'Jeeves',
     u'KDD-Explorer', u'KIT-Fireball', u'Linkidator', u'Lockon',
     u'MerzScope', u'MindCrawler', u'Motor', u'MuscatFerret',
     u'MwdSearch', u'NEC-MeshExplorer', u'Nederland.zoek', u'NetScoop',
     u'ObjectsSearch', u'Occam', u'Orbsearch/1.0', u'ParaSite',
     u'Pimptrain', u'PlumtreeWebAccessor', u'PortalBSpider', u'RHCS',
     u'Raven', u'RixBot', u'Robbie', u'RoboCrawl',
     u'SLCrawler/2.0', u'Scooter', u'Search-AU', u'Senrigan',
     u'Shagseeker', u'SimBot', u'Site Valet', u'SpiderBot/1.0',
     u'T-H-U-N-D-E-R-S-T-O-N-E', u'TechBOT', u'Teoma', u'UdmSearch',
     u'Ukonline', u'VWbot_K', u'Valkyrie libwww-perl', u'Victoria',
     u'Voyager', u'WOLP', u'WWWC', u'WebBandit/1.0',
     u'WebMechanic', u'WebMoose', u'WebWalker', u'XGET',
     u'ahoy', u'anthill', u'appie', u'arale',
     u'araneo', u'ariadne', u'arks', u'bbot',
     u'borg-bot/0.9', u'boxseabot', u'bspider', u'calif',
     u'christcrawler', u'combine', u'confuzzledbot', u'cosmos',
     u'crawlpaper', u'cusco', u'cyberspyder', u'cydralspider',
     u'desertrealm, desert realm', u'digger', u'downloadexpress', u'dwcp',
     u'ebiness', u'ecollector', u'elfinbot', u'esculapio',
     u'esther', u'fastcrawler', u'fido', u'fouineur',
     u'gammaSpider', u'gazz', u'gcreep', u'golem',
     u'googlebot', u'grabber', u'griffon', u'gulliver',
     u'gulper', u'hambot', u'havIndex', u'hotwired',
     u'htdig', u'http://www.sygol.com', u'iajabot', u'image.kapsi.net',
     u'inspectorwww', u'irobot', u'jcrawler', u'jobo',
     u'ko_yappo_robot', u'label-grabber', u'larbin', u'legs',
     u'linkwalker', u'logo_gif_crawler', u'marvin', u'mattie',
     u'mediafox', u'moget', u'msnbot', u'muncher',
     u'muninn', u'newscan-online', u'nil', u'packrat',
     u'pageboy', u'patric', u'pegasus', u'perlcrawler',
     u'phpdig', u'piltdownman', u'pjspider', u'psbot',
     u'roadrunner', u'robi', u'robofox', u'robots.txt',
     u'searchprocess', u'sharp-info-agent', u'sift', u'skymob',
     u'slurp', u'snooper', u'solbot', u'speedy',
     u'spider_monkey', u'spiderline', u'suke', u'tach_bw',
     u'templeton', u'titin', u'topiclink', u'udmsearch',
     u'urlck', u'verticrawl', u'void-bot', u'wapspider',
     u'webcatcher', u'webquest', u'webreaper', u'webs',
     u'webspider', u'wget', u'whowhere', u'winona',
     u'wlm',

    # have to add
    u'bingbot', u'baiduspider', u'YandexBot', u'YoudaoBot', u'AdsBot-Google',
    u'MJ12bot', u'SeznamBot', u'YodaoBot', u'SurveyBot', u'discobot',
    u'IErachnid', u'Sogou web spider', u'findlinks',
     
    ])


def is_robot(user_agent):
    if not isinstance(user_agent, basestring):
        raise TypeError
    if len(user_agent) == 0:
        raise ValueError

    try:
        # See if any one matches
        return any(robot_ua.lower() in user_agent.lower() for robot_ua in robot_useragents)
    except UnicodeDecodeError:
        # Unicode error, robot_useragents is unicode strings. user_agent might have malformed bytes, so try looking at boring ascii
        return any(robot_ua.lower().encode('ascii', 'ignore') in user_agent.lower() for robot_ua in robot_useragents)



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
        print("robot_detection is out of date. Here's the new robot_useragents variable:")
        print(exclude_ua)
    else:
        print("No changes, robot_detection is up to date")


if __name__ == '__main__' and len(sys.argv) == 2:
    _parse_db_export(sys.argv[1])

