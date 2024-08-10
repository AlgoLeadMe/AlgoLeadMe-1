genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
answer = []

dic = {}
info = {}

for i in range(len(genres)):
    g = genres[i]
    p = plays[i]

    info[i] = g
    
    if g in dic:
        dic[g] += p
    else:
        dic[g] = p

best_g = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for g, _ in best_g:
    best_album = [(plays[i], i) for i in range(len(genres)) if genres[i] == g]
    for i in range(len(best_album)):
        for j in range(i+1, len(best_album)):
            if best_album[j][0] > best_album[i][0]: #재생수가 작은 경우
                best_album[i], best_album[j] = best_album[j], best_album[i]
            elif best_album[j][0] == best_album[i][0] and best_album[j][1] < best_album[i][1]: #idx가 작은 경우
                best_album[i], best_album[j] = best_album[j], best_album[i]
    
    answer.extend([x[1] for x in best_album[:2]])


print(answer)