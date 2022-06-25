from typing import List
# https://leetcode.com/problems/flood-fill/


class Solution:
    def dfs_fill(self, image, sr, sc, initial, color):
        if 0 > sr or sr >= len(image) or 0 > sc or sc >= len(image[0]) or image[sr][sc] != initial:
            return

        image[sr][sc] = color
        self.dfs_fill(image, sr + 1, sc, initial, color)
        self.dfs_fill(image, sr - 1, sc, initial, color)
        self.dfs_fill(image, sr, sc + 1, initial, color)
        self.dfs_fill(image, sr, sc - 1, initial, color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image is None or image[sr][sc] == color:
            return image

        self.dfs_fill(image, sr, sc, image[sr][sc], color)
        return image