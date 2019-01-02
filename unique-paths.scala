// https://leetcode.com/problems/unique-paths
object Solution {
  def uniquePaths(m: Int, n: Int): Int = {
    if (m <= 0 || n <= 0) {
      return 0
    }
    val matrix = Array.fill[Int](m + 1)(0)
    for (j <- 0 until n; i <- 1 to m) {
      if (j == 0 && i == 1) {
        matrix(i) = 1
      } else {
        matrix(i) = matrix(i - 1) + matrix(i)
      }
    }
    return matrix(m)
  }
}

