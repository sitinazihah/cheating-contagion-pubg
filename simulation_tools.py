from collections import defaultdict
import random

def main():
    pass


def get_matches_with_cheaters(cheaters, kills):
    '''Given two lists of formatted values, i.e. cheaters and kills,
    returns a dictionary that maps matches with active cheaters to
    the active cheaters in those matches.'''

    # create a dictionary to map cheaters to the dates they started cheating
    cheater_dic = {}
    for cheater_id, cheat_date, banned_date in cheaters:
        cheater_dic[cheater_id] = cheat_date

    # create a dictionary that maps matches with active cheaters
    # to active cheaters in that match
    match_and_active_cheaters = defaultdict(list)
    for j in kills:
        try:
            # append killers who were active cheaters in that match
            if cheater_dic[j[1]] < j[3] and\
            j[1] not in match_and_active_cheaters[j[0]]:
                match_and_active_cheaters[j[0]].append(j[1])

            # append victims who were active cheaters in that match
            if cheater_dic[j[2]] < j[3] and\
            j[2] not in match_and_active_cheaters[j[0]]:
                match_and_active_cheaters[j[0]].append(j[2])

        except KeyError:
            continue
    return match_and_active_cheaters


def group_all_matches(kills):
    '''Given a list of formatted values i.e. kills, groups data in kills
    by matches. Returns a dictionary that maps each match to the details
    of each killing within the match.'''

    group_matches = defaultdict(list)
    for match, killer, victim, timing in kills:
        group_matches[match].append([killer, victim, timing])

    return group_matches


def get_non_cheaters(dic_cheaters, dic_groups):
    '''Given 2 dictionaries, i.e. dic_cheaters that maps matches with cheaters
    to cheaters in those matches and dic_groups that groups same matches
    together, returns a dictionary that maps matches with cheaters to the
    non-cheaters in those matches.'''

    non_cheaters = defaultdict(list)
    # iterate over each value component that is mapped to each match
    for match in dic_groups.keys():
        for value in dic_groups[match]:

            # only look at matches with cheaters
            if match in dic_cheaters.keys():
                # append killers who were in matches with active cheaters
                # but were themselves not active cheaters
                if value[0] not in dic_cheaters[match] and\
                value[0] not in non_cheaters[match]:
                    non_cheaters[match].append(value[0])

                # append victims who were in matches with active cheaters
                # but were themselves not active cheaters
                if value[1] not in dic_cheaters[match] and\
                value[1] not in non_cheaters[match]:
                    non_cheaters[match].append(value[1])

    return non_cheaters


def get_simulation(dic_cheaters, dic_groups, dic_non_cheaters):
    '''Takes 3 dictionaries as inputs, i.e. 1) dic_cheaters that maps matches
    with cheaters to cheaters in those matches, 2) dic_groups that groups same
    matches together, and 3) dic_non_cheaters that maps matches with cheaters
    to non-cheaters in those matches. Returns a list that randomizes the
    positions of non-cheaters in matches with active cheaters but preserves
    the positions of cheaters in those matches.'''

    kills_randomized = []
    # iterate over each match
    for match in dic_groups.keys():
        # prepare for randomisation in matches with active cheaters
        if match in dic_cheaters.keys():

            # create a temporary dictionary that maps cheaters to themselves
            # and non-cheaters to other non-cheaters within the match
            temp = dic_non_cheaters[match][:]
            random.shuffle(temp)
            dic_mapping = {}
            for i in dic_cheaters[match]:
                dic_mapping[i] = i
            for j,k in zip(dic_non_cheaters[match], temp):
                dic_mapping[j] = k

        # look at each value component mapped to each match
        for value in dic_groups[match]:
            # preserve order for matches with no active cheaters
            if match not in dic_cheaters.keys():
                kills_randomized.append([match, value[0], value[1], value[2]])
            # conduct randomisation for matches with active cheaters
            else:
                value[0] = dic_mapping[value[0]]
                value[1] = dic_mapping[value[1]]
                kills_randomized.append([match, value[0], value[1], value[2]])

    return kills_randomized


if __name__ == '__main__':
    main()
