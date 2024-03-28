def solution(friends, gifts):
    i, j, k, l = 0, 0, 0, 0

    friend_dic = {}

    for i in range(len(friends)):
        friend_dic[friends[i]] = i

    #선물 데이터 테이블 크기 정하기
    present_data = [[0 for j in range(len(friends))] for j in range(len(friends))]

    #선물 데이터 테이블 채우기    
    for j in range(len(gifts)):
        giveName, takeName = gifts[j].split(" ")
        present_tempList = []
        present_tempList.append(giveName)
        present_tempList.append(takeName)

        present_data[friend_dic[giveName]][friend_dic[takeName]] += 1

    #받을 선물 데이터 리스트
    result_data = [0 for k in range(len(friends))]

    #선물 지수 데이터 리스트
    present_point = [[0 for k in range(3)] for k in range(len(friends))]
    for k in range(len(friends)):
        give_total = 0
        take_total = 0
        for l in range(len(friends)):
            give_total += present_data[k][l]
            take_total += present_data[l][k]
        present_point[k][0] = give_total
        present_point[k][1] = take_total
        if (k == 3):
            i = 0
            for i in range(len(friends)):
                present_point[i][2] = present_point[i][0] - present_point[i][1]


    k_start = 0
    l_start = 1
    for k in range(k_start, len(friends)):
        for l in range(l_start, len(friends)):
            if present_data[k][l] > present_data[l][k]:
                result_data[k] += 1
            elif present_data[k][l] < present_data[l][k]:
                result_data[l] += 1
            elif present_data[k][l] == present_data[l][k]:
                if present_point[k][2] > present_point[l][2]:
                    result_data[k] += 1
                elif present_point[k][2] < present_point[l][2]:
                    result_data[l] += 1
                else:
                    continue
        l_start += 1
    answer = max(result_data)
    
    return answer
