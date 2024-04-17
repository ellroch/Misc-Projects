from RiotAPI import RiotAPI
from main import *

#true / false tracker
_TF_tracker={
    True: 0,
    False: 0
}

_Team_tracker={
    100: 0,
    #100= blue
    200: 0
    #200= red
}

#true / false tracker index0 =true index1=false
_TF_tracker_list=[0,0]

match_list_request_params={
    'championIds': 'EMPTY',
    'rankedQeues': 'EMPTY',
    'seasons': 'EMPTY',
    'beginTime': 'EMPTY',
    #of type long
    #The begin time to use for fetching games specified as epoch milliseconds.
    'endTime': 'EMPTY',
    #of type long
    #The end time to use for fetching games specified as epoch milliseconds.
    'beginIndex': 'EMPTY',
    #of type int
    #The begin index to use for fetching games.
    'endIndex': 'EMPTY'
    #of type int
    #The end index to use for fetching games.
}

alt_avg_stats_appendable={
    'firstBloodParticipationRate': float,
    'winRate': float,
}

_alternative_stat_calculations_template={
    'firstBloodKill': 0,
    'firstBloodAssist': 0,
    #make an array of 100's and 200's
    #100=blue team
    #200=red team
    'winner': 0
}

_match_stats_calculations_template={
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

_match_stats={
    'minionsKilled': 'EMPTY',
    'neutralMinionsKilled': 'EMPTY',
    'neutralMinionsKilledEnemyJungle': 'EMPTY',
    'neutralMinionsKilledTeamJungle': 'EMPTY',

    'kills': 'EMPTY',
    'deaths': 'EMPTY',
    'assists': 'EMPTY',

    'doubleKills': 'EMPTY',
    'tripleKills': 'EMPTY',
    'quadraKills': 'EMPTY',
    'pentaKills': 'EMPTY',
    'unrealKills': 'EMPTY',

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

    'sightWardsBoughtInGame': 'EMPTY',
    'visionWardsBoughtInGame': 'EMPTY',

    'totalTimeCrowdControlDealt': 'EMPTY',

    'killingSprees': 'EMPTY',
    'largestKillingSpree': 'EMPTY',
    'largestMultiKill': 'EMPTY',

    'goldEarned': 'EMPTY',
    'goldSpent': 'EMPTY',

    'firstBloodKill': 'EMPTY',
    'firstBloodAssist': 'EMPTY',

    'champLevel': 'EMPTY',

    'teamId': 'EMPTY',
    #make an array of 100's and 100's
    #100=blue team
    #200=red team
    'winner': 'EMPTY'
}

stat_summary={
    'botGamesPlayed',
    'normalGamesPlayed',
    'rankedPremadeGamesPlayed',
    'rankedSoloGamesPlayed',
    'totalSessionsPlayed',
    'totalSessionsWon',
    'totalSessionsLost',

    'totalMinionKills',
    'totalNeutralMinionsKilled',
    'totalTurretsKilled',
    'totalGoldEarned',

    'totalChampionKills',

    'totalAssists',

    'totalDamageDealt',
    'totalPhysicalDamageDealt',
    'totalMagicDamageDealt',
    'totalDamageTaken',
    'totalHeal',

    'maxLargestCriticalStrike',

    'maxTimePlayed',

    'maxChampionsKilled',
    'maxNumDeaths',

    'killingSpree',
    'maxLargestKillingSpree',
    'mostChampionKillsPerSession',
    'totalFirstBlood',
    'totalDoubleKills',
    'totalTripleKills',
    'totalQuadraKills',
    'totalPentaKills',
    'totalUnrealKills'
}
_stat_blocks={
    #    'max stats': _match_stats_calulations_template,
    'max stats': {
        'minionsKilled': 'EMPTY',
        'neutralMinionsKilled': 'EMPTY',
        'neutralMinionsKilledEnemyJungle': 'EMPTY',
        'neutralMinionsKilledTeamJungle': 'EMPTY',

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
    },
    #    'min stats':  _match_stats_calulations_template,
    'min stats': {
        'minionsKilled': 'EMPTY',
        'neutralMinionsKilled': 'EMPTY',
        'neutralMinionsKilledEnemyJungle': 'EMPTY',
        'neutralMinionsKilledTeamJungle': 'EMPTY',

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
    },
    #    'avg stats':  _match_stats_calulations_template,
    'avg stats': {
        'minionsKilled': 'EMPTY',
        'neutralMinionsKilled': 'EMPTY',
        'neutralMinionsKilledEnemyJungle': 'EMPTY',
        'neutralMinionsKilledTeamJungle': 'EMPTY',

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
    },
    #    'total stats': _match_stats_calulations_template
    'total stats': {
        'minionsKilled': 'EMPTY',
        'neutralMinionsKilled': 'EMPTY',
        'neutralMinionsKilledEnemyJungle': 'EMPTY',
        'neutralMinionsKilledTeamJungle': 'EMPTY',

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
    #    'total stats': {
    #        'alt_stats': alt_avg_stats_appendable,
    #        'calculable': _match_stats_calulations_template
    #    }
}

_info={
    'summoner_info': {
        'name': 'EMPTY',
        'region': 'EMPTY',
        'id': 'EMPTY'
    },
    'match_params': {},
    'match_id_list': [],
    'stats_book': {
        'max stats': {},
        'min stats': {},
        'total stats': {},
        'avg stats': {}
    },
    'stats_summary': {}
}

_info_stat_book_directory={
    'max stats': 0,
    'min stats': 1,
    'total stats': 2,
    'avg stats': 3
}

_switch={
    1: '# something that manages RiotAPI.get_stat_summary_ranked',
    2: '# something that manages RiotAPI.get_recent_games',
    3: matchlist_and_match_function_operator,
    0: 'EMPTY'
}

example_info={
    'summoner_info': {
        'name': 'Ellroch',
        'region': 'na',
        'id': '25462406'
    },
    'match_params': {
        'championIds': '63',
        'rankedQeues': 'RANKED_TEAM_5x5',
        'seasons': 'PRESEASON2016',
    },
    'match_id_list': ['2030610589'],
    'stats_book': {
        'max stats': {},
        'min stats': {},
        'total stats': {},
        'avg stats': {}
    },
    'stats_summary': {}
}
