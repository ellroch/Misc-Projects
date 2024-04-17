import Variables
import RiotConsts as Consts

def get_name():
    print "Summoner Name:"
    user_input=raw_input()
    return user_input

def get_region():
    print "region:"
    print ' 1) na    '
    print ' 2) euw   '
    print ' 3) eune  '
    print ' 4) br    '
    print ' 5) lan   '
    print ' 6) las   '
    print ' 7) oce   '
    print ' 8) kr    '
    print ' 9) tr    '
    print '10) ru    '
    user_input=raw_input()
    return user_input

def confirm_input(user_input):
    print 'is (', str(user_input), ') correct? y/n'
    confirmation=raw_input()
    while confirmation!='y' and confirmation!='n':
        print "------  INVALID INPUT  ------"
        print 'is (', str(user_input), ') correct? (y/n)'
        confirmation=raw_input()
    if confirmation=='y':
        return True
    else:
        return False

def switch_select():
    print 'What do:'
    print ' 1) get basic stat summary'
    print ' 2) get recent "match history"'
    print ' 3) get stat summary for any combination of conditional specifiers below:'
    print '     - champion played'
    print '     - select ranked qeues or general qeues'
    #print '     - timeframe (last 24 hrs, 48 hrs, 1 week, 1 month, 3 months, 6 months, 1 year, all time) '
    #print '     - can set a max index for matches parsed'
    print ' 0) end program'
    user_input = raw_input()
    user_choice= int(user_input)
    while user_choice not in Variables._switch:
        if user_choice==0:
            return False
        print "---------  INVALID INPUT  -----------"
        print "-input only the corresponding number-"
        print ' 1) get basic stat summary'
        print ' 2) get recent "match history"'
        print ' 3) get stat summary for any combination of conditional specifiers below:'
        print '     - champion played'
        print '     - select ranked qeues or general qeues'
        #print '     - timeframe (last 24 hrs, 48 hrs, 1 week, 1 month, 3 months, 6 months, 1 year, all time) '
        #print '     - can set a max index for matches parsed'
        print ' 0) end program'
        user_input = raw_input()
        user_choice= int(user_input)
    else:
        return user_choice

def get_match_params():
    params=Variables.match_list_request_params
    #champion --------------------------------
    #rank qeue if specifiable-----------------
    #seasons----------------------------------
    #beginTime (earliest time to start from), unspecified = beginning of history
    #endTime (latest time to start from), unspecified = now
    #beginIndex
    #endIndex
    #checked= checklist concept
    _invalid_check=True
    checked=False
    while not checked:
        print "specify champion if desired ('0' if unspecified):"
        params['championIds']=raw_input()
        if params['championIds']=='0':
            params['championIds']='EMPTY'
            checked=True
            _invalid_check=False
        else:
            for _champ, _id in Consts.CHAMPIONS.items():
                if params['championIds']==_champ:
                    params['championIds']=_id
                    checked=True
                    _invalid_check=False
        if _invalid_check:
            print "---------  INVALID INPUT  -----------"
    _invalid_check=True
    checked=False
    while not checked:
        print "specify ranked Qeue's ('0' if unspecified):"
        print " 1) ranked solo 5v5"
        print " 2) ranked tean 3v3"
        print " 3) ranked team 5v5"
        print " 4) team builder ranked 5v5"
        params['rankedQeues']=raw_input()
        if params['rankedQeues']=='0':
            params['rankedQeues']='EMPTY'
            checked=True
            _invalid_check=False
        else:
            for Qeue_number, _id in Consts.ranked_qeues.items():
                if params['rankedQeues']==Qeue_number:
                    params['rankedQeues']=_id
                    checked=True
                    _invalid_check=False
            if _invalid_check:
                print "---------  INVALID INPUT  -----------"
    _invalid_check=True
    checked=False
    url_params={}
    params['seasons']=Consts._seasons_array
    for _param, _value in params.items():
        if _value!='EMPTY':
            url_params[_param]=_value
    print 'match params:', url_params
    return url_params
