@echo off

cd App\ModelService
uvicorn ModelAPI:app --reload