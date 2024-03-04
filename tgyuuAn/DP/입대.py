import sys

remain_days, need_score = map(int,sys.stdin.readline().split())
volunteer_scores = [0]
volunteer_scores.extend(list(map(int,sys.stdin.readline().split())))

blood_donation_score, blood_donation_break_time = map(int,sys.stdin.readline().split())

volunteer_scores.extend([0 for _ in range(blood_donation_break_time-1)])
maximum_blood_donation_count = (len(volunteer_scores)+blood_donation_break_time-1)//blood_donation_break_time+1

dp_table = [[0 for _ in range(maximum_blood_donation_count)] for _ in range(len(volunteer_scores))]

for date in range(len(volunteer_scores)):
    if date >= blood_donation_break_time:
        for blood_donation_count in range(1,maximum_blood_donation_count):
            dp_table[date][blood_donation_count] = max(dp_table[date][blood_donation_count],
                                                       dp_table[date-1][blood_donation_count] + volunteer_scores[date],
                                                       dp_table[date-blood_donation_break_time][blood_donation_count-1] + blood_donation_score)

    dp_table[date][0] = dp_table[date-1][0] + volunteer_scores[date]

print(dp_table)

for count in range(len(dp_table[-1])):
    if dp_table[-1][count] >= need_score:
        print(count)
        break

else: print(-1)