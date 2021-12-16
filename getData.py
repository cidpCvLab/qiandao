import requests
import json
from pprint import pprint
import time

class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.time_point_all = []
        self.time_point_week = {"Mon": [], "Tues": [], "Wed": [], "Thur": [], "Fri":[], "Sat": [], "Sun": []}
        self.time_length = {"Mon": 0, "Tues": 0, "Wed": 0, "Thur": 0, "Fri":0, "Sat": 0, "Sun": 0}

class Get:
    def __init__(self, member_dict, begin_time, end_time):
        self.member_dict = member_dict
        self.rqData = {"opencheckindatatype": 1,
                        "starttime": begin_time,
                        "endtime": end_time,
                        "useridlist": list(self.member_dict.keys())}
        self.rqJson = json.dumps(self.rqData)
        self.corpId = "ww15631b0d64da0525"
        self.corpSecret = "wgFg1rZKpewyzyOpmy4kenGlTYD_16T7ij2VqYaAdMk"
        self.acess_tokenUrl = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpId}&corpsecret={self.corpSecret}"
        self.dataUrl = "https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckindata?access_token="
        self.intWeekToEng = {
            "1": "Mon",
            "2": "Tues",
            "3": "Wed",
            "4": "Thur",
            "5": "Fri",
            "6": "Sat",
            "7": "Sun"
        }
        self._get_access()
        self._generate_time_length()

    def _get_access(self):
        access = requests.get(self.acess_tokenUrl)
        self.access_token = access.json()["access_token"]

    def getWeek(self, unixTime):
        intWeek = (unixTime % (7 * 24 * 60 * 60)) // (24 * 60 * 60) + 4
        if intWeek >= 8:
            intWeek -= 7
        return intWeek, self.intWeekToEng[str(intWeek)]

    def cal_time_length(self, time_list):
        time_length_day = []
        if len(time_list) % 2 == 0:
            for t in range(len(time_list))[1::2]:
                time_length_day.append(time_list[t] - time_list[t-1])
        else:
            for t in range(len(time_list))[1:]:
                time_length_day.append(time_list[t] - time_list[t-1])
            time_length_day = sorted(time_length_day)[:int((len(time_list)-1)/2)]
        return sum(time_length_day)
    
    def _request_data(self):
        self.member_list = [Member(i, n) for i, n in self.member_dict.items()]
        res = requests.post(url=self.dataUrl + self.access_token, data=self.rqJson)
        if res.json()["errmsg"] == "ok":
            for t in res.json()["checkindata"]:
                for m in self.member_list:
                    if t["userid"] == m.id:
                        m.time_point_week[self.getWeek(t["checkin_time"])[1]].append(t["checkin_time"])
    
    def _generate_time_length(self):
        self._request_data()
        for member in self.member_list:
            for k in member.time_point_week.keys():
                time_length = self.cal_time_length(member.time_point_week[k])
                member.time_length[k] = time_length

    def get_tar_data(self):
        time_length_list = {"Mon": [], "Tues": [], "Wed": [], "Thur": [], "Fri":[], "Sat": [], "Sun": [], "member": []}
        for m in self.member_list:
            time_length_list["member"].append(m.name)
            for k, v in m.time_length.items():
                time_length_list[k].append(round(v/3600, 2))
        return time_length_list
            
            
if __name__ == "__main__":
    with open("./static/members.json") as m:
        member = eval(m.read())
    t = time.time()
    g = Get(member["20"], 1636329600, 1636934400)
    print(g.get_tar_data())
    print(time.time()-t)
