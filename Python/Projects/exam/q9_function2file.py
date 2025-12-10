#354

#1, 2, 3, 4
with open('files/scores.csv', encoding='utf-8') as fi:
    contents = fi.read()
    
    score = {}
    subjects = []
    save_data = "이름, 총점, 평균" + "\n"

    is_header = True
    for line in contents.split('\n'):
        if line == "":
            break

        data = [s.strip() for s in line.split(',')]
        
        if is_header:
            # key 생성
            for i in range(len(data)):
                score[data[i]] = []
                subjects.append(data[i])

            is_header = False
            continue
        
        # score 정리
        for i in range(len(data)):
            if data[i].isdigit():
                score[subjects[i]].append(int(data[i]))
            else:
                score[subjects[i]].append(data[i])

        # 저장 데이터 정리 ｢이름 총점 평균｣
        save_data = save_data + data[0] + ","
        save_data = save_data + str(sum(int(total) for total in data if total.isdigit())) + ","
        save_data = save_data + str(sum(int(total) for total in data if total.isdigit()) / len([total for total in data if total.isdigit()])) + "\n"


    for subj in subjects:
        if subj == '이름':
            continue

        val = score[subj]

        print("{} - 평균: {}, 최고점 : {}, 최저점 : {}".format(subj, sum(val) / len(val), max(val), min(val)))


    with open('files/result.csv', 'w', encoding='utf-8') as fi_save:
        fi_save.write(save_data)