import redis


# def search_suggestion_insertions():
#     import redis
#     x  = redis.Redis(host="redis-15137.c257.us-east-1-3.ec2.cloud.redislabs.com", port=15137, password="HfQf7YcyrF2JOSuDlWnxsQbjqdMCJDzw", db = 0)
#     print(x.get("zz"))
#     data = ['26 Jennifer Pl', '152 Lombard St #507', '45 Ney St', '1 Hawthorne St Unit 15B', '250 King St #812', '1075 Market St #211', '167 Delano Ave', '1175 Pine St', '25 - 27 Blanken Ave', '1298 Treat Ave', '48 Terra Vista Ave Unit D', '39 Forest View Dr', '250 King St #704', '1201 California St #602', '230 Irving St', '1688 Pine St Unit W205', '2880 Green St', '1288 Howard St #315', '1400 Lake St', '22 Fairfield Way', '774 Potrero Ave', '4145 Ulloa St', '53 Harrington St', '24 - 34 Jasper Pl', '1163 - 1169 Alabama St Unit 1163A', '1219 York St', '2070 Bush St', '1745 Market St', '425 Hyde St', '715 Moultrie St', '2846 Sacramento St', '104 Collins St', '33 Rice St', '77 Jordan Ave', '999 Green St #2905', '766 Harrison St #706', '47 Richland Ave', '2925 California St #3', '219 Brannan St Unit 4J', '909 Divisadero St', '3319 Divisadero St', '430 Arch St', '92 Putnam St', '3301 - 3311 Cesar Chavez St Unit 3309A', '280 Spear St Unit 34C', '75 Navajo Ave', '786 Minna St #9', '1238 Sutter St #702', '883 39th Ave', '1590 Funston Ave', '349 - 351 Mississippi St', '1592 Funston Ave', '47 Arroyo Way', '3969 - 3971 Cesar Chavez St', '3 Topaz Way', '124 Lily St', '188 Minna St Unit 37B', '601 4th St #206', '400 Beale St #2104', '1165 - 1167 Kearny St', '1170 Prague St', '260 King St #553', '932 Silliman St', '1210 Stanyan St', '416 Peninsula Ave', '1374 18th Ave', '72 Dawnview Way', '80 JENNINGS Ct', '170 Highland Ave', '3227 - 3229 Broderick St', '160 Gardenside Dr #401', '4641 Lincoln Way', '298 Portola Dr #204', '1315 Laguna St #4', '142 Russ St #4', '2379 47th Ave', '719 Larkin St #506', '225 Bay St #203', '1809 Gough St #101', '55 Elgin Park', '601 Van Ness Ave #40', '174 Langton St Unit B', '171 San Marcos Ave', '719 Brunswick St', '601 Ortega St', '631 Folsom St Unit 11E', '2200 Sacramento St #805', '527 - 529 Birch St', '243 Paris St', '1604 Church St #1', '2037 Revere Ave', '1258 - 1260 Chestnut St', '52 - 56 Langton St', '1043 Plymouth Ave', '1001 California St #4', '2666 18th Ave', '618 Lisbon St', '188 Minna St Unit 32C', '2865 Clay St #3', '381 Turk St', '488 Folsom St #4204', '135 8th St', '247 - 249 Edna St', '763 45th Ave', '24 Page St #3', '564 Chenery St', '1363 Sanchez St', '355 Moscow St', '286 Maynard St', '4527 Lincoln Way', '1333 Jones St #802', '347 Hamilton St', '199 New Montgomery St #1311', '960 Market St #205', '960 Market St #314', '2631 - 2633 Leavenworth St', '32 Landers St', '1630 Hyde St', '171 Langton St', '201 Harrison St #912', '181 Fremont Unit 67C', '245 5th St #201', '840 Powell St #501', '55 Page St #411', '1451 Montgomery St #8', '2400 Green St', '219 Brannan St Unit 18D', '2601 Lyon St', '1701 Broadway St #3', '835 Douglass St', '555 Fulton St #214', '246 Casitas Ave', '1720 Clay St #1', '787 Arguello Blvd', '731 - 733 Capp St', '1471 48th Ave', '201 Folsom St Unit 12F', '2463 47th Ave', '888 7th St #120', '2646 16th Ave', '736 Excelsior Ave', '1652 Palou Ave', '38 Belcher St #3', '1320 Scott St Unit B', '1682 46th Ave', '1268 Lombard St #4', '10 Innes Ct #208', '566 South Van Ness Ave #5', '2444 Taraval St', '1645 Golden Gate Ave', '1719 Baker St', '219 Bocana St', '388 Townsend St #1', '260 King St #647', '1855 - 1857 Pine St', '4150 17th St #18', '195 Jersey St', '1840 Washington St #501', '66 Cleary Ct #105', '260 King St #575', '1150 Lombard St #24', '2701 Van Ness Ave #601', '3354 20th St #101', '1788 Clay St #205', '1000 Franklin St #403', '3519 21st St', '32 Prescott Ct', '20 North 25th Ave', '41 Delmar St', '7 Langton St', '137 Sickles Ave', '74 New Montgomery St #609', '425 1st St #3403', '207 Diamond Cove Ter', '481 36th Ave', '300 3rd St #503', '145 Santa Rosa Ave', '1310 Minnesota St #204', '166 Hearst Ave', '74 New Montgomery St #701', '1237 Chestnut St #4', '855 La Playa St #154', '199 New Montgomery St #604', '301 Mission St Unit 14B', '223 Theresa St', '2331 30th Ave', '1310 Minnesota St #302', '835 Alabama St', '1201 Sutter St #311', '74 New Montgomery St #412', '1201 Sutter St #303', '1811 Turk Blvd #101', '830 Cole St', '1491 21st Ave', '1716 Larkin St', '142 Jules Ave', '601 Van Ness Ave #825', '3966-8 18Th St', '115 Crown Ter', '1132 Pine St', '1735 Grove St', '520 Vicente St', '1777 Eucalyptus Dr', '45 Alton Ave', '44 San Antonio Pl', '212 Lexington St', '48 - 50 Divisadero St', '88 Townsend St #212', '68 Harriet St #14', '1888 20th Ave', '650 Turk St #402', '2539 18th Ave', '54 Caine Ave', '1566 34th Ave', '27 Ramona Ave', '3208 Pierce St #404', '95 Santa Cruz Ave', '361 11th Ave', '300 3rd St #302', '231 Topaz Way', '435 - 441 Powell St', '2977 24th St', '330 Flood Ave', '1443 Lombard St', '2480 Broadway St', '747 38th Ave', '17 Hodges Aly', '100 Duboce Ave #407', '553 Gates St', '644 Fillmore St', '435 China Basin St #442', '318 Scott St', '1834 Eddy St', '1345 Turk St #218', '196 Ocean Ave', '2206 Vallejo St', '958 Ingerson Ave', '10 Innes Ct #102', '2028 Leavenworth St', '1947 Palou Ave', '690 Market St #901', '1960 Broadway', '1310 Greenwich St #401', '2106 22nd Ave', '390 Somerset St', '336 Wilde Ave', '3230 Washington St', '1118 - 1120 Capitol Ave', '728 Page St', '262 Frederick St #5', '1456 Jefferson St', '1669 Grove St', '875 Francisco St', '3229 Broderick St', '246 2nd St #1404', '2337 Judah St', '225 9th St Unit C', '4027 23rd St', '787 Pacheco St', '1501 Filbert St Unit 4C', '1322 Vallejo St', '401 Harrison St Unit 11F', '3817 Folsom St', '3583 Sacramento St', '624 - A Guerrero St', '1825 Turk St #2', '320 30th Ave', '2363 Larkin St #31', '1225 - 1229 Rhode Island St', '115 Plymouth Ave Unit B', '745 27th Ave', '2655 Bush St #203', '483 Tehama St', '888 Union St', '197 Goethe St', '1125 - 1129 Clay St', '333 Main St Unit 6E', '115 Plymouth Ave Unit A', '1073 - 1077 South Van Ness Ave', '403 Main St #520', '1878 Bush St', '2811 Market St', '1876 Bush St', '350 Church St Unit J', '1354 46th Ave', '1236 Willard St', '1001 California St #7', '200 Darien Way', '3310 Mission St #4', '280 Spear St Unit 26A', '3326 California St #1', '5020 Mission St #4', '2130 Sutter St Unit B', '624 - 626 Castro St #626', '261 17th Ave', '1454 South Van Ness Ave', '1515 15th St #510', '950 Tennessee St #317', '1156 - 1158 Geneva Ave', '1473 Hudson Ave', '1415 San Bruno Ave Unit A', '1415 San Bruno Ave', '88 King St #124', '1583 Dolores St', '1457 Hudson Ave', '559 Texas St', '525 Gennessee St', '1355 35th Ave', '1927 - 1929 Taraval St', '2242 Judah St', '2240 Judah St', '225 Downey St', '708 Long Bridge St #306', '149 Albion St', '257 Montana St', '250 King St #264', '99 Rausch St #202', '324 Hyde St', '11 Imperial Ave', '1429 Sacramento St', '573 Donahue St', '170 Alpine Ter', '338 Spear St Unit 39E', '332 South Hill Blvd', '566 Athens St', '601 Van Ness Ave #141', '15 Lucerne St Unit B', '201 Harrison St #201', '150 Palm Ave #1', '1671 34th Ave', '125 Majestic Ave', '534 Dorado Ter', '1722 Larkin St', '2576 - 2578 Folsom St', '1587 15th St #403', '3410 Jackson St', '259 Clara St #202', '650 11th Ave', '3949 21St St', '586 Paris St', '4 Newell St Unit A', '4 Newell St', '1342 Fell St', '1320 Vallejo St', '750 Great Hwy #1', '3501 Lawton St', '197 Lower Ter', '425 1st St #4706', '1874 Quesada Ave', '473 Andover St']
#     for each_address in data:
#         for i in range(1,len(each_address)):
#             prefix = each_address[0:i]
#             print("prefix is", prefix)
#             x.zadd('autocomplete',{prefix:0})
#         x.zadd('autocomplete',{each_address+"%":0})

#     # Connect to Redis
#
# def address_insertion():
#     import redis
#     x  = redis.Redis(host="redis-15137.c257.us-east-1-3.ec2.cloud.redislabs.com", port=15137, password="HfQf7YcyrF2JOSuDlWnxsQbjqdMCJDzw", db = 0)
#     print(x.get("zz"))
#     data = ['26 Jennifer Pl', '152 Lombard St #507', '45 Ney St', '1 Hawthorne St Unit 15B', '250 King St #812', '1075 Market St #211', '167 Delano Ave', '1175 Pine St', '25 - 27 Blanken Ave', '1298 Treat Ave', '48 Terra Vista Ave Unit D', '39 Forest View Dr', '250 King St #704', '1201 California St #602', '230 Irving St', '1688 Pine St Unit W205', '2880 Green St', '1288 Howard St #315', '1400 Lake St', '22 Fairfield Way', '774 Potrero Ave', '4145 Ulloa St', '53 Harrington St', '24 - 34 Jasper Pl', '1163 - 1169 Alabama St Unit 1163A', '1219 York St', '2070 Bush St', '1745 Market St', '425 Hyde St', '715 Moultrie St', '2846 Sacramento St', '104 Collins St', '33 Rice St', '77 Jordan Ave', '999 Green St #2905', '766 Harrison St #706', '47 Richland Ave', '2925 California St #3', '219 Brannan St Unit 4J', '909 Divisadero St', '3319 Divisadero St', '430 Arch St', '92 Putnam St', '3301 - 3311 Cesar Chavez St Unit 3309A', '280 Spear St Unit 34C', '75 Navajo Ave', '786 Minna St #9', '1238 Sutter St #702', '883 39th Ave', '1590 Funston Ave', '349 - 351 Mississippi St', '1592 Funston Ave', '47 Arroyo Way', '3969 - 3971 Cesar Chavez St', '3 Topaz Way', '124 Lily St', '188 Minna St Unit 37B', '601 4th St #206', '400 Beale St #2104', '1165 - 1167 Kearny St', '1170 Prague St', '260 King St #553', '932 Silliman St', '1210 Stanyan St', '416 Peninsula Ave', '1374 18th Ave', '72 Dawnview Way', '80 JENNINGS Ct', '170 Highland Ave', '3227 - 3229 Broderick St', '160 Gardenside Dr #401', '4641 Lincoln Way', '298 Portola Dr #204', '1315 Laguna St #4', '142 Russ St #4', '2379 47th Ave', '719 Larkin St #506', '225 Bay St #203', '1809 Gough St #101', '55 Elgin Park', '601 Van Ness Ave #40', '174 Langton St Unit B', '171 San Marcos Ave', '719 Brunswick St', '601 Ortega St', '631 Folsom St Unit 11E', '2200 Sacramento St #805', '527 - 529 Birch St', '243 Paris St', '1604 Church St #1', '2037 Revere Ave', '1258 - 1260 Chestnut St', '52 - 56 Langton St', '1043 Plymouth Ave', '1001 California St #4', '2666 18th Ave', '618 Lisbon St', '188 Minna St Unit 32C', '2865 Clay St #3', '381 Turk St', '488 Folsom St #4204', '135 8th St', '247 - 249 Edna St', '763 45th Ave', '24 Page St #3', '564 Chenery St', '1363 Sanchez St', '355 Moscow St', '286 Maynard St', '4527 Lincoln Way', '1333 Jones St #802', '347 Hamilton St', '199 New Montgomery St #1311', '960 Market St #205', '960 Market St #314', '2631 - 2633 Leavenworth St', '32 Landers St', '1630 Hyde St', '171 Langton St', '201 Harrison St #912', '181 Fremont Unit 67C', '245 5th St #201', '840 Powell St #501', '55 Page St #411', '1451 Montgomery St #8', '2400 Green St', '219 Brannan St Unit 18D', '2601 Lyon St', '1701 Broadway St #3', '835 Douglass St', '555 Fulton St #214', '246 Casitas Ave', '1720 Clay St #1', '787 Arguello Blvd', '731 - 733 Capp St', '1471 48th Ave', '201 Folsom St Unit 12F', '2463 47th Ave', '888 7th St #120', '2646 16th Ave', '736 Excelsior Ave', '1652 Palou Ave', '38 Belcher St #3', '1320 Scott St Unit B', '1682 46th Ave', '1268 Lombard St #4', '10 Innes Ct #208', '566 South Van Ness Ave #5', '2444 Taraval St', '1645 Golden Gate Ave', '1719 Baker St', '219 Bocana St', '388 Townsend St #1', '260 King St #647', '1855 - 1857 Pine St', '4150 17th St #18', '195 Jersey St', '1840 Washington St #501', '66 Cleary Ct #105', '260 King St #575', '1150 Lombard St #24', '2701 Van Ness Ave #601', '3354 20th St #101', '1788 Clay St #205', '1000 Franklin St #403', '3519 21st St', '32 Prescott Ct', '20 North 25th Ave', '41 Delmar St', '7 Langton St', '137 Sickles Ave', '74 New Montgomery St #609', '425 1st St #3403', '207 Diamond Cove Ter', '481 36th Ave', '300 3rd St #503', '145 Santa Rosa Ave', '1310 Minnesota St #204', '166 Hearst Ave', '74 New Montgomery St #701', '1237 Chestnut St #4', '855 La Playa St #154', '199 New Montgomery St #604', '301 Mission St Unit 14B', '223 Theresa St', '2331 30th Ave', '1310 Minnesota St #302', '835 Alabama St', '1201 Sutter St #311', '74 New Montgomery St #412', '1201 Sutter St #303', '1811 Turk Blvd #101', '830 Cole St', '1491 21st Ave', '1716 Larkin St', '142 Jules Ave', '601 Van Ness Ave #825', '3966-8 18Th St', '115 Crown Ter', '1132 Pine St', '1735 Grove St', '520 Vicente St', '1777 Eucalyptus Dr', '45 Alton Ave', '44 San Antonio Pl', '212 Lexington St', '48 - 50 Divisadero St', '88 Townsend St #212', '68 Harriet St #14', '1888 20th Ave', '650 Turk St #402', '2539 18th Ave', '54 Caine Ave', '1566 34th Ave', '27 Ramona Ave', '3208 Pierce St #404', '95 Santa Cruz Ave', '361 11th Ave', '300 3rd St #302', '231 Topaz Way', '435 - 441 Powell St', '2977 24th St', '330 Flood Ave', '1443 Lombard St', '2480 Broadway St', '747 38th Ave', '17 Hodges Aly', '100 Duboce Ave #407', '553 Gates St', '644 Fillmore St', '435 China Basin St #442', '318 Scott St', '1834 Eddy St', '1345 Turk St #218', '196 Ocean Ave', '2206 Vallejo St', '958 Ingerson Ave', '10 Innes Ct #102', '2028 Leavenworth St', '1947 Palou Ave', '690 Market St #901', '1960 Broadway', '1310 Greenwich St #401', '2106 22nd Ave', '390 Somerset St', '336 Wilde Ave', '3230 Washington St', '1118 - 1120 Capitol Ave', '728 Page St', '262 Frederick St #5', '1456 Jefferson St', '1669 Grove St', '875 Francisco St', '3229 Broderick St', '246 2nd St #1404', '2337 Judah St', '225 9th St Unit C', '4027 23rd St', '787 Pacheco St', '1501 Filbert St Unit 4C', '1322 Vallejo St', '401 Harrison St Unit 11F', '3817 Folsom St', '3583 Sacramento St', '624 - A Guerrero St', '1825 Turk St #2', '320 30th Ave', '2363 Larkin St #31', '1225 - 1229 Rhode Island St', '115 Plymouth Ave Unit B', '745 27th Ave', '2655 Bush St #203', '483 Tehama St', '888 Union St', '197 Goethe St', '1125 - 1129 Clay St', '333 Main St Unit 6E', '115 Plymouth Ave Unit A', '1073 - 1077 South Van Ness Ave', '403 Main St #520', '1878 Bush St', '2811 Market St', '1876 Bush St', '350 Church St Unit J', '1354 46th Ave', '1236 Willard St', '1001 California St #7', '200 Darien Way', '3310 Mission St #4', '280 Spear St Unit 26A', '3326 California St #1', '5020 Mission St #4', '2130 Sutter St Unit B', '624 - 626 Castro St #626', '261 17th Ave', '1454 South Van Ness Ave', '1515 15th St #510', '950 Tennessee St #317', '1156 - 1158 Geneva Ave', '1473 Hudson Ave', '1415 San Bruno Ave Unit A', '1415 San Bruno Ave', '88 King St #124', '1583 Dolores St', '1457 Hudson Ave', '559 Texas St', '525 Gennessee St', '1355 35th Ave', '1927 - 1929 Taraval St', '2242 Judah St', '2240 Judah St', '225 Downey St', '708 Long Bridge St #306', '149 Albion St', '257 Montana St', '250 King St #264', '99 Rausch St #202', '324 Hyde St', '11 Imperial Ave', '1429 Sacramento St', '573 Donahue St', '170 Alpine Ter', '338 Spear St Unit 39E', '332 South Hill Blvd', '566 Athens St', '601 Van Ness Ave #141', '15 Lucerne St Unit B', '201 Harrison St #201', '150 Palm Ave #1', '1671 34th Ave', '125 Majestic Ave', '534 Dorado Ter', '1722 Larkin St', '2576 - 2578 Folsom St', '1587 15th St #403', '3410 Jackson St', '259 Clara St #202', '650 11th Ave', '3949 21St St', '586 Paris St', '4 Newell St Unit A', '4 Newell St', '1342 Fell St', '1320 Vallejo St', '750 Great Hwy #1', '3501 Lawton St', '197 Lower Ter', '425 1st St #4706', '1874 Quesada Ave', '473 Andover St']
#     address_data = []
#     with open('../dataset.csv', 'r') as csvfile:
#         csv_reader = csv.DictReader(csvfile)
#         for row in csv_reader:
#             # Get the key from the desired column
#             key = row['CITY']
#             price = row['PRICE']
#             add = row['ADDRESS']
#             zip = row['ZIP OR POSTAL CODE']
#             url = row['URL']
#             address_data.append(row['CITY'])
#             address_data.append(row['URL'])
#             address_data.append(row['ZIP OR POSTAL CODE'])
#             address_data.append(row['ADDRESS'])
#             address_data.append(row['PRICE'])
#             print(add,address_data)
#             x.set(add,json.dumps(address_data))
#             address_data = []
#
#
#     # for each_address in data:
#     #         print("prefix is", prefix)
#     #         x.zadd(each_address,{prefix:0})
#     #     x.zadd('autocomplete',{each_address+"%":0})

#     # Open CSV file and read data

# def complete(r, prefix, count):
#     results = []
#     grab = 50
#     start = r.zrank('autocomplete', prefix)
#     print(start)
#     if not start:
#         return []
#     while (len(results) != count):
#         rang = r.zrange('autocomplete', start, start + grab - 1)
#         start += grab
#         if not rang or len(rang) == 0:
#             break
#         range = [addr.decode() for addr in rang]
#         for entry in range:
#
#             minlen = min(len(entry), len(prefix))
#
#             if entry[0:minlen] != prefix[0:minlen]:
#                 print("here")
#                 print(minlen)
#                 print(prefix)
#                 print("entry", entry)
#                 count = len(results)
#                 break
#             if entry[-1] == "%" and len(results) != count:
#                 results.append(entry[0:-1])
#
#     print("res",results)
#     return results

# def dynamic_fetch(r, prefix, pattern):
#     results = []
#     grab = 50
#     start = r.zrank('autocomplete', prefix)
#     print(start)
#     start = r.zrange('autocomplete', 0, -1)
#     if not start:
#         return []
#
#     matching_elements = r.zrangebylex('autocomplete', min="[" + prefix, max="(" + prefix + "\xff")
#     # matching_elements = r.zrangebylex('autocomplete', min="["+prefix, max="("+prefix+"\xff")
#     print(matching_elements)
#     filtered_elements = [elem.decode() for elem in matching_elements if not elem.endswith(b'%')]
#     print(filtered_elements)
#     # while (len(results) != count):
#     #     rang = r.zrange('autocomplete', start, start + grab - 1)
#     #     start += grab
#     #     if not rang or len(rang) == 0:
#     #         break
#     #     range = [addr.decode() for addr in rang]
#     #     for entry in range:
#     #
#     #         minlen = min(len(entry), len(prefix))
#     #
#     #         if entry[0:minlen] != prefix[0:minlen]:
#     #             print("here")
#     #             print(minlen)
#     #             print(prefix)
#     #             print("entry", entry)
#     #             count = len(results)
#     #             break
#     #         if entry[-1] == "%" and len(results) != count:
#     #             results.append(entry[0:-1])
#     #
#     # print("res",results)
#     return results


def autoComplete():
    r = redis.Redis(host="redis-15137.c257.us-east-1-3.ec2.cloud.redislabs.com", port=15137,
                    password="HfQf7YcyrF2JOSuDlWnxsQbjqdMCJDzw", db=0)
    print(r.keys())
    # print(complete(r, "260", 8))


    # print(slow_complete(r, "1", 8))


if __name__ == "__main__":
    pass
    # address_insertion()
    # autoComplete()

# if __name__=="__main__":
#     start_redis()
#
