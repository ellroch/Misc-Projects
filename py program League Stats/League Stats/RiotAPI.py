import requests
import RiotConsts as Consts

class RiotAPI(object):

    def __init__(self, api_key, region):
        self.api_key = api_key
        self.region = Consts.REGIONS[region]

    def build_request_url(self, api_url, version_key, params):
        args= {'api_key': self.api_key,}
        for key, value in params.items():
            if key not in args:
                args[key]= value
        first_run=True
        first_in_array=True
        params_str= '?'
        for _key, _value in args.items():
            if not first_run:
                params_str=params_str+'&'
            first_in_array=True
            params_str=params_str + str(_key) + '='
            #if type(_value)!=int and _key!='api_key':
            if type(_value)!=str and type(_value)==list:
                for _each in _value:
                    if not first_in_array:
                        params_str=params_str+','
                    if type(_each)==str:
                        params_str=params_str+_each
                    else:
                        params_str=params_str+str(_each)
                    if first_in_array:
                        first_in_array=False
            else:
                if type(_value)==str:
                    params_str=params_str+_value
                else:
                    params_str=params_str+str(_value)
            if first_run:
                first_run=False
        url=Consts.URL['base'].format(
            proxy=self.region,
            region=self.region,
            version=Consts.API_VERSIONS[version_key],
            url=api_url,
            params=params_str
            )
        response=requests.get(url, args)
        print url
        print response
        print response.json()
        return response.json()
    #json stands for JavaScript Object Notation, it basically
    #parses the response which is in the form
    #of a string into a working and navigable dictionary...
    #:D which makes my job a lot easier

    def get_summoner_by_name(self, name):
        api_url= Consts.URL['summoner_by_name'].format(
            summonerNames= name
            )
        return self.build_request_url(api_url, 'summoner', {})

    def get_stat_summary(self, summoner_id, params):
        #check the riot api page for the further params involved
        #can request multiple (even all) seasons in a comma-separated list.
        api_url= Consts.URL['stats_summary'].format(
            summonerId= summoner_id
            )
        return self.build_request_url(api_url, 'stats', params)

    def get_stat_summary_ranked(self, summoner_id, params):
        #check the riot api page for the further params involved
        #can request multiple (even all) seasons in a comma-separated list.
        api_url= Consts.URL['stats_ranked'].format(
            summonerId= summoner_id
            )
        return self.build_request_url(api_url, 'stats', params)

    def get_recent_games(self, summoner_id, params):
        #check the riot api page for the further params involved
        #can request multiple (even all) seasons in a comma-separated list.
        api_url= Consts.URL['stats_ranked'].format(
            summonerId= summoner_id
            )
        return self.build_request_url(api_url, 'stats', params)

    def get_matchlist(self, summoner_id, params):
        #check the riot api page for the further params involved (can search for certain champs)
        #can request multiple (even all) seasons in a comma-separated list.
        api_url= Consts.URL['matchlist'].format(
            summonerId= summoner_id
            )
        return self.build_request_url(api_url, 'matchlist', params)

    def get_match(self, match_id, params):
        #check the riot api page for the further params involved
        #can request multiple (even all) seasons in a comma-separated list.
        api_url= Consts.URL['match'].format(
            matchID= match_id
            )
        return self.build_request_url(api_url, 'match', params)
