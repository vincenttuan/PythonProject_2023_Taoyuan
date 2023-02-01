# 請計算這五科的總分
scores = "100,90,80,70,60"
score = scores.split(",")
print(score, len(score), type(score))
print(score[0], type(score[0]))
print(score[1], type(score[1]))
print(score[2], type(score[2]))
print(score[3], type(score[3]))
print(score[4], type(score[4]))
total = int(score[0]) + int(score[1]) + int(score[2]) + int(score[3]) + int(score[4])
print(total)
print(sum(int(x) for x in score))
