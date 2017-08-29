# -*- coding: utf-8 -*-
from facepp import API, File
from pprint import pformat
import ConfigParser


config=ConfigParser.ConfigParser()
config.read('conf.ini')


api = API(config.get('API','API_KEY'), config.get('API','API_SECRET'))

def get_person():
    person_list=config.get('PERSON','person')
    return person_list
def get_confidence():
    confidence=config.get('CONFIDENCE','confidence')
    return confidence

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


def get_faceset():
    result = api.faceset.getfacesets()
    return result


def delete_faceset(id):
    result = api.faceset.delete( ourter_id=id, check_empty=0)
    return result


def create_faceset(id):
    result = api.faceset.create(outer_id=id, display_name=id)
    return result


def add_faceset(id, face_token):
    result = api.faceset.addface(outer_id=id, face_tokens=face_token)
    return result


def detail_faceset(id):
    result = api.faceset.getdetail(outer_id=id)
    return result


def detect(file_path):
    result = api.detect(image_file=File(file_path), return_attributes='gender,age')
    return result


def search_faceset(file_path, id):
    result = api.search(image_file=File(file_path), outer_id=id)
    return result
