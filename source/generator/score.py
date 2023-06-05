import random

# Hàm random điểm (theo thang 0-10) dựa trên phân phối chuẩn
def get_score(num_results): # num_results = số lượng điểm cho mỗi học sinh
    mean = 6.5 # Trung vị = 6.5 (mức điểm trung bình)
    std_dev = 1.5 # Độ lệch chuẩn 1.5 (để phổ điểm lệch phải)
    # Lấy giá trị điểm và làm tròn 2 chữ số
    scores = [round(random.normalvariate(mean, std_dev), 2) for _ in range(num_results)]

    if num_results >= 1:
        for i in range(1, num_results):
            # Nếu học sinh đó có nhiều hơn 1 kết quả thì các điểm sau đó sẽ nằm trong khoảng [-2;2]
            # (Cho giống thực tế :v)
            adjustment = random.uniform(-2, 2)
            scores[i] = round(scores[i-1] + adjustment, 2)
            scores[i] = max(0, min(10, scores[i])) # Nếu điểm vượt quá 0 hoặc 10 thì thành 0 hoặc 10
    else:
        scores = [max(0, min(10, score)) for score in scores]

    return scores


