from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

team = {
    1: {"name": "Alex aka 🔫AK", "job title": "master coder"},
    2: {"name": "Johnny aka 🤑Johnny Profits", "job title": "apprentice to the master coder"},
    3: {"name": "HJ", "job title": "intern turned full time SWE!"}
}

# Pydantic is used here to validate the structure of the data being sent/received.
# member_id is not in this class because it is not used as a data but a path
class TeamMember(BaseModel):
    name: str
    # i have to use Field because I don't want to add an underscore to the dictionary above
    job_title: str = Field(alias="job title")

# CRUD
# CREATE
@app.post("/team/")
# argument member is referencing the pydantic class ensuring name and job titles are both strings
def create_new_team_member(member: TeamMember):
    # using comprehension, this will get the max number of keys and increment the new key by 1
    # i did not use "len(team) + 1" because this returns the number of items, not keys
    new_id = max(team.keys()) + 1 if team else 1
    team[new_id] = member

# READ All
@app.get("/")
def get_team():
    if len(team) == 0:
        raise HTTPException(status_code=404, detail="Team has no member, hire more people! I recommend that Johnny Lieu guy.")
    return team
# READ By ID
@app.get("/team/{member_id}")
# we are not referencing member: TeamMember here, it will cause and error as there is no member_id in the pydantic class
def get_team_member_by_ID(member_id: int):
    if member_id not in team:
        raise HTTPException(status_code=404, detail=f"No member with ID of {member_id} was found.")
    return team[member_id]
# READ By name
@app.get("/team/name/{name}")
def get_team_member_by_name(name: str):
    for teammate in team.values():
        if teammate["name"] == name:
            return teammate
    raise HTTPException(status_code=404, detail=f"{name} not found.")

# Update
@app.put("/team/{member_id}")
def udate_member_by_id(member_id:int, member: TeamMember):
    if member_id not in team:
        raise HTTPException(status_code=404, detail=f"Member with {member_id} not found.")
    team[member_id] = member.dict()
    return f"Member with {member_id} was updated to {team[member_id]} "

# Delete
@app.put("/team/{member_id}")
def delete_member_by_id(member_id: int):
    if member_id not in team:
        raise HTTPException(status_code=404, detail=f"Member with {member_id} not found.")
    del team[member_id]
    return f"Team member deleted."