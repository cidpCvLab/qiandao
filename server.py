from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apscheduler.schedulers.blocking import BlockingScheduler
from getData import Get
from pprint import pprint
from pydantic import BaseModel

class Item(BaseModel):
    begin_time: int
    end_time: int
    member: int

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("./static/members.json") as m:
        member_dict = eval(m.read())

@app.get("/data")
def root(begin_time: int = Query(None), end_time: int = Query(None), member:int = Query(None)):
    data = Get(member_dict[str(member)], begin_time, end_time)
    return data.get_tar_data()

@app.get("/")
def root():
    return "pa"


if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=522, reload=True)
