import time
import Variables

def RateLimited(maxPerSecond):
    if maxPerSecond!=0:
        minInterval = 1.0 / float(maxPerSecond)
    def decorate(func):
        lastTimeCalled = [0.0]
        def rateLimitedFunction(*args,**kargs):
            elapsed = time.clock() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.clock()
            return ret
        return rateLimitedFunction
    return decorate

def get_participant_id(bulk_match_stats, name):
    participant_id=-1
    for stat_page in bulk_match_stats:
        for each in stat_page["participantIdentities"]:
            if each["player"]["summonerName"].lower()==name.lower():
                participant_id=each["participantId"]
    return participant_id

def pull_stats(new_element, stats):
    for x, y in new_element.items():
        for a, b in stats.items():
            if x==a:
                new_element[x]=b
                print '{:<40}{:<20}'.format((str(a)+' :'), b)
    return new_element

def pull_player_stats(bulk_match_stats, participant_id, total_games):
    player_stats=[{} for i in range(total_games)]
    counter=0
    for stat_page in bulk_match_stats:
        new_element={
            'minionsKilled': 'EMPTY',
            'neutralMinionsKilled': 'EMPTY',
            'neutralMinionsKilledEnemyJungle': 'EMPTY',
            #'neutralMinionsKilledTeamJungle': 'EMPTY',

            'kills': 'EMPTY',
            'deaths': 'EMPTY',
            'assists': 'EMPTY',

            'doubleKills': 'EMPTY',
            'tripleKills': 'EMPTY',
            'quadraKills': 'EMPTY',
            'pentaKills': 'EMPTY',

            'physicalDamageDealtToChampions': 'EMPTY',
            'magicDamageDealtToChampions': 'EMPTY',
            'trueDamageDealtToChampions': 'EMPTY',
            'totalDamageDealtToChampions': 'EMPTY',

            'physicalDamageDealt': 'EMPTY',
            'magicDamageDealt': 'EMPTY',
            'trueDamageDealt': 'EMPTY',
            'totalDamageDealt': 'EMPTY',

            'physicalDamageTaken': 'EMPTY',
            'magicDamageTaken': 'EMPTY',
            'trueDamageTaken': 'EMPTY',
            'totalDamageTaken': 'EMPTY',

            'totalHeal': 'EMPTY',

            'wardsPlaced': 'EMPTY',
            'wardsKilled': 'EMPTY',

            #'sightWardsBoughtInGame': 'EMPTY',
            #'visionWardsBoughtInGame': 'EMPTY',

            'totalTimeCrowdControlDealt': 'EMPTY',

            'killingSprees': 'EMPTY',

            'goldEarned': 'EMPTY',
            'goldSpent': 'EMPTY',
        }
        print "--------------------------------------------------------------------"
        print "--------------------------------------------------------------------"
        print "----------------------------game: {game_number}---------------------------------".format(game_number=counter+1)
        print "--------------------------------------------------------------------"
        print "--------------------------------------------------------------------"
        player_stats.append(pull_stats(new_element, stat_page["participants"][participant_id]['stats']))
        print "--------------------------------------------------------------------"
        print "--------------------------------------------------------------------"
        print "--------------------------------------------------------------------"
        print "--------------------------------------------------------------------"
        print "--------------------------------------------------------------------"
        print ''
        counter+=1
    return player_stats

def max_stats(raw_stats_array):
    max_stats={
        'minionsKilled': 'EMPTY',
        'neutralMinionsKilled': 'EMPTY',
        'neutralMinionsKilledEnemyJungle': 'EMPTY',
        #'neutralMinionsKilledTeamJungle': 'EMPTY',

        'kills': 'EMPTY',
        'deaths': 'EMPTY',
        'assists': 'EMPTY',

        'doubleKills': 'EMPTY',
        'tripleKills': 'EMPTY',
        'quadraKills': 'EMPTY',
        'pentaKills': 'EMPTY',

        'physicalDamageDealtToChampions': 'EMPTY',
        'magicDamageDealtToChampions': 'EMPTY',
        'trueDamageDealtToChampions': 'EMPTY',
        'totalDamageDealtToChampions': 'EMPTY',

        'physicalDamageDealt': 'EMPTY',
        'magicDamageDealt': 'EMPTY',
        'trueDamageDealt': 'EMPTY',
        'totalDamageDealt': 'EMPTY',

        'physicalDamageTaken': 'EMPTY',
        'magicDamageTaken': 'EMPTY',
        'trueDamageTaken': 'EMPTY',
        'totalDamageTaken': 'EMPTY',

        'totalHeal': 'EMPTY',

        'wardsPlaced': 'EMPTY',
        'wardsKilled': 'EMPTY',

        #'sightWardsBoughtInGame': 'EMPTY',
        #'visionWardsBoughtInGame': 'EMPTY',

        'totalTimeCrowdControlDealt': 'EMPTY',

        'killingSprees': 'EMPTY',

        'goldEarned': 'EMPTY',
        'goldSpent': 'EMPTY',
    }
    for _x, _y in max_stats.items():
        max_stats[_x]=0
    for x, y in max_stats.items():
        for each in raw_stats_array:
            for a, b in each.items():
                if x==a and each[a]>max_stats[x]:
                    max_stats[x]=each[a]
    max_stats['name']='max stats'
    return max_stats

def min_stats(raw_stats_array):
    min_stats={
        'minionsKilled': 'EMPTY',
        'neutralMinionsKilled': 'EMPTY',
        'neutralMinionsKilledEnemyJungle': 'EMPTY',
        #'neutralMinionsKilledTeamJungle': 'EMPTY',

        'kills': 'EMPTY',
        'deaths': 'EMPTY',
        'assists': 'EMPTY',

        'doubleKills': 'EMPTY',
        'tripleKills': 'EMPTY',
        'quadraKills': 'EMPTY',
        'pentaKills': 'EMPTY',

        'physicalDamageDealtToChampions': 'EMPTY',
        'magicDamageDealtToChampions': 'EMPTY',
        'trueDamageDealtToChampions': 'EMPTY',
        'totalDamageDealtToChampions': 'EMPTY',

        'physicalDamageDealt': 'EMPTY',
        'magicDamageDealt': 'EMPTY',
        'trueDamageDealt': 'EMPTY',
        'totalDamageDealt': 'EMPTY',

        'physicalDamageTaken': 'EMPTY',
        'magicDamageTaken': 'EMPTY',
        'trueDamageTaken': 'EMPTY',
        'totalDamageTaken': 'EMPTY',

        'totalHeal': 'EMPTY',

        'wardsPlaced': 'EMPTY',
        'wardsKilled': 'EMPTY',

        #'sightWardsBoughtInGame': 'EMPTY',
        #'visionWardsBoughtInGame': 'EMPTY',

        'totalTimeCrowdControlDealt': 'EMPTY',

        'killingSprees': 'EMPTY',

        'goldEarned': 'EMPTY',
        'goldSpent': 'EMPTY',
    }
    for _x, _y in min_stats.items():
        for _a, _b in raw_stats_array[1].items():
            if _x==_a:
                min_stats[_x]=_b
    for x, y in min_stats.items():
        for each in raw_stats_array:
            for a, b in each.items():
                if x==a and each[a]<min_stats[x]:
                    min_stats[x]=each[a]
    min_stats['name']='min stats'
    return min_stats

def total_stats(raw_stats_array):
    total_stats={
        'minionsKilled': 'EMPTY',
        'neutralMinionsKilled': 'EMPTY',
        'neutralMinionsKilledEnemyJungle': 'EMPTY',
        #'neutralMinionsKilledTeamJungle': 'EMPTY',

        'kills': 'EMPTY',
        'deaths': 'EMPTY',
        'assists': 'EMPTY',

        'doubleKills': 'EMPTY',
        'tripleKills': 'EMPTY',
        'quadraKills': 'EMPTY',
        'pentaKills': 'EMPTY',

        'physicalDamageDealtToChampions': 'EMPTY',
        'magicDamageDealtToChampions': 'EMPTY',
        'trueDamageDealtToChampions': 'EMPTY',
        'totalDamageDealtToChampions': 'EMPTY',

        'physicalDamageDealt': 'EMPTY',
        'magicDamageDealt': 'EMPTY',
        'trueDamageDealt': 'EMPTY',
        'totalDamageDealt': 'EMPTY',

        'physicalDamageTaken': 'EMPTY',
        'magicDamageTaken': 'EMPTY',
        'trueDamageTaken': 'EMPTY',
        'totalDamageTaken': 'EMPTY',

        'totalHeal': 'EMPTY',

        'wardsPlaced': 'EMPTY',
        'wardsKilled': 'EMPTY',

        #'sightWardsBoughtInGame': 'EMPTY',
        #'visionWardsBoughtInGame': 'EMPTY',

        'totalTimeCrowdControlDealt': 'EMPTY',

        'killingSprees': 'EMPTY',

        'goldEarned': 'EMPTY',
        'goldSpent': 'EMPTY',
    }
    for _x, _y in total_stats.items():
        total_stats[_x]=0
    for x, y in total_stats.items():
        for each in raw_stats_array:
            for a, b in each.items():
                if x==a:
                    total_stats[x]=total_stats[x]+b
    total_stats['name']='total stats'
    return total_stats

def avg_stats(raw_stats_array, total_stats, total_games):
    avg_stats_calculable={
        'minionsKilled': 'EMPTY',
        'neutralMinionsKilled': 'EMPTY',
        'neutralMinionsKilledEnemyJungle': 'EMPTY',
        #'neutralMinionsKilledTeamJungle': 'EMPTY',

        'kills': 'EMPTY',
        'deaths': 'EMPTY',
        'assists': 'EMPTY',

        'doubleKills': 'EMPTY',
        'tripleKills': 'EMPTY',
        'quadraKills': 'EMPTY',
        'pentaKills': 'EMPTY',

        'physicalDamageDealtToChampions': 'EMPTY',
        'magicDamageDealtToChampions': 'EMPTY',
        'trueDamageDealtToChampions': 'EMPTY',
        'totalDamageDealtToChampions': 'EMPTY',

        'physicalDamageDealt': 'EMPTY',
        'magicDamageDealt': 'EMPTY',
        'trueDamageDealt': 'EMPTY',
        'totalDamageDealt': 'EMPTY',

        'physicalDamageTaken': 'EMPTY',
        'magicDamageTaken': 'EMPTY',
        'trueDamageTaken': 'EMPTY',
        'totalDamageTaken': 'EMPTY',

        'totalHeal': 'EMPTY',

        'wardsPlaced': 'EMPTY',
        'wardsKilled': 'EMPTY',

        #'sightWardsBoughtInGame': 'EMPTY',
        #'visionWardsBoughtInGame': 'EMPTY',

        'totalTimeCrowdControlDealt': 'EMPTY',

        'killingSprees': 'EMPTY',

        'goldEarned': 'EMPTY',
        'goldSpent': 'EMPTY',
    }
    for x, y in avg_stats_calculable.items():
        for a, b in total_stats.items():
                if x==a and x!='name':
                    avg_stats_calculable[x]=b/float(total_games)
    avg_stats_calculable['name']='avg stats'
    return avg_stats_calculable
#the below would be placed above the avg_stats['name']... ... ... if it worked
#    avg_stats_alternate=Variables._alternative_stat_calculations_template
#    first_blood=Variables._TF_tracker_list
#    first_assist=Variables._TF_tracker_list
#    win_tracker=Variables._TF_tracker_list
#    team_tracker=Variables._TF_tracker_list
#    for each in raw_stats_array:
#        if each['firstBloodKill']:
#            first_blood[0]=first_blood[0]+1
#        else:
#            first_blood[1]=first_blood[1]+1
#        if each['firstBloodAssist']:
#            first_assist[0]=first_assist[0]+1
#        else:
#            first_assist[1]=first_assist[1]+1
#        if each['winner']:
#            win_tracker[0]=win_tracker[0]+1
#        else:
#            win_tracker[1]=win_tracker[1]+1
##        if each['teamId']==100:
##            team_tracker[0]=team_tracker[0]+1
##        else:
##            team_tracker[1]=team_tracker[1]+1
#    alt_stats=Variables.alt_avg_stats_appendable
#    first_blood_participation=(first_blood[0]/float(total_games))*100
#    alt_stats['firstBloodParticipationRate']=first_blood_participation+((first_assist[0]/float(total_games))*100)
#    alt_stats['winRate']=(win_tracker[0]/float(total_games))*100
#    alt
#    alt_stats['blueTeamFrequency']=(team_tracker[0]/float(total_games))*100
#    alt_stats['redTeamFrequency']=(team_tracker[1]/float(total_games))*100
#    avg_stats={}
#    avg_stats['calculable']=avg_stats_calculable
#    avg_stats['alt_stats']=alt_stats
    #first blood
    #first assists
    #win / loss
    #blue / red

def collect_match_ids(match_data_list):
        return match_data_list["matchId"]

@RateLimited(float(5/6))
def request_bulk_stats_long(api, _Id):
    bulk=api.get_match(_Id, {})
    return bulk

@RateLimited(1)
def request_bulk_stats_short(api, _Id):
    bulk=api.get_match(_Id, {})
    return bulk
