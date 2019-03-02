messages = ['11223344@John@211$$$$', 'aabbcc@Mary@56800$0929222211', 'hualianndhu@Peter@999$1000111000']
pos_nstr = [messages[0].find('@'), messages[1].find('@'), messages[2].find('@')]
pos_nend = [messages[0].find('@', pos_nstr[0]+1), messages[1].find('@', pos_nstr[1]+1), messages[2].find('@', pos_nstr[2]+1)]
pos_mony = [messages[0].find('$', pos_nend[0]+1), messages[1].find('$', pos_nend[1]+1), messages[2].find('$', pos_nend[2]+1)]

name = [messages[0][pos_nstr[0]+1:pos_nend[0]], messages[1][pos_nstr[1]+1:pos_nend[1]], messages[2][pos_nstr[2]+1:pos_nend[2]]]
money = [int(messages[0][pos_nend[0]+1:pos_mony[0]]), int(messages[1][pos_nend[1]+1:pos_mony[1]]), int(messages[2][pos_nend[2]+1:pos_mony[2]])]
print (name[0], ':', money[0], sep='')
print (name[1], ':', money[1], sep='')
print (name[2], ':', money[2], sep='')

total = sum(money)
print ('TOTAL:',total, sep='') 
maxmony = max(money)
max_index = money.index(maxmony)
print('MAX:',name[max_index], sep='')
