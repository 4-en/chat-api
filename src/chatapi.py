
# fastapi
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# pydantic
from pydantic import BaseModel

# typing
from typing import Dict, List

# uuid
import uuid

# request models
class User(BaseModel):
    user_id: str = None
    token: str = None
    username: str = None

class Message(BaseModel):
    message_id: str = None
    user: User = None
    message: str = None

class SendMessage(BaseModel):
    user: User = None
    message: str = None
    conversation_id: str = None

class ConversationRequest(BaseModel):
    user: User = None
    conversation_id: str = None

class Conversation:
    def __init__(self, conversation_id: str, users: List[User]=[], messages: List[Message]=[]):
        self.conversation_id = conversation_id
        self.users = users
        self.messages = messages

class ChatAPI:

    def __init__(self):

        self.app = FastAPI()
        self.conversations = {}

    async def get_conversation(self, conversation_id: str):
        return self.conversations[conversation_id]

    
    def create_routes(self):

        @self.app.get("conversation")
        async def get_conversation(conversation_request: ConversationRequest):
            return await self.get_conversation(conversation_request.conversation_id)


