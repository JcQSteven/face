# -*- coding: utf-8 -*-

import facetool
import os

confidence = facetool.get_confidence()
person = facetool.get_person().split(',')


def file_exit(file_path):
    if os.path.exits(file_path):
        return 1
    else:
        return 0


menu = '''
---------Menu---------
0.Set person
1.Add face to storage
2.Face check
3.
4.
5.Get all storage
6.Delete storage
7.Create storage
8.Detail storage
q.Exit
'''
lock = 1
if __name__ == "__main__":
    while lock:
        print menu
        try:
            case = raw_input('Input your option:')
            if case == '0':
                for i in range(len(person)):
                    print '%s.%s' % (i, person[i])
                person_choice = raw_input('Input your person number:')
                person_choice = person[int(person_choice)]

            if case == '1':
                file_path = raw_input('Enter you file path:')
                face_token = facetool.detect(file_path.rstrip())['faces'][0]['face_token']
                print 'face_token', face_token
                facetool.add_faceset(person_choice, face_token)
                print'[+]Add Successfully!\n'
            elif case == '2':
                file_path = raw_input('Enter you file path:')
                check_result = facetool.search_faceset(file_path.rstrip(), person_choice)['results'][0][
                    'confidence']
                print 'check_result', check_result
                if float(check_result) >= float(confidence):
                    print'[+]Highly !'
                else:
                    print'[-]Not the same one !'
            elif case == '3':
                pass
            elif case == '4':
                pass
            elif case == '5':
                facetool.print_result('Message', facetool.get_faceset())
                pass
            elif case == '6':
                id = raw_input('Input your id:')
                facetool.delete_faceset(id.rstrip())
            elif case == '7':
                id = raw_input('Input your id:')
                facetool.create_faceset(id)
            elif case == '8':
                id = raw_input('Input id:')
                facetool.print_result(id.rstrip(), facetool.detail_faceset(id))

            elif case == 'q':
                lock = 0
        except Exception, e:
            print e
# file_path='./demo.jpeg'

# facetool.print_result('search',facetool.search_faceset(file_path,'','88722683e5b70d8410ad1776326c5798')['results'][0]['confidence'])
# 指定仓库详细信息
# print_result('detail',detail_faceset('','88722683e5b70d8410ad1776326c5798'))

# 添加人脸至仓库
# print_result('add_faceset', add_faceset('', '88722683e5b70d8410ad1776326c5798', 'b8d4ac5272b4d084fd42add24fb97069'))

# 创建人脸仓库
# print_result('create',create_faceset())


# 删除人脸仓库
# result = api.faceset.delete(faceset_token='8ddd1d84cf35187b50d626b47c085fab',ourter_id=id, check_empty=1)


# 获取人脸仓库
# print_result('whole', get_faceset())

# 人脸检测
#
# print_result('detect',detect(file_path))
