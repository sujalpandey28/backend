import uvicorn
from fastapi import FastAPI
from app import models
# from app.routers import auth, org, superadmin, temp, 
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user 


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

# Define the list of allowed origins
origins = ["*"]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Add other allowed methods as needed
    allow_headers=["*"],  # You can specify specific headers if needed
)

# app.include_router(auth.router)
# app.include_router(org.router)
# app.include_router(superadmin.router)
# app.include_router(temp.router)
# app.include_router(count.router)

app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Server running"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "_main_":
    uvicorn.run(app, host="0.0.0.0", port=8000)