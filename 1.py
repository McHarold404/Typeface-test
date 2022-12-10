import cv2 as cv
import numpy as np
import sys

imgFile = input()

img = cv.imread(imgFile, cv.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3), np.uint8)
img = cv.erode(img, kernel)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
m = img.shape[0]
n = img.shape[1]
minI = m + 1
minJ = n + 1
maxI = -1
maxJ = -1
vis = [[0 for _ in range(m)] for _ in range(n)]
sys.setrecursionlimit(1000000)


def dfs(i, j, arr):
    vis[i][j] = 1
    arr[0] = min(arr[0], i)
    arr[1] = min(arr[1], j)
    arr[2] = max(arr[2], i)
    arr[3] = max(arr[3], j)
    for itr in range(4):
        ni = i + di[itr]
        nj = j + dj[itr]
        if ni < 0 or nj >= m:
            continue
        if nj < 0 or nj >= m:
            continue
        if img[ni][nj] == 0:
            continue
        if vis[ni][nj] == 1:
            continue
        dfs(ni, nj, arr)


for i in range(m):
    for j in range(n):
        if img[i][j] == 1 and vis[i][j] == 0:
            arr = [m + 1, n + 1, -1, -1]
            dfs(i, j, arr)
            print(
                (arr[0] + arr[2]) // 2,
                (arr[1] + arr[3]) // 2,
                arr[2] - arr[0],
                arr[3] - arr[1],
            )
