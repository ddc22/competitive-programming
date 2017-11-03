
def get_word_map(word_array):
    dict = {}
    for magW in word_array:
        if dict.get(magW) == None:
            dict[magW] = 0
        dict[magW] += 1
    return dict

def ransom_note(magazine, ransom):
    mag_map = get_word_map(magazine)
    ran_map = get_word_map(ransom)
    for word in ran_map:
        if mag_map.get(word) == None or mag_map[word] < ran_map[word]:
            return False
    return True


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print "Yes"
else:
    print "No"

