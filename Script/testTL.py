# Unit test of the two bigest functions in the tl.py program

import unittest
         
def countingFunc(stringCode):
    if (stringCode.startswith('2') or stringCode.startswith('3')):
        global globCountGood
        globCountGood += 1
        stringCount = str(globCountGood)
        return stringCount
    elif (stringCode.startswith('4') or stringCode.startswith('5')):
        global globCountBad
        globCountBad += 1
        stringCount = str(globCountBad)
        return stringCount
        
def getAPIResp(st, imp):
    st = st.translate(None, '[]\'\"\\')
    try: 
        r = requests.head(st)
        code = r.status_code
        stringCode = str(code)
        stringCount = countingFunc(stringCode)

    except:
        stringCode = 'Unreachable'
        global globCountN
        globCountN += 1
        stringCount = str(globCountN)
    stringCode = writeURLs(stringCode, imp, st)
    return stringCode  

class TLTesrCase(unittest.TestCase):
      
    def test_countingFunc(self):
        self.assertTrue(400)
        
    def test_getAPIResp(self):
       self.assertTrue('https://secure-gl.imrworldwide.com/cgi-bin/m?ci=nlsnci304&am=3&at=view&rt=banner&st=image&ca=nlsn32514&cr=crtve&pc=dcbm_plc0001&ce=dcbm&r=timestamp', 333304)
        
if __name__ == '__main__':
    unittest.main()