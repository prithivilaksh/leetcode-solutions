class Solution:
    def isNumber(self, s: str) -> bool:
        # observation/idea:
        #     1) valid atomic values -> 0-9, ., e, +-, 
        #     2) possible transitions:
        #         empty -> . -> can be decimal
        #         empty -> 0-9 -> integer
        #         empty -> -+ -> symbol
        #         symbol -> . -> can be decimal
        #         symbol -> 0-9 -> integer
        #         integer -> 0-9 -> integer
        #         can be decimal -> 0-9 -> decimal
        #         integer -> . -> decimal
        #         decimal -> 0-9 -> decimal
        #         integer -> eE -> with e
        #         decimal -> eE -> with e
        #         with e -> +- -> with e +-
        #         with e -> 0-9 -> final
        #         with e +- -> 0-9 -> final
        #         final -> 0-9 -> final
                
        trans={
            ".":{
                ''      :'can be dec',
                '+-'    :'can be dec',
                'int'   :'dec',
            },
            "09":{
                ''          :'int',
                '+-'        :'int',
                'int'       :'int',
                'can be dec':'dec',
                'dec'       :'dec',
                'num e'    :'final',
                'num e+-'  :'final',
                'final'     :'final',
            },
            "+-":{
                ''          :'+-',
                'num e'    :'num e+-'
            },
            "e":{
                'int'       :'num e',
                'dec'       :'num e'
            }
        }
        state=''
        for c in s:
            if c.isdigit(): c="09"
            elif c in "+-": c="+-"
            elif c in "eE": c="e"
            elif c==".": pass
            if c not in trans: return False
            if state not in trans[c]: return False
            state=trans[c][state]
        
        return state in ('int','dec','final')