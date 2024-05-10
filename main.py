from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

# from controllers.home import router as home
# from controllers.certs import router as certs

from version import router as apiRouter

app = FastAPI()

# CORS Integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# app.include_router(home)
# app.include_router(certs)
app.include_router(apiRouter)

if __name__ == "__main__":
    app.run(debug=True)