from pprint import pformat
from facepp import API, File

API_KEY = ''
API_SECRET = ''

def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))

api = API(API_KEY, API_SECRET)

result=api.faceset.addface(outer_id='jcq',face_tokens='d687cd0ca50fc1214f928ebd34fb8120')
print_result('test',result)