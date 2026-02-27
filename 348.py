class TicTacToe(object):
  def __init__(self, n):
    self.rows = [0] * n
    self.cols = [0] * n
    self.diag = self.antiDiag = 0
    self.n = n

  def move(self,row, col, player):
      delta = 3 - player * 2
      self.rows[row] += delta
      self.cols[col] += delta
      self.diag += (row == col and delta)
      self.antiDiag += (row + col == self.n - 1 and delta)
      if delta * self.n in [self.rows[row], self.cols[col], self.diag, self.antiDiag]: return player
      return 0