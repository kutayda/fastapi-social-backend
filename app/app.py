from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {"title": "First Post", "content": "Hello world! This is my first FastAPI test post."},
    2: {"title": "PC Build Advice", "content": "Should I get the RTX 5070 Ti or wait for the new series?"},
    3: {"title": "Valorant Patch Notes", "content": "The new agent's abilities seem a bit too overpowered for competitive mode."},
    4: {"title": "My Flutter Experience", "content": "State management became much easier after figuring out the GetX architecture."},
    5: {"title": "Dandadan Review", "content": "I read the manga, but the anime's animation and soundtrack are truly incredible!"},
    6: {"title": "FastAPI and Pydantic", "content": "Using BaseModel for data validation is a lifesaver compared to doing it manually."},
    7: {"title": "Database Connection", "content": "Finally connected my API to the database successfully. Next step: JWT security!"},
    8: {"title": "OLED Monitor Choice", "content": "How much has the burn-in issue been resolved on the new generation 2K OLED panels? Anyone using one?"},
    9: {"title": "Internship Diaries", "content": "Started working with Python and FastAPI on the backend today. It's been fun."},
    10: {"title": "Latest MrBeast Video", "content": "The production quality in the latest video has truly surpassed TV shows."}
}
@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit: 
        return list(text_posts.values())[:limit]
    return text_posts   


@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    return text_posts.get(id)

@app.post("/post")
def create_post(post: PostCreate):
    text_posts[max(text_posts.keys())+ 1] = {"title": post.title, "content": post.content}