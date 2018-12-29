import itertools
import numpy as np

class Sudoku:
  def __init__(self,sudokustring):
    self.sudoku = sudokustring

  def allprobes(self):
    '''Create an array of all possible permutations of a sudoku row.'''
    allprobes=[]
    for probe in itertools.permutations('123456789'):
      allprobes.append(np.array([int(x) for x in probe]))
    allprobes=np.array(allprobes)
    return np.array(allprobes)

  def parse(self):
    '''Convert sudoku string to an array.'''
    self.array=np.array([[[int(x) for x in list(self.sudoku)][i:i+9] for i in map(lambda x:9*x, range(9))]])

  def probe(self,array,rownum):
    '''Find all the valid permutations of a row (probes) in a sudoku. Return all possible outcomes in sudoku arrays.'''
    sudokuarray=array
    rowprobes,sudokuprobes=[],[]
    starti={0:0,1:0,2:0,3:3,4:3,5:3,6:6,7:6,8:6}
    endi={0:3,1:3,2:3,3:6,4:6,5:6,6:9,7:9,8:9}
    for probe in self.allprobes():
      if all(probe[i] == sudokuarray[rownum,i] for i in range(9) if sudokuarray[rownum,i] != 0):
        if all(probe[i] not in sudokuarray[:,i] for i in range(9) if sudokuarray[rownum,i] == 0) and all(probe[i] not in sudokuarray[starti[rownum]:endi[rownum],starti[i]:endi[i]] for i in range(9) if sudokuarray[rownum,i] == 0):
          rowprobes.append(probe)
    rowprobes=np.array(rowprobes)
    if rowprobes.size != 0:
      for i in range(len(rowprobes)):
        sudokuprobes.append(sudokuarray)
      sudokuprobes=np.array(sudokuprobes)
      for i in range(len(sudokuprobes)):
        sudokuprobes[i][rownum]=rowprobes[i]
    return sudokuprobes

  def ler(self):
    '''Find the least empty row.'''
    zerodict={}
    for rownum in range(len(self.array[0])):
      zeros=0
      for i in self.array[0][rownum]:
        if i == 0:
          zeros+=1
      zerodict[rownum]=zeros
    return min(zerodict,key=zerodict.get)


  def solve(self,array,i):
    '''Loop self.probe() for each row. Only the valid outcomes will be passed into the next recursion.'''
    if i < 9 and i >= 0:
      sol=[]
      solution = [n for n in map(lambda x: self.probe(x,i),array)]
      for j in solution:
        if j is not None:
          for k in j:
            sol.append(k)
      sol=np.array(sol)
      i+=1
      return self.solve(sol,i)
    else:
      return array



sudoku='004782010801005300029003000008900060206000904030006500000600450005800203080357100'

a=Sudoku(sudoku)
a.parse()
print(a.array[0]+'\n')
print(a.solve(a.array,0))

