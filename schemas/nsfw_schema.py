from pydantic import Field, BaseModel


class NsfwSchema(BaseModel):
    id: str = Field(...)
    image_url: str = Field(...)
    prompt: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "00031dd8-97af-4c9c-a0c8-681b5d7d0af3",
                "image_url": "https://imagedelivery.net/E9jTnsG9warNlQK5dUFRKA/0e988055-96f4-4e33-6b2a-5672b1c65900/public",
                "prompt": "Brie Larson, Captain Marvel, bare chest, award winning photo, HDR, show pussy, completely nude",
            }
        }
