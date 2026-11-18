
# Nhóm các ký tự tiếng Việt dễ gõ nhầm (cùng gốc nguyên âm/thanh điệu hoặc phụ âm gần giống)
SIMILAR_GROUPS = [
    set("aăâáàảãạắằẳẵặấầẩẫậ"),
    set("eêéèẻẽẹếềểễệ"),
    set("iíìỉĩị"),
    set("oôơóòỏõọốồổỗộớờởỡợ"),
    set("uưúùủũụứừửữự"),
    set("yýỳỷỹỵ"),
    set("dđ"),
    set("sx"),
    set("ln")
]

def char_cost(c1: str, c2: str, weighted: bool = False) -> float:
    """Tính chi phí thay thế giữa 2 ký tự."""
    if c1 == c2:
        return 0.0
    if weighted:
        for group in SIMILAR_GROUPS:
            if c1 in group and c2 in group:
                return 0.5
    return 1.0

def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Tính khoảng cách Levenshtein chuẩn bằng Quy hoạch động (ma trận (m+1) x (n+1)).
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo điều kiện biên
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Điền bảng quy hoạch động
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,          # Xóa (Deletion)
                dp[i][j - 1] + 1,          # Chèn (Insertion)
                dp[i - 1][j - 1] + cost    # Thay thế (Substitution)
            )
    return dp[m][n]

def weighted_damerau_levenshtein(s1: str, s2: str) -> float:
    """
    Mở rộng Damerau-Levenshtein (có phép hoán vị 2 ký tự liền kề và trọng số tiếng Việt).
    """
    m, n = len(s1), len(s2)
    dp = [[0.0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = float(i)
    for j in range(n + 1):
        dp[0][j] = float(j)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = char_cost(s1[i - 1], s2[j - 1], weighted=True)
            dp[i][j] = min(
                dp[i - 1][j] + 1.0,
                dp[i][j - 1] + 1.0,
                dp[i - 1][j - 1] + cost
            )
            # Kiểm tra điều kiện hoán vị 2 ký tự liền kề
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 0.5)

    return dp[m][n]
