# Copyright 2018 Qinjin Jia qjia@bu.edu

import MongoDBPython

from MongoDBPython import DatabaseUpdate

# Most popular 20 twitter accounts
# https://en.wikipedia.org/wiki/List_of_most-followed_Twitter_accounts
DatabaseUpdate('katyperry');
DatabaseUpdate('justinbieber');
DatabaseUpdate('BarackObama');
DatabaseUpdate('rihanna');
DatabaseUpdate('taylorswift13');
DatabaseUpdate('ladygaga');
DatabaseUpdate('TheEllenShow');
DatabaseUpdate('Cristiano');
DatabaseUpdate('Youtube');
DatabaseUpdate('jtimberlake');
DatabaseUpdate('twitter');
DatabaseUpdate('KimKardashian');
DatabaseUpdate('britneyspears');
DatabaseUpdate('ArianaGrande');
DatabaseUpdate('selenagomez');
DatabaseUpdate('ddlovato');
DatabaseUpdate('cnnbrk');
DatabaseUpdate('shakira');
DatabaseUpdate('jimmyfallon');
DatabaseUpdate('realDonaldTrump');
print('All set!');

from MongoDBPython import TotalTags
data = TotalTags();