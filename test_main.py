import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_sequence(self) :
        for i in range(1,5) : 
            inseq = i*[0]
            for j in range(i) : inseq[j] = j 
            fullseq = allseq( inseq, i+1 )
            self.assertTrue( len(fullseq)==i+1 )
            for seq in fullseq : self.assertTrue( len(seq)==i+, "your code is not generating all the lists it should" )
  
            for j in range(i) :
                newseq = i*[0] 
                newseq[j] = i+1
                for k in range(i-1) : 
                    if k>=j : newseq[k+1] = inseq[k] 
                    else : newseq[k] = inseq[k]
                found=False
                for seq in fullseq : 
                    isseq=True 
                    for k in range(len(seq)) : 
                        if seq[k]!=seq[k] : isseq=False
                    if isseq : found=True
                self.assertTrue( found, "your code is not generating all the lists it should" )
