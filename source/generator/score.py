import random
import numpy as np
import matplotlib.pyplot as plt
# Hàm random điểm (theo thang 0-10) dựa trên phân phối chuẩn

def visualize_score(num_schools, num_students):
    # Phổ điểm của học sinh được tạo theo phân phối chuẩn dưới đây

    mean = 6.5  # Trung vị
    std_dev = 1.5  # Độ lệch chuẩn

    x = np.linspace(0, 10, 100)
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-(x - mean) ** 2 / (2 * std_dev ** 2))
    y = y * num_students * num_schools

    plt.plot(x, y, color='blue', linewidth=2)
    plt.xlabel('Điểm')
    plt.ylabel('Số học sinh')
    plt.title('Phổ điểm học sinh trung học')

    plt.show()
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

#visualize_score()
