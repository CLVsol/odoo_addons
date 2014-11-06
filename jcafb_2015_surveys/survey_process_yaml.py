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

def survey_colunm(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, key4, question_type, question_id, collumn_sequence):

    _title_ = doc[key1][key2][key3][key4]['title'].encode("utf-8")
    _model_ = doc[key1][key2][key3][key4]['model']
    if collumn_sequence < 100:
        _id_ = question_id + '_0' + str(collumn_sequence / 10)
    else:
        _id_ = question_id + '_' + str(collumn_sequence / 10)
    _question_id_ = question_id
    _sequence_ = str(collumn_sequence)

    yaml_out_file.write('            %s:\n' % (_id_))
    yaml_out_file.write('                model: %s\n' % (_model_))
    yaml_out_file.write('                title: \'%s\'\n' % (_title_))

    _title_ = '[' + _id_ + '] ' + _title_

    txt_file.write('            %s\n' % (_title_))

    xml_file.write('                    <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                        <field name="title">%s</field>\n' % (_title_))
    xml_file.write('                        <field name="question_id" ref="%s"/>\n' % (_question_id_))
    #xml_file.write('                        <field name="sequence" eval="%s"/>\n' % (_sequence_))

    yaml_out_file.write('\n')

    xml_file.write('                    </record>\n')
    xml_file.write('\n')

def survey_answer(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, key4, question_type, question_id, answer_sequence):

    _answer_ = doc[key1][key2][key3][key4]['answer'].encode("utf-8")
    _model_ = doc[key1][key2][key3][key4]['model']
    if answer_sequence < 100:
        _id_ = question_id + '_0' + str(answer_sequence / 10)
    else:
        _id_ = question_id + '_' + str(answer_sequence / 10)
    _question_id_ = question_id
    _sequence_ = str(answer_sequence)

    yaml_out_file.write('            %s:\n' % (_id_))
    yaml_out_file.write('                model: %s\n' % (_model_))
    yaml_out_file.write('                answer: \'%s\'\n' % (_answer_))

    _answer_ = '[' + _id_ + '] ' + _answer_

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
        yaml_out_file.write('                type: %s\n' % (_type_))
        xml_file.write('                        <field name="type">%s</field>\n' % (_type_))
    except Exception, e:
        pass

    yaml_out_file.write('\n')

    xml_file.write('                    </record>\n')
    xml_file.write('\n')

def survey_question(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, page_id, question_sequence):

    _question_ = doc[key1][key2][key3]['question'].encode("utf-8")
    _type_ = doc[key1][key2][key3]['type']
    _model_ = doc[key1][key2][key3]['model']
    if question_sequence < 100:
        _id_ = page_id + '_0' + str(question_sequence / 10)
    else:
        _id_ = page_id + '_' + str(question_sequence / 10)
    _page_id_ = page_id
    _sequence_ = str(question_sequence)
    _is_require_answer_ = str(doc[key1][key2][key3]['is_require_answer'])
    _req_error_msg_ = doc[key1][key2][key3]['req_error_msg'].encode("utf-8")

    yaml_out_file.write('        %s:\n' % (_id_))
    yaml_out_file.write('            model: %s\n' % (_model_))
    yaml_out_file.write('            question: \'%s\'\n' % (_question_))
    yaml_out_file.write('            type: %s\n' % (_type_))
    yaml_out_file.write('            is_require_answer: %s\n' % (_is_require_answer_))
    yaml_out_file.write('            req_error_msg: \'%s\'\n' % (_req_error_msg_))

    _question_ = '[' + _id_ + '] ' + _question_

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
        yaml_out_file.write('            required_type: %s\n' % (_required_type_))
        xml_file.write('                    <field name="required_type">%s</field>\n' % (_required_type_))
    except Exception, e:
        print '             Missing: "%s"' % (e)
    
    try:
        _req_ans_ = str(doc[key1][key2][key3]['req_ans'])
        yaml_out_file.write('            req_ans: %s\n' % (_req_ans_))
        xml_file.write('                    <field name="req_ans">%s</field>\n' % (_req_ans_))
    except Exception, e:
        print '             Missing: "%s"' % (e)
    try:
        _is_comment_require_ = str(doc[key1][key2][key3]['is_comment_require'])
        yaml_out_file.write('            is_comment_require: %s\n' % (_is_comment_require_))
        xml_file.write('                    <field name="is_comment_require">%s</field>\n' % (_is_comment_require_))
    except Exception, e:
        print '             Missing: "%s"' % (e)
    
    try:
        _comment_label_ = doc[key1][key2][key3]['comment_label'].encode("utf-8")
        yaml_out_file.write('            comment_label: \'%s\'\n' % (_comment_label_))
        xml_file.write('                    <field name="comment_label">%s</field>\n' % (_comment_label_))
    except Exception, e:
        print '             Missing: "%s"' % (e)

    yaml_out_file.write('\n')

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
                    survey_answer(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, key4, _type_, _id_, answer_sequence)
                if _model_ == 'survey.question.column.heading':
                    answer_sequence += 10
                    survey_colunm(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, key4, _type_, _id_, answer_sequence)
            except Exception, e:
                pass

    try:
        _is_comment_require_ = doc[key1][key2][key3]['is_comment_require']
        if doc[key1][key2][key3]['is_comment_require'] == True:
            _comment_label_ = doc[key1][key2][key3]['comment_label'].encode("utf-8")
            txt_file.write('            %s____________________________________\n' % _comment_label_)
    except Exception, e:
        pass

def survey_page(doc, yaml_out_file, xml_file, txt_file, key1, key2, survey_id, page_sequence):

    _title_ = doc[key1][key2]['title'].encode("utf-8")
    _model_ = doc[key1][key2]['model']
    if page_sequence < 100:
        _id_ = survey_id + '_0' + str(page_sequence / 10)
    else:
        _id_ = survey_id + '_' + str(page_sequence / 10)
    _note_ = doc[key1][key2]['note'].encode("utf-8")
    _survey_id_ = key1
    _sequence_ = str(page_sequence)

    yaml_out_file.write('    %s:\n' % (_id_))
    yaml_out_file.write('        model: %s\n' % (_model_))
    yaml_out_file.write('        title: \'%s\'\n' % (_title_))
    yaml_out_file.write('        note: \'%s\'\n' % (_note_))
    yaml_out_file.write('\n')

    _title_ = '[' + _id_ + '] ' + _title_
    _note_ = '[' + _id_ + '] ' + _note_

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
                survey_question(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, _id_, question_sequence)
        except Exception, e:
            pass

def survey(doc, yaml_out_file, xml_file, txt_file, key1):

    _title_ = doc[key1]['title'].encode("utf-8")
    _model_ = doc[key1]['model']
    _id_ = key1
    _note_ = doc[key1]['note'].encode("utf-8")
    _responsible__id_ = doc[key1]['responsible_id']
    _type_ = doc[key1]['type']
    _color_ = str(doc[key1]['color'])

    yaml_out_file.write('%s:\n' % (key1))
    yaml_out_file.write('    model: %s\n' % (_model_))
    yaml_out_file.write('    title: \'%s\'\n' % (_title_))
    yaml_out_file.write('    note: \'%s\'\n' % (_note_))
    yaml_out_file.write('    responsible_id: %s\n' % (_responsible__id_))
    yaml_out_file.write('    type: %s\n' % (_type_))
    yaml_out_file.write('    color: %s\n' % (_color_))
    yaml_out_file.write('\n')

    _title_ = '[' + _id_ + '] ' + _title_
    _note_ = '[' + _id_ + '] ' + _note_

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
                survey_page(doc, yaml_out_file, xml_file, txt_file, key1, key2, key1, page_sequence)
        except Exception, e:
            pass

def survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename):

    yaml_file = open(yaml_filename, 'r')
    doc = yaml.load(yaml_file)

    yaml_out_file = open(yaml_out_filename, "w")
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
            survey(doc, yaml_out_file, xml_file, txt_file, key1)

    xml_file.write('    </data>\n')
    xml_file.write('</openerp>\n')

    yaml_file.close()
    yaml_out_file.close()
    txt_file.close()
    xml_file.close()

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],[(t*1000,),1000,60,60])

if __name__ == '__main__':

    from time import time
    start = time()

    print '--> Executing survey_process_yaml.py ...'

    yaml_filename = 'survey_jcafb_QSE15_data.yaml'
    yaml_out_filename = 'survey_jcafb_QSE15_data_out.yaml'
    xml_filename = 'survey_jcafb_QSE15_data.xml'
    txt_filename = 'survey_jcafb_QSE15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    yaml_filename = 'survey_jcafb_ISE15_data.yaml'
    yaml_out_filename = 'survey_jcafb_ISE15_data_out.yaml'
    xml_filename = 'survey_jcafb_ISE15_data.xml'
    txt_filename = 'survey_jcafb_ISE15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    yaml_filename = 'survey_jcafb_CSE15_data.yaml'
    yaml_out_filename = 'survey_jcafb_CSE15_data_out.yaml'
    xml_filename = 'survey_jcafb_CSE15_data.xml'
    txt_filename = 'survey_jcafb_CSE15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    yaml_filename = 'survey_jcafb_QMD15_data.yaml'
    yaml_out_filename = 'survey_jcafb_QMD15_data_out.yaml'
    xml_filename = 'survey_jcafb_QMD15_data.xml'
    txt_filename = 'survey_jcafb_QMD15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    yaml_filename = 'survey_jcafb_QAN15_data.yaml'
    yaml_out_filename = 'survey_jcafb_QAN15_data_out.yaml'
    xml_filename = 'survey_jcafb_QAN15_data.xml'
    txt_filename = 'survey_jcafb_QAN15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    yaml_filename = 'survey_jcafb_QDH15_data.yaml'
    yaml_out_filename = 'survey_jcafb_QDH15_data_out.yaml'
    xml_filename = 'survey_jcafb_QDH15_data.xml'
    txt_filename = 'survey_jcafb_QDH15.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    print '--> survey_process_yaml.py'
    print '--> Execution time:', secondsToStr(time() - start)
