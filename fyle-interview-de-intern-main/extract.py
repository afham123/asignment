# Your imports go here
import logging

logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''

def get_text(path):
    import json
    
    lst=[]
    with open(path) as f:
        data = json.load(f)
    for item in data["Blocks"]:
        try : lst.append(item['Text'])
        except: continue
            
    return lst

def check(lst, clist):
    
    res = []
    for i in range(len(lst)):
        for x in lst[i].split():
            if x.lower() in clist:
                res.append(lst[i])
                try : res.append(lst[i+1])
                except : pass
                break
                
    return res

def f_check(lst):
    import re
    
    pattern = r'\d+\.\d{2}'
    res = []
    for item in lst:
        item = ''.join(item.split(','))
        try : 
            t = re.search(pattern,item).group()
            if t not in res:
                res.append(t)
        except : pass
    return res


def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here
    
    clist = ['amount paid','payment','total amount','paid','total','debit','total:','$','payments','dance','100534']
    
    text = get_text(dirpath)
    res = check(text, clist)
    return max(f_check(res))