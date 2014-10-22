#!/usr/bin/env python
# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2014-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

import yaml

def level_3_process_1(doc, xml_file, txt_file, mneumonic, key1, key2, key3, key4):

    _answer_ = doc[key1][key2][key3][key4]['answer'].encode("utf-8")
    _model_ = doc[key1][key2][key3][key4]['model']
    _id_ = doc[key1][key2][key3][key4]['id']
    _question_id_ = doc[key1][key2][key3][key4]['question_id']
    _sequence_ = str(doc[key1][key2][key3][key4]['sequence'])
    _type_ = doc[key1][key2][key3][key4]['type']

    txt_file.write('            %s____________________________________\n' % (_answer_))

    xml_file.write('                    <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                        <field name="answer">%s</field>\n' % (_answer_))
    xml_file.write('                        <field name="question_id" ref="%s"/>\n' % (_question_id_))
    xml_file.write('                        <field name="sequence" eval="%s"/>\n' % (_sequence_))
    xml_file.write('                        <field name="type">%s</field>\n' % (_type_))
    xml_file.write('                    </record>\n')
    xml_file.write('\n')

def level_3_process_2(doc, xml_file, txt_file, mneumonic, key1, key2, key3, key4):


    _answer_ = doc[key1][key2][key3][key4]['answer'].encode("utf-8")
    _model_ = doc[key1][key2][key3][key4]['model']
    _id_ = doc[key1][key2][key3][key4]['id']
    _question_id_ = doc[key1][key2][key3][key4]['question_id']
    _sequence_ = str(doc[key1][key2][key3][key4]['sequence'])

    txt_file.write('            %s\n' % (_answer_))

    xml_file.write('                    <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                        <field name="answer">%s</field>\n' % (_answer_))
    xml_file.write('                        <field name="question_id" ref="%s"/>\n' % (_question_id_))
    xml_file.write('                        <field name="sequence" eval="%s"/>\n' % (_sequence_))
    xml_file.write('                    </record>' + '\n')
    xml_file.write('\n')

def level_3_process(doc, xml_file, txt_file, mneumonic, key1, key2, key3):

    _question_ = doc[key1][key2][key3]['question'].encode("utf-8")
    _type_ = doc[key1][key2][key3]['type']
    _model_ = doc[key1][key2][key3]['model']
    _id_ = doc[key1][key2][key3]['id']
    _page_id_ = doc[key1][key2][key3]['page_id']
    _sequence_ = str(doc[key1][key2][key3]['sequence'])
    _is_require_answer_ = str(doc[key1][key2][key3]['is_require_answer'])
    _req_error_msg_ = doc[key1][key2][key3]['req_error_msg'].encode("utf-8")

    txt_file.write('        %s\n' % (_question_))
    txt_file.write('            (%s)\n' % (_type_))

    xml_file.write('                <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                    <field name="question">%s</field>\n' % (_question_))
    xml_file.write('                    <field name="type">%s</field>\n' % (_type_))
    xml_file.write('                    <field name="page_id" ref="%s"/>\n' % (_page_id_))
    xml_file.write('                    <field name="sequence" eval="%s"/>\n' % (_sequence_))
    xml_file.write('                    <field name="is_require_answer">%s</field>\n' % (_is_require_answer_))
    xml_file.write('                    <field name="req_error_msg">%s</field>\n' % (_req_error_msg_))

    try:
        _required_type_ = doc[key1][key2][key3]['required_type']
        xml_file.write('                    <field name="required_type">%s</field>\n' % (_required_type_))
    except Exception, e:
        print '             Missing: "%s"' % (e)
    
    try:
        _req_ans_ = str(doc[key1][key2][key3]['req_ans'])
        xml_file.write('                    <field name="req_ans">%s</field>\n' % (_req_ans_))
    except Exception, e:
        print '             Missing: "%s"' % (e)
    try:
        _is_comment_require_ = str(doc[key1][key2][key3]['is_comment_require'])
        xml_file.write('                    <field name="is_comment_require">%s</field>\n' % (_is_comment_require_))
    except Exception, e:
        print '             Missing: "%s"' % (e)
    
    try:
        _comment_label_ = doc[key1][key2][key3]['comment_label'].encode("utf-8")
        xml_file.write('                    <field name="comment_label">%s</field>\n' % (_comment_label_))
    except Exception, e:
        print '             Missing: "%s"' % (e)

    xml_file.write('                </record>\n')
    xml_file.write('\n')

    if  _type_ == 'comment':
        txt_file.write('            ' + '____________________________________\n')

    if  _type_ == 'multiple_textboxes_diff_type':
        for key4 in sorted(doc[key1][key2][key3].keys()):
            if not key4.find(mneumonic):
                print '            ', key4
                level_3_process_1(doc, xml_file, txt_file, mneumonic, key1, key2, key3, key4)

    else:
        for key4 in sorted(doc[key1][key2][key3].keys()):
            if not key4.find(mneumonic):

                print '            ', key4
                level_3_process_2(doc, xml_file, txt_file, mneumonic, key1, key2, key3, key4)

    try:
        _is_comment_require_ = doc[key1][key2][key3]['is_comment_require']
        if doc[key1][key2][key3]['is_comment_require'] == True:
            _comment_label_ = doc[key1][key2][key3]['comment_label']
            txt_file.write('            %s____________________________________\n' % _comment_label_)
    except:
        pass

def level_2_process(doc, xml_file, txt_file, mneumonic, key1, key2):

    _title_ = doc[key1][key2]['title'].encode("utf-8")
    _model_ = doc[key1][key2]['model']
    _id_ = doc[key1][key2]['id']
    _note_ = doc[key1][key2]['note'].encode("utf-8")
    _survey_id_ = doc[key1][key2]['survey_id']
    _sequence_ = str(doc[key1][key2]['sequence'])

    txt_file.write('    %s\n' % (_title_))

    xml_file.write('            <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                <field name="title">%s</field>\n' % (_title_))
    xml_file.write('                <field name="note">%s</field>\n' % (_note_))
    xml_file.write('                <field name="survey_id" ref="%s"/>\n' % (_survey_id_))
    xml_file.write('                <field name="sequence" eval="%s"/>\n' % (_sequence_))
    xml_file.write('            </record>' + '\n')
    xml_file.write('\n')

    for key3 in sorted(doc[key1][key2].keys()):
        if not key3.find(mneumonic):
            print '        ', key3
            level_3_process(doc, xml_file, txt_file, mneumonic, key1, key2, key3)

def level_1_process(doc, xml_file, txt_file, mneumonic, key1):

    _title_ = doc[key1]['title'].encode("utf-8")
    _model_ = doc[key1]['model']
    _id_ = doc[key1]['id']
    _note_ = doc[key1]['note'].encode("utf-8")
    _responsible__id_ = doc[key1]['responsible_id']
    _type_ = doc[key1]['type']
    _color_ = str(doc[key1]['color'])

    txt_file.write('%s\n' % (_title_))
    
    xml_file.write('        <!-- %s -->\n' % (_title_))
    xml_file.write('        <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('            <field name="title">%s</field>\n' % (_title_))
    xml_file.write('            <field name="note">%s</field>\n' % (_note_))
    xml_file.write('            <field name="responsible_id" ref="%s"/>\n' % (_responsible__id_))
    xml_file.write('            <field name="type" ref="%s"/>\n' % (_type_))
    xml_file.write('            <field name="color">%s</field>\n' % (_color_))
    xml_file.write('        </record>\n')
    xml_file.write('\n')
    
    for key2 in sorted(doc[key1].keys()):
        if not key2.find(mneumonic):
            print '    ', key2
            level_2_process(doc, xml_file, txt_file, mneumonic, key1, key2)

def survey_process(yaml_filename, xml_filename, txt_filename, mneumonic):

    yaml_file = open(yaml_filename, 'r')
    doc = yaml.load(yaml_file)

    txt_file = open(txt_filename, "w")
    xml_file = open(xml_filename, "w")

    xml_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
    xml_file.write('<openerp>\n')
    xml_file.write('    <data noupdate="1">\n')
    xml_file.write('\n')

    for key1 in sorted(doc.keys()):
        print key1
        level_1_process(doc, xml_file, txt_file, mneumonic, key1)

    xml_file.write('    </data>\n')
    xml_file.write('</openerp>\n')

    txt_file.close()
    xml_file.close()

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],[(t*1000,),1000,60,60])

if __name__ == '__main__':

    from time import time
    start = time()

    print '--> Executing survey_process.py ...'

    yaml_filename = 'survey_jcafb_QSE15_data.yaml'
    xml_filename = 'survey_jcafb_QSE15_data.xml'
    txt_filename = 'survey_jcafb_QSE15.txt'
    mneumonic = 'QSE15_'
    print '--> Executing survey_process(%s, %s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename, mneumonic)
    survey_process(yaml_filename, xml_filename, txt_filename, mneumonic)

    yaml_filename = 'survey_jcafb_QMD15_data.yaml'
    xml_filename = 'survey_jcafb_QMD15_data.xml'
    txt_filename = 'survey_jcafb_QMD15.txt'
    mneumonic = 'QMD15_'
    print '--> Executing survey_process(%s, %s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename, mneumonic)
    survey_process(yaml_filename, xml_filename, txt_filename, mneumonic)

    yaml_filename = 'survey_jcafb_QAN15_data.yaml'
    xml_filename = 'survey_jcafb_QAN15_data.xml'
    txt_filename = 'survey_jcafb_QAN15.txt'
    mneumonic = 'QAN15_'
    print '--> Executing survey_process(%s, %s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename, mneumonic)
    survey_process(yaml_filename, xml_filename, txt_filename, mneumonic)

    yaml_filename = 'survey_jcafb_QDH15_data.yaml'
    xml_filename = 'survey_jcafb_QDH15_data.xml'
    txt_filename = 'survey_jcafb_QDH15.txt'
    mneumonic = 'QDH15_'
    print '--> Executing survey_process(%s, %s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename, mneumonic)
    survey_process(yaml_filename, xml_filename, txt_filename, mneumonic)

    print '--> survey_process.py'
    print '--> Execution time:', secondsToStr(time() - start)
