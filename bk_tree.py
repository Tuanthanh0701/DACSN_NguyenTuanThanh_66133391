from edit_distance import levenshtein_distance


class BKNode:
    def __init__(self, word):
        self.word = word
        self.children = {}  # key: khoảng cách Levenshtein (int), value: BKNode


class BKTree:
    def __init__(self, distance_func=levenshtein_distance):
        self.root = None
        self.distance_func = distance_func
        self.call_count = 0  # Biến đếm số lần gọi hàm tính khoảng cách

    def insert(self, word):
        if self.root is None:
            self.root = BKNode(word)
            return

        curr = self.root
        while True:
            dist = self.distance_func(word, curr.word)
            if dist == 0:
                return  # Từ đã tồn tại trong cây
            if dist in curr.children:
                curr = curr.children[dist]
            else:
                curr.children[dist] = BKNode(word)
                break

    def build_from_list(self, words):
        for w in words:
            self.insert(w)

    def search(self, query, max_dist):
        """
        Tìm tất cả các từ trong cây có khoảng cách <= max_dist so với query.
        Trả về: (danh_sach_ket_qua, so_lan_goi_ham_khoang_cach)
        """
        self.call_count = 0
        results = []
        if self.root is None:
            return results, self.call_count

        stack = [self.root]
        while stack:
            node = stack.pop()
            self.call_count += 1
            dist = self.distance_func(query, node.word)

            if dist <= max_dist:
                results.append((node.word, dist))

            # Cắt tỉa nhánh theo bất đẳng thức tam giác: [dist - k, dist + k]
            low = dist - max_dist
            high = dist + max_dist
            for edge_dist, child in node.children.items():
                if low <= edge_dist <= high:
                    stack.append(child)

        # Sắp xếp kết quả theo khoảng cách tăng dần, sau đó theo bảng chữ cái
        results.sort(key=lambda x: (x[1], x[0]))
        return results, self.call_count
