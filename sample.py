def groupAnagrams(strs):
    res = {}

    for i in strs:
        count = [0]*26

        for j in i:
            count[ord(j) -ord('a')] +=1

        # print(count)
        key = tuple(count)
        print(res[key])

        if key in res:
            res[key].append(i)
        else:
            res[key] = [i]
        
    # print(res)
    return list(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]
res = groupAnagrams(strs)
print(res)