from RiotAPI import RiotAPI
import RiotConsts as Consts
import UserInterface as UI
import Variables
import _other_functions as Other

def matchlist_and_match_function_operator(information):
    api=RiotAPI(Consts.API_KEY, information['summoner_info']['region'])
    information['match_params']=UI.get_match_params()
    raw_match_list=api.get_matchlist(information['summoner_info']['id'], information['match_params'])
    totalGames=raw_match_list["totalGames"]
    print "totalGames: ", str(totalGames)
    information['match_id_list']=[]
    for each_match in raw_match_list["matches"]:
        information['match_id_list'].append(each_match["matchId"])

    print "match id list: ", information['match_id_list']
    bulk_match_stats=[]
    counter_a=0
                 # 498 + the two prior requests would==500 which calls a lower rate request timer in accordance with my current api request limit
    if totalGames>498:
        for each_id in information['match_id_list']:
            bulk_match_stats.append(Other.request_bulk_stats_long(api, each_id))
            print 'matches collected: ', counter_a+1, ' of ', totalGames
            counter_a+=1
        for each_id in information['match_id_list']:
            bulk_match_stats.append(Other.request_bulk_stats_long(api, each_id))
            print 'matches collected: ', counter_a+1, ' of ', totalGames
            counter_a+=1
    else:
        for each_id in information['match_id_list']:
            bulk_match_stats.append(Other.request_bulk_stats_short(api, each_id))
            print 'matches collected: ', counter_a+1, ' of ', totalGames
            counter_a+=1
    participant_id=Other.get_participant_id(bulk_match_stats,  information['summoner_info']['name'])
    pulled_stats_array=Other.pull_player_stats(bulk_match_stats, participant_id, totalGames)
    stats={}
    if len(pulled_stats_array)>1:
        information['stats_book']['max stats']=Other.max_stats(pulled_stats_array)
        information['stats_book']['min stats']=Other.min_stats(pulled_stats_array)
        information['stats_book']['total stats']=Other.total_stats(pulled_stats_array)
        information['stats_book']['avg stats']=Other.avg_stats(pulled_stats_array, information['stats_book']['total stats'], totalGames)
        for a, b in information['stats_book'].items():
            _buff_header_length=len('/|\\|/|\\|/|\\|/|\\|/\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\')
            print '\\|/|\\|/|\\|/|\\|/\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/'
            print '/|\\|/|\\|/|\\|/|\\|/\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\'
            print str(a).center(_buff_header_length,'|')
            print '/|\\|/|\\|/|\\|/|\\|/\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\'
            print '\\|/|\\|/|\\|/|\\|/\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/|\\|/'
            print '{:<40} : {:<20}'.format('minions killed', b['minionsKilled'])
            print ''
            print '{:<40} : {:<20}'.format('total jungle monsters killed', b['neutralMinionsKilled'])
            print '{:<40} : {:<20}'.format('enemy jungle monsters killed', b['neutralMinionsKilledEnemyJungle'])
            print ''
            print '{:<40} : {:<20}'.format('kills', b['kills'])
            print '{:<40} : {:<20}'.format('deaths', b['deaths'])
            print '{:<40} : {:<20}'.format('assists', b['assists'])
            print ''
            print '{:<40} : {:<20}'.format('double kills', b['doubleKills'])
            print '{:<40} : {:<20}'.format('triple kills', b['tripleKills'])
            print '{:<40} : {:<20}'.format('quadra kills', b['quadraKills'])
            print '{:<40} : {:<20}'.format('penta kills', b['pentaKills'])
            print ''
            print '{:<40} : {:<20}'.format('physical damage to champions', b['physicalDamageDealtToChampions'])
            print '{:<40} : {:<20}'.format('magic damage to champions', b['magicDamageDealtToChampions'])
            print '{:<40} : {:<20}'.format('true damage to champions', b['trueDamageDealtToChampions'])
            print '{:<40} : {:<20}'.format('total damage to champions', b['totalDamageDealtToChampions'])
            print ''
            print '{:<40} : {:<20}'.format('physical damage dealt', b['physicalDamageDealt'])
            print '{:<40} : {:<20}'.format('magic damage dealt', b['magicDamageDealt'])
            print '{:<40} : {:<20}'.format('true damage dealt', b['trueDamageDealt'])
            print '{:<40} : {:<20}'.format('total damage dealt', b['totalDamageDealt'])
            print ''
            print '{:<40} : {:<20}'.format('physical damage taken', b['physicalDamageTaken'])
            print '{:<40} : {:<20}'.format('magic damage taken', b['magicDamageTaken'])
            print '{:<40} : {:<20}'.format('true damage taken', b['trueDamageTaken'])
            print '{:<40} : {:<20}'.format('total damage taken', b['totalDamageTaken'])
            print ''
            print '{:<40} : {:<20}'.format('total healing', b['totalHeal'])
            print ''
            print '{:<40} : {:<20}'.format('wards placed', b['wardsPlaced'])
            print '{:<40} : {:<20}'.format('wards killed', b['wardsKilled'])
            print ''
            print '{:<40} : {:<20}'.format('total cc dealt (in seconds)', b['totalTimeCrowdControlDealt'])
            print ''
            print '{:<40} : {:<20}'.format('number of killing sprees', b['killingSprees'])
            print ''
            print '{:<40} : {:<20}'.format('gold earned', b['goldEarned'])
            print '{:<40} : {:<20}'.format('gold spent', b['goldSpent'])
    else:
        information['stats_book']=pulled_stats_array
    #pull player stats from the bulk:
    #participantIdentities is a list of dictionaries... navigate via element numbers(below the '###' stands to fill in each element when cycling through to find the player's participant id)
    #to get participant ID
    #["participantIdentities"][###]["player"]["summonerName"]
    #["participantIdentities"][###]["participantId"]
    #
    #to access stats use the participant ID to access the elements of dictionary at key "participants"like so:
    #["participants"][#^^---^^Participant ID^^---^^#]["stats"][_____collect___________from__________matches__________in______________variables._match_stats_____]
    #
    #calculate the max stats
    #calculate the min stats
    #calculate the total stats
    #divide each total stat by the number of games played in order to get the avg stats
    return information

def get_NameRegionId(information):
    region=UI.get_region()
    while region not in Consts.REGIONS:
        print "------  INVALID INPUT  ------"
        region=UI.get_region()
    #get summoner name
    name=UI.get_name()
    name_confirmation=UI.confirm_input(name)
    while not name_confirmation:
        name=UI.get_name()
        name_confirmation=UI.confirm_input(name)
    api=RiotAPI(Consts.API_KEY, region)
    r=api.get_summoner_by_name(name)
    # if response is not what we are looking for it should give us an error
    summoner_id= r[name]['id']
    information['summoner_info']= Variables._info['summoner_info']
    information['summoner_info']['name']= name
    information['summoner_info']['region']= Consts.REGIONS[region]
    information['summoner_info']['id']= summoner_id
    print 'name:   ', name
    print 'region: ', region
    print 'id:     ', summoner_id
    return information

def main():
    info=Variables._info
    info=get_NameRegionId(info)
    #info=Variables.example_info
    switch_key=UI.switch_select()
    if switch_key!=0:
        info=Variables._switch[switch_key](info)
    else:
        return 0

if __name__ == "__main__":
    main()
    raw_input("yo, this is one dope way to pause a program :D")
