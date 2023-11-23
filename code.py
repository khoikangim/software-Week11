
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 시드 설정
np.random.seed(0)

# 데이터 생성
data = np.random.randn(100, 2)
a = data[:, 0]
b = data[:, 1]

# 그래픽 초기화
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 첫 번째 그래프: 평균과 중앙값의 막대 그래프
axes[0, 0].bar(['Mean', 'Median'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='Variable 1')
axes[0, 0].bar(['Mean', 'Median'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='Variable 2')
axes[0, 0].legend()
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# 두 번째 그래프: 상관관계 히트맵
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1], cmap='coolwarm')
axes[0, 1].set_title('Correlation Analysis')

# 세 번째 그래프: 히스토그램
sns.histplot(a, bins=15, color='blue', alpha=0.7, kde=True, label='Variable 1', ax=axes[1, 0])
sns.histplot(b, bins=15, color='green', alpha=0.7, kde=True, label='Variable 2', ax=axes[1, 0])
axes[1, 0].legend()
axes[1, 0].set_title('Histogram of Variables')

# 네 번째 그래프: 산점도
sns.scatterplot(x=a, y=b, alpha=0.7, ax=axes[1, 1])
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

# 그래프 간격 조정 및 표시
plt.tight_layout()
plt.show()

