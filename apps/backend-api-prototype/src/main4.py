import json
import os
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, HttpUrl
from typing import List
import sys
import random
import pymysql
import logging
from collections import Counter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mkapi.image_utils import analyze_images_and_cluster, find_signiture_color, exact_match, count_matches, \
    find_matching_images, random_exhibition, find_nearby_exhibitions

app = FastAPI()

color_dict = {
    'Cinnabar': ['(231, 47, 39)',
                 '?뱀떊? Cinnabar (231, 47, 39)??痍⑦뼢??媛吏??щ엺?낅땲?? Cinnabar ?됱뿉 ?뚮━???뱀떊? 媛뺣젹?섍퀬 ?댁젙?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Black': ['(152, 152, 152)', '?뱀떊? Black (44, 60, 49)??痍⑦뼢??媛吏??щ엺?낅땲?? Black?됱뿉 ?뚮━???뱀떊? ?좊퉬濡?퀬 媛뺣젹???깃꺽??媛吏??щ엺?낅땲??'],

    'Matterhorn': ['(86, 86, 86)',
                   '?뱀떊? Matterhorn (86, 86, 86)??痍⑦뼢??媛吏??щ엺?낅땲?? Matterhorn ?됱뿉 ?뚮━???뱀떊? ?덉젙?곸씠怨??좊ː?????덈뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Nobel': ['(152, 152, 152)',
              '?뱀떊? Nobel (152, 152, 152)??痍⑦뼢??媛吏??щ엺?낅땲?? Nobel ?됱뿉 ?뚮━???뱀떊? ?ㅼ슜?곸씠硫?李⑤텇???깃꺽??媛吏??щ엺?낅땲??'],

    'Very Light Grey': ['(206, 206, 206)',
                        '?뱀떊? Very Light Grey (206, 206, 206)??痍⑦뼢??媛吏??щ엺?낅땲?? Very Light Grey ?됱뿉 ?뚮━???뱀떊? ?ъ꽭?섍퀬 ?뺣룉???깃꺽??媛吏??щ엺?낅땲??'],

    'White Smoke': ['(244, 244, 244)',
                    '?뱀떊? White Smoke (244, 244, 244)??痍⑦뼢??媛吏??щ엺?낅땲?? White Smoke ?됱뿉 ?뚮━???뱀떊? ?쒖닔?섍퀬 源⑤걮???깃꺽??媛吏??щ엺?낅땲??'],

    'Paris Daisy': ['(255, 236, 79)',
                    '?뱀떊? Paris Daisy (255, 236, 79)??痍⑦뼢??媛吏??щ엺?낅땲?? Paris Daisy ?됱뿉 ?뚮━???뱀떊? 諛앷퀬 湲띿젙?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Corn Field': ['(249, 239, 189)',
                   '?뱀떊? Corn Field (249, 239, 189)??痍⑦뼢??媛吏??щ엺?낅땲?? Corn Field ?됱뿉 ?뚮━???뱀떊? ?곕쑜?섍퀬 遺?쒕윭???깃꺽??媛吏??щ엺?낅땲??'],

    'Bahia': ['(170, 198, 27)',
              '?뱀떊? Bahia (170, 198, 27)??痍⑦뼢??媛吏??щ엺?낅땲?? Bahia ?됱뿉 ?뚮━???뱀떊? ?앷린 ?섏튂怨??쒓린李??깃꺽??媛吏??щ엺?낅땲??'],

    'Kournikova': ['(255, 203, 88)',
                   '?뱀떊? Kournikova (255, 203, 88)??痍⑦뼢??媛吏??щ엺?낅땲?? Kournikova ?됱뿉 ?뚮━???뱀떊? ?곕쑜?섍퀬 ?ㅼ젙???깃꺽??媛吏??щ엺?낅땲??'],

    'Gossip': ['(146, 198, 131)',
               '?뱀떊? Gossip (146, 198, 131)??痍⑦뼢??媛吏??щ엺?낅땲?? Gossip ?됱뿉 ?뚮━???뱀떊? 移쒖젅?섍퀬 ?곷깷???깃꺽??媛吏??щ엺?낅땲??'],

    'Tangerine Yellow': ['(255, 200, 8)',
                         '?뱀떊? Tangerine Yellow (255, 200, 8)??痍⑦뼢??媛吏??щ엺?낅땲?? Tangerine Yellow ?됱뿉 ?뚮━???뱀떊? 李쎌쓽?곸씠怨??쒕컻???깃꺽??媛吏??щ엺?낅땲??'],

    'Pumpkin': ['(238, 113, 25)',
                '?뱀떊? Pumpkin (238, 113, 25)??痍⑦뼢??媛吏??щ엺?낅땲?? Pumpkin ?됱뿉 ?뚮━???뱀떊? ?댁젙?곸씠怨??곴레?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Harvest Gold': ['(242, 178, 103)',
                     '?뱀떊? Harvest Gold (242, 178, 103)??痍⑦뼢??媛吏??щ엺?낅땲?? Harvest Gold ?됱뿉 ?뚮━???뱀떊? ?곕쑜?섍퀬 ?띾????깃꺽??媛吏??щ엺?낅땲??'],

    'Persian Indigo': ['(46, 20, 141)',
                       '?뱀떊? Persian Indigo (46, 20, 141)??痍⑦뼢??媛吏??щ엺?낅땲?? Persian Indigo ?됱뿉 ?뚮━???뱀떊? ?좊퉬濡?퀬 吏?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Cobalt': ['(3, 86, 155)',
               '?뱀떊? Cobalt (3, 86, 155)??痍⑦뼢??媛吏??щ엺?낅땲?? Cobalt ?됱뿉 ?뚮━???뱀떊? 源딄퀬 吏꾩쨷???깃꺽??媛吏??щ엺?낅땲??'],

    'Dark Pastel Green': ['(19, 166, 50)',
                          '?뱀떊? Dark Pastel Green (19, 166, 50)??痍⑦뼢??媛吏??щ엺?낅땲?? Dark Pastel Green ?됱뿉 ?뚮━???뱀떊? 議곗슜?섍퀬 李⑤텇???깃꺽??媛吏??щ엺?낅땲??'],

    'Shamrock Green': ['(4, 148, 87)',
                       '?뱀떊? Shamrock Green (4, 148, 87)??痍⑦뼢??媛吏??щ엺?낅땲?? Shamrock Green ?됱뿉 ?뚮━???뱀떊? ?щ쭩李④퀬 ?쒓린李??깃꺽??媛吏??щ엺?낅땲??'],

    'Salem': ['(6, 134, 84)',
              '?뱀떊? Salem (6, 134, 84)??痍⑦뼢??媛吏??щ엺?낅땲?? Salem ?됱뿉 ?뚮━???뱀떊? ?좊ː?????덇퀬 ?덉젙???깃꺽??媛吏??щ엺?낅땲??'],

    'Wistful': ['(170, 165, 199)',
                '?뱀떊? Wistful (170, 165, 199)??痍⑦뼢??媛吏??щ엺?낅땲?? Wistful ?됱뿉 ?뚮━???뱀떊? 媛먯꽦?곸씠怨??ъ깋?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Eastern Blue': ['(0, 147, 159)',
                     '?뱀떊? Eastern Blue (0, 147, 159)??痍⑦뼢??媛吏??щ엺?낅땲?? Eastern Blue ?됱뿉 ?뚮━???뱀떊? 李⑤텇?섍퀬 ?쇰━?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Brandy Rose': ['(171, 131, 115)',
                    '?뱀떊? Brandy Rose (171, 131, 115)??痍⑦뼢??媛吏??щ엺?낅땲?? Brandy Rose ?됱뿉 ?뚮━???뱀떊? ?곗븘?섍퀬 ?뺢탳???깃꺽??媛吏??щ엺?낅땲??'],

    'Granite Green': ['(144, 135, 96)',
                      '?뱀떊? Granite Green (144, 135, 96)??痍⑦뼢??媛吏??щ엺?낅땲?? Granite Green ?됱뿉 ?뚮━???뱀떊? ?먯뿰?ㅻ읇怨??뚮컯???깃꺽??媛吏??щ엺?낅땲??'],

    'Manz': ['(219, 220, 93)',
             '?뱀떊? Manz (219, 220, 93)??痍⑦뼢??媛吏??щ엺?낅땲?? Manz ?됱뿉 ?뚮━???뱀떊? 諛앷퀬 ?숈쿇?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Wild Willow': ['(195, 202, 101)',
                    '?뱀떊? Wild Willow (195, 202, 101)??痍⑦뼢??媛吏??щ엺?낅땲?? Wild Willow ?됱뿉 ?뚮━???뱀떊? ?좎뿰?섍퀬 ?댄빐??留롮? ?깃꺽??媛吏??щ엺?낅땲??'],

    'Cioccolato': ['(88, 60, 50)',
                   '?뱀떊? Cioccolato (88, 60, 50)??痍⑦뼢??媛吏??щ엺?낅땲?? Cioccolato ?됱뿉 ?뚮━???뱀떊? 源딄퀬 吏꾩쨷???깃꺽??媛吏??щ엺?낅땲??'],

    'Cerulean': ['(6, 113, 148)',
                 '?뱀떊? Cerulean (6, 113, 148)??痍⑦뼢??媛吏??щ엺?낅땲?? Cerulean ?됱뿉 ?뚮━???뱀떊? 李⑤텇?섍퀬 ?좊ː?????덈뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Chelsea Cucumber': ['(141, 188, 90)',
                         '?뱀떊? Chelsea Cucumber (141, 188, 90)??痍⑦뼢??媛吏??щ엺?낅땲?? Chelsea Cucumber ?됱뿉 ?뚮━???뱀떊? ?곸풄?섍퀬 ?먯뿰???щ옉?섎뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Fun Green': ['(24, 89, 63)',
                  '?뱀떊? Fun Green (24, 89, 63)??痍⑦뼢??媛吏??щ엺?낅땲?? Fun Green ?됱뿉 ?뚮━???뱀떊? 紐⑦뿕?곸씠怨??낆갹?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Deep Teal': ['(27, 86, 49)',
                  '?뱀떊? Deep Teal (27, 86, 49)??痍⑦뼢??媛吏??щ엺?낅땲?? Deep Teal ?됱뿉 ?뚮━???뱀떊? 源딄퀬 ?щ젮 源딆? ?깃꺽??媛吏??щ엺?낅땲??'],

    'Deep Bronze': ['(75, 63, 45)',
                    '?뱀떊? Deep Bronze (75, 63, 45)??痍⑦뼢??媛吏??щ엺?낅땲?? Deep Bronze ?됱뿉 ?뚮━???뱀떊? 怨좎쟾?곸씠怨??꾪넻?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Timber Green': ['(44, 60, 49)',
                     '?뱀떊? Timber Green (44, 60, 49)??痍⑦뼢??媛吏??щ엺?낅땲?? Timber Green ?됱뿉 ?뚮━???뱀떊? ?덉젙?곸씠怨??좊ː?????덈뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Palm Green': ['(31, 56, 45)',
                   '?뱀떊? Palm Green (31, 56, 45)??痍⑦뼢??媛吏??щ엺?낅땲?? Palm Green ?됱뿉 ?뚮━???뱀떊? 議곗슜?섍퀬 ?댁꽦?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Tiber': ['(25, 62, 63)',
              '?뱀떊? Tiber (25, 62, 63)??痍⑦뼢??媛吏??щ엺?낅땲?? Tiber ?됱뿉 ?뚮━???뱀떊? ?좊퉬濡?퀬 源딆씠 ?덈뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Metallic Copper': ['(111, 61, 56)',
                        '?뱀떊? Metallic Copper (111, 61, 56)??痍⑦뼢??媛吏??щ엺?낅땲?? Metallic Copper ?됱뿉 ?뚮━???뱀떊? ?댁젙?곸씠怨?寃곕떒???덈뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Tamarillo': ['(116, 47, 50)',
                  '?뱀떊? Tamarillo (116, 47, 50)??痍⑦뼢??媛吏??щ엺?낅땲?? Tamarillo ?됱뿉 ?뚮━???뱀떊? 媛먯젙?곸씠怨??댁젙?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Apple Blossom': ['(175, 92, 87)',
                      '?뱀떊? Apple Blossom (175, 92, 87)??痍⑦뼢??媛吏??щ엺?낅땲?? Apple Blossom ?됱뿉 ?뚮━???뱀떊? 遺?쒕읇怨??ㅼ젙???깃꺽??媛吏??щ엺?낅땲??'],

    'Surfie Green': ['(3, 130, 122)',
                     '?뱀떊? Surfie Green (3, 130, 122)??痍⑦뼢??媛吏??щ엺?낅땲?? Surfie Green ?됱뿉 ?뚮━???뱀떊? 吏꾩랬?곸씠怨??쒓린李??깃꺽??媛吏??щ엺?낅땲??'],

    'Feldspar': ['(211, 142, 110)',
                 '?뱀떊? Feldspar (211, 142, 110)??痍⑦뼢??媛吏??щ엺?낅땲?? Feldspar ?됱뿉 ?뚮━???뱀떊? ?곕쑜?섍퀬 媛먯꽦?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Vesuvius': ['(169, 87, 49)',
                 '?뱀떊? Vesuvius (169, 87, 49)??痍⑦뼢??媛吏??щ엺?낅땲?? Vesuvius ?됱뿉 ?뚮━???뱀떊? ?댁젙?곸씠怨?媛뺣젹???깃꺽??媛吏??щ엺?낅땲??'],

    'Blue Lagoon': ['(8, 87, 107)',
                    '?뱀떊? Blue Lagoon (8, 87, 107)??痍⑦뼢??媛吏??щ엺?낅땲?? Blue Lagoon ?됱뿉 ?뚮━???뱀떊? 李⑤텇?섍퀬 吏?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Tonys Pink': ['(233, 163, 144)',
                   '?뱀떊? Tonys Pink (233, 163, 144)??痍⑦뼢??媛吏??щ엺?낅땲?? Tonys Pink ?됱뿉 ?뚮━???뱀떊? 遺?쒕읇怨???쭔?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Wafer': ['(206, 185, 179)',
              '?뱀떊? Wafer (206, 185, 179)??痍⑦뼢??媛吏??щ엺?낅땲?? Wafer ?됱뿉 ?뚮━???뱀떊? ?곕쑜?섍퀬 ?몃젴???깃꺽??媛吏??щ엺?낅땲??'],

    'Camarone': ['(20, 114, 48)',
                 '?뱀떊? Camarone (20, 114, 48)??痍⑦뼢??媛吏??щ엺?낅땲?? Camarone ?됱뿉 ?뚮━???뱀떊? 吏꾩랬?곸씠怨??⑦샇???깃꺽??媛吏??щ엺?낅땲??'],

    'Vida Loca': ['(91, 132, 47)',
                  '?뱀떊? Vida Loca (91, 132, 47)??痍⑦뼢??媛吏??щ엺?낅땲?? Vida Loca ?됱뿉 ?뚮━???뱀떊? 李쎌쓽?곸씠怨??쒓린李??깃꺽??媛吏??щ엺?낅땲??'],

    'Green House': ['(54, 88, 48)',
                    '?뱀떊? Green House (54, 88, 48)??痍⑦뼢??媛吏??щ엺?낅땲?? Green House ?됱뿉 ?뚮━???뱀떊? ?좊ː?????덇퀬 ?먯뿰???щ옉?섎뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Granny Smith': ['(130, 154, 145)',
                     '?뱀떊? Granny Smith (130, 154, 145)??痍⑦뼢??媛吏??щ엺?낅땲?? Granny Smith ?됱뿉 ?뚮━???뱀떊? 李⑤텇?섍퀬 ?좊ː?????덈뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Wheat': ['(245, 223, 181)',
              '?뱀떊? Wheat (245, 223, 181)??痍⑦뼢??媛吏??щ엺?낅땲?? Wheat ?됱뿉 ?뚮━???뱀떊? ?곕쑜?섍퀬 遺?쒕윭???깃꺽??媛吏??щ엺?낅땲??'],

    'Pale Rose': ['(235, 219, 224)',
                  '?뱀떊? Pale Rose (235, 219, 224)??痍⑦뼢??媛吏??щ엺?낅땲?? Pale Rose ?됱뿉 ?뚮━???뱀떊? ?ъ꽭?섍퀬 濡쒕㎤?깊븳 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Oyster Pink': ['(218, 176, 176)',
                    '?뱀떊? Oyster Pink (218, 176, 176)??痍⑦뼢??媛吏??щ엺?낅땲?? Oyster Pink ?됱뿉 ?뚮━???뱀떊? 媛먯꽦?곸씠怨??ㅼ젙???깃꺽??媛吏??щ엺?낅땲??'],

    'Opal': ['(184, 190, 189)',
             '?뱀떊? Opal (184, 190, 189)??痍⑦뼢??媛吏??щ엺?낅땲?? Opal ?됱뿉 ?뚮━???뱀떊? 李⑤텇?섍퀬 ?좎쨷???깃꺽??媛吏??щ엺?낅땲??'],

    'London Hue': ['(178, 137, 166)',
                   '?뱀떊? London Hue (178, 137, 166)??痍⑦뼢??媛吏??щ엺?낅땲?? London Hue ?됱뿉 ?뚮━???뱀떊? ?ъ꽭?섍퀬 李쎌쓽?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Lemon Ginger': ['(156, 137, 37)',
                     '?뱀떊? Lemon Ginger (156, 137, 37)??痍⑦뼢??媛吏??щ엺?낅땲?? Lemon Ginger ?됱뿉 ?뚮━???뱀떊? 李쎌쓽?곸씠怨??낆갹?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Guardsman Red': ['(172, 36, 48)',
                      '?뱀떊? Guardsman Red (172, 36, 48)??痍⑦뼢??媛吏??щ엺?낅땲?? Guardsman Red ?됱뿉 ?뚮━???뱀떊? 媛뺣젹?섍퀬 ?댁젙?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Mandy': ['(204, 63, 92)',
              '?뱀떊? Mandy (204, 63, 92)??痍⑦뼢??媛吏??щ엺?낅땲?? Mandy ?됱뿉 ?뚮━???뱀떊? 媛먯꽦?곸씠怨?濡쒕㎤?깊븳 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Costa Del Sol': ['(103, 91, 44)',
                      '?뱀떊? Costa Del Sol (103, 91, 44)??痍⑦뼢??媛吏??щ엺?낅땲?? Costa Del Sol ?됱뿉 ?뚮━???뱀떊? 怨좎쟾?곸씠怨??곗븘???깃꺽??媛吏??щ엺?낅땲??'],

    'Chetwode Blue': ['(92, 104, 163)',
                      '?뱀떊? Chetwode Blue (92, 104, 163)??痍⑦뼢??媛吏??щ엺?낅땲?? Chetwode Blue ?됱뿉 ?뚮━???뱀떊? 吏?곸씠怨??щ젮 源딆? ?깃꺽??媛吏??щ엺?낅땲??'],

    'Aqua Squeeze': ['(209, 234, 211)',
                     '?뱀떊? Aqua Squeeze (209, 234, 211)??痍⑦뼢??媛吏??щ엺?낅땲?? Aqua Squeeze ?됱뿉 ?뚮━???뱀떊? 李⑤텇?섍퀬 ?좎쨷???깃꺽??媛吏??щ엺?낅땲??'],

    'Siam': ['(109, 116, 73)',
             '?뱀떊? Siam (109, 116, 73)??痍⑦뼢??媛吏??щ엺?낅땲?? Siam ?됱뿉 ?뚮━???뱀떊? ?덉젙?곸씠怨??ㅼ슜?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Sprout': ['(179, 202, 157)',
               '?뱀떊? Sprout (179, 202, 157)??痍⑦뼢??媛吏??щ엺?낅땲?? Sprout ?됱뿉 ?뚮━???뱀떊? ?앷린 ?섏튂怨??쒓린李??깃꺽??媛吏??щ엺?낅땲??'],

    'Oxley': ['(122, 165, 123)',
              '?뱀떊? Oxley (122, 165, 123)??痍⑦뼢??媛吏??щ엺?낅땲?? Oxley ?됱뿉 ?뚮━???뱀떊? ?먯뿰?ㅻ읇怨??좊ː?????덈뒗 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Seagull': ['(126, 188, 209)',
                '?뱀떊? Seagull (126, 188, 209)??痍⑦뼢??媛吏??щ엺?낅땲?? Seagull ?됱뿉 ?뚮━???뱀떊? ?곸풄?섍퀬 吏?곸씤 ?깃꺽??媛吏??щ엺?낅땲??'],

    'Gulf Stream': ['(117, 173, 169)',
                    '?뱀떊? Gulf Stream (117, 173, 169)??痍⑦뼢??媛吏??щ엺?낅땲?? Gulf Stream ?됱뿉 ?뚮━???뱀떊? 李⑤텇?섍퀬 ?됱삩???깃꺽??媛吏??щ엺?낅땲??'],

    'Heather': ['(165, 184, 199)',
                '?뱀떊? Heather (165, 184, 199)??痍⑦뼢??媛吏??щ엺?낅땲?? Heather ?됱뿉 ?뚮━???뱀떊? 遺?쒕읇怨?李⑤텇???깃꺽??媛吏??щ엺?낅땲??'],

    'Hawkes Blue': ['(203, 215, 232)',
                    '?뱀떊? Hawkes Blue (203, 215, 232)??痍⑦뼢??媛吏??щ엺?낅땲?? Hawkes Blue ?됱뿉 ?뚮━???뱀떊? 吏?곸씠怨??댁꽦?곸씤 ?깃꺽??媛吏??щ엺?낅땲??']
}

'port': 3306
# }

db_config = {
    "host": os.getenv("RESTART_DB_HOST", "localhost"),
    "user": os.getenv("RESTART_DB_USER", "restart_user"),
    "password": os.getenv("RESTART_DB_PASSWORD", ""),
    "database": os.getenv("RESTART_DB_NAME", "restart"),
}

def connect_db(config):
    """ ?곗씠?곕쿋?댁뒪 ?곌껐 ?⑥닔 """
    try:
        connection = pymysql.connect(host=config['host'],
                                     user=config['user'],
                                     password=config['password'],
                                     database=config['database'],
                                     cursorclass=pymysql.cursors.DictCursor)
        logging.info("Database connection successful")
        return connection
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        return None

# ?곗씠?곕쿋?댁뒪 ?곌껐
db_connection = connect_db(db_config)



class ImageData(BaseModel):
    user_images_urls: List[HttpUrl] = [
        "https://ifh.cc/g/oY2K9B.jpg",
        "https://ifh.cc/g/zwxOAA.jpg",
        "https://ifh.cc/g/XSAScb.jpg",
        "https://ifh.cc/g/DgrlJL.jpg"]



class SignitureImageData(BaseModel):
    user_images_urls: List[str]

class lat_long(BaseModel):
    lat_long_list: List[float] = [
        37.5173319258532,
        127.047377408384
    ]
class lat_long_input(BaseModel):
    lat_input: float = 37.5173319258532
    long_input: float = 127.047377408384

@app.post('/find_near_exhibition/')
async def find_near_exhibition(location: lat_long_input):
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM exhibitions")
    exhibition = [row['name'] for row in cursor.fetchall()]
    cursor.execute("SELECT latitude FROM exhibitions")
    exhibition2 = [row['latitude'] for row in cursor.fetchall()]
    cursor.execute("SELECT longitude FROM exhibitions")
    exhibition3 = [row['longitude'] for row in cursor.fetchall()]

    exhibition_info = [
        [exhibition[i], [float(exhibition2[i]), float(exhibition3[i])]]
        for i in range(len(exhibition))
    ]
    print(location.long_input)
    real_exhibition =[]
    real_exhibition.append(location.lat_input)
    real_exhibition.append(location.long_input)
    loaction_ex = lat_long(
        lat_long_list = real_exhibition
    )

    #print(loaction_ex)
    radius = 5
    exhibition_information = find_nearby_exhibitions(loaction_ex.lat_long_list, exhibition_info, radius)
    return exhibition_information

@app.post("/leaflet_creating/")
async def leaflet_creating(image_data: ImageData):
    cursor = db_connection.cursor()
    cursor.execute("SELECT url FROM images_exhibition_13")
    row_images = [row['url'] for row in cursor.fetchall()]

    cursor.execute("SELECT color_cluster_ratio FROM images_exhibition_13")
    row_images2 = [row['color_cluster_ratio'] for row in cursor.fetchall()]

    result = {
        'url': [],
        'color_cluster_ratio' : []
    }
    result['url'] = row_images
    result['color_cluster_ratio'] = row_images2

    try:

        find_matching_payload = ImageData(
            user_images_urls=image_data.user_images_urls,
        )
        # 1. ?좎궗??遺꾩꽍 ?뚮━湲?
        matching_images_response = find_matching_images(find_matching_payload, result)

        matching_urls = matching_images_response['matching_urls']
        print("留ㅼ묶" + matching_urls)

        # 2. ?ㅽ럺?몃윺 ?대윭?ㅽ꽣留??섍린
        analysis_result = analyze_images_and_cluster(
            matching_urls, result
        )
        print(analysis_result)
        # 3. 痍⑦뼢遺꾩꽍?섍린
        #max_color = 0

        # color_number_one = find_signiture_color(matching_urls['color_cluster_ratio'])
        # text_user = {}
        # for i in color_dict.keys():
        #     if i == color_number_one:
        #         text_user = {"user_color": color_dict[i][1]}
        #         dominant_color = i
        #         user_rgb = color_dict[i][0]
        #         break
        if matching_urls['url'] != []:
            color_number_one = find_signiture_color(matching_urls['color_cluster_ratio'])
        else:
            color_number_one = find_signiture_color(random.choices(result['color_cluster_ratio'],k=4))
        text_user = {}
        for i in color_dict.keys():
            if i == color_number_one:
                text_user = {"user_color": color_dict[i][1]}
                dominant_color = i
                user_rgb = color_dict[i][0]
                break
        
        # 4. ?묓뭹 異붿쿇?섍린
        cursor.execute("SELECT * FROM images_exhibition_1")
        rrow = cursor.fetchall()

        cursor.execute("SELECT url FROM images_exhibition_1")
        row2 = [row['url'] for row in cursor.fetchall()]
        cursor.execute("SELECT color_cluster_ratio FROM images_exhibition_1")
        row3 = [row['color_cluster_ratio'] for row in cursor.fetchall()]

        new_color_dict = {}
        jj = 0
        for i in row2:
            new_color_dict[i] = json.loads(row3[jj])
            jj+=1

        recommend_picture = None

        mood_dict = {}
        for i in range(len(rrow)):
            mood_dict[rrow[i]['url']] = rrow[i]['emotions']

        
        max_color = 0
        for key, colors in new_color_dict.items():
            for color in colors:
                if color[0] == dominant_color:
                    if color[2] > max_color:
                        max_color = color[2]
                        recommend_picture = key
        
        recommend_picture_list = []
        if recommend_picture:
            for i in range(len(new_color_dict)):
                if recommend_picture == rrow[i]['url']:
                    recommend_picture_list.append(rrow[i]['url'])
                    recommend_picture_list.append(rrow[i]['title'])
                    recommend_picture_list.append(rrow[i]['author'])
                    recommend_picture_list.append(rrow[i]['description'])
        else:
            no_no = random.randint(1, len(rrow))
            recommend_picture_list.append(rrow[no_no]['url'])
            recommend_picture_list.append(rrow[no_no]['title'])
            recommend_picture_list.append(rrow[no_no]['author'])
            recommend_picture_list.appedn(rrow[no_no]['description'])
            recommend_picture = rrow[no_no]['url']

        target_mood = mood_dict[recommend_picture]

        del mood_dict[recommend_picture]
        all_three_matches = [k for k, v in mood_dict.items() if exact_match(v, target_mood)]

        if all_three_matches:
            # If there are multiple, choose one randomly
            result = random.choice(all_three_matches)
        else:
            # Find all entries with at least two matching emotions
            two_matches = [k for k, v in mood_dict.items() if count_matches(v, target_mood) == 2]

            if two_matches:
                # If there are multiple, choose one randomly
                result = random.choice(two_matches)
            else:
                # Find all entries with at least one matching emotion
                one_match = [k for k, v in mood_dict.items() if count_matches(v, target_mood) == 1]

                if one_match:
                    # If there are multiple, choose one randomly
                    result = random.choice(one_match)
                else:
                    result = None

        recommend_picture_list2 = []
        for i in range(len(mood_dict)):
            if result == rrow[i]['url']:
                recommend_picture_list2.append(rrow[i]['url'])
                recommend_picture_list2.append(rrow[i]['title'])
                recommend_picture_list2.append(rrow[i]['author'])
                recommend_picture_list2.append(rrow[i]['description'])
                
        cursor.execute("SELECT * FROM exhibitions")
        exhibition = cursor.fetchall()

        recom_exhibition = random_exhibition(exhibition)

        text_user['user_rgb'] = user_rgb
        text_user['recom_picture1'] = recommend_picture_list
        text_user['recom_picture2'] = recommend_picture_list2
        text_user['spectral_key'] = [analysis_result]
        text_user['recom_exhibition'] = recom_exhibition
        return text_user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

