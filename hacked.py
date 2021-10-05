import requests
import time

uuid = "42b56ab3-3a85-4a69-83e3-e6b803ec000b"                                 // changes always
token = "9502cafb4cd4c53b419e2e9b4eba40f79f8d1056d55d38fe4bfd644c59df1054"   // changes always

headers= {
    "x-device-uuid": uuid,
    "x-altissia-token": token,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "content-type": "application/json"
}

def cheater(missionList):
    for mission in missionList:
        for lesson in mission["lessons"]:
    #         if lesson["level"] == "C1":
            missionId = mission["externalId"]
            lessonId = lesson["externalId"]
            getUrl = f"https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/{lessonId}"
            getActivities = requests.get(getUrl, headers=headers)
            for activity in getActivities.json()["activities"]:
                if activity["status"] != "SUCCESS":
                    activityId = activity["externalId"]
                    trickUrl = f'https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/{lessonId}/activities/{activityId}'
                    getTricky = requests.get(trickUrl, headers=headers)
                    putUrl = f'https://learn.altissia.org/gw//lcapi/main/api/lc/lessons/{lessonId}/activities'
                    data = {
                    "externalActivityId":activityId,
                     "externalLessonId":lessonId,
                     "externalMissionId":missionId,
                     "score":100,
                     "status":"SUCCESS"
                    }
                    putScore = requests.put(putUrl,json=data,headers=headers)
                    try :
                        print(putScore.json()['status'])
                    except Exception:
                        print(putScore.json())
                    print("activity done : ",activityId)
                else:
                    print("already : ",activityId)

    #     print("MISSION done : ",missionId)
    print("ALL DONE :)")

enGB = requests.get("https://learn.altissia.org/gw//lcapi/main/api/lc/user-learning-paths/language/en_GB", headers=headers)

cheater(enGB.json()["missions"])