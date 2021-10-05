data = {"externalActivityId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_POLITICS_3","externalLessonId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS","externalMissionId":"PRESENTING_YOUR_POSITION_POLITICS","externalLearningPathId":"PROGRESS_IN_THE_LANGUAGE_EN_GB","score":100,"status":"SUCCESS"}

headers = {
    'authority': 'learn.altissia.org',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'x-device-uuid': '21b54486-10ca-463f-82e0-0664461f1570',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    'x-altissia-token': 'a0d17b24cae232c624f54d6bbdba91162ae7a82873cf4877dbe0a5f0c68e26c3',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://learn.altissia.org',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://learn.altissia.org/platform/',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8,fr;q=0.7',
    'cookie': 'deviceuuid=21b54486-10ca-463f-82e0-0664461f1570; NG_TRANSLATE_LANG_KEY=%22en-GB%22',
}

/////////////////////// 

after success u cant change back to failure or lower the score

////////////// 

load lesson data has all the exercise titles and exams

Lessons = externalLessonId 
    activity (ex , exam ...) = externalActivityId or externalId

{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS","status":"IN_PROGRESS","title":"Giving Your Opinion About Politics","description":null,"language":"en_GB","level":"B1","type":"OTHER","highlighted":false,"image":"/data/content_resources/current/lessons/EN_GB/EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS-16-9.jpg","topic":{"externalId":"ARGUMENTATION","image":"/data/content_resources/current/topics/ARGUMENTATION.jpg","name":"Argumentation","position":2000,"translationKey":"lc_topic_other_argumentation_label"},"activities":[{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_VIDEO_VIDEO_WHAT_DO_YOU_THINK_ABOUT_POLITICS","title":"Video : What do you think about politics?","score":null,"status":"SUCCESS","activityType":"VIDEO","highlighted":false},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_POLITICS","title":"Politics","score":100,"status":"SUCCESS","activityType":"EXERCISE","highlighted":false},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_POLITICS_2","title":"Politics","score":100,"status":"SUCCESS","activityType":"EXERCISE","highlighted":false},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_LESSON_3","title":"Lesson 3","score":100,"status":"SUCCESS","activityType":"EXERCISE","highlighted":false},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_POLITICS_3","title":"Politics","score":null,"status":null,"activityType":"EXERCISE","highlighted":true},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_VOCABULARY_LIST_VOCABULARY","title":"Vocabulary","score":null,"status":null,"activityType":"VOCABULARY_LIST","highlighted":false}]}

/////////////

curl "https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS" ^
  -H "authority: learn.altissia.org" ^
  -H "sec-ch-ua: ^\^"Chromium^\^";v=^\^"94^\^", ^\^"Google Chrome^\^";v=^\^"94^\^", ^\^";Not A Brand^\^";v=^\^"99^\^"" ^
  -H "accept: application/json, text/plain, */*" ^
  -H "x-device-uuid: 21b54486-10ca-463f-82e0-0664461f1570" ^
  -H "x-altissia-token: a0d17b24cae232c624f54d6bbdba91162ae7a82873cf4877dbe0a5f0c68e26c3" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  -H "sec-fetch-site: same-origin" ^
  -H "sec-fetch-mode: cors" ^
  -H "sec-fetch-dest: empty" ^
  -H "referer: https://learn.altissia.org/platform/" ^
  -H "accept-language: en-US,en;q=0.9,ar;q=0.8,fr;q=0.7" ^
  -H "cookie: deviceuuid=21b54486-10ca-463f-82e0-0664461f1570; NG_TRANSLATE_LANG_KEY=^%^22en-GB^%^22" ^
  --compressed
  
 get all activities inside of a lesson 
 
 json response exmaple : {"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS","status":"VALIDATED","title":"Giving Your Opinion About Politics","description":null,"language":"en_GB","level":"B1","type":"OTHER","highlighted":false,"image":"/data/content_resources/current/lessons/EN_GB/EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS-16-9.jpg","topic":{"externalId":"ARGUMENTATION","image":"/data/content_resources/current/topics/ARGUMENTATION.jpg","name":"Argumentation","position":2000,"translationKey":"lc_topic_other_argumentation_label"},"activities":[{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_VIDEO_VIDEO_WHAT_DO_YOU_THINK_ABOUT_POLITICS","title":"Video : What do you think about politics?","score":null,"status":"SUCCESS","activityType":"VIDEO","highlighted":true},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_POLITICS","title":"Politics","score":100,"status":"SUCCESS","activityType":"EXERCISE","highlighted":false},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_POLITICS_2","title":"Politics","score":100,"status":"SUCCESS","activityType":"EXERCISE","highlighted":false},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_LESSON_3","title":"Lesson 3","score":100,"status":"SUCCESS","activityType":"EXERCISE","highlighted":false},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_EXERCISE_POLITICS_3","title":"Politics","score":100,"status":"SUCCESS","activityType":"EXERCISE","highlighted":false},{"externalId":"EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS_VOCABULARY_LIST_VOCABULARY","title":"Vocabulary","score":null,"status":"SUCCESS","activityType":"VOCABULARY_LIST","highlighted":false}]}
 
 
 ///////////////
 getting all missions
                lessons
                    activities
          
curl 'https://learn.altissia.org/gw//lcapi/main/api/lc/user-learning-paths/language/en_GB' \
  -H 'authority: learn.altissia.org' \
  -H 'sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'x-device-uuid: 8ebe5e58-2078-4ee0-9fe6-fbc1e43763fa' \
  -H 'x-altissia-token: ce816afd63bc2a3669f37ecab4f215e182de262e385f764ad32f58e682da20cb' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://learn.altissia.org/platform/' \
  -H 'accept-language: en-US,en;q=0.9,ar;q=0.8,fr;q=0.7' \
  -H 'cookie: NG_TRANSLATE_LANG_KEY=%22en-GB%22; deviceuuid=8ebe5e58-2078-4ee0-9fe6-fbc1e43763fa' \
  --compressed
 
/////////////////////////////////////
important headers

x-device-uuid = 8ebe5e58-2078-4ee0-9fe6-fbc1e43763fa
x-altissia-token = ce816afd63bc2a3669f37ecab4f215e182de262e385f764ad32f58e682da20cb
content-type = application/json
user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36


fb0516a5-41eb-43d1-8fdd-c56c2f3b600d ent 


does this user id change in this error  id = 939861
{
  "errorCode": "404 NOT_FOUND",
  "message": "Unable to find user activity EN_GB_C1_VOCABULARY_GIVING_A_REPORT_ON_ELECTORAL_RESULTS_VIDEO_ANIMATION_ELECTIONS_AT_WETWATER_UNDER for user 939861"
}

maybe get this url first 

get all about english 
https://learn.altissia.org/gw//lcapi/main/api/lc/user-learning-paths/language/en_GB => the long json above


https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/<lessonID>

PRESENTING_YOUR_VIEW_THE_WRITTEN_PRESS
EN_GB_C1_VOCABULARY_FOLLOWING_THE_NEWS_THE_WRITTEN_PRESS
EN_GB_C1_VOCABULARY_FOLLOWING_THE_NEWS_THE_WRITTEN_PRESS_VIDEO_ANIMATION_SOME_SECTIONS_OF_A_NEWSPAPE

optional paramater => ?learningPathExternalId=PROGRESS_IN_THE_LANGUAGE_EN_GB 


https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/EN_GB_C1_VOCABULARY_GIVING_A_REPORT_ON_ELECTORAL_RESULTS/activities/EN_GB_C1_VOCABULARY_GIVING_A_REPORT_ON_ELECTORAL_RESULTS_VIDEO_ANIMATION_ELECTIONS_AT_WETWATER_UNDER?translationLg=fr_FR
https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/<lessonID>/activities/<activityID or video>

https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/EN_GB_B1_OTHER_GIVING_YOUR_OPINION_ABOUT_POLITICS/activities




https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/EN_GB_C1_VOCABULARY_GIVING_A_REPORT_ON_ELECTORAL_RESULTS/activities


resumé => 
GET https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/<lessonID> to get activities
GET https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/<lessonID>/activities/<activityID>
PUT https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/<lessonID>/activities

/////////////////////////////////////////////////////


