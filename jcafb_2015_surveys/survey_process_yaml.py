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

def survey_answer(doc, xml_file, txt_file, key1, key2, key3, key4, question_type, answer_sequence):

    _answer_ = '[' + key4 + '] ' + doc[key1][key2][key3][key4]['answer'].encode("utf-8")
    _model_ = doc[key1][key2][key3][key4]['model']
    _id_ = key4
    _question_id_ = key3
    _sequence_ = str(answer_sequence)

    if  question_type == 'multiple_textboxes_diff_type':
        txt_file.write('            %s____________________________________\n' % (_answer_))
    else:
        txt_file.write('            %s\n' % (_answer_))

    xml_file.write('                    <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                        <field name="answer">%s</field>\n' % (_answer_))
    xml_file.write('                        <field name="question_id" ref="%s"/>\n' % (_question_id_))
    xml_file.write('                        <field name="sequence" eval="%s"/>\n' % (_sequence_))
    try:
        _type_ = doc[key1][key2][key3][key4]['type']
        xml_file.write('                        <field name="type">%s</field>\n' % (_type_))
    except Exception, e:
        pass
    xml_file.write('                    </record>\n')
    xml_file.write('\n')

def survey_question(doc, xml_file, txt_file, key1, key2, key3, question_sequence):

    _question_ = '[' + key3 + '] ' + doc[key1][key2][key3]['question'].encode("utf-8")
    _type_ = doc[key1][key2][key3]['type']
    _model_ = doc[key1][key2][key3]['model']
    _id_ = key3
    _page_id_ = key2
    _sequence_ = str(question_sequence)
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

    else:
        answer_sequence = 0
        for key4 in sorted(doc[key1][key2][key3].keys()):
            try:
                _model_ = doc[key1][key2][key3][key4]['model']
                print '            ', key4, _model_
                if _model_ == 'survey.answer':
                    answer_sequence += 10
                    survey_answer(doc, xml_file, txt_file, key1, key2, key3, key4, _type_, answer_sequence)
            except Exception, e:
                pass

    try:
        _is_comment_require_ = doc[key1][key2][key3]['is_comment_require']
        if doc[key1][key2][key3]['is_comment_require'] == True:
            _comment_label_ = doc[key1][key2][key3]['comment_label']
            txt_file.write('            %s____________________________________\n' % _comment_label_)
    except Exception, e:
        pass

def survey_page(doc, xml_file, txt_file, key1, key2, page_sequence):

    _title_ = '[' + key2 + '] ' + doc[key1][key2]['title'].encode("utf-8")
    _model_ = doc[key1][key2]['model']
    _id_ = key2
    _note_ = '[' + key2 + '] ' + doc[key1][key2]['note'].encode("utf-8")
    _survey_id_ = key1
    _sequence_ = str(page_sequence)

    txt_file.write('    %s\n' % (_title_))

    xml_file.write('            <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                <field name="title">%s</field>\n' % (_title_))
    xml_file.write('                <field name="note">%s</field>\n' % (_note_))
    xml_file.write('                <field name="survey_id" ref="%s"/>\n' % (_survey_id_))
    xml_file.write('                <field name="sequence" eval="%s"/>\n' % (_sequence_))
    xml_file.write('            </record>' + '\n')
    xml_file.write('\n')

    question_sequence = 0
    for key3 in sorted(doc[key1][key2].keys()):
        try:
            _model_ = doc[key1][key2][key3]['model']
            print '        ', key3, _model_
            if _model_ == 'survey.question':
                question_sequence += 10
                survey_question(doc, xml_file, txt_file, key1, key2, key3, question_sequence)
        except Exception, e:
            pass

def survey(doc, xml_file, txt_file, key1):

    _title_ = '[' + key1 + '] ' + doc[key1]['title'].encode("utf-8")
    _model_ = doc[key1]['model']
    _id_ = key1
    _note_ = '[' + key1 + '] ' + doc[key1]['note'].encode("utf-8")
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
    
    page_sequence = 0
    for key2 in sorted(doc[key1].keys()):
        try:
            _model_ = doc[key1][key2]['model']
            print '    ', key2, _model_
            if _model_ == 'survey.page':
                page_sequence += 10
                survey_page(doc, xml_file, txt_file, key1, key2, page_sequence)
        except Exception, e:
            pass

def survey_process_yaml(yaml_filename, xml_filename, txt_filename):

    yaml_file = open(yaml_filename, 'r')
    doc = yaml.load(yaml_file)

    txt_file = open(txt_filename, "w")
    xml_file = open(xml_filename, "w")

    xml_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
    xml_file.write('<openerp>\n')
    xml_file.write('    <data noupdate="1">\n')
    xml_file.write('\n')

    for key1 in sorted(doc.keys()):
        _model_ = doc[key1]['model']
        print key1, _model_
        if _model_ == 'survey':
            survey(doc, xml_file, txt_file, key1)

    xml_file.write('    </data>\n')
    xml_file.write('</openerp>\n')

    txt_file.close()
    xml_file.close()

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],[(t*1000,),1000,60,60])

if __name__ == '__main__':

    from time import time
    start = time()

    print '--> Executing survey_process_yaml.py ...'

    yaml_filename = 'survey_jcafb_QSE15_data.yaml'
    xml_filename = 'survey_jcafb_QSE15_data.xml'
    txt_filename = 'survey_jcafb_QSE15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, xml_filename, txt_filename)

    yaml_filename = 'survey_jcafb_QMD15_data.yaml'
    xml_filename = 'survey_jcafb_QMD15_data.xml'
    txt_filename = 'survey_jcafb_QMD15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, xml_filename, txt_filename)

    yaml_filename = 'survey_jcafb_QAN15_data.yaml'
    xml_filename = 'survey_jcafb_QAN15_data.xml'
    txt_filename = 'survey_jcafb_QAN15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, xml_filename, txt_filename)

    yaml_filename = 'survey_jcafb_QDH15_data.yaml'
    xml_filename = 'survey_jcafb_QDH15_data.xml'
    txt_filename = 'survey_jcafb_QDH15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, xml_filename, txt_filename)

    print '--> survey_process_yaml.py'
    print '--> Execution time:', secondsToStr(time() - start)
