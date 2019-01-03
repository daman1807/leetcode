// https://leetcode.com/problems/unique-paths/submissions/
object Solution {
  def uniquePaths(m: Int, n: Int): Int = {
    if (m <= 0 || n <= 0) {
      return 0
    }
    var cache: Map[String, Int] = Map()
    def move(i: Int, j: Int): Int = {
      val key: String = List(i, j, m, n).mkString("-")
      if (cache.contains(key)) cache(key)
      else {
        var res = 0
        if (i >= m - 1 || j >= n - 1) res = 1
        else res = move(i + 1, j) + move(i, j + 1)
        cache += key -> res
        res
      }
    }
    move(0, 0)
  }
}
